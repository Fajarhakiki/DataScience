!pip install ucimlrepo
from ucimlrepo import fetch_ucirepo

# Fetch dataset
automobile = fetch_ucirepo(id=10)

# Combine features and target
df = pd.concat([automobile.data.features, automobile.data.targets], axis=1)

print(f"Dataset shape: {df.shape}")
print(f"\nColumns:\n{df.columns.tolist()}")
df.head()