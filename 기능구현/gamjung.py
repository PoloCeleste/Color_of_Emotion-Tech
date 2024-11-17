import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Data with English emotion names
data = [
    {'Joy': 0.0, 'Confusion': 0.94, 'Anger': 1.29, 'Anxiety': 4.23, 'Hurt': 3.9, 'Sadness': 2.03, 'Neutral': 87.6},
    {'Joy': 0.0, 'Confusion': 8.06, 'Anger': 1.35, 'Anxiety': 7.21, 'Hurt': 6.09, 'Sadness': 1.3, 'Neutral': 76.01},
    {'Joy': 0.0, 'Confusion': 1.18, 'Anger': 3.51, 'Anxiety': 5.64, 'Hurt': 14.98, 'Sadness': 8.57, 'Neutral': 66.12},
    {'Joy': 0.0, 'Confusion': 1.45, 'Anger': 16.34, 'Anxiety': 12.8, 'Hurt': 11.31, 'Sadness': 5.98, 'Neutral': 52.12},
    {'Joy': 0.0, 'Confusion': 3.9, 'Anger': 7.58, 'Anxiety': 11.8, 'Hurt': 2.73, 'Sadness': 0.97, 'Neutral': 73.02},
    {'Joy': 0.0, 'Confusion': 0.54, 'Anger': 0.43, 'Anxiety': 4.81, 'Hurt': 6.5, 'Sadness': 8.41, 'Neutral': 79.31},
    {'Joy': 0.0, 'Confusion': 38.61, 'Anger': 0.86, 'Anxiety': 12.12, 'Hurt': 3.6, 'Sadness': 2.14, 'Neutral': 42.67},
    {'Joy': 0.0, 'Confusion': 5.11, 'Anger': 13.52, 'Anxiety': 23.27, 'Hurt': 4.91, 'Sadness': 1.55, 'Neutral': 51.64},
    {'Joy': 0.0, 'Confusion': 10.43, 'Anger': 5.69, 'Anxiety': 52.11, 'Hurt': 6.04, 'Sadness': 1.14, 'Neutral': 24.58},
    {'Joy': 0.0, 'Confusion': 3.59, 'Anger': 1.42, 'Anxiety': 10.77, 'Hurt': 16.99, 'Sadness': 6.14, 'Neutral': 61.09},
    {'Joy': 0.0, 'Confusion': 5.3, 'Anger': 1.3, 'Anxiety': 13.78, 'Hurt': 3.6, 'Sadness': 1.93, 'Neutral': 74.1},
    {'Joy': 0.0, 'Confusion': 0.35, 'Anger': 1.1, 'Anxiety': 10.01, 'Hurt': 21.24, 'Sadness': 13.76, 'Neutral': 53.55},
    {'Joy': 0.0, 'Confusion': 7.55, 'Anger': 1.15, 'Anxiety': 6.64, 'Hurt': 4.13, 'Sadness': 1.42, 'Neutral': 79.11},
    {'Joy': 0.0, 'Confusion': 14.34, 'Anger': 0.46, 'Anxiety': 4.69, 'Hurt': 1.08, 'Sadness': 0.33, 'Neutral': 79.1},
    {'Joy': 0.0, 'Confusion': 3.77, 'Anger': 0.17, 'Anxiety': 8.98, 'Hurt': 4.05, 'Sadness': 0.68, 'Neutral': 82.35},
    {'Joy': 0.0, 'Confusion': 13.05, 'Anger': 1.8, 'Anxiety': 9.92, 'Hurt': 0.78, 'Sadness': 0.42, 'Neutral': 74.04},
    {'Joy': 0.0, 'Confusion': 22.83, 'Anger': 0.15, 'Anxiety': 8.83, 'Hurt': 3.46, 'Sadness': 0.73, 'Neutral': 64.0},
    {'Joy': 0.0, 'Confusion': 11.98, 'Anger': 2.55, 'Anxiety': 1.99, 'Hurt': 0.2, 'Sadness': 0.14, 'Neutral': 83.14},
    {'Joy': 0.0, 'Confusion': 6.58, 'Anger': 0.3, 'Anxiety': 1.03, 'Hurt': 1.02, 'Sadness': 0.19, 'Neutral': 90.88},
    {'Joy': 0.0, 'Confusion': 4.1, 'Anger': 1.99, 'Anxiety': 7.56, 'Hurt': 2.74, 'Sadness': 0.37, 'Neutral': 83.23},
    {'Joy': 0.0, 'Confusion': 33.08, 'Anger': 2.05, 'Anxiety': 8.01, 'Hurt': 2.32, 'Sadness': 0.45, 'Neutral': 54.1},
    {'Joy': 0.0, 'Confusion': 17.08, 'Anger': 1.84, 'Anxiety': 8.07, 'Hurt': 1.12, 'Sadness': 0.29, 'Neutral': 71.59},
    {'Joy': 0.0, 'Confusion': 11.13, 'Anger': 0.98, 'Anxiety': 7.19, 'Hurt': 1.35, 'Sadness': 0.73, 'Neutral': 78.61},
    {'Joy': 0.0, 'Confusion': 15.86, 'Anger': 0.17, 'Anxiety': 7.52, 'Hurt': 3.53, 'Sadness': 0.79, 'Neutral': 72.13},
    {'Joy': 0.0, 'Confusion': 6.14, 'Anger': 2.79, 'Anxiety': 13.23, 'Hurt': 7.21, 'Sadness': 1.05, 'Neutral': 69.57},
    {'Joy': 0.0, 'Confusion': 5.71, 'Anger': 0.63, 'Anxiety': 3.05, 'Hurt': 0.29, 'Sadness': 0.07, 'Neutral': 90.25},
    {'Joy': 0.0, 'Confusion': 5.8, 'Anger': 2.43, 'Anxiety': 8.14, 'Hurt': 2.02, 'Sadness': 0.96, 'Neutral': 80.64},
    {'Joy': 0.0, 'Confusion': 14.01, 'Anger': 2.82, 'Anxiety': 14.09, 'Hurt': 1.71, 'Sadness': 1.22, 'Neutral': 66.15},
    {'Joy': 0.0, 'Confusion': 11.03, 'Anger': 7.63, 'Anxiety': 11.78, 'Hurt': 1.53, 'Sadness': 0.37, 'Neutral': 67.66},
    {'Joy': 0.0, 'Confusion': 6.3, 'Anger': 0.16, 'Anxiety': 8.96, 'Hurt': 5.75, 'Sadness': 3.62, 'Neutral': 75.21},
    {'Joy': 0.0, 'Confusion': 4.89, 'Anger': 0.82, 'Anxiety': 3.18, 'Hurt': 1.89, 'Sadness': 0.5, 'Neutral': 88.72},
    {'Joy': 0.0, 'Confusion': 1.37, 'Anger': 0.72, 'Anxiety': 7.05, 'Hurt': 5.25, 'Sadness': 2.61, 'Neutral': 83.0},
    {'Joy': 0.0, 'Confusion': 0.77, 'Anger': 1.71, 'Anxiety': 5.32, 'Hurt': 4.41, 'Sadness': 0.75, 'Neutral': 87.05}
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Perform Min-Max normalization
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Calculate standard deviation for each emotion after normalization
std_devs_normalized = df_normalized.std()

print("Standard deviation for each emotion after normalization:")
for emotion, std in std_devs_normalized.items():
    print(f"{emotion}: {std:.4f}")

# Visualize standard deviations of normalized data with a bar graph
plt.figure(figsize=(12, 6))
std_devs_normalized.plot(kind='bar')
plt.title('Standard Deviation of Each Emotion After Normalization')
plt.xlabel('Emotion')
plt.ylabel('Standard Deviation')
plt.xticks(rotation=45)
for i, v in enumerate(std_devs_normalized):
    plt.text(i, v, f'{v:.4f}', ha='center', va='bottom')
plt.tight_layout()
plt.show()

# Compare standard deviations of original and normalized data
std_devs_original = df.std()
comparison = pd.DataFrame({
    'Original Data std': std_devs_original,
    'Normalized Data std': std_devs_normalized
})

print("\nComparison of standard deviations between original and normalized data:")
print(comparison)

# Visualize comparison results
plt.figure(figsize=(12, 6))
comparison.plot(kind='bar')
plt.title('Comparison of Standard Deviations: Original vs Normalized Data')
plt.xlabel('Emotion')
plt.ylabel('Standard Deviation')
plt.xticks(rotation=45)
plt.legend(['Original Data', 'Normalized Data'])
plt.tight_layout()
plt.show()
