def PizzaTime(price, quantity):
    numPrice = float(price)
    numQuant = int(quantity)
    print("Total pizza cost: ", (numPrice*numQuant))

pizzaPrice = input("Enter price of 1 pizza  ")
pizzaQuant = input("Enter the number of pizzas you want to buy"  )
PizzaTime(pizzaPrice,pizzaQuant)