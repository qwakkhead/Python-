
# Ask the user to input their preferred numbers of rows
n = int(input("Numbers of rows: "))
if n % 2 == 0:
    print(" Odd integers only. ")
else:
    middle = n // 2
    for i in range(middle + 1):
        spaces = middle - i
        stars = n - 2 * spaces
        print(' ' * spaces + '*' * stars)
    
    for i in range(middle - 1, -1, -1):
        spaces = middle - i
        stars = n - 2 * spaces
        print(' ' * spaces + '*' * stars)
