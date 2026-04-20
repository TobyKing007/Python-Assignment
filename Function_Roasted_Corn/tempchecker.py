temp_value = float(input("Enter a temperature unit "))
measurement_unit = (input("Enter a measurement unit (C for Celcius and F for Fahrenheit) "))
threshold = float(input("Enter a threshold temperature "))

if (measurement_unit.upper() == "C"):
    converted = ((temp_value * 9/5) + 32)
    print (converted)

elif (measurement_unit.upper() == "F"):
    converted = ((temp_value - 32) * 5/9)
    print (converted)

else:
    print ("Invalid input. Use 'C' or 'F'")

if (converted < threshold):
    print ("Cold advisory")

elif (converted >= threshold):
    print ("Hest alert")




