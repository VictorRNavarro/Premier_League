import pandas as pd
import os
import chardet

class CargadorDatos:
    def __init__(self, ruta_archivo, sep=None, encoding=None):
        self.ruta = ruta_archivo
        self.sep = sep
        self.encoding = encoding
        self.df = None

    # Detectar encoding automáticamente
    def detectar_encoding(self):
        with open(self.ruta, "rb") as f:
            result = chardet.detect(f.read(500000))  # analiza medio MB
        return result["encoding"]

    # Detectar delimitador automáticamente
    def detectar_delimitador(self):
        import csv

        with open(self.ruta, "r", encoding=self.encoding or "utf-8", errors="ignore") as f:
            sniffer = csv.Sniffer()
            sample = f.read(2048)
            f.seek(0)
            try:
                return sniffer.sniff(sample).delimiter
            except:
                return ","  # por defecto

    def cargar_csv(self):
        if not os.path.exists(self.ruta):
            raise FileNotFoundError(f"El archivo no existe: {self.ruta}")

        # Detectar encoding si no lo pasaron
        if self.encoding is None:
            self.encoding = self.detectar_encoding()
            print(f" Encoding detectado: {self.encoding}")

        # Detectar separador si no lo pasaron
        if self.sep is None:
            self.sep = self.detectar_delimitador()
            print(f" Separador detectado: '{self.sep}'")

        # Cargar CSV de forma robusta
        try:
            self.df = pd.read_csv(
                self.ruta,
                encoding=self.encoding,
                sep=self.sep,
                engine="python"
            )
        except Exception as e:
            print(" Error al leer el archivo CSV:")
            print(e)
            return None

        # Reporte obligatorio + mejorado

        print(" CARGA DE DATOS REALIZADA ")
        print(f" Archivo: {self.ruta}")
        print(f" Filas cargadas: {len(self.df)}")
        print(f" Columnas: {self.df.shape[1]}")

        # Porcentaje de nulos por columna
        print("\n Porcentaje de nulos por columna:")
        print((self.df.isnull().mean() * 100).round(2))

        # Nuevo: porcentaje total de nulos en el dataset
        total_celdas = self.df.size
        total_nulos = self.df.isnull().sum().sum()
        porcentaje_total = round((total_nulos / total_celdas) * 100, 2)

        print(f"\n Nulos totales: {total_nulos} de {total_celdas} celdas")
        print(f" Porcentaje total de nulos: {porcentaje_total}%")

        return self.df

