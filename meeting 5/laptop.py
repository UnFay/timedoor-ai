class Laptop:
    def __init__(self, brand, release_year, color, RAM):
        self.laptop_brand = brand
        self.laptop_release_year = release_year
        self.laptop_color = color
        self.laptop_RAM = RAM

    def info(self):
        return f"Color: {self.laptop_color}, Brand: {self.laptop_brand}, Release: {self.laptop_release_year}, Gigs of RAM: {self.laptop_RAM}"
    
    def coding(self):
        print("If laptop is used for coding...")
        print("RAM usage: 2 GB")
        self.laptop_RAM -= 2
        print("Remaining RAM: " + str(self.laptop_RAM)+ " GB")
    
    def office(self):
        print("If laptop is used for office work...")
        print("RAM usage: 1 GB")
        self.laptop_RAM -= 1
        print("Remaining RAM: " + str(self.laptop_RAM)+ " GB")
        
    def videoEditing(self):
        print("If laptop is used for video editing...")
        print("RAM usage: 3 GB")
        self.laptop_RAM -= 3
        print("Remaining RAM: " + str(self.laptop_RAM)+ " GB")

class GamingLaptop(Laptop):
    def __init__(self, brand, release_year, color, RAM, VGA):
        super().__init__(brand, release_year, color, RAM)
        self.laptop_VGA = VGA
    
    def gaming(self):
        print("If laptop is used for gaming..")
        print("RAM usage: 10 GB")
        self.laptop_RAM -= 10
        print("Remaining RAM: " + str(self.laptop_RAM)+ " GB")


laptop1 = Laptop("Dell", 2021, "Grey", 8)
laptop2 = GamingLaptop("Asus", 2022, "Black", 16, "RTX 1650")
laptop3 = Laptop("Macbook", 2022, "Silver", 8)
print(laptop1)

print(laptop1.info())
laptop1.coding()
laptop1.office()
laptop2.coding()
laptop2.gaming()
