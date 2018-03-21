import sys
import default
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
