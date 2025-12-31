import math

pizza_menu = """

            IYA SCAMBIRAH PIZZA MENU

PIZZA TYPE      NUMBER OF SLICES        PRICE PER BOX

SAPA SIZE               4                   2000

SMALL MONEY             6                   2400

BIG BOYS                8                   3000

ODOGWU                  12                  4200

    """

print (pizza_menu)

guests = int(input("Enter number of guests: "))
pizza_type = input("Enter pizza type: ").lower()

if  pizza_type == "sapa size":
    pizza_slices = 4
    price_per_box = 2000

elif    pizza_type == "small money":
        pizza_slices = 6
        price_per_box = 2400

elif    pizza_type == "big boys":
        pizza_slices = 8
        price_per_box = 3000    

elif    pizza_type == "odogwu":
        pizza_slices = 12
        price_per_box = 4200

else:
        print(f"{pizza_type} NOT AVAILABLE!")

number_of_boxes = math.ceil(guests / pizza_slices)
leftover_slices = number_of_boxes * pizza_slices - guests
total_price = number_of_boxes * price_per_box

print(f"Number of boxes to buy: {number_of_boxes}")
print(f"Leftover slices: {leftover_slices}")
print(f" Total price: {total_price}")

