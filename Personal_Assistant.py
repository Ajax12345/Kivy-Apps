from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import Color
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from gtts import gTTS

import time
import datetime
import speech_recognition as sr
import os


class Personal_Assistant(BoxLayout):


    def greeting(self):

        self.time_now = datetime.datetime.now().hour
        if 12 > self.time_now > 5:
            return 'Good Morning, James'
        elif 17> self.time_now > 12:
            return 'Good Afternoon, James'

        elif 22> self.time_now > 17:
            return 'Good Evening, James'



    def reminder(self):
        self.time_now = datetime.datetime.now().hour #this might be able to go in greeting()
        self.the_day_now = datetime.datetime.now().strftime("%A")
        if self.time_now == 11 and (the_day_now == 'Tuesday' or the_day_now == 'Thursday'):

            os.system("say 'you have calculus in twenty minutes'")

        elif self.time_now == 14 and the_day_now == 'Friday':

            return os.system("say 'you have composition at two thirty'")

        elif self.time_now == 18 and the_day_now == 'Monday':

            os.system("say 'Your python class is starting soon'")

    def on_click(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source) #might need self


        try:
            #might need self

            my_audio_input = r.recognize_sphinx(audio)

            if my_audio_input == 'monday schedule':

                os.system("say 'Your python class is on Monday evenings'")

            elif my_audio_input == 'tuesday schedule':
                os.system("say 'you have assumption in the morning, then calculus at eleven. Finally, you meet with david in the afternoon. That is a busy day!'")

            elif my_audio_input == 'wednesday schedule':
                os.system("say 'nothing is scheduled for wednesday, however, I suggest you work on composition'")

            elif my_audio_input == 'thursday schedule':
                os.system("say 'You have calculus in the morning at eleven'")

            elif my_audio_input == 'friday schedule':
                os.system("say 'you have composition in the afternoon at two thirty'")

            elif my_audio_input == 'i hate you':
                os.system("say 'I hate you too'")

            elif my_audio_input == 'what is your name':


                os.system("say 'my name is Jarvis. At your service'")

            elif my_audio_input == 'hello':
                os.system("say 'hi'")


            else:
                os.system("say 'I do not understand what was said'")

                #might need self
        except sr.UnknownValueError:

            os.system("say 'I am sorry, I do not understand what was said'")
            #might need self
        except sr.RequestError as e:
            os.system("say 'Internal error. Please try again'")

        except:
            os.system("say 'Unkown error. I am working on this problem'")

    def news(self):
        pass



class Tester(App):
    def build(self):
        return Personal_Assistant()



if __name__ == '__main__':
    Tester().run()
