class Juego:
    def __init__(self):
        self.puntaje_jugador = 0
        self.puntaje_pc = 0
        self.opciones = {"piedra": "🪨", "papel": "📄", "tijera": "✂️"}
        self.colores = {"piedra": "#30FFF7", "papel": "#FFFB00", "tijera": "#FF00FF"}
