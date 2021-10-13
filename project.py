# ****** HANIEH GHORBANPOUR ... PYTHON CODE ... PHONEBOOK ******

#baraye khoroj az barname va khata haye ehtemali estefade az sys:
import sys
#...............................................................................
def menu():
    # neshon dadan yek menu be karbar baraye anjam amaliat morede nazar
    print("THIS PHONE BOOK CAN PROVIDE BELOW FUNCTIONS FOR YOU :)\n")
    print("1: ADD A NEW CONTACT")
    print("2: REMOVE AN EXISTING CONTACT")
    print("3: SEARCH FOR A CONTACT")
    print("4: SHOW ALL CONTACTS")
    print("5: EXIT \n")
    selection = int(input("PLEAZE ENTER YOUR CHOICE :) \n"))

    return selection
#...............................................................................
# tabe baraye anjam dastor aval:
def our_first_phonebook():
    #tedad contact hara vared mikonad
    rows = int(input("PLEASE ENTER NUMBER OF CONTACTS YOU WANT TO ADD: \n"))
    # az karbar baraye har contact etelaat gerefte mishavad
    columns = 4

    our_phone_book = []
    for i in range(rows):
        print("complete this fields please:) \n")
        temp = []
        for j in range(columns):
            if j == 0:
                temp.append(str(input("ENTER HER/HIS NAME : ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("YOU SHOULD ENTER HIS/HER NAME : ")

            if j == 1:
                temp.append(int(input("ENTER HIS/HER NUMBER : ")))

            if j == 2:
                temp.append(str(input("Enter date of birth if you like : ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("ENTER HIS/HER E-MAIL ADDRESS if you like : \n")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        # hala etelaat ro dar listmon zakhire mikonim
        our_phone_book.append(temp)

    print(our_phone_book)
    return our_phone_book
#...............................................................................
def add_contact(phonebook):

    temp2 = []
    for i in range(len(phonebook[0])):
        if i == 0:
            temp2.append(str(input("ENTER HER/HIS NAME : ")))
            if temp2[j] == '' or temp[j] == ' ':
                sys.exit("YOU SHOULD ENTER HIS/HER NAME : ")

        if i == 1:
            temp2.append(int(input("ENTER HIS/HER NUMBER : ")))

        if i == 2:
            temp2.append(str(input("Enter date of birth if you like : ")))
            if temp2[j] == '' or temp2[j] == ' ':
                temp2[j] = None

        if i == 3:
            temp2.append(str(input("ENTER HIS/HER E-MAIL ADDRESS if you like : \n")))
            if temp2[j] == '' or temp2[j] == ' ':
                temp2[j] = None

    phonebook.append(temp2)
    return phonebook
#...............................................................................
def remove_contact(phonebook):
    contact = str(input("PLEASE ENTER THE NAME OF THE CONTACT YOU WANT TO REMOVE : "))
    temp = 0

    for i in range(len(phonebook)):
        if contact == phonebook[i][0]:
            temp += 1

            print(phonebook.pop(i))
            print("THIS CONTACT HAS NOW BEEN REMOVED")

            return phonebook

    if temp == 0:
        print("SORRY, INVALID CONTACT :( ")

        return phonebook
#...............................................................................
def search_contact(phonebook):
    selection = int(input("SEARCH OPTIONS: \n 1: NAME\n 2: NUMBER\n 3: EMAIL\n 4: DATE OF BIRTH\n ENTER PLEASE : "))
    temp = []
    check = -1

    if selection == 1:
        contact = str(input("PLEASE ENTER THE NAME OF THE CONTACT YOU WANT TO SEARCH : "))
        for i in range(len(phonebook)):
            if contact == phonebook[i][0]:
                check = i
                temp.append(phonebook[i])

    elif selection == 2:
        number = int(input("PLEASE ENTER THE NUMBER OF THE CONTACT YOU WANT TO SEARCH : "))
        for i in range(len(phonebook)):
            if number == phonebook[i][1]:
                check = i
                temp.append(phonebook[i])

    elif selection == 3:
        email = str(input("PLEASE ENTER THE E-MAIL : "))
        for i in range(len(phonebook)):
            if email == phonebook[i][2]:
                check = i
                temp.append(phonebook[i])

    elif selection == 4:
        birth = str(input("PLEASE ENTER THE DATE OF BIRTH : "))
        for i in range(len(phonebook)):
            if birth == phonebook[i][3]:
                check = i
                temp.append(phonebook[i])

    else:
        print("INVALID NUMBER")
        return -1

    if check == -1:
        return -1
    else:
        show(temp)
        return check
#...............................................................................
def show(phonebook):
    if not phonebook:
        print(" LIST IS EMPTY ")
    else:
        for i in range(len(phonebook)):
            print(phonebook[i])
#...............................................................................
def goodbye():
    print("Thank you for using our phonebook :) ")
    sys.exit("have a nice day!")
#...............................................................................
code = 1
phonebook = our_first_phonebook()
while code in (1, 2, 3, 4):
    code = menu()
    if code == 1:
        phonebook = add_contact(phonebook)
    elif code == 2:
        phonebook = remove_contact(phonebook)
    elif code == 3:
        a = search_contact(phonebook)
        if a == -1:
            print("SORRY THE CONTACT DOESNT EXIST :( ")
    elif code == 4:
        show(phonebook)
    else:
        goodbye()
