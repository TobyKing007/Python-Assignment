item_name = (input("Enter name of item"))
original_item_price = float(input("Enter item price"))
promo_code = (input("Enter promo code"))

if (promo_code.upper() == "SAVE10"):
    print (original_item_price * 0.1)

elif (promo_code.upper() == "HALFOFF"):
    print (original_item_price * 0.5)

else:
    print (original_item_price)
