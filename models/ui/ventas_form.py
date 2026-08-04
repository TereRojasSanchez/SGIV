
import flet as ft
from datetime import date

from dao.ventas_dao import VentasDAO
from models.ventas import Ventas


# ==========================
# COLORES
# ==========================

VIOLETA = "#683266"
PURPURA = "#E1BEE7"
FONDO = "#F8F2FA"
BLANCO = "#FFFFFF"
NEGRO = "#000000"


def ventas_form(page, regresar, venta=None):

    dao = VentasDAO()

    # ==========================
    # ESTILO DE CAMPOS
    # ==========================

    estilo_texto = ft.TextStyle(
        weight=ft.FontWeight.BOLD,
        color=NEGRO
    )

    estilo_label = ft.TextStyle(
        weight=ft.FontWeight.BOLD,
        color=NEGRO
    )

    # ==========================
    # CAMPOS
    # ==========================

    id_input = ft.TextField(
        label="ID de la venta",
        width=400,
        read_only=True,
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    fecha_input = ft.TextField(
        label="Fecha de venta",
        width=400,
        value=str(date.today()),
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    id_producto_input = ft.TextField(
        label="ID del producto",
        width=400,
        keyboard_type=ft.KeyboardType.NUMBER,
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    producto_input = ft.TextField(
        label="Nombre del producto",
        width=400,
        read_only=True,
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    precio_input = ft.TextField(
        label="Precio de venta",
        width=400,
        read_only=True,
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    cantidad_input = ft.TextField(
        label="Cantidad",
        width=400,
        keyboard_type=ft.KeyboardType.NUMBER,
        value="1",
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    subtotal_input = ft.TextField(
        label="Subtotal",
        width=400,
        read_only=True,
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    total_input = ft.TextField(
        label="Total",
        width=400,
        read_only=True,
        filled=True,
        fill_color=PURPURA,
        text_style=estilo_texto,
        label_style=estilo_label
    )

    estado_input = ft.Dropdown(
        label="Estado",
        width=400,
        filled=True,
        fill_color=PURPURA,
        options=[
            ft.DropdownOption(
                key="Activa",
                text="Activa"
            ),
            ft.DropdownOption(
                key="Cancelada",
                text="Cancelada"
            )
        ],
        value="Activa"
    )

    # ==========================
    # BUSCAR PRODUCTO
    # ==========================

    def buscar_producto(e):

        if not id_producto_input.value:
            return

        try:

            id_producto = int(
                id_producto_input.value
            )

            producto = dao.obtener_producto(
                id_producto
            )

            if producto:

                # producto:
                # [id, nombre, precio_producto, existencia]

                producto_input.value = str(
                    producto[1]
                )

                precio_input.value = (
                    f"{float(producto[2]):.2f}"
                )

                calcular_total()

                page.update()

            else:

                producto_input.value = ""
                precio_input.value = ""
                subtotal_input.value = ""
                total_input.value = ""

                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        "El producto no existe."
                    )
                )

                page.snack_bar.open = True
                page.update()

        except ValueError:

            producto_input.value = ""
            precio_input.value = ""

            page.update()

        except Exception as ex:

            print(
                "Error al buscar producto:",
                ex
            )

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    f"Error: {ex}"
                )
            )

            page.snack_bar.open = True
            page.update()

    # ==========================
    # CALCULAR TOTAL
    # ==========================

    def calcular_total(e=None):

        try:

            precio = float(
                precio_input.value
            )

            cantidad = int(
                cantidad_input.value
            )

            if cantidad <= 0:
                raise ValueError()

            subtotal = precio * cantidad

            subtotal_input.value = (
                f"{subtotal:.2f}"
            )

            total_input.value = (
                f"{subtotal:.2f}"
            )

        except:

            subtotal_input.value = ""
            total_input.value = ""

        page.update()

    # ==========================
    # GUARDAR VENTA
    # ==========================

    def guardar(e):

        try:

            # --------------------------
            # VALIDACIONES
            # --------------------------

            if not id_producto_input.value:
                raise Exception(
                    "Debes ingresar el ID del producto."
                )

            if not producto_input.value:
                raise Exception(
                    "El producto no existe."
                )

            if not cantidad_input.value:
                raise Exception(
                    "Debes ingresar la cantidad."
                )

            id_producto = int(
                id_producto_input.value
            )

            cantidad = int(
                cantidad_input.value
            )

            if cantidad <= 0:
                raise Exception(
                    "La cantidad debe ser mayor a 0."
                )

            precio = float(
                precio_input.value
            )

            subtotal = precio * cantidad
            total = subtotal

            # ==========================
            # EDITAR VENTA
            # ==========================

            if venta:

                venta.fecha_venta = (
                    fecha_input.value
                )

                venta.producto_nombre = (
                    producto_input.value
                )

                venta.producto_precio_venta = (
                    precio
                )

                venta.cantidad = cantidad

                venta.subtotal = subtotal

                venta.total = total

                venta.id_producto = (
                    id_producto
                )

                venta.estado = (
                    estado_input.value
                )

                dao.actualizar(venta)

            # ==========================
            # NUEVA VENTA
            # ==========================

            else:

                nuevo_id = (
                    dao.obtener_ultimo_id() + 1
                )

                nueva_venta = Ventas(
                    nuevo_id,
                    fecha_input.value,
                    producto_input.value,
                    precio,
                    cantidad,
                    subtotal,
                    total,
                    id_producto,
                    estado_input.value
                )

                dao.insertar(
                    nueva_venta
                )

                # --------------------------
                # DESCONTAR EXISTENCIA
                # --------------------------

                dao.actualizar_existencia(
                    id_producto,
                    cantidad
                )

            # ==========================
            # MENSAJE
            # ==========================

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Venta guardada correctamente."
                )
            )

            page.snack_bar.open = True
            page.update()

            regresar()

        except Exception as ex:

            print(
                "Error al guardar venta:",
                ex
            )

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    f"Error al guardar: {ex}"
                )
            )

            page.snack_bar.open = True
            page.update()

    # ==========================
    # EVENTOS
    # ==========================

    id_producto_input.on_blur = buscar_producto

    cantidad_input.on_change = calcular_total

    # ==========================
    # EDITAR
    # ==========================

    if venta:

        id_input.value = str(
            venta.id
        )

        fecha_input.value = str(
            venta.fecha_venta
        )

        id_producto_input.value = str(
            venta.id_producto
        )

        producto_input.value = str(
            venta.producto_nombre
        )

        precio_input.value = (
            f"{float(venta.producto_precio_venta):.2f}"
        )

        cantidad_input.value = str(
            venta.cantidad
        )

        subtotal_input.value = (
            f"{float(venta.subtotal):.2f}"
        )

        total_input.value = (
            f"{float(venta.total):.2f}"
        )

        estado_input.value = str(
            venta.estado
        )

    # ==========================
    # NUEVA VENTA
    # ==========================

    else:

        id_input.value = str(
            dao.obtener_ultimo_id() + 1
        )

    # ==========================
    # TÍTULO
    # ==========================

    titulo = ft.Text(
        "Editar venta" if venta else "Agregar venta",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=VIOLETA
    )

    # ==========================
    # BOTÓN GUARDAR
    # ==========================

    boton_guardar = ft.ElevatedButton(
        content=ft.Text(
            "Guardar",
            weight=ft.FontWeight.BOLD
        ),
        icon=ft.Icons.SAVE,
        bgcolor=VIOLETA,
        color=BLANCO,
        width=150,
        height=45,
        on_click=guardar
    )

    # ==========================
    # BOTÓN CANCELAR
    # ==========================

    boton_cancelar = ft.ElevatedButton(
        content=ft.Text(
            "Cancelar",
            weight=ft.FontWeight.BOLD
        ),
        icon=ft.Icons.CANCEL,
        bgcolor=PURPURA,
        color=NEGRO,
        width=150,
        height=45,
        on_click=lambda e: regresar()
    )

    # ==========================
    # FORMULARIO
    # ==========================

    formulario = ft.Container(

        content=ft.Column(

            controls=[

                titulo,

                ft.Divider(
                    color=PURPURA
                ),

                # --------------------------
                # ID / FECHA
                # --------------------------

                ft.Row(
                    controls=[
                        id_input,
                        fecha_input
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30
                ),

                # --------------------------
                # PRODUCTO
                # --------------------------

                ft.Row(
                    controls=[
                        id_producto_input,
                        producto_input
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30
                ),

                # --------------------------
                # PRECIO / CANTIDAD
                # --------------------------

                ft.Row(
                    controls=[
                        precio_input,
                        cantidad_input
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30
                ),

                # --------------------------
                # SUBTOTAL / TOTAL
                # --------------------------

                ft.Row(
                    controls=[
                        subtotal_input,
                        total_input
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30
                ),

                # --------------------------
                # ESTADO
                # --------------------------

                ft.Row(
                    controls=[
                        estado_input
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                ft.Container(
                    height=20
                ),

                # --------------------------
                # BOTONES
                # --------------------------

                ft.Row(
                    controls=[
                        boton_guardar,
                        boton_cancelar
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )

            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=15,

            scroll=ft.ScrollMode.AUTO
        ),

        bgcolor=BLANCO,

        border_radius=15,

        padding=30,

        width=950,

        expand=True
    )

    # ==========================
    # VISTA
    # ==========================

    vista = ft.Container(

        content=formulario,

        bgcolor=FONDO,

        padding=30,

        expand=True
    )

    return vista
