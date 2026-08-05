import flet as ft

from dao.empleado_dao import EmpleadoDAO
from models.ui.empleado_form import empleado_form


# ==========================================================
# COLORES
# ==========================================================

VIOLETA = "#683266"
PURPURA = "#8E618C"
LILA = "#CE93D8"
FONDO = "#F8F2FA"
BLANCO = "#FFFFFF"
ROJO = "#D32F2F"
NEGRO = "#000000"

PURPURA_CELDAS = "#E1BEE7"


def empleados_list(regresar, agregar_empleado):

    dao = EmpleadoDAO()

    # ==========================================================
    # MENSAJE
    # ==========================================================

    mensaje = ft.Text(
        "",
        size=15,
        weight=ft.FontWeight.BOLD,
        color=VIOLETA
    )

    # ==========================================================
    # TABLA
    # ==========================================================

    tabla = ft.DataTable(

        # COLOR DEL ENCABEZADO
        heading_row_color=VIOLETA,

        # COLOR DE LAS FILAS
        data_row_color=PURPURA_CELDAS,

        # LINEAS VERTICALES
        vertical_lines=ft.BorderSide(
            width=1,
            color=NEGRO
        ),

        # LINEAS HORIZONTALES
        horizontal_lines=ft.BorderSide(
            width=1,
            color=NEGRO
        ),

        # BORDE
        border=ft.Border.all(
            width=1,
            color=NEGRO
        ),

        # TEXTO DEL ENCABEZADO
        heading_text_style=ft.TextStyle(
            color=BLANCO,
            weight=ft.FontWeight.BOLD,
            size=14
        ),

        # FILAS MÁS COMPACTAS
        data_row_min_height=65,

        # MENOS ESPACIO ENTRE COLUMNAS
        column_spacing=20,

        columns=[

            # ==================================================
            # ESTADO
            # ==================================================

            ft.DataColumn(
                ft.Container(
                    width=75,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "Estado",
                        color=BLANCO,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            ),

            # ==================================================
            # NOMBRE
            # ==================================================

            ft.DataColumn(
                ft.Container(
                    width=190,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "Nombre",
                        color=BLANCO,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            ),

            # ==================================================
            # USUARIO
            # ==================================================

            ft.DataColumn(
                ft.Container(
                    width=140,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "Usuario",
                        color=BLANCO,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            ),

            # ==================================================
            # ROL
            # ==================================================

            ft.DataColumn(
                ft.Container(
                    width=140,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "Rol",
                        color=BLANCO,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            ),

            # ==================================================
            # EDITAR
            # ==================================================

            ft.DataColumn(
                ft.Container(
                    width=75,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "Editar",
                        color=BLANCO,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            ),

            # ==================================================
            # ELIMINAR
            # ==================================================

            ft.DataColumn(
                ft.Container(
                    width=80,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "Eliminar",
                        color=BLANCO,
                        weight=ft.FontWeight.BOLD,
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            )
        ],

        rows=[]
    )

    # ==========================================================
    # EDITAR EMPLEADO
    # ==========================================================

    def editar(id_empleado):

        try:

            empleados = dao.obtener_todo()

            empleado = None

            for e in empleados:

                if e.id == id_empleado:
                    empleado = e
                    break

            if empleado is None:

                mensaje.value = (
                    "No se encontró el empleado."
                )

                mensaje.color = ROJO

                if tabla.page:
                    tabla.page.update()

                return

            tabla_container.content = empleado_form(
                volver_tabla,
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

    # ==========================================================
    # ELIMINAR EMPLEADO
    # ==========================================================

    def confirmar_eliminar(id_empleado):

        try:

            empleado = dao.obtener_por_id(
                id_empleado
            )

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

            # ==================================================
            # CANCELAR
            # ==================================================

            def cancelar(e):

                dialog.open = False
                e.page.update()

            # ==================================================
            # ELIMINAR
            # ==================================================

            def eliminar_confirmado(e):

                try:

                    dao.eliminar(id_empleado)

                    dialog.open = False

                    cargar_tabla()

                    mensaje.value = (
                        f"El empleado {nombre_empleado} "
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

            # ==================================================
            # DIALOGO
            # ==================================================

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
                            size=16,
                            color=NEGRO
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

                actions_alignment=(
                    ft.MainAxisAlignment.END
                )
            )

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

    # ==========================================================
    # CARGAR TABLA
    # ==========================================================

    def cargar_tabla(e=None):

        tabla.rows.clear()

        try:

            empleados = dao.obtener_todo()

            for empleado in empleados:

                # ==============================================
                # ESTADO
                # ==============================================

                estado = ft.Container(

                    expand=True,

                    alignment=ft.Alignment(0, 0),

                    content=ft.Switch(

                        value=bool(
                            empleado.activo
                        ),

                        active_color=PURPURA
                    )
                )

                # ==============================================
                # NOMBRE
                # ==============================================

                nombre = ft.Container(

                    expand=True,

                    alignment=ft.Alignment(0, 0),

                    content=ft.Row(

                        controls=[

                            ft.CircleAvatar(

                                radius=18,

                                bgcolor=LILA,

                                content=ft.Icon(
                                    ft.Icons.PERSON,
                                    color=VIOLETA,
                                    size=21
                                )
                            ),

                            ft.Text(

                                f"{empleado.nombre} "
                                f"{empleado.apellido_paterno}",

                                size=13,

                                weight=ft.FontWeight.BOLD,

                                color=NEGRO,

                                text_align=(
                                    ft.TextAlign.CENTER
                                )
                            )
                        ],

                        alignment=(
                            ft.MainAxisAlignment.CENTER
                        ),

                        vertical_alignment=(
                            ft.CrossAxisAlignment.CENTER
                        ),

                        spacing=7
                    )
                )

                # ==============================================
                # USUARIO
                # ==============================================

                usuario = ft.Container(

                    expand=True,

                    alignment=ft.Alignment(0, 0),

                    content=ft.Text(

                        empleado.usuario
                        if empleado.usuario
                        else "",

                        size=13,

                        weight=ft.FontWeight.BOLD,

                        color=NEGRO,

                        text_align=(
                            ft.TextAlign.CENTER
                        )
                    )
                )

                # ==============================================
                # ROL
                # ==============================================

                rol = ft.Container(

                    expand=True,

                    alignment=ft.Alignment(0, 0),

                    content=ft.Container(

                        padding=7,

                        bgcolor="#EBD7F2",

                        border_radius=18,

                        content=ft.Text(

                            empleado.puesto_usuario
                            if empleado.puesto_usuario
                            else "Sin rol",

                            color=VIOLETA,

                            weight=ft.FontWeight.BOLD,

                            size=12,

                            text_align=(
                                ft.TextAlign.CENTER
                            )
                        )
                    )
                )

                # ==============================================
                # EDITAR
                # ==============================================

                editar_boton = ft.Container(

                    expand=True,

                    alignment=ft.Alignment(0, 0),

                    content=ft.IconButton(

                        icon=ft.Icons.EDIT,

                        icon_color=PURPURA,

                        icon_size=22,

                        tooltip="Editar empleado",

                        on_click=lambda e,
                        id=empleado.id:
                        editar(id)
                    )
                )

                # ==============================================
                # ELIMINAR
                # ==============================================

                eliminar_boton = ft.Container(

                    expand=True,

                    alignment=ft.Alignment(0, 0),

                    content=ft.IconButton(

                        icon=ft.Icons.DELETE,

                        icon_color=ROJO,

                        icon_size=22,

                        tooltip="Eliminar empleado",

                        on_click=lambda e,
                        id=empleado.id:
                        confirmar_eliminar(id)
                    )
                )

                # ==============================================
                # AGREGAR FILA
                # ==============================================

                tabla.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                estado
                            ),

                            ft.DataCell(
                                nombre
                            ),

                            ft.DataCell(
                                usuario
                            ),

                            ft.DataCell(
                                rol
                            ),

                            ft.DataCell(
                                editar_boton
                            ),

                            ft.DataCell(
                                eliminar_boton
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

    # ==========================================================
    # TITULO
    # ==========================================================

    titulo = ft.Row(

        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        vertical_alignment=(
            ft.CrossAxisAlignment.CENTER
        ),

        controls=[

            ft.Column(

                spacing=2,

                controls=[

                    ft.Text(
                        "Empleados",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=VIOLETA
                    ),

                    ft.Text(
                        "Administración de empleados",
                        color=PURPURA,
                        size=13,
                        weight=ft.FontWeight.BOLD
                    )
                ]
            ),

            # ==================================================
            # AGREGAR
            # ==================================================

            ft.ElevatedButton(

                content=ft.Text(
                    "Agregar empleado",
                    weight=ft.FontWeight.BOLD
                ),

                icon=ft.Icons.PERSON_ADD,

                bgcolor=VIOLETA,

                color=BLANCO,

                style=ft.ButtonStyle(

                    shape=ft.RoundedRectangleBorder(
                        radius=10
                    )
                ),

                on_click=lambda e:
                agregar_empleado()
            )
        ]
    )

    # ==========================================================
    # CONTENEDOR DE LA TABLA
    # ==========================================================

    tabla_container = ft.Container(

        # TABLA MÁS PEQUEÑA
        width=900,

        # TABLA MÁS BAJA
        height=430,

        bgcolor=BLANCO,

        padding=10,

        border_radius=12,

        content=ft.Column(

            expand=True,

            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.Row(

                    controls=[tabla],

                    alignment=(
                        ft.MainAxisAlignment.CENTER
                    ),

                    vertical_alignment=(
                        ft.CrossAxisAlignment.CENTER
                    ),

                    scroll=ft.ScrollMode.AUTO
                )
            ]
        )
    )

        # ==========================================================
    # VOLVER A LA TABLA DESDE EDITAR
    # ==========================================================

    def volver_tabla():

        tabla_container.content = ft.Column(

            expand=True,

            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.Row(

                    controls=[tabla],

                    alignment=ft.MainAxisAlignment.CENTER,

                    vertical_alignment=ft.CrossAxisAlignment.CENTER,

                    scroll=ft.ScrollMode.AUTO
                )
            ]
        )

        cargar_tabla()

        tabla_container.update()

    # ==========================================================
    # BOTON REGRESAR
    # ==========================================================

    botones = ft.Row(

        alignment=ft.MainAxisAlignment.START,

        controls=[

            ft.OutlinedButton(

                content=ft.Text(
                    "Regresar",
                    weight=ft.FontWeight.BOLD
                ),

                icon=ft.Icons.ARROW_BACK,

                style=ft.ButtonStyle(

                    color=VIOLETA,

                    side=ft.BorderSide(
                        width=1,
                        color=LILA
                    ),

                    shape=ft.RoundedRectangleBorder(
                        radius=10
                    )
                ),

                on_click=lambda e:
                regresar()
            )
        ]
    )

    # ==========================================================
    # CARGAR DATOS
    # ==========================================================

    cargar_tabla()

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    return ft.Container(

        expand=True,

        bgcolor=FONDO,

        padding=15,

        content=ft.Column(

            spacing=8,

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

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