
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Robô de Futebol - Análise Completa", layout="wide")
st.title("Robô de Futebol - Gols e Escanteios por Tempo com Probabilidades Reais")

tab1, tab2 = st.tabs(["⚽ Jogos AO VIVO", "📅 Jogos FUTUROS"])

# Dados fictícios simulando dados reais (em produção, virão de API)
agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with tab1:
    st.subheader("Jogos ao vivo - atualizados em tempo real")
    st.info(f"Última atualização: {agora}")
    df_live = pd.read_csv("data/jogos_ao_vivo.csv")
    st.dataframe(df_live, use_container_width=True)

with tab2:
    st.subheader("Jogos futuros - todos os campeonatos")
    df_future = pd.read_csv("data/jogos_futuros.csv")
    df_future['Destaque'] = df_future.apply(lambda row: '🟢' if row['Over_1.5_Gols(%)'] > 85 and float(row['EV']) > 0 else '', axis=1)
    st.dataframe(df_future, use_container_width=True)
