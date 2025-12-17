fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Histogram
axes[0].hist(df['price'].dropna(), bins=30, edgecolor='black', alpha=0.7, color='skyblue')
axes[0].set_xlabel('Price ($)', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].set_title('Distribusi Harga Mobil', fontsize=14, fontweight='bold')
axes[0].grid(alpha=0.3)

# Box plot
axes[1].boxplot(df['price'].dropna())
axes[1].set_ylabel('Price ($)', fontsize=12)
axes[1].set_title('Box Plot Harga Mobil', fontsize=14, fontweight='bold')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()


# Hitung korelasi
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlations = df[numeric_cols].corr()['price'].sort_values(ascending=False)

# Plot
plt.figure(figsize=(10, 8))
correlations[1:11].plot(kind='barh', color='coral', edgecolor='black')
plt.xlabel('Correlation with Price', fontsize=12)
plt.title('Top 10 Fitur yang Berkorelasi dengan Harga', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("Top 10 Correlations with Price:")
print(correlations[1:11])


# Pilih top features
top_corr_features = correlations[1:11].index.tolist() + ['price']
corr_matrix = df[top_corr_features].corr()

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Heatmap Korelasi Fitur Terpenting', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))
plt.scatter(df['engine-size'], df['price'], alpha=0.6, edgecolors='black', s=50)
plt.xlabel('Engine Size', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('Hubungan Engine Size dengan Harga', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()