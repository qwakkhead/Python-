
conversion_choice = input("Type 'I' to find current, 'V' to find voltage, and 'R' to find resistance: ")

if conversion_choice == 'I':
    Voltage = float(input("What is the value of your voltage: "))
    Resistance = float(input("What is the value of your resistance: "))
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
    Resistance = Voltage / Current
    print("Your resistance is ", Resistance) 
else:
    print("Invalid input ")