from spy_details import SPY
from spy_details import SPY,ChatMessage
import sys
#import default
import spy_status
import spy_friend

def start_chat(spy_name,spy_salutation,spy_age,spy_rating):
    current_status_message=None
    show_menu = True
    while show_menu == True:
        Menu_choice = raw_input("1.Add a status update\n2.Add a friend\n3.Send secret message\n4.Read secret message\n5.Exit Application")
        if Menu_choice == '1':
            #update the status
           print("you have choosn to add a status")
           current_status_message = spy_status.add_status(current_status_message)
        elif Menu_choice =='2':
             print("you have to choosen to add a friend\n")
             spy_friend.add_friend()
        elif Menu_choice =='3':
             print("you have choosen to Send message\n")
        elif Menu_choice =='4':
             print("you have choosen to Read message\n")
        elif Menu_choice == '5':
             print("you have choosen to close the Application\n")
             show_menu=False
        else:
            print("incorrect choice\n")

print("Welcome to Spychat Application")
choice = raw_input("Enter 1 for default choice:")

#spy = {
#      'name':" ",
#      'salutation':" ",
#      'age' : 0,
#      'rating': ' ',
#      'is_online':True
#}
if choice == '1':
    SPY.name = SPY.name
    SPY.salutation = SPY.salutation
    SPY.age = SPY.age
    SPY.rating = SPY.rating
    SPY.is_online = SPY.is_online
else:
    SPY.name=raw_input("Enter your Name:")
    SPY.salutation=raw_input("Enter your Salutation(Mr. or Mrs.:)")
    SPY.age=raw_input("Enter your Age:")
    SPY.rating=raw_input("Enter your Rating:")
    SPY.is_online=True

#Validating the name of the spy
if SPY.name.isalpha() == False:
    print("Name is invalid")
    sys.exit(0)

#Validating the age of the spy
if int(SPY.age) <= 12 or int(SPY.age) >= 50:
    print("Age is invalid")
    sys.exit(0)

#Rating of the spy
if SPY.rating == 'A':
   print("you are a 3 star spy")
elif SPY.rating == 'B':
    print("you are a 2 star spy")
elif SPY.rating == 'C':
    print("you are a 1 star spy")
else:
    print("you have entered incorrect string")
    sys.exit(0)

print("Hello " + SPY.salutation + SPY.name + ".")
print("your age is %d" % int(SPY.age))
print("your rating is " + SPY.rating)
start_chat(SPY.name,SPY.salutation,SPY.age,SPY.rating)
