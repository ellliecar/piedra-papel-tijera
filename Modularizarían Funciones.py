def mostrar_elecciones(jugador, computadora):
    etiqueta_usuario.config(
        text=f"🧑 Tú: {opciones[jugador]} ({jugador.capitalize()})",
        bg=colores[jugador]
    )
    etiqueta_computadora.config(
        text=f"💻 PC: {opciones[computadora]} ({computadora.capitalize()})",
        bg=colores[computadora]
    )
