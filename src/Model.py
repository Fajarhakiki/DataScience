print("="*60)
print("MODEL 1: LINEAR REGRESSION")
print("="*60)

# Train
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

# Predict
y_pred_lr_train = lr_model.predict(X_train_scaled)
y_pred_lr_test = lr_model.predict(X_test_scaled)

# Evaluate
lr_train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_lr_train))
lr_test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr_test))
lr_train_r2 = r2_score(y_train, y_pred_lr_train)
lr_test_r2 = r2_score(y_test, y_pred_lr_test)
lr_test_mae = mean_absolute_error(y_test, y_pred_lr_test)

print(f"\nTrain RMSE: ${lr_train_rmse:,.2f}")
print(f"Test RMSE:  ${lr_test_rmse:,.2f}")
print(f"Train R²:   {lr_train_r2:.4f}")
print(f"Test R²:    {lr_test_r2:.4f}")
print(f"Test MAE:   ${lr_test_mae:,.2f}")

joblib.dump(lr_model, 'linear_regression_model.pkl')



print("="*60)
print("MODEL 2: RANDOM FOREST REGRESSOR")
print("="*60)

# Train
rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)

# Predict
y_pred_rf_train = rf_model.predict(X_train)
y_pred_rf_test = rf_model.predict(X_test)

# Evaluate
rf_train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_rf_train))
rf_test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_rf_test))
rf_train_r2 = r2_score(y_train, y_pred_rf_train)
rf_test_r2 = r2_score(y_test, y_pred_rf_test)
rf_test_mae = mean_absolute_error(y_test, y_pred_rf_test)

print(f"\nTrain RMSE: ${rf_train_rmse:,.2f}")
print(f"Test RMSE:  ${rf_test_rmse:,.2f}")
print(f"Train R²:   {rf_train_r2:.4f}")
print(f"Test R²:    {rf_test_r2:.4f}")
print(f"Test MAE:   ${rf_test_mae:,.2f}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 5 Feature Importance:")
print(feature_importance.head())

joblib.dump(rf_model, 'random_forest_model.pkl')



print("="*60)
print("MODEL 3: DEEP LEARNING (NEURAL NETWORK)")
print("="*60)

# Build model
dl_model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(16, activation='relu'),
    layers.Dense(1)
])

# Compile
dl_model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# Train
history = dl_model.fit(
    X_train_scaled, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=32,
    verbose=1
)

# Predict
y_pred_dl_train = dl_model.predict(X_train_scaled, verbose=0).flatten()
y_pred_dl_test = dl_model.predict(X_test_scaled, verbose=0).flatten()

# Evaluate
dl_train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_dl_train))
dl_test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_dl_test))
dl_train_r2 = r2_score(y_train, y_pred_dl_train)
dl_test_r2 = r2_score(y_test, y_pred_dl_test)
dl_test_mae = mean_absolute_error(y_test, y_pred_dl_test)

print(f"\nTrain RMSE: ${dl_train_rmse:,.2f}")
print(f"Test RMSE:  ${dl_test_rmse:,.2f}")
print(f"Train R²:   {dl_train_r2:.4f}")
print(f"Test R²:    {dl_test_r2:.4f}")
print(f"Test MAE:   ${dl_test_mae:,.2f}")

dl_model.save('deep_learning_model.h5')