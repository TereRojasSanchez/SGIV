import flet as ft

from dao.empleado_dao import EmpleadoDAO
from models.empleado import Empleado


# PALETA DE COLORES

VIOLETA = "#683266"
PURPURA = "#7B1FA2"
LILA = "#CE93D8"
FONDO = "#F8F2FA"
BLANCO = "#FFFFFF"


def empleado_form(regresar, empleado=None):

    dao = EmpleadoDAO()


    # ==========================
    # ESTILOS
    # ==========================

    ESTILO_CAMPO = ft.TextStyle(
        weight=ft.FontWeight.BOLD,
        size=16,
        color="#333333"
    )


    ESTILO_ETIQUETA = ft.TextStyle(
        weight=ft.FontWeight.BOLD,
        color=VIOLETA
    )


    # ==========================
    # CAMPOS
    # ==========================

    nombre = ft.TextField(
        label="Nombre",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    apellido_paterno = ft.TextField(
        label="Apellido paterno",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    apellido_materno = ft.TextField(
        label="Apellido materno",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    telefono = ft.TextField(
        label="Teléfono",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    correo = ft.TextField(
        label="Correo",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    usuario = ft.TextField(
        label="Usuario",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    municipio = ft.TextField(
        label="Municipio",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    codigo_postal = ft.TextField(
        label="Código postal",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    colonia = ft.TextField(
        label="Colonia",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    calle = ft.TextField(
        label="Calle",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    numero_exterior = ft.TextField(
        label="Número exterior",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    numero_interior = ft.TextField(
        label="Número interior",
        width=260,
        text_style=ESTILO_CAMPO,
        label_style=ESTILO_ETIQUETA
    )


    puesto_usuario = ft.Dropdown(
        label="Rol",
        width=260,
        options=[
            ft.dropdown.Option("Administrador"),
            ft.dropdown.Option("Veterinario"),
            ft.dropdown.Option("Recepcionista")
        ]
    )


    mensaje = ft.Text(
        "",
        size=16,
        color=VIOLETA,
        weight=ft.FontWeight.BOLD
    )


    # ==========================
    # CARGAR DATOS AL EDITAR
    # ==========================

    if empleado:

        nombre.value = empleado.nombre or ""

        apellido_paterno.value = (
            empleado.apellido_paterno or ""
        )

        apellido_materno.value = (
            empleado.apellido_materno or ""
        )

        telefono.value = (
            empleado.telefono or ""
        )

        correo.value = (
            empleado.correo or ""
        )

        usuario.value = (
            empleado.usuario or ""
        )

        contraseña.value = (
            empleado.contraseña or ""
        )

        municipio.value = (
            empleado.municipio or ""
        )

        codigo_postal.value = (
            empleado.codigo_postal or ""
        )

        colonia.value = (
            empleado.colonia or ""
        )

        calle.value = (
            empleado.calle or ""
        )

        numero_exterior.value = (
            empleado.numero_exterior or ""
        )

        numero_interior.value = (
            empleado.numero_interior or ""
        )

        puesto_usuario.value = (
            empleado.puesto_usuario
        )

            # ==========================
    # LIMPIAR CAMPOS
    # ==========================

    def limpiar():

        nombre.value = ""
        apellido_paterno.value = ""
        apellido_materno.value = ""
        telefono.value = ""
        correo.value = ""
        usuario.value = ""
        contraseña.value = ""
        municipio.value = ""
        codigo_postal.value = ""
        colonia.value = ""
        calle.value = ""
        numero_exterior.value = ""
        numero_interior.value = ""
        puesto_usuario.value = None



    # ==========================
    # GUARDAR / ACTUALIZAR
    # ==========================

    def guardar(e):

        try:

            if not nombre.value or nombre.value.strip() == "":

                mensaje.value = (
                    "El nombre es obligatorio"
                )

                mensaje.color = "red"

                e.page.update()

                return



            empleado_nuevo = Empleado(

                empleado.id if empleado else None,

                nombre.value.strip(),

                apellido_paterno.value.strip(),

                apellido_materno.value.strip(),

                telefono.value.strip(),

                correo.value.strip(),

                usuario.value.strip(),

                contraseña.value,

                municipio.value.strip(),

                codigo_postal.value.strip(),

                colonia.value.strip(),

                calle.value.strip(),

                numero_exterior.value.strip(),

                numero_interior.value.strip(),

                True,

                puesto_usuario.value

            )



            if empleado:

                dao.actualizar(
                    empleado_nuevo
                )

                mensaje.value = (
                    "Empleado actualizado correctamente"
                )


            else:

                dao.insertar(
                    empleado_nuevo
                )

                mensaje.value = (
                    "Empleado registrado correctamente"
                )



            mensaje.color = "green"

            e.page.update()



        except Exception as error:

            mensaje.value = (
                f"Error al guardar: {error}"
            )

            mensaje.color = "red"

            e.page.update()



    # ==========================
    # FORMULARIO
    # ==========================

    formulario = ft.Column(

        spacing=15,

        scroll=ft.ScrollMode.AUTO,

        controls=[


            ft.Row(
                controls=[
                    nombre,
                    apellido_paterno,
                    apellido_materno
                ]
            ),



            ft.Row(
                controls=[
                    telefono,
                    correo,
                    usuario
                ]
            ),



            ft.Row(
                controls=[
                    contraseña,
                    puesto_usuario
                ]
            ),



            ft.Row(
                controls=[
                    municipio,
                    codigo_postal,
                    colonia
                ]
            ),



            ft.Row(
                controls=[
                    calle,
                    numero_exterior,
                    numero_interior
                ]
            )

        ]
    )



    # ==========================
    # BOTONES
    # ==========================

    botones = ft.Row(

        spacing=20,

        controls=[


            ft.ElevatedButton(

                content=ft.Text(

                    "Actualizar empleado"
                    if empleado
                    else "Guardar empleado",

                    weight=ft.FontWeight.BOLD

                ),

                icon=ft.Icons.SAVE,

                bgcolor=VIOLETA,

                color=BLANCO,

                on_click=guardar

            ),



            ft.OutlinedButton(

                content=ft.Text(

                    "Cancelar",

                    weight=ft.FontWeight.BOLD

                ),

                icon=ft.Icons.ARROW_BACK,

                on_click=lambda e: regresar()

            )

        ]

    )



    # ==========================
    # VISTA FINAL CORREGIDA
    # ==========================

    return ft.Container(

        expand=True,

        bgcolor=FONDO,

        padding=25,


        content=ft.Column(

            expand=True,

            spacing=18,

            scroll=ft.ScrollMode.AUTO,


            controls=[


                ft.Text(

                    "Editar empleado"
                    if empleado
                    else "Crear empleado",

                    size=32,

                    weight=ft.FontWeight.BOLD,

                    color=VIOLETA

                ),



                ft.Text(

                    "Complete la información del empleado.",

                    color=PURPURA,

                    size=15,

                    weight=ft.FontWeight.BOLD

                ),



                ft.Divider(

                    color=LILA

                ),



                formulario,



                botones,



                mensaje


            ]

        )

    )