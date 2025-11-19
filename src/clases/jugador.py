class Jugador:
    def __init__(self, name, team, position, age, minutes, goals, assists, **kwargs):
        self.name = name
        self.team = team
        self.position = position
        self.age = age
        self.minutes = minutes
        self.goals = goals
        self.assists = assists

        # Guardar cualquier otro atributo extra (xG, xAG, etc.)
        self.extra = kwargs

    def __repr__(self):
        return f"Jugador({self.name}, {self.team}, {self.position})"

    def rendimiento_general(self):

        # Métrica simple de rendimiento:
        # goles + asistencias + (extras como xG si existen)

        rendimiento = self.goals + self.assists
        if "xG" in self.extra:
            rendimiento += self.extra["xG"]
        return rendimiento
