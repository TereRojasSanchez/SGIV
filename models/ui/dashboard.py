import flet as ft
from dao.mascota_dao import MascotaDAO

VIOLETA = "#683266"
PURPURA = "#8E618C"
LILA = "#CE93D8"
FONDO = "#F8F2FA"
BLANCO = "#FFFFFF"
NEGRO = "#212121"


def tarjeta(titulo, numero, icono):

    return ft.Container(
        width=220,
        height=130,
        bgcolor=PURPURA,
        border_radius=20,
        padding=20,

        shadow=ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 4),
        ),

        content=ft.Column(

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[

                ft.Icon(
                    icono,
                    size=40,
                    color=VIOLETA
                ),

                ft.Text(
                    titulo,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=VIOLETA
                ),

                ft.Text(
                    str(numero),
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=VIOLETA
                ),

            ]
        )
    )



def dashboard():

    mascota_dao = MascotaDAO()

    pacientes = len(mascota_dao.obtener_todo())


    return ft.Container(

        expand=True,
        bgcolor=FONDO,
        padding=30,

        content=ft.Column(

            scroll=ft.ScrollMode.AUTO,

            controls=[


                ft.Text(
                    "Bienvenido",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color=VIOLETA
                ),


                ft.Text(
                    "Sistema de Gestión Veterinaria",
                    size=18,
                    color=PURPURA
                ),


                ft.Container(height=25),



                # TARJETAS CENTRADAS

                ft.Row(

                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,

                    controls=[

                        tarjeta(
                            "Consultas de hoy",
                            0,
                            ft.Icons.CALENDAR_MONTH
                        ),


                        tarjeta(
                             "Pacientes",
                              pacientes,
                              ft.Icons.PETS
),


                        tarjeta(
                            "Alertas",
                            0,
                            ft.Icons.WARNING
                        ),

                    ]
                ),



                ft.Container(height=30),



                ft.Row(

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    controls=[



                        # IMAGEN MASCOTA

                        ft.Container(

                            width=380,
                            height=260,

                            bgcolor=BLANCO,

                            border_radius=25,

                            padding=15,


                            content=ft.Image(

                                src="mascota.png",

                                fit="cover"

                            )

                        ),




                        # PANEL ALERTAS

                        ft.Container(

                            width=420,

                            bgcolor=BLANCO,

                            border_radius=25,

                            padding=20,


                            content=ft.Column(

                                spacing=15,

                                controls=[


                                    ft.Text(

                                        "Alertas",

                                        size=24,

                                        weight=ft.FontWeight.BOLD,

                                        color=VIOLETA

                                    ),



                                    ft.ListTile(

                                        leading=ft.Icon(

                                            ft.Icons.WARNING,

                                            color="orange"

                                        ),

                                        title=ft.Text(

                                            "Productos con stock bajo",

                                            color=NEGRO

                                        ),

                                        trailing=ft.Text(

                                            "0",

                                            color=NEGRO,

                                            weight=ft.FontWeight.BOLD

                                        )

                                    ),




                                    ft.ListTile(

                                        leading=ft.Icon(

                                            ft.Icons.CALENDAR_MONTH,

                                            color="red"

                                        ),

                                        title=ft.Text(

                                            "Consultas pendientes",

                                            color=NEGRO

                                        ),

                                        trailing=ft.Text(

                                            "0",

                                            color=NEGRO,

                                            weight=ft.FontWeight.BOLD

                                        )

                                    ),





                                    ft.ListTile(

                                        leading=ft.Icon(

                                            ft.Icons.MEDICATION,

                                            color="green"

                                        ),

                                        title=ft.Text(

                                            "Medicamentos por vencer",

                                            color=NEGRO

                                        ),

                                        trailing=ft.Text(

                                            "0",

                                            color=NEGRO,

                                            weight=ft.FontWeight.BOLD

                                        )

                                    ),


                                ]

                            )

                        )


                    ]

                )


            ]

        )

    )