import sys
import default
import spy_status
import spy_friend

def start_chat(spy_name,spy_salutation,spy_age,spy_rating):
    current_status_message=None
    show_menu = True
    while show_menu == True:
        Menu_choice = raw_input("1.Add a status update\n2.Add a friend\n3.Exit Application")
        if Menu_choice == '1':
            #update the status
           print("you have choosn to add a status")
           current_status_message = spy_status.add_status(current_status_message)
        elif Menu_choice =='2':
             print("you have to choosen to add a friend")
             spy_friend.add_friend()
        elif Menu_choice == '3':
             show_menu=False

print("Welcome to Spychat Application")
choice = raw_input("Enter 1 for default choice:")

spy = {
     'name' : " ",
     'salutation' : " ",
     'age' : 0,
     'rating' : ' ',
     'is_online':True
}
if choice == '1':
    spy['name'] = default.spy['name']
    spy['salutation'] = default.spy['salutation']
    spy['age'] = default.spy['age']
    spy['rating'] = default.spy['rating']
    spy['is_online'] = default.spy['is_online']
else:
    spy['name']=raw_input("Enter your Name:")
    spy['salutation']=raw_input("Enter your Salutation(Mr. or Mrs.:)")
    spy['age']=raw_input("Enter your Age:")
    spy['rating']=raw_input("Enter your Rating:")
    spy['is_online']=True

#Validating the name of the spy
if spy['name'].isalpha() == False:
    print("Name is invalid")
    sys.exit(0)

#Validating the age of the spy
if int(spy['age']) <= 12 or int(spy['age']) >= 50:
    print("Age is invalid")
    sys.exit(0)

#Rating of the spy
if spy['rating'] == 'A':
   print("you are a 3 star spy")
elif spy['rating'] == 'B':
    print("you are a 2 star spy")
elif spy['rating'] == 'C':
    print("you are a 1 star spy")
else:
    print("you have entered incorrect string")
    sys.exit(0)

print("Hello " + spy['salutation'] + spy['name']+".")
print("your age is %d" % (spy['age']))
print("your rating is " + spy['rating'])
start_chat(spy['name'],spy['salutation'],spy['age'],spy['rating'])
