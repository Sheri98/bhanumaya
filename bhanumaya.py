import requests
from tkinter import *

def Recieve():
    url = "http://localhost:8080/dashboard/book.json"
    x = requests.get(url=url).json()
    label = Label(root,text=x)
    label.grid(row=2, column=0)
# def Post():
#     url = "http://localhost:8080/dashboard/book.json"
#     kunden = JSON.parse([book.json]);


root = Tk()
root.title("Api Data_Fetch")
root.geometry("400x400")
Recieve = Button(root,text="View",command= Recieve)
Recieve.grid(row=0,column=0)
Post = Button(root,text="Post")
Post.grid(row=1,column=0)

root.mainloop()



##########updated################################################

import requests
from tkinter import *
import json


def Recieve():
    url = "http://localhost:8080/dashboard/book.json"
    x = requests.get(url=url)
    y = json.loads(x.text)
    l = Label(root).grid(row=2,column=0)
    label = Label(root,text=json.dumps(y,indent=2))
    label.grid(row=3,column=3)


def Post():
    url = "http://localhost:8080/dashboard/"
    with open('D:\\xampp\\htdocs\\dashboard\\book.json','r+') as f:
        data = json.load(f)
        data['name'] = entry.get()
        f.seek(0)
        json.dump(data,f,indent=2)
        f.truncate()




root = Tk()
root.title("Api Data_Fetch")
root.geometry("400x400")
Recieve = Button(root,text="View",command= Recieve,font=('calibri',15,'bold'))
Recieve.grid(row=0,column=1,pady=10,padx=10)
Post = Button(root,text="Post",command=Post,font=('calibri',15,'bold'))
Post.grid(row=0,column=2,pady=10)
entry = Entry(root, text="enter book name to update.",font=('calibri',15,'bold'))
entry.grid(row=0, column=3)
root.mainloop()
