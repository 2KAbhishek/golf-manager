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

    # Create a label
    label = Label(root, text="Tee Time: (HH:MM)")
    label.grid(row=0, column=0, padx=10, pady=10)

    # Create a text entry box
    teeTimeEntry = Entry(root)
    teeTimeEntry.grid(row=0, column=1, padx=10, pady=10)
    teeTimeEntry.insert(0, "07:08")

    # Create a label
    label = Label(root, text="Course:")
    label.grid(row=1, column=0, padx=10, pady=10)

    # Create a radio button
    courseName = StringVar()
    courseName.set("Augusta.txt")
    R1 = Radiobutton(root, text="Augusta", variable=courseName,
                     value="Augusta.txt")
    R1.grid(row=1, column=1, padx=10, pady=10)

    R2 = Radiobutton(root, text="Laguna", variable=courseName,
                     value="Laguna.txt")
    R2.grid(row=2, column=1, padx=10, pady=10)

    R3 = Radiobutton(root, text="Pebble Bay", variable=courseName,
                     value="Pebble_Bay.txt")
    R3.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()
