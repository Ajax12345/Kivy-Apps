from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import Color
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.screenmanager import ScreenManager, Screen



#here, you can use Builder.load_string(""" kivy code goes here """)

class Test(TabbedPanel):
    kalinka_song = SoundLoader.load('/Users/davidpetullo/Downloads/Alexandrov-Red-Army-Choir-Kalinka-_SUBTITLES_.wav')
    o_sole_mio_song = SoundLoader.load('/Users/davidpetullo/Downloads/o-sole-mio-__.wav')
    my_fields = SoundLoader.load('/Users/davidpetullo/Downloads/Red-Army-Choir-Polyushka-Polye.wav')
    my_smuglyanka = SoundLoader.load('/Users/davidpetullo/Downloads/Red-Russian-Army-Choir-Smuglyanka-Moldavanka.wav')
    my_nessun_dorma = SoundLoader.load('/Users/davidpetullo/Downloads/Pavarotti\ -\ Nessun\ Dorma\ 1994\ \(High\ Quality\ With\ Lyrics\).wav')


    def kalinka(self):
        if self.kalinka_song.state == 'stop':
            self.kalinka_song.play()
        else:
            self.kalinka_song.stop()   #this enables the music to be stopped or started by clicking


             #this works!!!!! Reference this function in kivy
    def o_sole_mio(self):
        if self.o_sole_mio_song.state == 'stop':
            self.o_sole_mio_song.play()
        else:
            self.o_sole_mio_song.stop()


    def fields(self):
        if self.my_fields.state == 'stop':
            self.my_fields.play()
        else:
            self.my_fields.stop()

    def smuglyanka(self):
        if self.my_smuglyanka.state == 'stop':
            self.my_smuglyanka.play()

        else:
            self.my_smuglyanka.stop()

    def nessun_dorma(self):
        if self.my_nessun_dorma.state == 'stop':
            self.my_nessun_dorma.play()

        else:
            self.my_nessun_dorma.stop()

    def core_ngrato(self):
        if self.my_core_ngrato.state == 'stop':
            self.my_core_ngrato.play()
        else:
            self.my_core_ngrato.stop()

    def stars_and_stripes(self):
        if self.my_starsandstripesforever.state == 'stop':
            self.my_starsandstripesforever.play()

        else:
            self.my_starsandstripesforever.stop()


class TabbedPanelApp(App):
    def build(self):
        return Test()



if __name__ == '__main__':
    TabbedPanelApp().run()

#use this for designing the framwork, and then use TabbedPanelApp.kv for the graphics
#for audio, work on the color of the buttons, make several buttons, all styled, and try to find audio files
#color: for text color
#background_color: for the background. always put parenthesis around color codes
