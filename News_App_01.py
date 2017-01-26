from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
import feedparser

Builder.load_string("""
<My_News_Feed>:
    do_default_tab: False
    Widget:
        background_color: (0, 0, 255, 0.6)
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos

    TabbedPanelItem:
        background_color: (0, 0, 255, 0.6)
        text: 'Politics'
        Label:
            text: root.politics()

    TabbedPanelItem:
        background_color: (255, 255, 0, 0.7)
        text: 'Science and Tech'
        Label:
            text: root.more_tech()

    TabbedPanelItem:
        background_color: (0, 0, 255, 0.9)
        text: 'Python News'
        Label:
            text: 'where python news goes'

    TabbedPanelItem:
        background_color: (0, 255, 0, 0)
        text: "Tech news"
        Label:
            text: root.tech_and_science()

    TabbedPanelItem:
        background_color: (0, 255, 255, 0)
        text: "Health and wellness"
        Label:
            text: root.health_and_wellness()

""")

class My_News_Feed(TabbedPanel):
    def politics(self):
        d = feedparser.parse('http://nm.nmcdn.us/rss/Politics/1')
        return d['entries'][0]['title']
        return d['entries'][1]['title']
        return d['entries'][2]['title']
        return d['entries'][3]['title']
        return d['entries'][4]['title']

    def tech_and_science(self):
        a = feedparser.parse('http://nm.nmcdn.us/rss/SciTech/20')
        return a['entries'][0]['title']
        return a['entries'][1]['title']
        return a['entries'][2]['title']
        return a['entries'][3]['title']
        return a['entries'][4]['title']

    def more_tech(self):
        c = feedparser.parse('https://techviral.com/feed/')
        return c['entries'][0]['title']
        return c['entries'][1]['title']
        return c['entries'][2]['title']
        return c['entries'][3]['title']

    def health_and_wellness(self):
        b = feedparser.parse('http://nm.nmcdn.us/rss/Diet-And-Fitness/185')
        self.my_string = b['entries'][0]['title'] + '\n' + '\n'+ b['entries'][1]['title'] + '\n'+ '\n'+ b['entries'][2]['title'] + '\n' + '\n'+ b['entries'][3]['title']
        return self.my_string




class the_news(App):
    def build(self):
        return My_News_Feed()



if __name__ == '__main__':
    the_news().run()
