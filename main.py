from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from utils import DBAccess
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
import json

Builder.load_file('utils/universoapp.kv')


class UniversoApp(MDScreenManager):
    pass


class HomeScreen(MDScreen):
    desejos = []
    path = ''
    
    frase_dia = DBAccess.buscar_frase_aleatoria_BD()
    Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
    Window.softinput_mode = "below_target"
    # print(frase_dia[0])
    if frase_dia is None or frase_dia is '':
        frase_dia = ('Você é incrível! Acredite em você mesmo(a)!')

    def validar_desejo(self):
        desejo = self.ids.text_field.text
        print(f'Desejo sem validação: {desejo}')  # para Debug
        return len(desejo) != 0
    
    def gravar_desejos(self):
        try:
            if self.validar_desejo():
                desejo = self.ids.text_field.text
                print(desejo)
                self.path = MDApp.get_running_app().user_data_dir + '/'
                try:
                    with open(self.path + 'data.json', 'r+') as data:
                        desejos_existentes = json.load(data)
                        desejos_existentes.extend((desejo,))
                        print(desejos_existentes)
                        data.seek(0)
                        json.dump(desejos_existentes, data)
                        data.truncate()
                except FileNotFoundError:
                    with open(self.path + 'data.json', 'w') as data:
                        json.dump((desejo,), data)
                        
                self.parent.current = 'desejo'
            else:
                pass
            
        except Exception as e:
            print(f'não foi possivel gravar o desejo no Banco de Dados. Erro: {e}')
            self.ids.text_field.text = ''  # limpar o campo TextField do desejo
            pass
        

class Frases(MDScreen):
    frases_do_dia = DBAccess.buscar_tres_frases_BD()
    # print(self.frases_do_dia[0], self.frases_do_dia[1], self.frases_do_dia[2])
    if frases_do_dia is None or frases_do_dia is '':
        frases_do_dia = ('Você é incrível! Acredite em você mesmo(a)!')

    def update_frases(self):
        self.frases_do_dia = DBAccess.buscar_tres_frases_BD()
        self.ids['frases_label'].text = str(self.frases_do_dia[0]) + '\n\n' + str(self.frases_do_dia[1]) + '\n\n' + str(
            self.frases_do_dia[2])


class Desejo(MDScreen):
    pass


class ListaDesejos(MDScreen):
    desejos = []
    path = ''
    """
    def db_consulta(consulta, parametros=()):
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute(consulta, parametros)
            resultado = cursor.fetchall()
            con.commit()
            return resultado
            """

    def on_pre_enter(self):
        try:
            # query_desejos = 'SELECT desejo FROM desejo'
            # desejos = self.db_consulta(query_desejos)
            self.path = MDApp.get_running_app().user_data_dir + '/'
            self.loadData()
            # Limpar os desejos da tela
            for child in self.ids.desejo_box.children:
                self.ids.desejo_box.remove_widget(child)
            # Carregar os novos desejos
            for desejo in self.desejos:
                self.ids.desejo_box.add_widget(DesejoLista(text=desejo))
        except Exception as e:
            print(f'Não foi possível buscar os desejos no arquivo JSON. Ou eles não existem ou há algum problema de conexão. Erro: {e}.')

    def loadData(self, *args):
        try:
            with open(self.path + 'data.json', 'r') as data:
                self.desejos = json.load(data)
        except FileNotFoundError:
            pass

    def saveData(self, *args):
        with open(self.path + 'data.json', 'w') as data:
            json.dump(self.desejos, data)

    def remove_desejos(self, desejo):
        texto = desejo.ids.label_desejo.text
        # query_remove = 'DELETE FROM desejo WHERE desejo = ?'
        self.ids.desejo_box.remove_widget(desejo)
        self.desejos.remove(texto)
        self.saveData()
        # self.db_consulta(query_remove, texto)


class DesejoLista(MDBoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label_desejo.text = text


class MyApp(MDApp):
    desejo_usuario = StringProperty()

    def build(self):
        self.theme_cls.primary_palette = 'Indigo'

        return UniversoApp()


if __name__ == '__main__':
    MyApp().run()
