# Name: Emman Torrecampo
# Program: Mohave High School Library
#Purpose: To teach us about python concepts while creating a Library Control Software


#**************************************************************************************
#***                             Dictionaries and Lists                             ***
#**************************************************************************************
import time
import datetime
import os

patron = {'Emman': 'Student', 'Fischer': 'Teacher'}                                                                     #Users
books = {'900-00': {'To Kill A Mockingbird': 'Harper Lee'}, '900-01': {'To Kill A Mockingbird': 'Harper Lee'}}          #Books
bookStatus = {'Emman': 1, 'Fischer': 1}                                                                                 #No of borrowed Books
avbooks = {'900-00': 0, '900-01': 1}                                                                                    #Available No. of Books
ebook = {'Emman': ['900-00'], 'Fischer': ['900-01']}                                                                    #ID no. of borrowed books
fines = {'Emman': 0.0, 'Fischer': 0.0}                                                                                  #Fines
vbooks = {'Emman': {'To Kill A Mockingbird': 'Harper Lee'}, 'Fischer': {'To Kill a Mockingbird': 'Harper Lee'}}         #Name of borrowed books
id = []
#**************************************************************************************
#**************************************************************************************
#Function menu -- User will select an option from the main menu
def menu():
    os.system('cls')
    #Variables
    correct = True
    option = ' '
    # Control Loop for function menu
    while correct:
        print('          Mohave High School Library')
        print('                    Main Menu')
        print()
        print('Check Out Books                        C')
        print('Add Patron                             P')
        print('Status of Books                        B')
        print('Status of Patron                       S')
        print('Add Books                              A')
        print('Reports                                R')
        print('Return Books                           Z')
        print('Quit                                   Q')

        option = input('Enter Selection: ')

        option = option.title()

        os.system('cls')
        # Check if user input a correct option on the menu
        if option == 'C':
            correct = False
        elif option == 'P':
            correct = False
        elif option == 'B':
            correct = False
        elif option == 'S':
            correct = False
        elif option == 'A':
            correct = False
        elif option == 'R':
            correct = False
        elif option == 'Z':
            correct = False
        elif option == 'Q' or option == 'Quit':
            correct = False
        else:
            print()
            print('      Error: Improper Menu Selection.      ')
            print()
    #Exit while loop
    return option

# Exit menu Function

#**************************************************************************************
#***                             Main Program                                       ***
#**************************************************************************************

#Variables
quit = True  # Used to continue and terminate main control loop
choice = ' '  # Choice returned by menu function
#Control Loop

