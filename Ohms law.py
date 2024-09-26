
# Ask the user what they want to calculate: Voltage, Current, or Resistance.
conversion_choice = input("Type 'I' to find current, 'V' to find voltage, and 'R' to find resistance: ")

# Ask the user to input the appropriate values.
if conversion_choice == 'I':
    Voltage = float(input("What is the value of your voltage: "))
    Resistance = float(input("What is the value of your resistance: "))
    if Resistance == 0:
        print("The Resistance cannot be zero")
    else:
        Current = Voltage / Resistance
        print(f"Your current is: ", Current)

elif conversion_choice == 'V':
    Resistance = float(input("What is the value of resistance: "))
    Current = float(input("What is the value of current: "))
    Voltage = Current * Resistance
    print(f"Your Voltage is ",Voltage)

elif conversion_choice == 'R':
    Current = float(input("What is the value of the current: "))
    Voltage = float(input("What is the voltage: "))
    if Current == 0:
        print("The Current cannot be zero")
    else:
        Resistance = Voltage / Current
        print("Your resistance is ", Resistance) 
else:
    print("Invalid input ")

