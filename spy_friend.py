friends=[]
def add_friend():
    new_friend = {
                 'name' : " ",
                 'salutation' : " ",
                 'age' : 0,
                 'rating' : ' ',
                 'is_online':True
    }
    new_friend['name'] = raw_input("Enter your name:")
    new_friend['salutation'] = raw_input("should we call you Mr. or Mrs.:")
    new_friend['age'] = int(raw_input("Enter your Age:"))
    new_friend['rating'] = raw_input("Enter your Rating:")

    if new_name.isalpha() == False:
        print("invalid name")
        sys.exit(0)
    if new_age <=12 or new_age >= 50:
        print("invalid Age")
        sys.exit(0)

    friends_name.append(new_friend)
