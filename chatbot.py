from tkinter import *
from random import choice

ask = ["hi", "hello", "Hello"]
name = ["what is your name?", "What is your name?", "What is your name", "what is your name"]
nameans = ["My name is Pybot"]
nameask = ["What is your name"]
hi = ["hi", "hello", "Hello too"]
error = ["sorry", "sorry too"]
askabt = ["How are you?", "how are you?", "How are you", "how are you"]
askabtans = ["I am fine, thank you. How are you?"]
abtreply = ["I am fine", "fine"]
abtrepans = ["Ok!"]
byeque = ["bye", "tata", "going"]
byereply = ["bye", "see you again", "tata"]

root = Tk()
user = StringVar()
bot = StringVar()

root.geometry("1000x600")

root.title("chatbot")

chatWindow = Text(root, bd=1, bg='black', width=50, height=50, font=('Helvetica', 15), fg='white')
chatWindow.place(x=6, y=6, height=500, width=990)

msgWindow = Text(root, bg='black', width=30, height=4)
msgWindow.place(x=120, y=515, height=75, width=875)

userMsg = Entry(root, textvariable=user, fg='white', bg='black', font=('Helvetica', 15))
userMsg.place(x=126, y=525, height=60, width=860)

botMsg = Entry(root, textvariable=bot, fg='white', bg='black', font=('Helvetica', 15))

def main(event):
    que = user.get()
    chatWindow.insert(END, "user : "+que+'\n')
    if que in ask:
        bot.set(choice(hi))
    elif que in name:
        bot.set(choice(nameans))
    elif que in askabt:
        bot.set(choice(askabtans))
    elif que in abtreply:
        bot.set(choice(abtrepans))
    elif que in byeque:
        bot.set(choice(byereply))
    else:
        bot.set(choice(error))
    ans = bot.get()
    chatWindow.insert(END, "bot : "+ans+'\n')
    userMsg.delete(0, END)

#Create a button to send the message
root.bind('<Return>', main)

button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 20), command=main)
button.place(x=6, y=515, height=75, width=110)


mainloop()
