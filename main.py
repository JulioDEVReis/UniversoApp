from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from utils import DBAccess
from kivy.uix.video import Video

Builder.load_file('utils/universoapp.kv')


class UniversoApp(MDScreenManager):
    pass


class HomeScreen(MDScreen):
    frase_dia = DBAccess.buscar_frase_aleatoria_BD()
    # print(frase_dia[0])
    if frase_dia is None or frase_dia is '':
        frase_dia = ('Você é incrível! Acredite em você mesmo(a)!')


class Frases(MDScreen):
    frases_do_dia = DBAccess.buscar_tres_frases_BD()
    # print(self.frases_do_dia[0], self.frases_do_dia[1], self.frases_do_dia[2])
    if frases_do_dia is None or frases_do_dia is '':
        frases_do_dia = ('Você é incrível! Acredite em você mesmo(a)!')
    todas_frases = DBAccess.mostrar_todas_frases_BD()
    if todas_frases is None or todas_frases is '':
        todas_frases = ('Você é incrível! Acredite em você mesmo(a)!')

    def update_frases(self):
        self.frases_do_dia = DBAccess.buscar_tres_frases_BD()
        self.ids['frases_label'].text = str(self.frases_do_dia[0]) + '\n\n' + str(self.frases_do_dia[1]) + '\n\n' + str(
            self.frases_do_dia[2])

    # Validação da frase colocada pelo usuário. Retorna TRUE se a frase tiver mais de 8 caracteres
    def validar_frase_inserida(self, frase_utilizador):
        return len(frase_utilizador) >= 8

    # Função para adicionar frase inserida SE validar_frase_inserida == True
    def add_frase(self, parametros):
        if self.validar_frase_inserida():
            DBAccess.add_frase_BD(parametros)
        else:
            print('A frase é obrigatória e deve ter no mínimo 8 caracteres.')


class Desejo(MDScreen):
    pass


class MyApp(MDApp):
    desejo_usuario = StringProperty()

    def build(self):
        self.theme_cls.primary_palette = 'Indigo'

        return UniversoApp()


if __name__ == '__main__':
    MyApp().run()
