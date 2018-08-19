def dectobin(n):
    """Translate a positive integer from decimal to binary.
    Params: n (int): decimal number > 0
    Returns: (string) binary number as a int
    """
    if n == 0:
        return ''
    else:
        return dectobin(n // 2) + str(n % 2)


def bintodec(x):
    n = 0
    for i in str(x):
        n *= 2
        if i == '1':
            n += 1
        if i > '1':
            print("Please Enter a Binary Number!\n")
            binaryCalculator()
    return n


def binaryCalculator():
    global first_number
    global second_number
    menuFormat = ("What do you want to do?" + "\n" 
                  "1. Enter the first number" + "\n"  
                  "2. Enter the second number" + "\n"  
                  "3. Add the two numbers together" + "\n"  
                  "4. Subtract the second number from the first" + "\n" 
                  "5. Exit the program")
    print(menuFormat)
    user_input = input('Enter Command\n')
    first_number_count = 0
    first_number_count2 = 0
    while user_input != '5':
        if user_input == '1':
            first_number = input("Enter the first number:\n")
            print("Your First Number is:", first_number, "in decimal:", bintodec(first_number))
            binaryCalculator()
            break
        if user_input == '2':
            second_number = (input("Enter the second number:\n"))
            print("Your Second Number is:", second_number, "in decimal:", bintodec(second_number))
            binaryCalculator()
            break
        if user_input == '3':
            if "first_number" and "second_number" not in globals():
                print("Please Do Commands 1&2 First")
                first_number = input("Enter the first number:\n")
                second_number = input("Enter the second number:\n")
                binaryCalculator()
                break
            else:
                first_number_count += bintodec(first_number)+bintodec(second_number)
                print(first_number,"+",second_number,"Sum Binary=",
                      dectobin(first_number_count),"Sum Decimal=",first_number_count)
                binaryCalculator()
                break
        if user_input == '4':
            if "first_number" and "second_number" not in globals():
                print("Please Do Commands 1&2 First")
                first_number = int(input("Enter the first number:\n"))
                second_number = int(input("Enter the second number:\n"))
                binaryCalculator()
                break
            if second_number < first_number:
                print("Second Number Should be Larger Than First")
            else:
                first_number_count2 += int(second_number)-int(first_number)   #second has to be greater than the first
                print(second_number,"-",first_number,"Difference Binary=",first_number_count2,"Difference Decimal=",bintodec(first_number_count2))
                binaryCalculator()
                break
        if user_input not in str("1,5"):
            print("Invalid User Input, Try Again")
            binaryCalculator()


binaryCalculator()
