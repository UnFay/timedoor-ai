from math import hypot
import cv2
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load overlay image with Alpha (transparency) channel
nose_img = cv2.imread("pig_nose.png", cv2.IMREAD_UNCHANGED)

mpDraw = mp.solutions.drawing_utils
mpDrawingStyles = mp.solutions.drawing_styles
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=4)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, c = frame.shape
            leftnosex, leftnosey = 0, 0
            rightnosex, rightnosey = 0, 0
            centernosex, centernosey = 0, 0

            for lm_id, lm in enumerate(face_landmarks.landmark):
                x, y = int(lm.x * w), int(lm.y * h)
                if lm_id == 49:
                    leftnosex, leftnosey = x, y
                elif lm_id == 279:
                    rightnosex, rightnosey = x, y
                elif lm_id == 5:
                    centernosex, centernosey = x, y

            # Correct distance calculation for scale
            nose_width = int(
                hypot(rightnosex - leftnosex, rightnosey - leftnosey) * 1.5
            )
            nose_height = int(nose_width * 0.8)

            if nose_width > 0 and nose_height > 0:
                pig_nose = cv2.resize(
                    nose_img, (nose_width, nose_height), interpolation=cv2.INTER_AREA
                )

                # Define bounding box coordinates
                top_left_x = int(centernosex - nose_width / 2)
                top_left_y = int(centernosey - nose_height / 2)

                # Ensure overlay stays within frame boundaries
                if (
                    top_left_x >= 0
                    and top_left_y >= 0
                    and (top_left_x + nose_width) <= w
                    and (top_left_y + nose_height) <= h
                ):

                    nose_area = frame[
                        top_left_y : top_left_y + nose_height,
                        top_left_x : top_left_x + nose_width,
                    ]

                    # Overlay logic using Alpha Channel if present
                    if pig_nose.shape[2] == 4:
                        alpha_nose = pig_nose[:, :, 3] / 255.0
                        alpha_frame = 1.0 - alpha_nose

                        for c_channel in range(0, 3):
                            frame[
                                top_left_y : top_left_y + nose_height,
                                top_left_x : top_left_x + nose_width,
                                c_channel,
                            ] = (
                                alpha_nose * pig_nose[:, :, c_channel]
                                + alpha_frame * nose_area[:, :, c_channel]
                            )
                    else:
                        # Fallback for 3-channel images without alpha transparency
                        pig_nose_gray = cv2.cvtColor(pig_nose, cv2.COLOR_BGR2GRAY)
                        _, mask = cv2.threshold(
                            pig_nose_gray, 25, 255, cv2.THRESH_BINARY_INV
                        )
                        no_nose = cv2.bitwise_and(
                            nose_area, nose_area, mask=mask
                        )
                        final_nose = cv2.add(no_nose, pig_nose)
                        frame[
                            top_left_y : top_left_y + nose_height,
                            top_left_x : top_left_x + nose_width,
                        ] = final_nose

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()