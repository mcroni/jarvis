from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ListProperty,ObjectProperty,NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp
from material.flatui.flatui import FloatingAction, RaisedButton, _MaterialButton
from garden import *
from sqlalchemy import *
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


##############UI########################
class MyTab(GridLayout, AndroidTabsBase):
    pass


class MyTabb(FloatLayout,AndroidTabsBase):
    thoughts = ObjectProperty()


class MyTabbb(FloatLayout,AndroidTabsBase):
    pass


class MyScreenManager(ScreenManager,Screen):
    pass

class ShoppingScreen(Screen):
    pass

class DonationScreen(Screen):
    pass

class WindowScreen(Screen):
    pass

class StatsScreen(Screen):
    pass

class CreditScreen(Screen):
    pass

class MiscScreen(Screen):
    pass






##############APP #########################
class ExampleApp(App):
    thoughts = ObjectProperty()
    def build(self):
        android_tabs = AndroidTabs()
        return android_tabs


if __name__=='__main__':
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    LabelBase.register(name='Modern Pictograms',
                       fn_regular='modernpics.ttf')
    LabelBase.register(name='Heydings',
                       fn_regular='heydings.ttf')

    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf')


    Window.clearcolor = get_color_from_hex('#008CD4')
    ExampleApp().run()
