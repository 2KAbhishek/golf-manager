import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import tkinter.font as tkFont
from course import Course


def showSchedule():
    try:
        course_obj = Course("../data/" + courseName.get().strip())
        schedule = course_obj.getScheduleStr(teeTimeEntry.get().strip())
        scroll.delete(1.0, END)
        scroll.insert(INSERT, schedule)
    except Exception as e:
        print(e)
        scroll.delete(1.0, END)
        scroll.insert(INSERT, "Please enter valid input")


def clearFields():
    scroll.delete(1.0, END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Golf Schedule")
    root.geometry("360x640")


    root.mainloop()
