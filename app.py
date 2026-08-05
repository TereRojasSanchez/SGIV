import flet as ft
from ui.login import pantalla_login

if __name__ == "__main__":
    ft.app(
        target=pantalla_login,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER
    )