#import کتابخانه های لازم
from tkinter import *
from tkinter import ttk
from pymongo import MongoClient

# اتصال به MongoDB
Client = MongoClient("localhost", 27017)
db = Client["person"]
persons = db["persons"]

screen = Tk()

Id = StringVar()
Name = StringVar()
Age = StringVar()
Section = StringVar()

def add_person():
    # dictionary از اطلاعات وارد شده
    person = {
        "Id": Id.get(),
        "Full Name": Name.get(),
        "Age": Age.get(),
        "Section": Section.get()
    }

    # اضافه کردن شخص به جدولadd tbl
    tbl.insert("", "end", values=(
        person["Id"], person["Full Name"], person["Age"], person["Section"]))

    # اضافه کردن شخص به پایگاه داده MongoDB
    persons.insert_one(person)

# read MongoDB و نمایش در جدول هنگام راه‌اندازی برنامه
def load_data():
    for person in persons.find():
        tbl.insert("", "end", values=(
        person["Id"], person["Full Name"], person["Age"], person["Section"]))

