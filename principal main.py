import tkinter as tk
import random
import threading
import time

# Opciones con emojis
opciones = {
    "piedra": "🪨",
    "papel": "📄",
    "tijera": "✂️"
}

# Colores neón para el tema
colores = {
    "piedra": "#30FFF7",   # Neón cyan
    "papel": "#FFFB00",    # Neón amarillo
    "tijera": "#FF00FF"    # Neón rosa
}

bg_neon = "#090024"
borde_neon = "#27F9FF"

# Variables globales de puntaje
puntaje_jugador = 0
puntaje_pc = 0

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate 🤝"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "¡Ganaste! 🎉"
    else:
        return "Perdiste 😢"

def animar_pensando():
    animacion = ["🤖", "🤖.", "🤖..", "🤖..."]
    for _ in range(2):
        for paso in animacion:
            etiqueta_pensando.config(text=f"La computadora está pensando{paso}")
            time.sleep(0.25)
    etiqueta_pensando.config(text="")

def jugar(eleccion_jugador):
    for b in botones:
        b.config(state=tk.DISABLED)
    boton_terminar.config(state=tk.DISABLED)
    boton_seguir.config(state=tk.DISABLED)
    etiqueta_resultado.config(text="")
    etiqueta_pensando.config(text="La computadora está pensando 🤖")
    etiqueta_computadora.config(text="")

    def turno_pc():
        global puntaje_jugador, puntaje_pc
        animar_pensando()
        computadora = random.choice(list(opciones.keys()))
        resultado = determinar_ganador(eleccion_jugador, computadora)
        etiqueta_usuario.config(
            text=f"🧑 Tú: {opciones[eleccion_jugador]} ({eleccion_jugador.capitalize()})",
            bg=colores[eleccion_jugador]
        )
        etiqueta_computadora.config(
            text=f"💻 PC: {opciones[computadora]} ({computadora.capitalize()})",
            bg=colores[computadora]
        )
        etiqueta_resultado.config(text=f"{resultado}")

        if resultado == "¡Ganaste! 🎉":
            puntaje_jugador += 1
        elif resultado == "Perdiste 😢":
            puntaje_pc += 1
        actualizar_puntaje()

        boton_terminar.config(state=tk.NORMAL)
        boton_seguir.config(state=tk.NORMAL)

    threading.Thread(target=turno_pc).start()

def actualizar_puntaje():
    texto = f"Puntaje  🧑 Tú: {puntaje_jugador}   |   💻 PC: {puntaje_pc}"
    etiqueta_puntaje.config(text=texto)

def reiniciar_ronda():
    for b in botones:
        b.config(state=tk.NORMAL)
    etiqueta_usuario.config(text="", bg=bg_neon)
    etiqueta_computadora.config(text="", bg=bg_neon)
    etiqueta_resultado.config(text="")
    etiqueta_pensando.config(text="")
    boton_terminar.config(state=tk.DISABLED)
    boton_seguir.config(state=tk.DISABLED)

def terminar_juego():
    for b in botones:
        b.config(state=tk.DISABLED)
    etiqueta_usuario.config(text="", bg=bg_neon)
    etiqueta_computadora.config(text="", bg=bg_neon)
    etiqueta_resultado.config(
        text="¡Gracias por jugar!\nPara volver a jugar, reinicia el programa.",
        fg="#00FF00"
    )
    etiqueta_pensando.config(text="")
    boton_terminar.config(state=tk.DISABLED)
    boton_seguir.config(state=tk.DISABLED)

def iniciar_juego():
    frame_inicio.pack_forget()
    frame_juego.pack(fill="both", expand=True)
    reiniciar_ronda()

# ---- VENTANA PRINCIPAL ----
ventana = tk.Tk()
ventana.title("🥊 Piedra, Papel o Tijera - Gamer Neon 🕹️")
ventana.configure(bg=bg_neon)
ventana.geometry("560x540")

# ---- FRAME INICIO ----
frame_inicio = tk.Frame(ventana, bg=bg_neon)
frame_inicio.pack(fill="both", expand=True)

titulo_inicio = tk.Label(frame_inicio, text="¡Piedra, Papel o Tijera!", font=("Arial Black", 28), fg="#FF00FF", bg=bg_neon)
titulo_inicio.pack(pady=40)

mensaje_inicio = tk.Label(frame_inicio, text="Click para INICIAR", font=("Arial", 18), bg=bg_neon, fg="#39FF14")
mensaje_inicio.pack(pady=20)

boton_iniciar = tk.Button(frame_inicio, text="INICIAR JUEGO", font=("Arial Black", 16), bg="#0FF0FC", fg=bg_neon, width=20, height=2, command=iniciar_juego, bd=8, relief="ridge", highlightbackground=borde_neon)
boton_iniciar.pack(pady=40)

# ---- FRAME JUEGO ----
frame_juego = tk.Frame(ventana, bg=bg_neon)

instruccion = tk.Label(frame_juego, text="Elige tu jugada:", font=("Arial", 16), bg=bg_neon, fg="#39FF14")
instruccion.pack(pady=(10, 0))

etiqueta_puntaje = tk.Label(frame_juego, text="", font=("Arial Black", 15), bg=bg_neon, fg="#FFF200")
etiqueta_puntaje.pack(pady=10)
actualizar_puntaje()

frame_botones = tk.Frame(frame_juego, bg=bg_neon)
frame_botones.pack(pady=20)
botones = []
for opcion in opciones:
    b = tk.Button(
        frame_botones,
        text=f"{opcion.capitalize()} {opciones[opcion]}",
        width=12,
        height=2,
        font=("Arial Black", 16),
        bg=colores[opcion],
        fg=bg_neon,
        command=lambda op=opcion: jugar(op),
        bd=6,
        relief="groove",
        highlightbackground="#FFF200"
    )
    b.pack(side=tk.LEFT, padx=15)
    botones.append(b)

etiqueta_pensando = tk.Label(frame_juego, text="", font=("Arial", 14, "italic"), bg=bg_neon, fg="#0FF0FC")
etiqueta_pensando.pack(pady=5)

etiqueta_usuario = tk.Label(frame_juego, text="", font=("Arial Black", 16), bg=bg_neon, fg="#39FF14")
etiqueta_usuario.pack(pady=5)

etiqueta_computadora = tk.Label(frame_juego, text="", font=("Arial Black", 16), bg=bg_neon, fg="#F72585")
etiqueta_computadora.pack(pady=5)

etiqueta_resultado = tk.Label(frame_juego, text="", font=("Arial Black", 20), bg=bg_neon, fg="#FFF200")
etiqueta_resultado.pack(pady=20)

frame_opciones = tk.Frame(frame_juego, bg=bg_neon)
frame_opciones.pack(pady=10)
boton_seguir = tk.Button(frame_opciones, text="Seguir jugando", font=("Arial Black", 13), bg="#0FF0FC", fg=bg_neon, width=16, state=tk.DISABLED, command=reiniciar_ronda, bd=6, relief="ridge", highlightbackground=borde_neon)
boton_seguir.pack(side=tk.LEFT, padx=10)
boton_terminar = tk.Button(frame_opciones, text="Terminar juego", font=("Arial Black", 13), bg="#FF00FF", fg=bg_neon, width=16, state=tk.DISABLED, command=terminar_juego, bd=6, relief="ridge", highlightbackground=borde_neon)
boton_terminar.pack(side=tk.LEFT, padx=10)

creditos = tk.Label(frame_juego, text="Hecho por ellliecar", font=("Arial", 10), bg=bg_neon, fg="#3273DC")
creditos.pack(side=tk.BOTTOM, pady=8)

ventana.mainloop()
