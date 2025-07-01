#importation des modules
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager


class tex(MDApp):
    #création de l'interface
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("sign.kv"))
        #assemble tout en un (screen_manager)
        return screen_manager
    #fonction pour retour à l'ecran de "se connecter"
    def back(self):
        screen_manager.transition.direction = "right"
        screen_manager.current = "login_page"
    #fonction pour aller à l'ecran de "s'inscrir"
    def sign_in(self):
        screen_manager.transition.direction = "left"
        screen_manager.current = "sign page"
#run the the app
if __name__ == "__main__":
    tex().run()
