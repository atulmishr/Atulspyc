from datetime import datetime
class SPY:

     def __init__(self,name,salutation,age,rating):
         self.name = name
         self.salutation = salutation
         self.age = age
         self.rating = rating
         self.is_online = True
         self.chats = []
         self.current_status_message = none

#spy = SPY('Naag Rajan','Mr.',40,'A')

#add friend of our Spy
#friend_one = Spy('Nirmal','Mr.',25,'B')
#friend_two = Spy('Madhu','Mrs.',27,'C')
#friend_three = Spy('Deepak','Mr.',24,'A')
#friend_four = Spy('Prem','Mr.',27,'B')
#friend_five = Spy('Nisha','Mrs.',26,'A')

#friend = [friend_one,friend_two,friend_three,friend_four,friend_five]

#create chat message
class ChatMessage:
     def __init__(self,message,sent_by_me):
         self.message = message
         self.timeStamp = datetime.now()
         self.sent_by_me = sent_by_me

def load_friends():
    read_object=open('friends.csv','r')
    reader=csv.reader(read_object)
    for row in reader:
        #order will be(name,age,salutation,rating)
        name = row[0]
        salutation = row[1]
        age =int(row[2])
        rating = row[3]
        is_online = bool(row[4])
        new_friend = SPY(name,salutation,age,rating)
        friends.append(new_friend)
    read_object.close()

def save_friends():
        write_object=open('friends.csv','w')
        writer = csv.writer(write_object)
        for i in range(len(friends)):
            name = friends[i].name
            salutation = friends[i].salutation
            age = friends[i].age
            rating = friends[i].is_online
            writer.writerow([name,salutation,age,rating,is_online])
        write_object.close()
