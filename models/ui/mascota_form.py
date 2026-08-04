import flet as ft
from models.mascota import Mascota
from dao.mascota_dao import MascotaDAO


# ==========================================================
# COLORES
# ==========================================================

VIOLETA = "#683266"
PURPURA = "#E1BEE7"
LILA = "#CE93D8"
BLANCO = "#FFFFFF"
NEGRO = "#000000"


def mascota_form(regresar, mascota=None):

    # ==========================================================
    # CAMPOS
    # ==========================================================

    cliente_input = ft.TextField(

        label="ID del cliente",

        width=400,

        # FONDO PÚRPURA
        bgcolor=PURPURA,

        text_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        ),

        label_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        )
    )

    nombre_input = ft.TextField(

        label="Nombre de la mascota",

        width=400,

        # FONDO PÚRPURA
        bgcolor=PURPURA,

        text_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        ),

        label_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        )
    )

    raza_input = ft.TextField(

        label="Raza",

        width=400,

        # FONDO PÚRPURA
        bgcolor=PURPURA,

        text_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        ),

        label_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        )
    )

    especie_input = ft.Dropdown(

        label="Especie",

        width=400,

        # FONDO PÚRPURA
        bgcolor=PURPURA,

        options=[],

        label_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        )
    )

    edad_input = ft.TextField(

        label="Edad",

        width=400,

        # FONDO PÚRPURA
        bgcolor=PURPURA,

        text_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        ),

        label_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        )
    )

    peso_input = ft.TextField(

        label="Peso",

        width=400,

        # FONDO PÚRPURA
        bgcolor=PURPURA,

        text_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        ),

        label_style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=NEGRO
        )
    )

    # ==========================================================
    # MENSAJE
    # ==========================================================

    mensaje = ft.Text(
        "",
        color=ft.Colors.GREEN,
        size=16,
        weight=ft.FontWeight.BOLD
    )

    # ==========================================================
    # CARGAR ESPECIES
    # ==========================================================

    try:

        mascota_dao = MascotaDAO()

        especies = mascota_dao.obtener_especies()

        for especie in especies:

            especie_input.options.append(

                ft.DropdownOption(

                    key=str(especie[0]),

                    text=especie[1]

                )

            )

    except Exception as error:

        mensaje.value = (
            f"Error al cargar especies: {error}"
        )

        mensaje.color = ft.Colors.RED

    # ==========================================================
    # CARGAR DATOS PARA EDITAR
    # ==========================================================

    if mascota is not None:

        cliente_input.value = str(
            mascota.id_cliente
        )

        nombre_input.value = str(
            mascota.nombre
        )

        raza_input.value = str(
            mascota.raza
        )

        edad_input.value = str(
            mascota.edad
        )

        peso_input.value = str(
            mascota.peso
        )

        especie_input.value = str(
            mascota.id_especie
        )

    # ==========================================================
    # GUARDAR
    # ==========================================================

    def guardar_mascota(e):

        cliente = cliente_input.value.strip()

        nombre = nombre_input.value.strip()

        raza = raza_input.value.strip()

        especie = especie_input.value

        edad = edad_input.value.strip()

        peso = peso_input.value.strip()

        # ======================================================
        # VALIDAR CAMPOS
        # ======================================================

        if (

            cliente == ""

            or nombre == ""

            or raza == ""

            or especie is None

            or especie == ""

            or edad == ""

            or peso == ""

        ):

            mensaje.value = (
                "Todos los campos son obligatorios."
            )

            mensaje.color = ft.Colors.RED

            e.page.update()

            return

        try:

            cliente = int(cliente)

            edad = int(edad)

            peso = float(peso)

            id_especie = int(especie)

            mascota_dao = MascotaDAO()

            # ==================================================
            # NUEVA MASCOTA
            # ==================================================

            if mascota is None:

                id = (
                    mascota_dao.obtener_ultimo_id()
                    + 1
                )

                nueva_mascota = Mascota(

                    id,

                    cliente,

                    nombre,

                    raza,

                    id_especie,

                    edad,

                    peso

                )

                mascota_dao.insertar(
                    nueva_mascota
                )

                mensaje.value = (

                    f"Mascota '{nombre}' "

                    f"ha sido registrada con éxito."

                )

                # LIMPIAR CAMPOS

                cliente_input.value = ""

                nombre_input.value = ""

                raza_input.value = ""

                especie_input.value = None

                edad_input.value = ""

                peso_input.value = ""

                cliente_input.focus()

            # ==================================================
            # EDITAR MASCOTA
            # ==================================================

            else:

                mascota.id_cliente = cliente

                mascota.nombre = nombre

                mascota.raza = raza

                mascota.id_especie = id_especie

                mascota.edad = edad

                mascota.peso = peso

                mascota_dao.actualizar(
                    mascota
                )

                mensaje.value = (

                    f"Mascota '{nombre}' "

                    f"ha sido actualizada con éxito."

                )

            mensaje.color = ft.Colors.GREEN

        except ValueError:

            mensaje.value = (

                "Cliente y edad deben ser números "
                "enteros. El peso debe ser un número."

            )

            mensaje.color = ft.Colors.RED

        except Exception as error:

            mensaje.value = (

                f"Error al guardar la mascota: "
                f"{error}"

            )

            mensaje.color = ft.Colors.RED

        e.page.update()

    # ==========================================================
    # TÍTULO
    # ==========================================================

    if mascota is None:

        titulo = "Registro de nueva mascota"

        subtitulo = (
            "Capture los datos básicos de la mascota"
        )

    else:

        titulo = "Editar mascota"

        subtitulo = (
            "Modifique los datos de la mascota"
        )

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    return ft.Container(

        padding=30,

        content=ft.Column(

            controls=[

                # ==================================================
                # TÍTULO
                # ==================================================

                ft.Text(

                    titulo,

                    size=24,

                    weight=ft.FontWeight.BOLD,

                    color=VIOLETA

                ),

                # ==================================================
                # SUBTÍTULO
                # ==================================================

                ft.Text(

                    subtitulo,

                    size=16,

                    weight=ft.FontWeight.BOLD,

                    color=VIOLETA

                ),

                # ==================================================
                # CAMPOS
                # ==================================================

                cliente_input,

                nombre_input,

                especie_input,

                raza_input,

                edad_input,

                peso_input,

                # ==================================================
                # GUARDAR
                # ==================================================

                ft.ElevatedButton(

                    content=ft.Text(

                        "Guardar",

                        weight=ft.FontWeight.BOLD,

                        color=BLANCO

                    ),

                    icon=ft.Icons.SAVE,

                    style=ft.ButtonStyle(

                        bgcolor=VIOLETA,

                        color=BLANCO

                    ),

                    on_click=guardar_mascota

                ),

                # ==================================================
                # REGRESAR
                # ==================================================

                ft.OutlinedButton(

                    content=ft.Text(

                        "Regresar",

                        weight=ft.FontWeight.BOLD,

                        color=VIOLETA

                    ),

                    icon=ft.Icons.ARROW_BACK,

                    on_click=lambda e: regresar()

                ),

                # ==================================================
                # MENSAJE
                # ==================================================

                mensaje

            ],

            spacing=15

        )

    )