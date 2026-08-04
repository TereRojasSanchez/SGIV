
import flet as ft

from dao.empleado_dao import EmpleadoDAO
from models.ui.empleado_form import empleado_form


VIOLETA = "#683266"
PURPURA = "#8E618C"
LILA = "#CE93D8"
FONDO = "#F8F2FA"
BLANCO = "#FFFFFF"
ROJO = "#D32F2F"

def empleados_list(regresar, agregar_empleado):

    dao = EmpleadoDAO()


    mensaje = ft.Text(
        "",
        size=16,
        color=VIOLETA
    )

    tabla = ft.DataTable(

        heading_row_color=VIOLETA,

        heading_text_style=ft.TextStyle(
            color=BLANCO,
            weight=ft.FontWeight.BOLD,
            size=16
        ),

        divider_thickness=0,

        data_row_min_height=65,

        column_spacing=45,

        columns=[
            ft.DataColumn(
                ft.Text("Estado")
            ),

            ft.DataColumn(
                ft.Text("Nombre")
            ),

            ft.DataColumn(
                ft.Text("Usuario")
            ),

            ft.DataColumn(
                ft.Text("Rol")
            ),

            ft.DataColumn(
                ft.Text("Editar")
            ),

            ft.DataColumn(
                ft.Text("Eliminar")
            )
        ],

        rows=[]
    )

    # EDITAR EMPLEADO
    def editar(id_empleado):
        try:
            empleados = dao.obtener_todo()
            empleado = None
            for e in empleados:
                if e.id == id_empleado:
                    empleado = e
                    break
            if empleado is None:
                mensaje.value = "No se encontró el empleado."
                mensaje.color = ROJO

                if tabla.page:
                    tabla.page.update()

                return

            # Mostrar formulario de edición
            tabla_container.content = empleado_form(
                regresar,
                empleado
            )

            tabla_container.update()

        except Exception as error:

            mensaje.value = (
                f"Error al editar empleado: {error}"
            )

            mensaje.color = ROJO

            if tabla.page:
                tabla.page.update()

    # ELIMINAR EMPLEADO

    def confirmar_eliminar(id_empleado):

        try:
            # BUSCAR EMPLEADO
            empleado = dao.obtener_por_id(id_empleado)
            if empleado is None:
                mensaje.value = (
                    "No se encontró el empleado."
                )

                mensaje.color = ROJO
                if tabla.page:
                    tabla.page.update()
                return
            
            nombre_empleado = (
                f"{empleado.nombre} "
                f"{empleado.apellido_paterno}"
            )

            # CANCELAR
            def cancelar(e):

                dialog.open = False

                e.page.update()

            # ELIMINAR CONFIRMADO
            def eliminar_confirmado(e):
                try:
                    dao.eliminar(id_empleado)
                    dialog.open = False

                    cargar_tabla()

                    # Mostrar mensaje
                    mensaje.value = (
                        f"El empleado "
                        f"{nombre_empleado} "
                        f"fue eliminado correctamente."
                    )

                    mensaje.color = "green"

                except Exception as error:

                    mensaje.value = (
                        f"Error al eliminar empleado: "
                        f"{error}"
                    )

                    mensaje.color = ROJO

                    dialog.open = False

                e.page.update()

            # VENTANA DE CONFIRMACIÓN
            dialog = ft.AlertDialog(

                modal=True,

                title=ft.Row(
                    controls=[

                        ft.Icon(
                            ft.Icons.WARNING,
                            color=ROJO,
                            size=28
                        ),

                        ft.Text(
                            "Eliminar empleado",
                            color=VIOLETA,
                            weight=ft.FontWeight.BOLD,
                            size=20
                        )
                    ]
                ),

                content=ft.Column(

                    tight=True,

                    controls=[

                        ft.Text(
                            "¿Deseas eliminar este empleado?",
                            size=16
                        ),

                        ft.Text(
                            nombre_empleado,
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=VIOLETA
                        ),

                        ft.Text(
                            "Esta acción no se puede deshacer.",
                            size=13,
                            color="#777777"
                        )
                    ]
                ),

                actions=[

                    # BOTÓN CANCELAR
                    ft.OutlinedButton(
                        content=ft.Text(
                            "Cancelar"
                        ),

                        icon=ft.Icons.CANCEL,
                        style=ft.ButtonStyle(
                            color=VIOLETA,
                            side=ft.BorderSide(
                                width=1,
                                color=LILA
                            )
                        ),

                        on_click=cancelar
                    ),

                    # BOTÓN ELIMINAR

                    ft.ElevatedButton(

                        content=ft.Text(
                            "Eliminar"
                        ),

                        icon=ft.Icons.DELETE,

                        bgcolor=ROJO,

                        color=BLANCO,

                        on_click=eliminar_confirmado
                    )
                ],

                actions_alignment=ft.MainAxisAlignment.END
            )

            # MOSTRAR DIÁLOGO
            if tabla.page:
                tabla.page.dialog = dialog
                dialog.open = True
                tabla.page.update()

        except Exception as error:

            mensaje.value = (
                f"Error al buscar empleado: "
                f"{error}"
            )

            mensaje.color = ROJO

            if tabla.page:
                tabla.page.update()

    # CARGAR TABLA
    def cargar_tabla(e=None):
        tabla.rows.clear()
        try:
            empleados = dao.obtener_todo()
            for empleado in empleados:
                tabla.rows.append(
                    ft.DataRow(
                        cells=[
            
                            # ESTADO
                            ft.DataCell(

                                ft.Switch(

                                    value=bool(
                                        empleado.activo
                                    ),

                                    active_color=PURPURA
                                )
                            ),

                           
                            # NOMBRE
                            ft.DataCell(

                                ft.Row(

                                    spacing=10,

                                    controls=[

                                        ft.CircleAvatar(

                                            radius=20,

                                            bgcolor=LILA,

                                            content=ft.Icon(

                                                ft.Icons.PERSON,

                                                color=VIOLETA
                                            )
                                        ),

                                        ft.Text(

                                            f"{empleado.nombre} "
                                            f"{empleado.apellido_paterno}",

                                            size=15,

                                            weight=ft.FontWeight.BOLD,

                                            color="#333333"
                                        )
                                    ]
                                )
                            ),

                            # USUARIO
                            ft.DataCell(
                                ft.Text(
                                    empleado.usuario
                                    if empleado.usuario
                                    else "",
                                    color="#333333",
                                    weight=ft.FontWeight.BOLD
                                )
                            ),

                            # ROL
                            ft.DataCell(
                                ft.Container(
                                    padding=8,
                                    bgcolor="#EBD7F2",
                                    border_radius=20,
                                    content=ft.Text(
                                        empleado.puesto_usuario
                                        if empleado.puesto_usuario
                                        else "Sin rol",
                                        color=VIOLETA,
                                        weight=ft.FontWeight.BOLD
                                    )
                                )
                            ),

                            # EDITAR
                            ft.DataCell(
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    icon_color=PURPURA,
                                    tooltip="Editar empleado",
                                    on_click=lambda e,
                                    id=empleado.id:
                                    editar(id)
                                )
                            ),

                            # ELIMINAR
                            ft.DataCell(
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color=ROJO,
                                    tooltip="Eliminar empleado",
                                    on_click=lambda e,
                                    id=empleado.id:
                                    confirmar_eliminar(id)
                                )
                            )
                        ]
                    )
                )

            mensaje.value = ""

        except Exception as error:

            mensaje.value = (
                f"Error cargando empleados: "
                f"{error}"
            )

            mensaje.color = ROJO

        if e:

            e.page.update()


    # TÍTULO
    titulo = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                spacing=2,
                controls=[
                    ft.Text(
                        "Empleados",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=VIOLETA
                    ),

                    ft.Text(
                        "Administración de empleados",
                        color=PURPURA,
                        size=14
                    )
                ]
            ),

            # AGREGAR EMPLEADO
            ft.ElevatedButton(
                content=ft.Text(
                    "Agregar empleado"
                ),

                icon=ft.Icons.PERSON_ADD,
                bgcolor=VIOLETA,
                color=BLANCO,
                on_click=lambda e:
                agregar_empleado()
            )
        ]
    )

    tabla_container = ft.Container(
        width=1100,
        height=500,
        bgcolor=BLANCO,
        padding=15,
        border_radius=15,
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[

                ft.Row(
                    controls=[tabla],
                    scroll=ft.ScrollMode.AUTO
                )
            ]
        )
    )

    # BOTÓN REGRESAR
    botones = ft.Row(
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.OutlinedButton(
                content=ft.Text(
                    "Regresar"
                ),

                icon=ft.Icons.ARROW_BACK,

                on_click=lambda e:
                regresar()
            )
        ]
    )

    cargar_tabla()

    return ft.Container(
        expand=True,
        bgcolor=FONDO,
        padding=15,
        content=ft.Column(
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                titulo,
                ft.Divider(
                    color=LILA,
                    height=1
                ),
                tabla_container,
                botones,
                mensaje
            ]
        )
    )
