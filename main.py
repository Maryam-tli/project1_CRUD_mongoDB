#import کتابخانه های لازم
from tkinter import *
from tkinter import ttk
from pymongo import MongoClient

# اتصال به MongoDB
Client = MongoClient("localhost", 27017)
db = Client["person"]
persons = db["persons"]

screen = Tk()