while quit:
    choice = menu()

    if choice == 'C':
        print()
        print('Enter the book ID: ')
        ibook = input()

        if ibook in books and avbooks[ibook] > 0:
            obooks = books.get(ibook, 0)            #Getting the value of the key ibook
            obooks = list(obooks.items())           #Converting that dictionary in to a list
            obooks = obooks[0]
            bookn, booka = obooks[0], obooks[1]     #Assigning the values of obooks in to the variables bookn and booka
            bookcom = bookn + ' by ' + booka
            print()
            print(bookcom)
            time.sleep(1)
            print()
            print('Do you want to check out this book? (Y or N)')
            print()
            k = input()
            k = k.title()
            os.system('cls')

            if k == 'Y':
                print()
                print('What\'s your name?: ')
                name = input()
                name = name.title()

                if name in patron:
                    bookStatus[name] = bookStatus[name] + 1         #Adding number of books the user borrowed in to his name

                    if bookStatus[name] < 10:
                        avbooks[ibook] = avbooks[ibook] - 1         #Subtracting the value of the book ID so users will know that it's not available
                        ebook[name] = id                            #Assigning the list id to be a value of the key name
                        id.append(ibook)                            #Putting the ibook in to the id list
                        status = patron.get(name, 0)                #Checking if the user is a Student or Teacher

                        if status == 'Student':
                            dt = datetime.datetime.now()            #Assigning the time and date in to the variable dt
                            ct = datetime.timedelta(days=10)        #Assigning the time after 10 days in to the variable ct
                            print()
                            print('You\'ve checked out %s on %s' % (bookcom, dt.strftime('%B %d,%Y %A')))
                            dt = dt + ct                            #Adding the current date and time in to ct
                            print()
                            print('You have 10 days to return this book which is in %s' % dt.strftime('%B %d,%Y  %A'))
                            print()

                            if datetime.datetime.now() < dt:
                                fines[name] = 0.0                       #Checking if the time exceeds the due date

                            else:
                                while datetime.datetime.now() > dt:
                                    fines[name] = 0.0 + .10                 #If the time exceeds the due date it adds fines in to your account
                                    vbooks[name][bookn] = booka             #It also adds the name and author of the book in to your overdue books

                            time.sleep(4)

                        else:
                            dt = datetime.datetime.now()            #Assigning the time and date in to the variable dt
                            ct = datetime.timedelta(days=20)        #Assigning the time after 20 days in to the variable ct
                            print()
                            print('You\'ve checked out %s on %s' % (bookcom, dt.strftime('%B %d,%Y %A')))
                            dt = dt + ct                            #Adding the current date and time in to ct
                            print()
                            print(' You have 20 days to return this book which is in %s' % dt.strftime('%B %d,%Y  %A'))
                            print()

                            if datetime.datetime.now() < dt:        #Checking if the time exceeds the due date
                                fines[name] = 0
                            else:
                                while datetime.datetime.now() > dt:
                                    fines[name] = 0 + .10                   #If the time exceeds the due date it adds fines in to your account
                                    vbooks[name][bookn] = booka             #It also adds the name and author of the book in to your overdue books
                            time.sleep(4)

                    elif bookStatus[name] > 10:         #If you have more than 10 books in to your account, it won't let you borrow a book
                        print()
                        print('       You have a lot of checked out books')
                        print('Please return a book first to checked out another book.')
                        print('           Sorry for the inconvenience')
                        print()

                else:
                    print()
                    print('You\'re not in the system.')
                    print()
                    print('Do you want to be a patron? (Y or N)')
                    print()
                    z = input()
                    z = z.title()

                    if z == 'Y':
                        print()
                        print('Enter P in the menu')
                        print()
                        time.sleep(2)

        else:
            print()
            print('This book is not available or not in the system.')
            print('       Put A in the menu to add book.')
            print('         Or check out other books')
            print('        Sorry for the inconvenience')
            print()
            time.sleep(3)

    elif choice == 'P':
        print()
        name = input('Enter name here: ')
        name = name.title()

        if name not in patron:              #Checking if your name is in the systemf
            print()
            print('You must be new here, do you want to be a patron?: (Y or N)')
            b = input()
            b = b.title()

            if b == 'Y':
                print()
                print('Are you a teacher or student?: ')
                new = input()
                new = new.title()
                patron[name] = new              #Assigning the new name in to the system
                bookStatus[name] = 0            #It creates a key of your name with the value of no. of borrowed books
                ebook[name] = ' '               #Creates a key of your name with the value of borrowed books
                fines[name] = 0                 #Creates a key of your name with the value of fines
                time.sleep(1)
                print()
                print('           System updated')
                print('Welcome to Mohave High School\'s Library')
                print()
                time.sleep(2)

            else:
                print()
                print('Thank you for using our Library Software.')
                print('  Study hard, Work hard, and Fly High.   ')
                quit = False

        else:
            print()
            print('   You\'re already a patron.')
            time.sleep(1)
            print()
            print('Would you like to check our books?: (Y or N)')
            a = input()
            a = a.title()

            if a == 'N':
                print()
                print('Thank you for using our Library Software.')
                print('  Study hard, Work hard, and Fly High.   ')
                quit = False

    elif choice == 'B':
        print()
        print('Enter the ID number of the book: ')
        ibook = input()

        if avbooks[ibook] < 1:              #Checking if the value of the ibook is 0, which means someone already borrowed the book
            print()
            print('The book is already checked out.')
            print()
            time.sleep(1)
        else:
            print()
            print('     This book is available')
            print('If you want to check out this book')
            print('      Press C in the menu')
            print()
            time.sleep(2)

    elif choice == 'S':
        print()
        name = input('Enter name here: ')
        name = name.title()

        if name in patron:              #Checking if you're on the system
            print()
            print(name + '\'s status is ' + patron[name])
            time.sleep(1)
            print()
            print('Do you want to change your name?: (Y or N)')
            change = input()
            change = change.title()

            if change == 'Y':
                print()
                print('What\'s your new name?')
                name1 = input()
                name1 = name1.title()
                patron[name1] = patron[name]                #Assign the new name into the users with the same value
                print()
                print('          System Updated')
                print()
                time.sleep(1)

        else:
            print()
            print(name + '\'s status is not a patron.')
            print()
            time.sleep(1)

    elif choice == 'A':
        print()
        print('Enter the name of the book: ')
        cbook = input()
        cbook = cbook.title()
        print()
        print('Enter the author of the book: ')
        abook = input()
        abook = abook.title()
        print()
        print('Enter the book ID: ')
        ibook = input()

        if ibook in books:                                  #Checking if the book id is already on the system
            print()
            print('The book is already in the system.')
            print()
            time.sleep(1)
        else:
            books[ibook] = {cbook: abook}                   #Adding the book in the system
            avbooks[ibook] = 1                              #Assigning the value 1 so that the system will show that it's available for checkout
            print()
            print('     Book Added     ')
            print()
            time.sleep(1)

    elif choice == 'R':
        print()
        print('Enter name here: ')
        name = input()
        name = name.title()

        if name in patron:
            print()
            print('                 Patron Report          ')
            print()
            print('Name:                                   ', name)
            print('Status:                                 ', patron[name])
            print('No. of checked out books                ', bookStatus[name])
            print('Checked out books                       ', ebook[name])
            if name in vbooks:
                print('Overdue Books                           ', vbooks[name])
            print('Fines                                   $', fines[name])
            print()
            h = input('Press anything to go back to the main menu')
        else:
            print('Your name is not on the system.')
            print()
            print('If you want to be a patron')
            print('    Put P on the menu')
            print()
            time.sleep(2)

    elif choice == 'Z':
        print()
        print('Enter the name of the returnee of the book: ')
        name = input()
        name = name.title()
        print()
        print('Enter the name of the book: ')
        cbook = input()
        cbook = cbook.title()
        print()
        print('Enter the book ID: ')
        ibook = input()

        if ibook in books and ibook in ebook[name]:
            avbooks[ibook] += 1                                 #Adding the value of the key ibook so that it's available again for checkout
            bookStatus[name] -= 1
            print(vbooks[name])
            del vbooks[name][cbook]                           #Deleting the pair cbook and book author in to the dictionary vbooks
            del ebook[name][ebook[name].index(ibook)]           #Deleting the book id in the value list of name in the ebook
            print()
            print('Thank You for returning the book %s' % name)
            print('It\'s always a great day to be a T-Bird')
            print()
            time.sleep(2)
        else:
            print()
            print('      The book ID is not on the system.')
            print('If you\'re trying to add a book, press A on the menu')
            print()
            time.sleep(2)

    elif choice == 'Q' or choice == 'Quit':
        print()
        print('Thank you for using our Library Software.')
        print('  Study hard, Work hard, and Fly High.   ')
        quit = False

#Exit Main Loop