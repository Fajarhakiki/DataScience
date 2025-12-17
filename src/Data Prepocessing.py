# Handle missing values
df_clean = df.dropna(subset=['price'])

# Select numeric features
numeric_features = ['symboling', 'normalized-losses', 'wheel-base', 'length',
                   'width', 'height', 'curb-weight', 'engine-size',
                   'bore', 'stroke', 'compression-ratio', 'horsepower',
                   'peak-rpm', 'city-mpg', 'highway-mpg']

available_features = [f for f in numeric_features if f in df_clean.columns]

# Prepare X and y
X = df_clean[available_features].copy()
y = df_clean['price'].copy()

# Drop rows with missing values
valid_idx = X.notna().all(axis=1)
X = X[valid_idx]
y = y[valid_idx]

print(f"Features used: {len(available_features)}")
print(f"Final data shape: {X.shape}")
print(f"Target shape: {y.shape}")
