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
