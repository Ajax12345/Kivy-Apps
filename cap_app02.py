from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

Builder.load_string("""
<CAP>:



    canvas:

        Rectangle:
            pos: self.pos
            size: self.size
            source: "/Users/davidpetullo/Desktop/bdaa2fd1e8809cc37b60cdf88969db7a.jpg"





    ActionBar:
        size: (40,75)
        pos_hint: {'x':10, 'y':0}
        background_color: (0, 0, 255, 0.9)
        pos_hint: {'top':1}
        ActionView:

            ActionPrevious:
                app_icon: "/Users/davidpetullo/Desktop/logo2.png"

                with_previous: False
                markup: True



    Button:
        background_color: (0, 0, 255, 0.9)

        id: btn

        on_release: dropdown.open(self)
        size_hint_y: None
        pos_hint: {'x':0.3, 'y':0.9}


        height: 60
        Image:
            source: "/Users/davidpetullo/Desktop/stuffcontentmgrfiles2ac67e44c30a21635f8a9d498f832bc1cmisc_resized80_313_257_hamenu.png"
            y: self.parent.y + self.parent.height - 50
            x: self.parent.x+300
            size: 50, 40
            allow_stretch: True

    DropDown:

        id: dropdown
        on_parent: self.dismiss()
        on_select: btn.text = '{}'.format(args[1])

        Button:
            text: 'Cadet Programs'

            background_color: (0, 0, 0, 0.8)

            size_hint_y: None
            height: 60
            on_release: root.sPop()



        Button:
            background_color: (0, 0, 0, 0.8)
            text: 'Emergency Services'
            size_hint_y: None
            height: 60
            on_release: root.sPop1()



        Button:
            background_color: (0, 0, 0, 0.8)
            text: 'Aerospace'
            size_hint_y: None
            height: 60
            on_release: root.sPop2()

    """)




class CAP(BoxLayout):

    def sPop(self):
        box = BoxLayout(background_color=(0, 255, 0, 0.8))
        #add everything to a boxlayout that is then passed to the popup box
        closer = Button(text="Close", pos_hint={'x': 6, 'center_y': 0.04}, size_hint=(0.1, 0.1), background_color=(0, 0, 255, 0.7)) #perfect sizing
        box.add_widget(closer)

        box.add_widget(Label(text="As part of their leadership education, cadets participate in drill and ceremonies.\nDrill is an excellent way to promote teamwork and develop an appreciation for Air Force traditions.", index=6))
        #p = Popup(title = "Drill and Ceremony", content = box, size=(25, 25), background="Users/davidpetullo/Desktop/drill_team_A9197512D2D2B.jpg")
        p = Popup(title = "Cadet Programs", content = box, size=(25, 25))
        with p.canvas:
            p.rect = Rectangle(size = (350, 150), pos=(250, 400), source = "/Users/davidpetullo/Desktop/drill_team_A9197512D2D2B.jpg")
            #(350, 150), (250, 400)
        p.background_color=(0, 0, 255, 0.9)

        closer.bind(on_press=p.dismiss)
        p.open()


    def sPop1(self):
        box = BoxLayout(background_color=(0, 255, 0, 0.8))
            #add everything to a boxlayout that is then passed to the popup box
        closer = Button(text="Close", pos_hint={'x': 6, 'center_y': 0.04}, size_hint=(0.1, 0.1), background_color=(0, 0, 255, 0.7)) #perfect sizing
        box.add_widget(closer)

        box.add_widget(Label(text="Growing from its World War II experience, the Civil Air Patrol has continued\n to save lives and alleviate human suffering through a myriad \nof emergency-services and operational missions.", index=6))
            #p = Popup(title = "Drill and Ceremony", content = box, size=(25, 25), background="Users/davidpetullo/Desktop/drill_team_A9197512D2D2B.jpg")
        p = Popup(title = "Emergency Services", content = box, size=(25, 25))
        with p.canvas:
            p.rect = Rectangle(size = (350, 200), pos=(250, 350), source = "/Users/davidpetullo/Desktop/51f99ce69553530d0f3b53840d3f6457.jpg")

        p.background_color=(0, 0, 255, 0.9)

        closer.bind(on_press=p.dismiss)
        p.open()

    def sPop2(self):
        box = BoxLayout(background_color=(0, 255, 0, 0.8))
            #add everything to a boxlayout that is then passed to the popup box
        closer = Button(text="Close", pos_hint={'x': 6, 'center_y': 0.04}, size_hint=(0.1, 0.1), background_color=(0, 0, 255, 0.7)) #perfect sizing
        box.add_widget(closer)

        box.add_widget(Label(text="Aerospace Education (AE) is one of the three primary missions of the Civil Air Patrol. \n There are two aspects to this program. The first is public oriented education programs \ndirected toward the aviation community and the public at large. \n The second is an internally focused program directed at CAP members, \n primarily Cadet members as part of their training program.", index=6))
            #p = Popup(title = "Drill and Ceremony", content = box, size=(25, 25), background="Users/davidpetullo/Desktop/drill_team_A9197512D2D2B.jpg")
        p = Popup(title = "Aerospace", content = box, size=(25, 25))
        with p.canvas:
            p.rect = Rectangle(size = (450, 200), pos=(200, 350), source = "/Users/davidpetullo/Desktop/AirFleet.jpg")
        p.background_color=(0, 0, 255, 0.9)

        closer.bind(on_press=p.dismiss)
        p.open()


'''
    canvas.before:
        Color:
            rgba: (0, 0, 255, 0.9)
        Rectangle:
            pos: self.pos
            size: self.size

'''

class TabbedPanelApp(App):
    def build(self):
        return CAP()

if __name__ == "__main__":
    TabbedPanelApp().run()
