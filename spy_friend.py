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
