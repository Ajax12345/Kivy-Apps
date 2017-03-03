import Tkinter as tk
import tkMessageBox
import random
import sys
sys.setrecursionlimit(500)

class ServerAssigner:
    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.wm_title("Schedule Master 3.0")

        self.schedule_box = tk.Text(height = 100, width = 30)
        self.the_canvas = tk.Canvas(height = 100, width = 50)
        self.the_canvas.pack()
        self.schedule_box.pack(side="right")

        self.the_title = tk.Label(text="Position List. Enter all names with a space between")

        self.MC_Label = tk.Label(text="Enter the MCs:")
        self.thurifer_label = tk.Label(text="Enter The Thurifers:")
        self.acolyte1_label = tk.Label(text="Enter The Acolyte 1s:")
        self.acolyte2_label = tk.Label(text="Enter The Acolye 2s:")
        self.boat_label = tk.Label(text="Enter Boat Bearers:")
        self.ccbs_label = tk.Label(text="Enter The Cross Bearers:")
        self.torches_label = tk.Label(text="Enter The Torch Bears:")


        self.the_mcs = tk.Entry()

        self.thurifers = tk.Entry()
        self.the_title.pack()
        self.MC_Label.pack()
        self.the_mcs.pack(pady=15)
        self.thurifer_label.pack()
        self.thurifers.pack(pady=15)

        self.acolyte1 = tk.Entry()
        self.acolyte1_label.pack()
        self.acolyte1.pack(pady=15)
        self.acolyte2 = tk.Entry()
        self.acolyte2_label.pack()
        self.acolyte2.pack(pady=15)
        self.boat_label.pack()
        self.bbs = tk.Entry()

        self.bbs.pack(pady=15)
        self.ccbs_label.pack()
        self.cbs = tk.Entry()
        self.cbs.pack(pady=15)
        self.torches_label.pack()
        self.torches = tk.Entry()
        self.torches.pack(pady=15)
        self.number_of_Sundays = tk.Label(text="Number of Weeks: ")
        self.number_of_Sundays.pack()
        self.Sunday_number = tk.Entry()
        self.Sunday_number.pack()
        self.make_schedule = tk.Button(text="Print Schedule", height=10, width=16, command=self.print_schedule, bg="blue")
        self.make_schedule.pack(pady=10)




        tk.mainloop()

    def print_schedule(self):
        self.mcs = str(self.the_mcs.get())
        self.the_thurifers = str(self.thurifers.get())
        self.mcs = self.mcs.split()
        self.the_thurifers = self.the_thurifers.split()
        self.acolyte1s = str(self.acolyte1.get())
        self.acolyte2s = str(self.acolyte2.get())
        self.boat = str(self.bbs.get())
        self.cross = str(self.cbs.get())
        self.bears = str(self.torches.get())
        self.acolyte1s = self.acolyte1s.split()
        self.acolyte2s = self.acolyte2s.split()
        self.boat = self.boat.split()
        self.cross = self.cross.split()
        self.bears = self.bears.split()
        self.number = int(self.Sunday_number.get())
        for i in range(self.number):
            self.schedule_box.insert('insert', "Week"+str(i+1)+":"+'\n'+"MC:"+random.choice(self.mcs)+"\n"+"Thurifers:"+random.choice(self.the_thurifers)+"\n"+"Acolyte 1:"+random.choice(self.acolyte1s)+"\n"
            +"Acolyte 2:"+random.choice(self.acolyte2s)+"\n"+"Boat Bearer:"+random.choice(self.boat)+"\n"+"Cross Bearer:"+random.choice(self.cross)+'\n'+"Torch Bearers:"+random.choice(self.bears)+" "+random.choice(self.bears)+"\n"+"\n")



my_app = ServerAssigner()
