import flet as ft
from dao.mascota_dao import MascotaDAO


def mascota_list(regresar, editar_mascota):

    # ==========================================================
    # COLORES
    # ==========================================================

    VIOLETA = "#683266"
    PURPURA = "#7B1FA2"
    LILA = "#E1BEE7"
    FONDO = "#F8F2FA"
    NEGRO = "#000000"
    BLANCO = "#FFFFFF"

    # ==========================================================
    # TABLA DE MASCOTAS
    # ==========================================================

    tabla = ft.DataTable(

        # ENCABEZADO MORADO FUERTE
        heading_row_color=VIOLETA,

        # FILAS MORADO CLARO
        data_row_color=LILA,

        # LINEAS VERTICALES NEGRAS
        vertical_lines=ft.BorderSide(
            width=1,
            color=NEGRO
        ),

        # LINEAS HORIZONTALES NEGRAS
        horizontal_lines=ft.BorderSide(
            width=1,
            color=NEGRO
        ),

        # BORDE EXTERIOR NEGRO
        border=ft.Border.all(
            width=1,
            color=NEGRO
        ),

        # ESPACIO ENTRE COLUMNAS
        column_spacing=55,

        columns=[

            # ==================================================
            # ID
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "ID",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            # ==================================================
            # CLIENTE
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "Cliente",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            # ==================================================
            # NOMBRE
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "Nombre",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            # ==================================================
            # RAZA
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "Raza",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            # ==================================================
            # ESPECIE
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "Especie",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            # ==================================================
            # EDAD
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "Edad",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            # ==================================================
            # PESO
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "Peso",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            ),

            # ==================================================
            # ACCIONES
            # ==================================================

            ft.DataColumn(
                ft.Text(
                    "Acciones",
                    weight=ft.FontWeight.BOLD,
                    color=BLANCO
                )
            )
        ],

        rows=[]
    )

    # ==========================================================
    # MENSAJE
    # ==========================================================

    mensaje = ft.Text(
        "",
        size=16,
        weight=ft.FontWeight.BOLD
    )

    # ==========================================================
    # CARGAR MASCOTAS
    # ==========================================================

    def cargar_mascotas():

        try:

            mascota_dao = MascotaDAO()

            mascotas = mascota_dao.obtener_todo()

            especies = mascota_dao.obtener_especies()

            nombres_especies = {}

            for especie in especies:

                id_especie = especie[0]
                nombre_especie = especie[1]

                nombres_especies[id_especie] = nombre_especie

            # LIMPIAR TABLA
            tabla.rows.clear()

            # ==================================================
            # AGREGAR MASCOTAS
            # ==================================================

            for mascota in mascotas:

                nombre_especie = nombres_especies.get(
                    mascota.id_especie,
                    str(mascota.id_especie)
                )

                tabla.rows.append(

                    ft.DataRow(

                        cells=[

                            # ==================================
                            # ID
                            # ==================================

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.id),
                                    weight=ft.FontWeight.BOLD,
                                    color=NEGRO
                                )
                            ),

                            # ==================================
                            # CLIENTE
                            # ==================================

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.id_cliente),
                                    weight=ft.FontWeight.BOLD,
                                    color=NEGRO
                                )
                            ),

                            # ==================================
                            # NOMBRE
                            # ==================================

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.nombre),
                                    weight=ft.FontWeight.BOLD,
                                    color=NEGRO
                                )
                            ),

                            # ==================================
                            # RAZA
                            # ==================================

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.raza),
                                    weight=ft.FontWeight.BOLD,
                                    color=NEGRO
                                )
                            ),

                            # ==================================
                            # ESPECIE
                            # ==================================

                            ft.DataCell(
                                ft.Text(
                                    nombre_especie,
                                    weight=ft.FontWeight.BOLD,
                                    color=NEGRO
                                )
                            ),

                            # ==================================
                            # EDAD
                            # ==================================

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.edad),
                                    weight=ft.FontWeight.BOLD,
                                    color=NEGRO
                                )
                            ),

                            # ==================================
                            # PESO
                            # ==================================

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.peso),
                                    weight=ft.FontWeight.BOLD,
                                    color=NEGRO
                                )
                            ),

                            # ==================================
                            # ACCIONES
                            # ==================================

                            ft.DataCell(

                                ft.Row(

                                    controls=[

                                        # EDITAR
                                        ft.IconButton(
                                            icon=ft.Icons.EDIT,
                                            tooltip="Editar",
                                            icon_color=VIOLETA,

                                            on_click=lambda e, m=mascota:
                                                editar_mascota(m)
                                        ),

                                        # ELIMINAR
                                        ft.IconButton(
                                            icon=ft.Icons.DELETE,
                                            tooltip="Eliminar",
                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, m=mascota:
                                                eliminar_mascota(e, m)
                                        )

                                    ],

                                    spacing=5

                                )

                            )

                        ]

                    )

                )

            mensaje.value = ""

        except Exception as error:

            mensaje.value = (
                f"Error al consultar mascotas: {error}"
            )

            mensaje.color = ft.Colors.RED

    # ==========================================================
    # ELIMINAR MASCOTA
    # ==========================================================

    def eliminar_mascota(e, mascota):

        # ======================================================
        # CONFIRMAR ELIMINACIÓN
        # ======================================================

        def confirmar_eliminacion(e):

            try:

                mascota_dao = MascotaDAO()

                mascota_dao.eliminar(mascota.id)

                dialogo.open = False

                mensaje.value = (
                    f"Mascota '{mascota.nombre}' "
                    f"eliminada correctamente."
                )

                mensaje.color = ft.Colors.GREEN

                cargar_mascotas()

                e.page.update()

            except Exception as error:

                dialogo.open = False

                mensaje.value = (
                    f"Error al eliminar mascota: {error}"
                )

                mensaje.color = ft.Colors.RED

                e.page.update()

        # ======================================================
        # CANCELAR
        # ======================================================

        def cancelar_eliminacion(e):

            dialogo.open = False

            e.page.update()

        # ======================================================
        # DIÁLOGO
        # ======================================================

        dialogo = ft.AlertDialog(

            modal=True,

            title=ft.Text(
                "Eliminar mascota",
                weight=ft.FontWeight.BOLD,
                color=VIOLETA
            ),

            content=ft.Text(
                f"¿Está seguro de eliminar a "
                f"'{mascota.nombre}'?",
                weight=ft.FontWeight.BOLD,
                color=NEGRO
            ),

            actions=[

                # CANCELAR
                ft.TextButton(
                    "Cancelar",
                    on_click=cancelar_eliminacion,
                    style=ft.ButtonStyle(
                        color=VIOLETA
                    )
                ),

                # ELIMINAR
                ft.ElevatedButton(
                    "Eliminar",
                    icon=ft.Icons.DELETE,
                    on_click=confirmar_eliminacion,
                    style=ft.ButtonStyle(
                        color=BLANCO,
                        bgcolor=VIOLETA
                    )
                )

            ]

        )

        e.page.overlay.append(dialogo)

        dialogo.open = True

        e.page.update()

    # ==========================================================
    # CARGAR DATOS
    # ==========================================================

    cargar_mascotas()

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    return ft.Container(

        padding=0,

        expand=True,

        bgcolor=FONDO,

        content=ft.Column(

            controls=[

                # ==================================================
                # ENCABEZADO
                # ==================================================

                ft.Row(

                    controls=[

                        ft.Column(

                            controls=[

                                ft.Text(
                                    "Mascotas registradas",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                    color=VIOLETA
                                ),

                                ft.Text(
                                    "Consulta de mascotas registradas",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_GREY_600
                                )

                            ],

                            spacing=2

                        ),

                        # ==================================================
                        # BOTONES
                        # ==================================================

                        ft.Row(

                            controls=[

                                # AGREGAR MASCOTA
                                ft.ElevatedButton(

                                    "Agregar mascota",

                                    icon=ft.Icons.ADD,

                                    on_click=lambda e:
                                        editar_mascota(),

                                    style=ft.ButtonStyle(

                                        color=BLANCO,

                                        bgcolor=VIOLETA,

                                        shape=ft.RoundedRectangleBorder(
                                            radius=10
                                        )

                                    )

                                ),

                                # REGRESAR
                                ft.OutlinedButton(

                                    "Regresar",

                                    icon=ft.Icons.ARROW_BACK,

                                    on_click=regresar,

                                    style=ft.ButtonStyle(

                                        color=VIOLETA,

                                        side=ft.BorderSide(
                                            width=1,
                                            color="#CE93D8"
                                        ),

                                        shape=ft.RoundedRectangleBorder(
                                            radius=10
                                        )

                                    )

                                )

                            ],

                            spacing=10

                        )

                    ],

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN

                ),

                # ==================================================
                # SEPARADOR
                # ==================================================

                ft.Divider(
                    height=5,
                    color="#CE93D8"
                ),

                # ==================================================
                # TABLA
                # ==================================================

                ft.Container(

                    content=ft.Row(

                        controls=[

                            tabla

                        ],

                        alignment=ft.MainAxisAlignment.CENTER,

                        scroll=ft.ScrollMode.AUTO

                    ),

                    # BAJAR TABLA APROXIMADAMENTE 3 CM
                    padding=ft.Padding(
                        top=110,
                        right=0,
                        bottom=0,
                        left=0
                    )

                ),

                # ==================================================
                # MENSAJE
                # ==================================================

                mensaje

            ],

            spacing=5,

            expand=True

        )

    )