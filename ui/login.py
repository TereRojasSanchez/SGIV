import flet as ft
from dao.empleado_dao import validar_usuario


def pantalla_login(page: ft.Page):
    page.title = "Inicio de Sesión - Yolpaki"
    page.window_width = 850
    page.window_height = 550
    page.bgcolor = "white"
    page.window_resizable = False
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    txt_usuario = ft.TextField(
    label="Usuario",
    width=280,
    border_radius=8,
    bgcolor=ft.Colors.WHITE,
    label_style=ft.TextStyle(color=ft.Colors.GREY_500),
    text_style=ft.TextStyle(color="#6B3F72"),
    )

    txt_pass = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=280,
        border_radius=8,
        bgcolor=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.GREY_500),
        text_style=ft.TextStyle(color="#6B3F72"),
    )

    lbl_mensaje = ft.Text(
        "",
        color="red",
        size=13,
        visible=False,
    )

    def btn_ingresar_click(e):
        lbl_mensaje.visible = False
        page.update()

        if txt_usuario.value.strip() == "" or txt_pass.value.strip() == "":
            lbl_mensaje.value = "Completa ambos campos"
            lbl_mensaje.visible = True
            page.update()
            return

        empleado = validar_usuario(
            txt_usuario.value.strip(),
            txt_pass.value.strip()
        )

        if empleado:
            page.session.set("usuario_id", empleado.id)
            page.session.set("usuario_nombre", empleado.nombre_completo())
            page.session.set("usuario_rol", empleado.rol)

            page.clean()

            # from ui.menu_principal import menu_principal
            # menu_principal(page)

        else:
            lbl_mensaje.value = "Usuario o contraseña incorrectos"
            lbl_mensaje.visible = True
            page.update()

    logo = ft.Image(
        src="logo_yolpaki.png",
        width=400,
        height=400,
    )

    contenedor_logo = ft.Container(
        content=logo,
        padding=20,
    )

    contenedor_form = ft.Container(
        width=380,
        height=480,
        bgcolor="#D4C2E0",
        border_radius=12,
        padding=30,
        content=ft.Column(
            [
                ft.Text(
                    "Iniciar sesión",
                    size=22,
                    weight="bold",
                    color="#6B3F72",
                ),

                txt_usuario,
                txt_pass,
                lbl_mensaje,

                ft.ElevatedButton(
                    "Ingresar",
                    on_click=btn_ingresar_click,
                    bgcolor="#6B3F72",
                    color="white",
                    width=180,
                    height=40,
                ),

                ft.Text(
                    "¿No tienes cuenta?\nRegistrarte aquí",
                    text_align="center",
                    color="#6B3F72",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=15,
        ),
    )

    page.add(
        ft.Row(
            [
                contenedor_logo,
                contenedor_form,
            ],
            alignment="center",
            spacing=40,
        )
    )