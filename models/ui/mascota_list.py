
import flet as ft

from dao.mascota_dao import MascotaDAO


def mascota_list(regresar, editar_mascota):

    tabla = ft.DataTable(

        columns=[

            ft.DataColumn(
                ft.Text(
                    "ID",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Cliente",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Nombre",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Raza",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Especie",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Edad",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Peso",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ),

            ft.DataColumn(
                ft.Text(
                    "Acciones",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            )

        ],

        rows=[]

    )

    mensaje = ft.Text(
        "",
        size=16,
        weight=ft.FontWeight.BOLD
    )


    
    # CARGAR MASCOTAS
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
            tabla.rows.clear()

            # AGREGAR MASCOTAS
            for mascota in mascotas:
                nombre_especie = nombres_especies.get(
                    mascota.id_especie,
                    str(mascota.id_especie)

                )

                tabla.rows.append(
                    ft.DataRow(
                        cells=[

                            # ID
                            ft.DataCell(
                                ft.Text(
                                    str(mascota.id),
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK

                                )

                            ),

                            # CLIENTE
                            ft.DataCell(
                                ft.Text(
                                    str(mascota.id_cliente),
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK

                                )

                            ),

                            # NOMBRE
                            ft.DataCell(

                                ft.Text(
                                    str(mascota.nombre),
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK

                                )

                            ),


                            
                            # RAZA
                            ft.DataCell(
                                ft.Text(
                                    str(mascota.raza),
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK

                                )

                            ),


                            # ESPECIE
                            ft.DataCell(
                                ft.Text(
                                    nombre_especie,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK

                                )

                            ),


                            
                            # EDAD

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.edad),
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK

                                )

                            ),


                            
                            # PESO
                            

                            ft.DataCell(
                                ft.Text(
                                    str(mascota.peso),
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK

                                )

                            ),


                        
                            # ACCIONES

                            ft.DataCell(
                                ft.Row(
                                    controls=[
                                        # EDITAR

                                        ft.IconButton(
                                            icon=ft.Icons.EDIT,
                                            tooltip="Editar",
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

                                    ]

                                )

                            )

                        ]

                    )

                )


            mensaje.value = ""
            mensaje.color = ft.Colors.GREEN
        except Exception as error:
            mensaje.value = (
                f"Error al consultar mascotas: {error}"

            )

            mensaje.color = ft.Colors.RED


    
    # ELIMINAR MASCOTA

    def eliminar_mascota(e, mascota):

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
        
        # CANCELAR
        
        def cancelar_eliminacion(e):
            dialogo.open = False
            e.page.update()

        # DIÁLOGO

        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                "Eliminar mascota",
                weight=ft.FontWeight.BOLD

            ),
            content=ft.Text(
                f"¿Está seguro de eliminar a "
                f"'{mascota.nombre}'?",
                weight=ft.FontWeight.BOLD

            ),

            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=cancelar_eliminacion

                ),

                ft.ElevatedButton(
                    "Eliminar",
                    icon=ft.Icons.DELETE,
                    on_click=confirmar_eliminacion

                )

            ]

        )


        e.page.overlay.append(dialogo)
        dialogo.open = True
        e.page.update()

    cargar_mascotas()


    # INTERFAZ

    return ft.Container(
        padding=30,
        content=ft.Column(
            controls=[

                # ENCABEZADO

                ft.Row(
                    controls=[

                        ft.Column(

                            controls=[

                                ft.Text(

                                    "Mascotas registradas",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                    color="#683266"

                                ),

                                ft.Text(

                                    "Consulta de mascotas registradas",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_GREY_600

                                )

                            ],

                            spacing=5

                        ),

                        ft.Row(

                            controls=[

                                
                                # AGREGAR MASCOTA
                                ft.ElevatedButton(
                                    "Agregar mascota",
                                    icon=ft.Icons.ADD,
                                    on_click=lambda e:
                                        editar_mascota(),
                                    style=ft.ButtonStyle(
                                        color=ft.Colors.WHITE,
                                        bgcolor="#683266",
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
                                        color="#683266",
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

                ft.Divider(),

                # TABLA

                ft.Container(
                    content=ft.Row(
                        controls=[
                            tabla

                        ],

                        scroll=ft.ScrollMode.AUTO

                    ),

                    border=ft.Border.all(
                        1,
                        ft.Colors.BLUE_GREY_200

                    ),

                    border_radius=10,
                    padding=10

                ),

                mensaje

            ],

            spacing=20,
            scroll=ft.ScrollMode.AUTO

        )

    )
