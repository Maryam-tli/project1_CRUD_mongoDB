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

# get selection
def set_to_entries(event):
    selected_item = tbl.focus()  # آیتم انتخاب شده
    if selected_item:
        values = tbl.item(selected_item, 'values')
        if values:
            Id.set(values[1])
            Name.set(values[2])
            Age.set(values[3])
            Section.set(values[4])

# تابع برای حذف سطر انتخابی و پاک کردن ورودی‌ها delete
def delete_person():
    # آیتم انتخاب شده از جدول
    selected_item = tbl.focus()

    if selected_item:
        # دریافت مقادیر از آیتم انتخاب شده
        values = tbl.item(selected_item, 'values')

        if values:
            # حذف از جدول
            tbl.delete(selected_item)

            # حذف از پایگاه داده MongoDB با استفاده از "Id"
            persons.delete_one({"Id": values[0]})

            # پاک کردن فیلدهای ورودی
            Id.set("")
            Name.set("")
            Age.set("")
            Section.set("")


#اضافه کردن تابع به‌روزرسانی  update
def update_person():
    # آیتم انتخاب شده از جدول
    selected_item = tbl.focus()

    if selected_item:
        # دریافت مقادیر از آیتم انتخاب شده
        values = tbl.item(selected_item, 'values')

        if values:
            # به‌روزرسانی جدول با مقادیر جدید
            tbl.item(selected_item, values=(
                Id.get(), Name.get(), Age.get(), Section.get()))

            # به‌روزرسانی رکورد در MongoDB با استفاده از "Id"
            persons.update_one(
                {"Id": values[0]},  # شرط جستجو برای پیدا کردن رکورد قدیمی
                {
                    "$set": {
                        "Id": Id.get(),
                        "Full Name": Name.get(),
                        "Age": Age.get(),
                        "Section": Section.get()
                    }
                }
            )

            # پاک کردن فیلدهای ورودی بعد از به‌روزرسانی
            Id.set("")
            Name.set("")
            Age.set("")
            Section.set("")
