import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul Utama
st.title("🌍 Air Quality Dashboard for Wanshouxigong District: Monitoring Changes in Pollutants Over Time")

# Sidebar
st.sidebar.header('🔍 Air Quality Exploration')

# Load dataset
df = pd.read_csv('dashboard/main_data.csv')

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

import numpy as np

# Menghitung rata-rata polutan berdasarkan jam
average_pollutants_by_hour = filtered_df.groupby('hour')[['PM10', 'SO2', 'O3']].mean().reset_index()

# Line Plot
st.header('Average Concentration of Pollutants by Hour (Line Plot)')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(average_pollutants_by_hour['hour'], average_pollutants_by_hour['PM10'], label='PM10', marker='o')
ax.plot(average_pollutants_by_hour['hour'], average_pollutants_by_hour['SO2'], label='SO2', marker='o')
ax.plot(average_pollutants_by_hour['hour'], average_pollutants_by_hour['O3'], label='O3', marker='o')
ax.set_title('Rata-rata Konsentrasi Polutan Berdasarkan Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Konsentrasi Polutan (µg/m³)')
ax.set_xticks(average_pollutants_by_hour['hour'])
ax.legend()
ax.grid()
st.pyplot(fig)

# Bar Plot
st.header('Average Concentration of Pollutants by Hour (Bar Plot)')
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.25
hours = np.arange(len(average_pollutants_by_hour['hour']))

# Plot untuk PM10, SO2, dan O3
ax.bar(hours - bar_width, average_pollutants_by_hour['PM10'], width=bar_width, label='PM10', color='skyblue')
ax.bar(hours, average_pollutants_by_hour['SO2'], width=bar_width, label='SO2', color='orange')
ax.bar(hours + bar_width, average_pollutants_by_hour['O3'], width=bar_width, label='O3', color='green')

# Menambahkan judul dan label
ax.set_title('Rata-rata Konsentrasi Polutan Berdasarkan Jam (Bar Plot)', fontsize=14)
ax.set_xlabel('Jam', fontsize=12)
ax.set_ylabel('Konsentrasi Polutan (µg/m³)', fontsize=12)

# Menampilkan grid dan legenda
ax.set_xticks(hours)
ax.set_xticklabels(average_pollutants_by_hour['hour'])
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)

# Visualisasi tren curah hujan setiap bulan
st.header('Monthly Rain Trend')
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_df['month'], y=filtered_df['RAIN'], hue=filtered_df['year'], palette='Set1', ax=ax)
ax.set_xlabel('Month')
ax.set_ylabel('Rainfall (mm)')
ax.set_title('Monthly Rainfall Trend')
st.pyplot(fig)

average_rain = filtered_df.groupby(['year', 'month'])['RAIN'].mean().reset_index()

# Menampilkan bar plot untuk rata-rata curah hujan
st.header('Average Monthly Rainfall by Year')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='month', y='RAIN', hue='year', data=average_rain, palette='Set1', ax=ax)
ax.set_xlabel('Month')
ax.set_ylabel('Average Rainfall (mm)')
ax.set_title('Average Monthly Rainfall per Year')
st.pyplot(fig)

# Korelasi antara Suhu dan Polutan
st.header('Correlation between Temperature and Pollutants')
temp_corr = filtered_df[['TEMP', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()

# Visualisasi heatmap korelasi
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(temp_corr, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Korelasi antara Suhu dan Polutan')
st.pyplot(fig)

# Pairplot untuk melihat hubungan antar variabel
st.header('Pairplot between Temperature and Pollutants')
pairplot_fig = sns.pairplot(filtered_df[['TEMP', 'PM10', 'SO2', 'O3']])

# Menambahkan judul pada pairplot
pairplot_fig.fig.suptitle('Pairplot antara Temperatur dan Polutan', y=1.02, fontsize=14)

# Menampilkan plot di Streamlit
st.pyplot(pairplot_fig)

# Menampilkan Data Terfilter
st.header('Filtered Data')
st.dataframe(filtered_df)

# Opsi untuk mengunduh data terfilter
st.download_button('Download Filtered Data', filtered_df.to_csv(index=False).encode('utf-8'), 'filtered_data.csv', 'text/csv')
