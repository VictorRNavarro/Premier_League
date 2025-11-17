import pandas as pd
import os

class ProcesadorEDA:

    def __init__(self, df):
        self.df = df

    def limpieza_datos(self):

        print(" PROCESO DE EDA ")

        # Eliminar duplicados
        self.df.drop_duplicates(inplace=True)

        # Convertir Age (de "26-290" a 26)
        if "Age" in self.df.columns:

            def obtener_age(valor):
                """
                Convierte '26-290' a 26 (solo años).
                """
                if pd.isna(valor):
                    return None
                try:
                    años = valor.split("-")[0]
                    return int(años)
                except:
                    return None

            self.df["Age"] = self.df["Age"].apply(obtener_age)

        # ---------------------------------------------------
        #  POSITION → CREAR DUMMIES (FW, AM, LW, RW, DM…)
        if "Position" in self.df.columns:

            # Convertir "FW,AM" → ["FW","AM"]
            self.df["PositionList"] = (
                self.df["Position"]
                .astype(str)
                .str.replace(" ", "", regex=False)
                .str.split(",")
            )

            # Obtener todas las posiciones detectadas
            posiciones_unicas = sorted(
                set(pos for lista in self.df["PositionList"] for pos in lista)
            )

            # Crear columna dummy por posición
            for pos in posiciones_unicas:
                self.df[f"POS_{pos}"] = self.df["PositionList"].apply(
                    lambda x: 1 if pos in x else 0
                )

            print(f"✔ Posiciones transformadas a columnas dummies: {posiciones_unicas}")

        # ------------------------------------
        # NORMALIZACIÓN DE PORCENTAJES
        if "Pass Completion %" in self.df.columns:
            self.df["Pass Completion %"] = (
                self.df["Pass Completion %"]
                .astype(str)
                .str.replace(",", ".", regex=False)
            )
            self.df["Pass Completion %"] = pd.to_numeric(
                self.df["Pass Completion %"], errors="coerce"
            )
            print("✔ Normalizado Pass Completion %")

        # ------------------------------------
        # CONVERSIÓN A NUMÉRICO DE OTRAS COLUMNAS
        columnas_float = [
            "Expected Goals (xG)",
            "Non-Penalty xG (npxG)",
            "Expected Assists (xAG)"
        ]

        for col in columnas_float:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors="coerce")

        # ------------------------------------
        # FECHAS
        if "Date" in self.df.columns:
            self.df["Date"] = pd.to_datetime(self.df["Date"], errors="coerce")
            print("✔ Convertida columna Date a datetime")

        # ------------------------------------
        # IMPUTACIÓN DE NULOS
        self.df.fillna(self.df.median(numeric_only=True), inplace=True)

        # ------------------------------------
        # GUARDAR CSV procesado
        output_folder = "src/data/processed"
        os.makedirs(output_folder, exist_ok=True)

        ruta_salida = f"{output_folder}/premier_clean.csv"
        self.df.to_csv(ruta_salida, index=False, encoding="utf-8")

        print("✔ Archivo limpio guardado en:", ruta_salida)

        return self.df

    # ============================================
    # MÉTODO: Resumen descriptivo
    # ============================================
    def resumen_descriptivo(self):
        """
        Retorna el resumen estadístico del dataset limpio.
        """
        print("=== RESUMEN DESCRIPTIVO ===")
        display(self.df.describe(include="all"))

    # ============================================
    # MÉTODO: Matriz de correlación
    # ============================================
    def matriz_correlacion(self):
        """
        Retorna la matriz de correlación de las columnas numéricas.
        """
        print("=== MATRIZ DE CORRELACIÓN ===")
        corr = self.df.corr(numeric_only=True)
        return corr
