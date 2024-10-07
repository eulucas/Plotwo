import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Título do app
st.title("Visualizador de Ações")

# Barra de pesquisa para selecionar o símbolo da ação
stock_symbol = st.text_input("Digite o símbolo da ação (ex: AAPL, MSFT, TSLA):").upper()

# Definindo o período de tempo
if stock_symbol:
    # Slider para selecionar o período
    start_date = st.slider(
        "Selecione a data de início",
        min_value=datetime.date(2000, 1, 1),
        max_value=datetime.date.today(),
        value=(datetime.date(2020, 1, 1)),
        format="YYYY-MM-DD"
    )
    end_date = datetime.date.today()

    # Buscando os dados da ação
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    if not stock_data.empty:
        # Plotando os dados
        st.line_chart(stock_data['Close'])
    else:
        st.write("Não foi possível encontrar dados para o símbolo fornecido.")
