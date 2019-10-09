from tkinter import *
import tkinter.messagebox as tkm
from datetime import *
from crontab import *


def createJob(monthOn, dayOn, hourOn, minuteOn, monthOff, dayOff, hourOff, minuteOff, pin):
    year = datetime.today().year
    #  job = cron.new(command='usr/bin/python /home/pi/onoff.py ' + str(entry5) + ' on', )
    print(pin)
    print(monthOn, dayOn, hourOn, minuteOn)
    print(monthOff, dayOff, hourOff, minuteOff)
    print("hi")

    on_list = [monthOn, dayOn, hourOn, minuteOn]
    off_list = [monthOff, dayOff, hourOff, minuteOff]

    cron = CronTab(user='pi')

    job_on = cron.new(command='/usr/bin/python /home/pi/pi_projects/vacationTimer/onoff.py ' + pin + ' on',
                      comment='vacaID')
    job_on.setall(datetime(int(year), int(monthOn), int(dayOn), int(hourOn), int(minuteOn)))

    job_off = cron.new(command='/usr/bin/python /home/pi/pi_projects/vacationTimer/onoff.py ' + pin + ' off',
                       comment='vacaID')
    job_off.setall(datetime(int(year), int(monthOff), int(dayOff), int(hourOff), int(minuteOff)))

    cron.write()

    print(job_on)


def main():
    box = Tk()
    box.geometry('800x800')

    box.title("Vacation Timer")

    # Message/toast/alertimport RPi.GPIO as GPIO


    # tkm.showinfo("Title Area", "This is a message.")

    label1 = Label(box, text="Time/Date")
    labelOn = Label(box, text="ON")
    labelOff = Label(box, text="OFF")
    labelMonth = Label(box, text="MONTH")
    labelDay = Label(box, text="DAY")
    labelHour = Label(box, text="HOUR")
    labelMinute = Label(box, text="MINUTE")
    labelRoom = Label(box, text="ROOM")
    labelSpace = Label(box, text="")

    month_on = Entry(box)
    day_on = Entry(box)
    hour_on = Entry(box)
    minute_on = Entry(box)

    month_off = Entry(box)
    day_off = Entry(box)
    hour_off = Entry(box)
    minute_off = Entry(box)

    room_number = Entry(box)

    btnAdd = Button(box, text="Add", command=lambda: createJob(month_on.get(), day_on.get(), hour_on.get(), minute_on.get(),
                                                               month_off.get(), day_off.get(), hour_off.get(), minute_off.get(),
                                                               room_number.get()))


    Label.configure(labelSpace, width=2)
    Entry.configure(month_on, width=2)
    Entry.configure(month_off, width=2)
    Entry.configure(day_on, width=2)
    Entry.configure(day_off, width=2)
    Entry.configure(hour_on, width=2)
    Entry.configure(hour_off, width=2)
    Entry.configure(minute_on, width=2)
    Entry.configure(minute_off, width=2)
    Entry.configure(room_number, width=2)

    label1.grid(row=0, column=1, columnspan=9)
    labelOn.grid(row=1, column=1, columnspan=3)
    labelOff.grid(row=1, column=5, columnspan=3)
    labelMonth.grid(row=2, column=0, stick=E)
    month_on.grid(row=2, column=2, stick=W)
    labelSpace.grid(row=2, column=4)
    month_off.grid(row=2, column=6, stick=E)
    labelDay.grid(row=3, column=0, stick=E)
    day_on.grid(row=3, column=2)
    labelSpace.grid(row=3, column=4)
    day_off.grid(row=3, column=6)
    labelHour.grid(row=4, column=0, stick=E)
    hour_on.grid(row=4, column=2, stick=E)
    hour_off.grid(row=4, column=6, stick=E)
    labelMinute.grid(row=5, column=0, stick=E)
    minute_on.grid(row=5, column=2, stick=E)
    minute_off.grid(row=5, column=6, stick=E)
    labelRoom.grid(row=6, column=0, stick=E)
    room_number.grid(row=6, column=1)
    btnAdd.grid(row=7, column=1)

    box.mainloop()


if __name__ == '__main__':
    main()