import flet as ft
from Model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    def telefono(numero):
        # CAMBIA NUMERO
        # Costruisci l'URL con il numero di telefono precompilato
        tel_url = f'tel:{numero}'
        # Apri l'URL nel browser
        page.launch_url(tel_url)
    my_model = Model(telefono)
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_login_interface()


ft.app(target=main, assets_dir='assets')
