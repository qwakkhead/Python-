
conversion_choice = input("Type 'C' to convert to Farenheit, Type 'F' to convert to Celsius: ")

if conversion_choice == 'C':
    Celsius = float(input("What is the Celsius: "))
    Celsius_to_Farenheit = (Celsius * 9/5) + 32
    print(f"Your Farenheit is: ", Celsius_to_Farenheit)
elif conversion_choice == 'F':
    Farenheit = float(input("What is the Farenheit"))
    Farenheit_to_Celsius = (Farenheit -32) * 5/9
    print(f"Your Celsius is: ", Farenheit_to_Celsius)
else:
    print("Invalid input")