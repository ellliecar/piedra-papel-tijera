import random
import time

# Opciones con emojis
opciones = {
    "piedra": "🪨",
    "papel": "📄",
    "tijera": "✂️"
}

# Reglas del juego
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate 🤝"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "¡Ganaste! 🎉"
    else:
        return "Perdiste 😢"

# Título
print("🕹️ ¡Bienvenido al juego Piedra, Papel o Tijera! 🕹️")
print("Elige una opción para jugar contra la computadora.\n")

# Bucle principal
while True:
    print("Opciones:")
    for opcion in opciones:
        print(f"- {opcion.capitalize()} {opciones[opcion]}")

    jugador = input("\n👉 Tu elección: ").lower()

    if jugador not in opciones:
        print("❌ Opción no válida. Intenta de nuevo.\n")
        continue

    print("\n🤖 La computadora está eligiendo", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    computadora = random.choice(list(opciones.keys()))

    print(f"\n🧍 Tú elegiste: {opciones[jugador]} ({jugador.capitalize()})")
    print(f"💻 Computadora eligió: {opciones[computadora]} ({computadora.capitalize()})")

    resultado = determinar_ganador(jugador, computadora)
    print(f"\n🔊 Resultado: {resultado}\n")

    jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra != "s":
        print("👋 Gracias por jugar. ¡Hasta pronto!")
        break
