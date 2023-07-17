#Author: Jure Cej
#Date: 5.9.2017

from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import random

color1 = [0.0, 0.4, 0.8, 0.8]
color2 = [1, 1, 0.8, 1]
color3 =  [1, 0, 0, 0.8]
color4 = [1, 1, 1, 1]

Window.clearcolor = (1, 1, 0.8, 1)

class Igra(GridLayout):
    def __init__(self):
        super(Igra, self).__init__()
        self.cols = 1

        self.players=[]

        self.igralec=-1

        self.label = Label(text='[size=80][b]THE GAME[/b][/size]', color=color1, font_size='26sp', halign='center', markup=True)
        self.add_widget(self.label)

        self.textinput1 = TextInput(text='Vpiši ime igralca tukaj.', size_hint=(.2, .3), font_size='36sp', multiline=False)
        self.add_widget(self.textinput1)

        self.button3 = Button(text='+ Dodaj igralca', font_size='56sp', size_hint=(.2, .3), background_color=color1, color=color2, on_press=self.textinput, markup=True)
        self.add_widget(self.button3)

        self.button1 = Button(text='[b]Začni[/b]', font_size='70sp', size_hint=(.2, .8), color=color2, background_color=color1, markup=True)
        self.add_widget(self.button1)
        
        self.button2 = Button(text='Izhod', font_size='56sp', size_hint=(.2, .3), background_color=color1, color=color3, on_release=self.stop, markup=True)
        self.add_widget(self.button2)

    def textinput(self, event):
        self.players.append(self.textinput1.text)
        self.textinput1.text=''
        self.button1.on_press=self.button_state

    def button_state(self):
            thiselem = self.players[self.igralec]
            self.igralec = (self.igralec + 1) % len(self.players)
            nextplayer = self.players[self.igralec]
            self.list=['[size=60]Pije[/size]\nIgralec, ki je na vrsti, naredi en požirek.', '[size=60]Pijejo vsi[/size] \nVsi pijejo en požirek.', '[size=60]Pije levo[/size]\nLevi sosed igralca, ki je na vrsti,\nnaredi požirek.', '[size=60]Limonce[/size]\n Vsak igralec dobi eno zaporedno število. \nIgralec, ki je na vrsti, pove svojo številko, \npol limonce, število naslednjega igralca, \nki si ga izbere, pol limonce. \nKdor naredi napako, pije en požirek.', '[size=60]Nikoli nisem[/size]\nIgralec, ki je na vrsti pove, \nkaj še ni nikoli naredil. \nIgralec, ki pa je, pije en požirek.', '[size=60]Zgodba[/size]\nIgralec, ki je na vrsti pove eno besedo, \nnato vsak naslednji igralec\n pove vse predhodne\n besede in še eno doda. \nKdor naredi napako, pije en požirek.', '[size=60]21[/size]\nIgralci štejejo do 21. \nTisti, ki doseže 21, naredi en požirek. \nČe igralec pove dve števili zapored, \n se smer obrne.', '[size=60]Pravilo[/size]\nIgralec, ki je na vrsti pove pravilo ali\n razveljavi že obstoječe pravilo. \nPravilo velja dokler, se ga ne razveljavi.', '[size=60]Prst[/size]\n Tisti, ki zadnji položi prst \nna mizo med igro, naredi en požirek.', '[size=60]BUM[/size]\n Igralci štejejo. Pri tem vsa števila, \nki vsebujejo števili 3 ali 7 in števila, \nki so deljiva s 3 ali 7 zamenjamo z BUM. \nKdor naredi napako, pije en požirek. ', '[size=60]Pije desno[/size]\nDesni sosed igralca, ki je na vrsti,\nnaredi požirek.']
            self.button1.text = '[b]Nadaljuj[/b]'
            self.label.text = str(nextplayer) + '\n' + random.choice(self.list) 
            self.remove_widget(self.button3)
            self.remove_widget(self.textinput1)
     
    def stop(self, event):
        Window.close()

class KivyApp(App):
    def build(self):
        self.icon = 'kozarec.png'
        return Igra()

if __name__ == "__main__":
    KivyApp().run()