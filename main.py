import sys
import default

friends_name=[]
friends_age=[]
friends_rating=[]
friends_is_online=[]

def add_friend():
    new_name = raw_input("Enter your name:")
    new_salutation = raw_input("should we call you Mr. or Mrs.:")
    new_age = int(raw_input("Enter your Age:"))
    new_rating = raw_input("Enter your Rating:")

    if new_name.isalpha() == False:
        print("invalid name")
        sys.exit(0)
    if new_age <=12 or new_age >= 50:
        print("invalid Age")
        sys.exit(0)

    friends_name.append(new_name)
    friends_age.append(new_age)
    friends_rating.append(new_rating)
    friends_is_online.append(True)

#funtion
STATUS_MESSAGE=[]
def add_status(current_status_message):
    if current_status_message == None:
        print("you do not have any current status")
    else:
        print("Your current status is" + current_status_message)

    update_choice = raw_input("Do you want to select from older status(y/n)?")
    if update_choice.upper() == 'N':
        new_status_message = raw_input("Enter New status Message:")
        if len(new_status_message)>0:
            updated_status_message=new_status_message
            STATUS_MESSAGE.append(updated_status_message)

    elif update_choice.upper() == 'Y':
        for i in range(len(STATUS_MESSAGE)):
            print(str(i+1) + "   " + STATUS_MESSAGE[i])

        message_selection = int(raw_input("choose from the older message:"))
        updated_status_message = STATUS_MESSAGE[message_selection-1]

    return (updated_status_message)

def start_chat(spy_name,spy_salutation,spy_age,spy_rating):
    current_status_message=None
    show_menu = True
    while show_menu == True:
        Menu_choice = raw_input("1.Add a status update\n2.Add a friend\n3.Exit Application")
        if Menu_choice == '1':
            #update the status
           print("you have choosn to add a status")
           current_status_message = add_status(current_status_message)
        elif Menu_choice =='2':
             print("you have to choosen to add a friend")
             add_friend()
        elif Menu_choice == '3':
             show_menu=False

print("Welcome to Spychat Application")
choice = raw_input("Enter 1 for default choice:")


if choice == '1':
    spy_name = default.spy_name
    spy_salutation = default.spy_salutation
    spy_age = default.spy_age
    spy_rating = default.spy_rating
else:
    spy_name=raw_input("Enter your Name:")
    spy_salutation=raw_input("Enter your Salutation(Mr. or Mrs.:)")
    spy_age=raw_input("Enter your Age:")
    spy_rating=raw_input("Enter your Rating:")

#Validating the name of the spy
if spy_name.isalpha() == False:
    print("Name is invalid")
    sys.exit(0)

#Validating the age of the spy
if int(spy_age) <= 12 or int(spy_age) >= 50:
    print("Age is invalid")
    sys.exit(0)

#Rating of the spy
if spy_rating == 'A':
   print("you are a 3 star spy")
elif spy_rating == 'B':
    print("you are a 2 star spy")
elif spy_rating == 'C':
    print("you are a 1 star spy")
else:
    print("you have entered incorrect string")
    sys.exit(0)

print("Hello " + spy_salutation + spy_name)
print("your age is "+ spy_age)
print("your rating is " + spy_rating)

start_chat(spy_name,spy_salutation,spy_age,spy_rating)
