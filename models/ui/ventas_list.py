
import flet as ft
from dao.ventas_dao import VentasDAO

VIOLETA = "#683266"
PURPURA = "#CE93D8"
FONDO = "#F8F2FA"
BLANCO = "#FFFFFF"
NEGRO = "#000000"


def ventas_list(agregar_venta, regresar=None):

    dao = VentasDAO()
    # TABLA
    tabla = ft.DataTable(
        column_spacing=30,
        horizontal_margin=15,
        heading_row_height=55,
        data_row_min_height=50,
        data_row_max_height=60,

        columns=[

            ft.DataColumn(
                ft.Text(
                    "ID",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Fecha venta",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Producto",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Cantidad",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Total",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "ID Producto",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Precio",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Estado",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            )

        ],

        rows=[]
    )

    titulo = ft.Text(
        "Historial de ventas",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=VIOLETA
    )

    # BOTÓN AGREGAR
    boton_agregar = ft.ElevatedButton(
        content=ft.Text(
            "Agregar venta",
            weight=ft.FontWeight.BOLD
        ),
        icon=ft.Icons.ADD,
        bgcolor=VIOLETA,
        color=BLANCO,
        height=45,
        on_click=agregar_venta
    )


    # ENCABEZADO
    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                titulo,
                ft.Container(
                    expand=True
                ),

                boton_agregar

            ],

            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),

        padding=ft.Padding(
            left=20,
            right=20,
            top=10,
            bottom=20
        )
    )

    # CONTENEDOR DE TABLA
    tabla_contenedor = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        tabla
                    ],
                    scroll=ft.ScrollMode.AUTO
                )

            ],

            scroll=ft.ScrollMode.AUTO
        ),

        bgcolor=BLANCO,
        border_radius=12,
        padding=10,
        expand=True
    )

    # CARGAR VENTAS
    def cargar_ventas():
        tabla.rows.clear()
        try:
            ventas = dao.obtener_todo()
            for venta in ventas:
                tabla.rows.append(
                    ft.DataRow(
                        color=PURPURA,
                        cells=[

                            ft.DataCell(
                                ft.Text(
                                    str(venta.id),
                                    color=NEGRO
                                )
                            ),

                            ft.DataCell(
                                ft.Text(
                                    str(
                                        venta.fecha_venta
                                    ),
                                    color=NEGRO
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(
                                        venta.producto_nombre
                                    ),
                                    color=NEGRO
                                )
                            ),

                            ft.DataCell(
                                ft.Text(
                                    str(
                                        venta.cantidad
                                    ),
                                    color=NEGRO
                                )
                            ),

                            ft.DataCell(
                                ft.Text(
                                    f"${float(venta.total):.2f}",
                                    color=NEGRO
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(
                                        venta.id_producto
                                    ),
                                    color=NEGRO
                                )
                            ),

                            ft.DataCell(
                                ft.Text(
                                    f"${float(venta.producto_precio_venta):.2f}",
                                    color=NEGRO
                                )
                            ),

                            # ==========================
                            # ESTADO
                            # ==========================

                            ft.DataCell(
                                ft.Text(
                                    str(
                                        venta.estado
                                    ),
                                    color=NEGRO
                                )
                            )

                        ]
                    )
                )

            # ==========================
            # COLOR DEL ENCABEZADO
            # ==========================

            tabla.heading_row_color = VIOLETA

        except Exception as e:

            print(
                "Error al cargar ventas:",
                e
            )


    # ==========================
    # VISTA
    # ==========================

    vista = ft.Column(

        controls=[

            encabezado,

            tabla_contenedor

        ],

        expand=True,

        spacing=0
    )


    # ==========================
    # CARGAR DATOS
    # ==========================

    cargar_ventas()


    # IMPORTANTE:
    # NO usamos tabla.update() aquí porque
    # todavía no está agregada a la página.

    return vista
