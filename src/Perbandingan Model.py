# Create comparison dataframe
results = {
    'Model': ['Linear Regression', 'Random Forest', 'Deep Learning'],
    'Test RMSE': [lr_test_rmse, rf_test_rmse, dl_test_rmse],
    'Test R²': [lr_test_r2, rf_test_r2, dl_test_r2],
    'Test MAE': [lr_test_mae, rf_test_mae, dl_test_mae]
}

results_df = pd.DataFrame(results)
print("="*60)
print("PERBANDINGAN MODEL")
print("="*60)
print(results_df.to_string(index=False))

# Visualisasi perbandingan
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

models = results['Model']

# RMSE
axes[0].bar(models, results['Test RMSE'],
           color=['#3498db', '#2ecc71', '#e74c3c'], edgecolor='black', linewidth=1.5)
axes[0].set_ylabel('RMSE ($)', fontsize=12)
axes[0].set_title('Test RMSE Comparison', fontsize=14, fontweight='bold')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(alpha=0.3, axis='y')

# R²
axes[1].bar(models, results['Test R²'],
           color=['#3498db', '#2ecc71', '#e74c3c'], edgecolor='black', linewidth=1.5)
axes[1].set_ylabel('R² Score', fontsize=12)
axes[1].set_title('Test R² Comparison', fontsize=14, fontweight='bold')
axes[1].tick_params(axis='x', rotation=45)
axes[1].set_ylim([0, 1])
axes[1].grid(alpha=0.3, axis='y')

# MAE
axes[2].bar(models, results['Test MAE'],
           color=['#3498db', '#2ecc71', '#e74c3c'], edgecolor='black', linewidth=1.5)
axes[2].set_ylabel('MAE ($)', fontsize=12)
axes[2].set_title('Test MAE Comparison', fontsize=14, fontweight='bold')
axes[2].tick_params(axis='x', rotation=45)
axes[2].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

best_model_idx = results_df['Test RMSE'].idxmin()
best_model = results_df.loc[best_model_idx, 'Model']

print("\n" + "="*60)
print("KESIMPULAN")
print("="*60)
print(f"\n🏆 Model Terbaik: {best_model}")
print(f"   Test RMSE: ${results_df.loc[best_model_idx, 'Test RMSE']:,.2f}")
print(f"   Test R²: {results_df.loc[best_model_idx, 'Test R²']:.4f}")
print(f"   Test MAE: ${results_df.loc[best_model_idx, 'Test MAE']:,.2f}")
print("\n" + "="*60)