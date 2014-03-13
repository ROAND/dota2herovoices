from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class RSGrid(GridLayout):
    category = 'Radiant Strength'

class RAGrid(GridLayout):
    category = 'Radiant Agility'

class RIGrid(GridLayout):
    category = 'Radiant Inteligence'

class Dota2HeroMain(Widget):
    pass

class Dota2HeroVoicesApp(App):
    def build(self):
        main = Dota2HeroMain()
        return main

if __name__=="__main__":
    Dota2HeroVoicesApp().run()
