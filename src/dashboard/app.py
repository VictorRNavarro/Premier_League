import streamlit as st
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
##streamlit run src/dashboard/app.py
##ejecutar en la terminal
# Añadir src al path
sys.path.append("src")

st.set_page_config(
    page_title="Premier League Dashboard",
    layout="wide"
)

st.title("Premier League Dashboard")


@st.cache_data
def cargar_datos():
    # Ruta absoluta segura
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(base_path, "data", "processed", "premier_clean.csv")

    st.write("Ruta cargada:", ruta)  # debug

    if not os.path.exists(ruta):
        st.error("No se encontró el archivo premier_clean.csv. Ejecute el EDA antes.")
        return pd.DataFrame()

    return pd.read_csv(ruta)


df = cargar_datos()

if df.empty:
    st.stop()


# ----------------------------
# KPIs
# ----------------------------
st.subheader("Indicadores generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de goles", int(df["Goals"].sum()))

with col2:
    st.metric("Total de asistencias", int(df["Assists"].sum()))

with col3:
    st.metric("Minutos promedio jugados", round(df["Minutes"].mean(), 2))


# ----------------------------
# Distribución Edad
# ----------------------------
st.subheader("Distribución de la edad de los jugadores")

fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(df["Age"], kde=True, ax=ax)
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
st.pyplot(fig)


# ----------------------------
# xG vs Goals
# ----------------------------
st.subheader("Relación entre Expected Goals (xG) y Goles")

fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=df, x="Expected Goals (xG)", y="Goals", ax=ax2)
plt.xlabel("Expected Goals (xG)")
plt.ylabel("Goles")
st.pyplot(fig2)


# ----------------------------
# Frecuencia de posiciones
# ----------------------------
st.subheader("Frecuencia de posiciones")

pos_cols = [c for c in df.columns if c.startswith("POS_")]
pos_sum = df[pos_cols].sum().sort_values(ascending=False)

fig3, ax3 = plt.subplots(figsize=(7, 5))
sns.barplot(x=pos_sum.values, y=pos_sum.index, ax=ax3)
plt.xlabel("Cantidad de jugadores")
plt.ylabel("Posición")
st.pyplot(fig3)


# ----------------------------
# Tabla completa
# ----------------------------
st.subheader("Datos completos")

st.dataframe(df, height=400)
