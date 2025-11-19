from clases.jugador import Jugador

class Equipo:
    def __init__(self, name, liga="Premier League"):
        self.name = name
        self.liga = liga
        self.jugadores: list[Jugador] = []

    def agregar_jugador(self, jugador: Jugador):
        if jugador.team == self.name:
            self.jugadores.append(jugador)
        else:
            raise ValueError("El jugador pertenece a otro equipo.")

    def total_goles(self):
        return sum(j.goals for j in self.jugadores)

    def total_asistencias(self):
        return sum(j.assists for j in self.jugadores)

    def promedio_edad(self):
        edades = [j.age for j in self.jugadores if j.age is not None]
        return sum(edades) / len(edades) if edades else 0

    def top_goleadores(self, n=5):
        return sorted(self.jugadores, key=lambda j: j.goals, reverse=True)[:n]

    def __repr__(self):
        return f"Equipo({self.name}, Jugadores={len(self.jugadores)})"
