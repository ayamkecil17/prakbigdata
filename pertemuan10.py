import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("pertemuan10 : interaksi streamlit dan yahoo finance")

kamus_ticker = {
    'GOOGL': 'Google',
    'AAPL' : 'Apple Inc',
    'SBUX' : 'Starbucks',
    'MCD' : "McDonal's Corp",
    'META' : "Meta Platforms Inc",
    'TLKM' : "Telkom Indonesia (Persero) Tbk PT",
    'BBNI' : "Bank Negara Indonesia (Persero) Tbk PT",
    'BMRI' : "Bank Mandiri (Persero) Tbk PT",
    'BBRI' : "Bank Rakyat Indonesia (Persero) Tbk PT",
    'NESN' : 'Nestle SA'
    
}
ticker_symbol = st.selectbox(
    'silihkan pilih kode perusahaan:',
    sorted( kamus_ticker.keys() )
)

st.write(ticker_symbol)
#ticker_symbol = 'GOOGL' 
#ticker_symbol ='AAPL'

ticker_data = yf.Ticker ( ticker_symbol )
pilihan_periode = st.selectbox(
    'pilih periode:',
    ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y']
)
tgl_mulai= st.date_input(
    'Mulai tanggal',
    value=date.today()
)
tgl_akhir= st.date_input(
    'sampai tanggal',
    value=date.today()
)
ticker_data = yf.Ticker( ticker_symbol )
df_ticker = ticker_data.history(
    period=pilihan_periode,
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

Pilihan_tampilan_tabel = st.checkbox('Tampilkan Tabel')
st.write(Pilihan_tampilan_tabel)

if Pilihan_tampilan_tabel == True:
    st.write("## Lima Data Awal")
    st.write( df_ticker.head())

pilihan_atribut = st.multiselect(
    'silahkan pilih atribut yang akan ditampilkan :',
    ['Low', 'High', 'Open', 'Close', 'Volume']
)
st.write(f"## Visualisasi Pergerakan Saham{kamus_ticker[ticker_symbol]}")


#st.write(pilihan_atribut)
grafik = px.line(
    df_ticker, 
    y = ['Open', 'Close'],
    title=f"Harga Saham {kamus_ticker[ticker_symbol]}"
)
st.plotly_chart(grafik)

