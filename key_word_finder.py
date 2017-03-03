import Tkinter as tk
import tkMessageBox
class KeyWordApp:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.wm_title("KeyWord picker")
        self.the_canvas = tk.Canvas(height = 36, width = 300)
        self.the_canvas.pack()
        self.story_box = tk.Text(height = 36, width = 30)
        self.output_box = tk.Text(height = 36, width=90)

        self.story_box.pack(side="left")
        self.output_box.pack(side="right")
        self.key_word_box = tk.Entry()
        self.key_word_box.pack()
        self.input_button = tk.Button(height = 20, width = 10, command=self.find_keywords)
        self.input_button.pack()
        tk.mainloop()

    def find_keywords(self):
        self.story_data = self.story_box.get("1.0", "end-1c")
        self.the_key_word = self.key_word_box.get()

        self.new_story_data = self.story_data.split('.')
        for i in self.new_story_data:
            if i.count(self.the_key_word) > 0:
                self.output_box.insert('insert', i+'\n')


the_app = KeyWordApp()
