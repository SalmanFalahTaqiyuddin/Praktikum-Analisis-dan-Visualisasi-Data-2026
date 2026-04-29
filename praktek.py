import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

df = pd.read_csv('data_praktikum_analisis_data.csv')

df = df[df['Price_Per_Unit'] > 0]
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
plt.title('Analisis Tren Penjualan Bulanan (Line Chart)')
plt.xticks(rotation=45)
plt.savefig('AnalisisTrenPenjualanBulanan(Line Chart).png', bbox_inches='tight')
plt.show()

correlation = df[['Total_Sales','Ad_Budget', 'Price_Per_Unit']].corr()
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Analisis Korelasi (Heatmap)')
plt.savefig('AnalisisKorelasi(Heatmap).png', bbox_inches='tight')
plt.show()

avg_price = df['Price_Per_Unit'].mean()
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Price_Per_Unit', y='Quantity', hue='Product_Category')
plt.axvline(avg_price, color='pink', linestyle='--', label='Rata-rata Harga')
plt.title('Identifikasi Produk "Underperformer"')
plt.legend()
plt.savefig('IdentifikasiProdukUnderperformer.png', bbox_inches='tight')
plt.show()

snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

rfm['RFM_Segment'] = rfm.R_Score.astype(str) + rfm.F_Score.astype(str) + rfm.M_Score.astype(str)
print("\nHasil Segmentasi RFM (5 Teratas):")
print(rfm.head())

category_analysis = df.groupby('Product_Category').agg({
    'Total_Sales': 'sum',
    'Ad_Budget': 'sum'
})
category_analysis['Efficiency'] = category_analysis['Total_Sales'] / category_analysis['Ad_Budget']
category_analysis = category_analysis.sort_values(by='Efficiency')

plt.figure(figsize=(10, 5))
category_analysis['Efficiency'].plot(kind='barh', color='skyblue')
plt.title('Segmentasi Pelanggan (RFM Analysis)')
plt.xlabel('Rasio Efisiensi')
plt.savefig('SegmentasiPelanggan(RFM Analysis).png', bbox_inches='tight')
plt.show()

median_ads = df['Ad_Budget'].median()
high_ads = df[df['Ad_Budget'] > median_ads]['Total_Sales']
low_ads = df[df['Ad_Budget'] <= median_ads]['Total_Sales']

print(f"\nRata-rata Penjualan Iklan Tinggi: {high_ads.mean():.2f}")
print(f"Rata-rata Penjualan Iklan Rendah: {low_ads.mean():.2f}")

if high_ads.mean() > low_ads.mean():
    print("Kesimpulan: Peningkatan Ad_Budget cenderung menghasilkan lebih banyak penjualan.")
else:
    print("Kesimpulan: Ad_Budget tidak memiliki dampak yang signifikan secara keseluruhan.")