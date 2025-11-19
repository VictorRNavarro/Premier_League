import matplotlib.pyplot as plt
import seaborn as sns

class Visualizador:

    def __init__(self, df):
        self.df = df
        plt.style.use("ggplot")

    def distribucion_edad(self):
        plt.figure(figsize=(8, 5))
        sns.histplot(self.df["Age"], kde=True)
        plt.title("Distribución de Edad")
        plt.xlabel("Edad")
        plt.ylabel("Frecuencia")
        plt.show()

    def top_goleadores(self, n=10):
        df_top = self.df.nlargest(n, "Goals")
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df_top, x="Goals", y="Player")
        plt.title(f"Top {n} jugadores con más goles")
        plt.xlabel("Goles")
        plt.ylabel("Jugador")
        plt.show()

    def top_asistencias(self, n=10):
        df_top = self.df.nlargest(n, "Assists")
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df_top, x="Assists", y="Player")
        plt.title(f"Top {n} jugadores con más asistencias")
        plt.xlabel("Asistencias")
        plt.ylabel("Jugador")
        plt.show()

    def distribucion_minutos(self):
        plt.figure(figsize=(8, 5))
        sns.histplot(self.df["Minutes"], kde=True)
        plt.title("Distribución de Minutos Jugados")
        plt.xlabel("Minutos")
        plt.ylabel("Frecuencia")
        plt.show()

    def xg_vs_goles(self):
        plt.figure(figsize=(7, 5))
        sns.scatterplot(data=self.df, x="Expected Goals (xG)", y="Goals")
        plt.title("Relación entre xG y Goles")
        plt.xlabel("Expected Goals (xG)")
        plt.ylabel("Goals")
        plt.show()

    def matriz_correlacion(self):
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.df.corr(numeric_only=True), cmap="coolwarm", annot=False)
        plt.title("Matriz de Correlación")
        plt.show()

    def frecuencia_posiciones(self):
        pos_cols = [c for c in self.df.columns if c.startswith("POS_")]
        pos_sum = self.df[pos_cols].sum().sort_values(ascending=False)

        plt.figure(figsize=(10, 5))
        sns.barplot(x=pos_sum.values, y=pos_sum.index)
        plt.title("Frecuencia de cada Posición")
        plt.xlabel("Cantidad de Jugadores")
        plt.ylabel("Posición")
        plt.show()
