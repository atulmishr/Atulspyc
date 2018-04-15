from steganography.steganography import Steganography
from datetime import datetime
friends=[]
def add_friend():
    #new_friend = {
    #             'name' : " ",
    #             'salutation' : " ",
    #             'age' : 0,
    #             'rating' : ' ',
    #             'is_online':True,
    #             'chats':[]
    #}
    new_friend.name = raw_input("Enter your name:")
    new_friend.salutation = raw_input("should we call you Mr. or Mrs.:")
    new_friend.age = int(raw_input("Enter your Age:"))
    new_friend.rating = raw_input("Enter your Rating:")

    if new_name.isalpha() == False:
        print("invalid name")
        sys.exit(0)
    if new_age <=12 or new_age >= 50:
        print("invalid Age")
        sys.exit(0)

    friends_name.append(new_friend)

def select_a_friend():
#print the all friends of a user
  for friend in friends():
    print('%d.%s' % (item_number+1),friend['name'])
    item_number = item_number + 1

#Asking the user for Select a friend
    friend_choice = raw_input("choose from your friends list")
    friend_choice_position = friend_choice - 1

#Returning the index
    return friend_choice_position

#for sending a secret message

def send_message():
    #friend_choice = select_a_friend()
    original_name = raw_input("what is the name of the image:")
    output_path='output.jpg'
    text = raw_input("what you want to say")
    Steganography.encode(original_name,output_path,text)

    #new_chat = {
    #    "message":text,
    #    "time":datetime.now(),
    #    "sent_by_me": True
    #}

    #friend[friend_choice].chats.append(new_chat)
    print("your secret message is ready")

def read_message():
    #sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    #new_chat = ChatMessage(secret_text, False)
    #new_chat = {
    #    "message": secret_text,
    #    "time":datetime.now(),
    #    "sent_by_me": False
    #}
    #friend[sender].chats.append(new_chat)
    print("your secret message has been  saved\n")
    print(secret_text)
