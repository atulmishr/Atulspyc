import sys
import spy_friend
from spy_details import SPY,ChatMessage
import csv

#funtion
STATUS_MESSAGE=[]
def add_status(current_status_message):

#print the current status message
    if current_status_message == None:
        print("you do not have any current status")
    else:
        print("Your current status is" + current_status_message)
#ask the user if wants to choose from the older status or want to add a new  status
    update_choice = raw_input("Do you want to select from older status(y/n)?")

#if the user wants to add a new status message,input the new status message
    if update_choice.upper() == 'N':
        new_status_message = raw_input("Enter New status Message:")
#validation of the status(is not empty and append it to the list holding all the status message)
        if len(new_status_message)>0:
            updated_status_message=new_status_message
            STATUS_MESSAGE.append(updated_status_message)

    elif update_choice.upper() == 'Y':
        for i in range(len(STATUS_MESSAGE)):
            print(str(i+1) + "   " + STATUS_MESSAGE[i])

        message_selection = int(raw_input("choose from the older message:"))
        if len(STATUS_MESSAGE) >= message_selection:
                updated_status_message = STATUS_MESSAGE[message_selection-1]

    return (updated_status_message)

#for loading a friend status
def load_status():
        read_object=open('status.csv','r')
        reader=csv.reader(read_object)
        for row in reader:
            STATUS_MESSAGE.append(row[0])
        read_object.close()
        if len(STATUS_MESSAGE)>0:
            return STATUS_MESSAGE[-1]
        else:
            return None

#for saving a status of friends
def save_status():
    write_object=open('write_object.csv','w')
    writer=csv.writer(write_object)
    for i in range(len(STATUS_MESSAGE)):
        writer.write_object([STATUS_MESSAGE[i]])
    write_object.close()
