# Premier League Analytics - Proyecto Final

Este proyecto realiza un analisis completo de la Premier League utilizando Python, Programacion Orientada a Objetos (POO), analisis exploratorio de datos (EDA), limpieza, visualizacion y un dashboard interactivo creado con Streamlit.

El objetivo es construir un sistema que cargue datos desde un archivo CSV, los procese, genere estadisticas y presente visualizaciones para comprender mejor el rendimiento de jugadores y equipos.

---

## Fuente del dataset

El dataset utilizado proviene de:

https://www.kaggle.com/datasets/eduardopalmieri/premier-league-player-stats-season-2425/data

---

## Descripcion de las columnas del dataset

- Player: Nombre del jugador  
- Team: Equipo del jugador  
- #: Numero de camiseta  
- Nation: Nacionalidad del jugador  
- Position: Posicion principal en el campo  
- Age: Edad del jugador  
- Minutes: Minutos jugados  
- Goals: Goles anotados  
- Assists: Asistencias realizadas  
- Penalty Shoot on Goal: Penales lanzados al arco  
- Penalty Shoot: Penales intentados  
- Total Shoot: Total de tiros realizados  
- Shoot on Target: Tiros que fueron al arco  
- Yellow Cards: Tarjetas amarillas recibidas  
- Red Cards: Tarjetas rojas recibidas  
- Touches: Toques de balon  
- Dribbles: Dribles realizados  
- Tackles: Entradas realizadas  
- Blocks: Bloqueos realizados  
- Expected Goals (xG): Expectativa de gol  
- Non-Penalty xG (npxG): Expectativa de gol sin penales  
- Expected Assists (xAG): Expectativa de asistencia  
- Shot-Creating Actions: Acciones que generan un tiro  
- Goal-Creating Actions: Acciones que generan un gol  
- Passes Completed: Pases completados  
- Passes Attempted: Pases intentados  
- Pass Completion %: Porcentaje de pases completados  
- Progressive Passes: Pases progresivos  
- Carries: Conducciones  
- Progressive Carries: Conducciones progresivas  
- Dribble Attempts: Intentos de drible  
- Successful Dribbles: Dribles exitosos  
- Date: Fecha del registro  

---

## Caracteristicas principales del proyecto

- Carga dinamica de datos  
- Limpieza completa del dataset  
- Transformacion avanzada  
- Columnas dummy para posiciones  
- Estadisticas globales  
- Visualizaciones con Matplotlib y Seaborn  
- Dashboard interactivo con Streamlit  
- Clases POO (Jugador, Equipo)  
- Flujo de trabajo Gitflow  

---
## Estructura del proyecto

Premier_League/
- ├── src/
- │   ├── cargaDatos/
- │   │   └── cargador_datos.py
- │   ├── eda/
- │   │   └── procesador_eda.py
- │   ├── visualizacion/
- │   │   └── visualizador.py
- │   ├── clases/
- │   │   ├── jugador.py
- │   │   └── equipo.py
- │   ├── dashboard/
- │   │   └── app.py
- │   └── notebooks/
- │       ├── 01_EDA.ipynb
- │       └── 02_Visualizaciones.ipynb
- ├── data/
- │   ├── raw/
- │   │   └── premier.csv
- │   └── processed/
- │       └── premier_clean.csv
- └── README.md









---
## 1.Carga de datos

Incluye:

- Lectura flexible de CSV

- Detección de encoding

- Detección de delimitador

- Generación de un reporte inicial

- Manejo de errores y advertencias


---
## 2. EDA

Realiza:

- Eliminación de duplicados

- Limpieza de columnas (edad, fechas, porcentajes)

- Conversión de tipos

- Imputación por mediana

- Generación de dummies para posición

- Exportación del CSV limpio

---

## 3. Visualizaciones

Incluye gráficos como:

- Histogramas

- Scatterplots

- Heatmaps

- Barplots

- Top goleadores / asistencias

--- 

## 4. Programación Orientada a Objetos (POO)

Clases principales:

- Jugador:

Representa estadísticas individuales.

- Equipo:

Agrupa jugadores y calcula métricas del plantel.


---

## 5. Dashboard interactivo

Incluye:

- KPIs globales

- Distribución de edad

- Gráfico xG vs Goles

- Frecuencia de posiciones

- Tabla completa del dataset limpio

---
## Flujo de Git (Gitflow)

Ramas utilizadas:

- main → código estable

- feature/carga → carga de datos

- feature/eda → EDA

- feature/visualizaciones

- feature/clases

- feature/dashboard: Incluye el read.me

Cada funcionalidad se desarrolló en una rama separada con su respectivo Pull Request.

---