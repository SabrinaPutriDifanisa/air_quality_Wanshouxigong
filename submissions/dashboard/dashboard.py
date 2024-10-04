import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul Utama
st.title("🌍 Air Quality Dashboard for Wanshouxigong District: Monitoring Changes in Pollutants Over Time")

# Sidebar
st.sidebar.header('🔍 Air Quality Exploration')

# Load dataset
df = pd.read_csv("dashboard/main_data.csv")

# Buat kolom Date
df['Date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

# Sidebar untuk filter rentang waktu
st.sidebar.header('Filter Data')
start_year, end_year = st.sidebar.slider('Tahun', min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=(2013, 2017))

filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]

# Sidebar untuk memilih beberapa polutan
st.sidebar.header('Pilih Polutan')
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
selected_pollutants = st.sidebar.multiselect('Polutan', pollutants, default=['PM2.5'])

# Deskripsi Data
st.subheader('Data Description')
st.write(filtered_df.describe())

# Visualisasi polutan yang dipilih dari waktu ke waktu
st.header(f'Change {", ".join(selected_pollutants)} Pollutants from {start_year} to {end_year}')
fig, ax = plt.subplots(figsize=(10, 5))
for pollutant in selected_pollutants:
    ax.plot(filtered_df['Date'], filtered_df[pollutant], label=pollutant)
ax.set_xlabel('Waktu')
ax.set_ylabel('Konsentrasi (µg/m³)')
plt.legend()
st.pyplot(fig)

# Histogram untuk distribusi polutan yang dipilih
st.header(f'Distribution of {selected_pollutants[0]} Pollutants')
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_df[selected_pollutants[0]], kde=True, ax=ax)
ax.set_xlabel(f'Konsentrasi {selected_pollutants[0]} (µg/m³)')
st.pyplot(fig)

# Visualisasi tren curah hujan setiap bulan
st.header('Monthly Rain Trend')
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_df['month'], y=filtered_df['RAIN'], hue=filtered_df['year'], palette='Set1', ax=ax)
ax.set_xlabel('Month')
ax.set_ylabel('Rainfall (mm)')
ax.set_title('Monthly Rainfall Trend')
st.pyplot(fig)

# Menampilkan Data Terfilter
st.header('Filtered Data')
st.dataframe(filtered_df)

# Opsi untuk mengunduh data terfilter
st.download_button('Download Filtered Data', filtered_df.to_csv(index=False).encode('utf-8'), 'filtered_data.csv', 'text/csv')
