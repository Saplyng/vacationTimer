from tkinter import *
import tkinter.messagebox as tkm
from datetime import *


def createJob():
    year = datetime.today().year

    job = cron.new(command='usr/bin/python /home/pi/onoff.py ' + str(entry5) + ' on', )


def main():
    box = Tk()
    box.geometry('800x800')
    box.title("Vacation Timer")

    # Message/toast/alert
    # tkm.showinfo("Title Area", "This is a message.")

    label1 = Label(box, text="Time/Date")
    labelOn = Label(box, text="ON")
    labelOff = Label(box, text="OFF")
    labelDate = Label(box, text="DATE")
    labelTime = Label(box, text="TIME")
    labelRoom = Label(box, text="ROOM")
    labelSpace = Label(box, text="")


    entry1 = Entry(box)
    entry2 = Entry(box)
    entry12 = Entry(box)
    entry13 = Entry(box)
    entry14 = Entry(box)
    entry15 = Entry(box)
    entry3 = Entry(box)
    entry4 = Entry(box)
    entry32 = Entry(box)
    entry33 = Entry(box)
    entry34 = Entry(box)
    entry35 = Entry(box)
    entry5 = Entry(box)

    Label.configure(labelSpace, width=2)
    Entry.configure(entry1, width=2)
    Entry.configure(entry2, width=2)
    Entry.configure(entry12, width=2)
    Entry.configure(entry13, width=2)
    Entry.configure(entry14, width=2)
    Entry.configure(entry15, width=2)
    Entry.configure(entry3, width=2)
    Entry.configure(entry4, width=2)
    Entry.configure(entry32, width=2)
    Entry.configure(entry33, width=2)
    Entry.configure(entry34, width=2)
    Entry.configure(entry35, width=2)
    Entry.configure(entry5, width=2)

    label1.grid(row=0, column=1, columnspan=9)
    labelOn.grid(row=1, column=1, columnspan=3)
    labelOff.grid(row=1, column=5, columnspan=3)
    labelDate.grid(row=2, column=0, stick=E)
    entry1.grid(row=2, column=1, stick=W)
    entry2.grid(row=2, column=2, stick=W)
    entry12.grid(row=2, column=3, stick=W)
    labelSpace.grid(row=2, column=4)
    entry13.grid(row=2, column=5, stick=E)
    entry14.grid(row=2, column=6, stick=E)
    entry15.grid(row=2, column=7, stick=E)
    labelTime.grid(row=3, column=0, stick=E)
    entry3.grid(row=3, column=1)
    entry4.grid(row=3, column=2)
    entry32.grid(row=3, column=3)
    entry33.grid(row=3, column=5)
    entry34.grid(row=3, column=6)
    entry35.grid(row=3, column=7)
    labelRoom.grid(row=4, column=0, stick=E)
    entry5.grid(row=4, column=1)

    box.mainloop()


if __name__ == '__main__':
    main()