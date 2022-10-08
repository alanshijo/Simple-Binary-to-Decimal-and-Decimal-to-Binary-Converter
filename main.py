from converter import BinToDec as a
from converter import DecToBin as b
def conti():
    cont = input("Do you want to continue(y/n)?: ")
    if(cont != "y"):
        exit()
while True:
    print("---Menu---")
    print("1. Binary-to-Decimal")
    print("2. Decimal-to-Binary")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        num = int(input('Enter the binary number: '))
        print('The decimal value is ', a.bintodec(num))
        conti()
    elif (choice == 2):
        num = int(input('Enter the decimal number: '))
        print('The decimal value is ', b.dectobin(num))
        conti()
    elif (choice == 3):
        break
    else:
        print("Invalid choice.")
