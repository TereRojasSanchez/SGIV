
import flet as ft
from models.ui.empleado_form import empleado_form
from models.ui.empleado_list import empleados_list
from models.ui.mascota_form import mascota_form
from models.ui.mascota_list import mascota_list
from models.ui.ventas_form import ventas_form
from models.ui.ventas_list import ventas_list


VIOLETA = "#683266"
PURPURA = "#7B1FA2"
LILA = "#CE93D8"
FONDO = "#F8F2FA"
BLANCO = "#FFFFFF"


def main_window(page: ft.Page):

    # ==========================
    # CONFIGURACIÓN
    # ==========================

    page.title = "Sistema de Gestión Veterinaria"
    page.assets_dir = "assets"
    page.window.width = 1400
    page.window.height = 800
    page.padding = 0
    page.spacing = 0
    page.bgcolor = FONDO


    # ==========================
    # CONTENIDO PRINCIPAL
    # ==========================

    contenido = ft.Container(
        expand=True,
        padding=30,
        bgcolor=FONDO
    )


    # ==========================
    # INICIO
    # ==========================

    def mostrar_inicio(e=None):

        contenido.content = ft.Column(
            controls=[

                ft.Text(
                    "Bienvenido",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color=VIOLETA
                ),

                ft.Text(
                    "Sistema de Gestión Veterinaria",
                    size=20,
                    color=PURPURA
                )

            ]
        )

        page.update()


    # ==========================
    # EMPLEADOS
    # ==========================

    def mostrar_empleados(e=None):

        contenido.content = empleados_list(
            mostrar_inicio,
            mostrar_formulario
        )

        page.update()


    # ==========================
    # FORMULARIO EMPLEADO
    # ==========================

    def mostrar_formulario(e=None):

        contenido.content = empleado_form(
            mostrar_empleados
        )

        page.update()


    # ==========================
    # MASCOTAS
    # ==========================

    def mostrar_mascotas(e=None):

        contenido.content = mascota_list(
            mostrar_inicio,
            mostrar_formulario_mascota
        )

        page.update()


    # ==========================
    # FORMULARIO MASCOTA
    # ==========================

    def mostrar_formulario_mascota(
        mascota=None
    ):

        contenido.content = mascota_form(
            mostrar_mascotas,
            mascota
        )

        page.update()


    # ==========================
    # VENTAS
    # ==========================

    def mostrar_ventas(e=None):

        contenido.content = ventas_list(
            agregar_venta=mostrar_formulario_venta,
            regresar=mostrar_inicio
        )

        page.update()


    # ==========================
    # FORMULARIO VENTA
    # ==========================

    def mostrar_formulario_venta(
        e=None,
        venta=None
    ):

        contenido.content = ventas_form(
            page=page,
            regresar=mostrar_ventas,
            venta=venta
        )

        page.update()


    # ==========================
    # HEADER
    # ==========================

    header = ft.Container(

        height=80,

        bgcolor=VIOLETA,

        padding=20,

        content=ft.Row(

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

            controls=[

                ft.Text(
                    "Veterinaria Yolpaki",
                    size=28,
                    color=BLANCO,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Row(

                    controls=[

                        ft.Text(
                            "Administrador",
                            color=BLANCO,
                            size=18
                        ),

                        ft.CircleAvatar(

                            radius=20,

                            bgcolor=LILA,

                            content=ft.Icon(
                                ft.Icons.PERSON,
                                color=VIOLETA
                            )

                        )

                    ]

                )

            ]

        )

    )


    # ==========================
    # BOTÓN DEL MENÚ
    # ==========================

    def boton_menu(
        texto,
        icono,
        evento=None
    ):

        return ft.OutlinedButton(

            content=ft.Text(texto),

            icon=icono,

            width=200,

            on_click=evento,

            style=ft.ButtonStyle(

                color=VIOLETA,

                side=ft.BorderSide(
                    width=1,
                    color=LILA
                ),

                shape=ft.RoundedRectangleBorder(
                    radius=10
                )

            )

        )


    # ==========================
    # MENÚ LATERAL
    # ==========================

    menu = ft.Container(

        width=240,

        bgcolor=BLANCO,

        padding=20,

        content=ft.Column(

            spacing=15,

            controls=[


                # ==========================
                # LOGO
                # ==========================

                ft.Container(

                    height=130,

                    border_radius=15,

                    alignment=ft.Alignment(0, 0),

                    content=ft.Image(

                        src="icons/logo.png.jpeg",

                        width=170,

                        height=110,

                        fit=ft.BoxFit.CONTAIN

                    )

                ),


                # ==========================
                # INICIO
                # ==========================

                boton_menu(
                    "Inicio",
                    ft.Icons.HOME,
                    mostrar_inicio
                ),


                # ==========================
                # EMPLEADOS
                # ==========================

                boton_menu(
                    "Empleados",
                    ft.Icons.BADGE,
                    mostrar_empleados
                ),


                # ==========================
                # MASCOTAS
                # ==========================

                boton_menu(
                    "Mascotas",
                    ft.Icons.PETS,
                    mostrar_mascotas
                ),


                # ==========================
                # CITAS
                # ==========================

                boton_menu(
                    "Citas",
                    ft.Icons.CALENDAR_MONTH
                ),


                # ==========================
                # PRODUCTOS
                # ==========================

                boton_menu(
                    "Productos",
                    ft.Icons.INVENTORY
                ),


                # ==========================
                # VENTAS
                # ==========================

                boton_menu(
                    "Ventas",
                    ft.Icons.SHOPPING_CART,
                    mostrar_ventas
                ),


                # ==========================
                # REPORTES
                # ==========================

                boton_menu(
                    "Reportes",
                    ft.Icons.BAR_CHART
                ),


                ft.Divider(),


                # ==========================
                # CERRAR SESIÓN
                # ==========================

                boton_menu(
                    "Cerrar sesión",
                    ft.Icons.LOGOUT
                )

            ]

        )

    )


    # ==========================
    # CUERPO
    # ==========================

    cuerpo = ft.Row(

        expand=True,

        controls=[

            menu,

            contenido

        ]

    )


    # ==========================
    # AGREGAR A LA PÁGINA
    # ==========================

    page.add(

        ft.Column(

            expand=True,

            spacing=0,

            controls=[

                header,

                cuerpo

            ]

        )

    )


    # ==========================
    # PANTALLA INICIAL
    # ==========================

    mostrar_inicio()

    page.update()