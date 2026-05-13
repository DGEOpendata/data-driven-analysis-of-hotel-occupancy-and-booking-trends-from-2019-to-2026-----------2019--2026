python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'path_to_your_file/Abu_Dhabi_Hotels_Open_Datasets_1_Supply_by_zones.xlsx'
df = pd.read_excel(file_path)

# Display basic information about the dataset
print("Dataset Information:")
df.info()

# Data Preprocessing: Handle missing values
df.dropna(subset=['Occupancy Rate', 'Room Type', 'Region'], inplace=True)

# Group by Region and calculate average occupancy rate
region_occupancy = df.groupby('Region')['Occupancy Rate'].mean().sort_values(ascending=False)

# Plotting the average occupancy rate by region
plt.figure(figsize=(12, 6))
region_occupancy.plot(kind='bar', color='skyblue')
plt.title('Average Hotel Occupancy Rate by Region (2019-2026)')
plt.xlabel('Region')
plt.ylabel('Average Occupancy Rate (%)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('average_occupancy_rate_by_region.png')
plt.show()
