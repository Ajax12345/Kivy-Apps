import Tkinter as tk
import tkMessageBox
import os


class TextEditor:
    def __init__(self):
        self.main_window = tk.Tk()

        self.main_window.wm_title("Text editor")

        ######

        second_options = tk.Menu(self.main_window)
        new_filemenu = tk.Menu(second_options, tearoff=0)

        new_filemenu.add_command(label="Indent", command=self.indent)
        new_filemenu.add_command(label="Save", command=self.save_work)
        new_filemenu.add_separator()
        second_options.add_cascade(label="Paper", menu=new_filemenu)
        #self.main_window.config(menu=menu)
        self.main_window.config(menu=second_options)
        #####
        self.the_canvas = tk.Canvas(height = 200, width = 100)
        self.schedule_box = tk.Text(height = 400, width = 100)
        self.comp = tk.Label(text="Enter name of document and then click 'Save': ")
        self.composition_title = tk.Entry()
        self.comp.pack()
        self.composition_title.pack()
        self.the_canvas.pack()
        self.schedule_box.pack()

        #self.schedule_box.pack()

        tk.mainloop()

    def double_space(self):
        self.the_text = self.schedule_box.get("1.0", "end-1c")
        print self.the_text.split('.')

    def indent(self):
        self.the_text = self.schedule_box.get("1.0", "end-1c")
        self.mutated = ["       "+i for i in self.the_text.split('\n') if i != '']

        self.schedule_box.delete('1.0', 'end-1c')
        for i in self.mutated:
            self.schedule_box.insert('insert', i)

    def save_work(self):
        self.file_name = str(self.composition_title.get())
        self.the_text = self.schedule_box.get("1.0", "end-1c")
        if os.path.isfile(self.file_name+".txt"):
            self.f = open(self.file_name+".txt", 'w')
            self.f.write('')
            self.f.close()
            self.new_file = open(self.file_name+".txt", 'w')
            self.new_file.write(self.the_text)
            self.new_file.close()
        else:
            self.f = open(self.file_name+".txt", 'a')
            self.f.write(self.the_text)
            self.f.close()

         #removes all text
myapp = TextEditor()
