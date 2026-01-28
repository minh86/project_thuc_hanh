import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV data
df = pd.read_csv('vietnam_population_data.csv')

# Filter for data that has values (not empty)
# We'll use the estimates variant for historical data and medium variant for projections
df['age_0_14'] = df['Population - Sex: all - Age: 0-14 - Variant: estimates'].fillna(
    df['Population - Sex: all - Age: 0-14 - Variant: medium'])
df['age_15_64'] = df['Population - Sex: all - Age: 15-64 - Variant: estimates'].fillna(
    df['Population - Sex: all - Age: 15-64 - Variant: medium'])
df['age_65_plus'] = df['Population - Sex: all - Age: 65+ - Variant: estimates'].fillna(
    df['Population - Sex: all - Age: 65+ - Variant: medium'])

# Remove rows with missing data
df_clean = df.dropna(subset=['age_0_14', 'age_15_64', 'age_65_plus'])

# Split data into historical (1950-2023) and projection (2024-2100)
historical_data = df_clean[df_clean['Year'] <= 2023]
projection_data = df_clean[df_clean['Year'] >= 2024]

# Convert population to millions for better readability
years_hist = historical_data['Year']
years_proj = projection_data['Year']

pop_0_14_hist = historical_data['age_0_14'] / 1_000_000
pop_15_64_hist = historical_data['age_15_64'] / 1_000_000
pop_65_plus_hist = historical_data['age_65_plus'] / 1_000_000

pop_0_14_proj = projection_data['age_0_14'] / 1_000_000
pop_15_64_proj = projection_data['age_15_64'] / 1_000_000
pop_65_plus_proj = projection_data['age_65_plus'] / 1_000_000

# Create the line chart
plt.figure(figsize=(14, 8))

# Plot Working age (15-64 years) - Green line
plt.plot(years_hist, pop_15_64_hist, color='green', linewidth=2.5, label='Working age (15–64 years)')
plt.plot(years_proj, pop_15_64_proj, color='green', linewidth=2.5, linestyle='--')

# Plot Elderly (65+ years) - Red line  
plt.plot(years_hist, pop_65_plus_hist, color='red', linewidth=2.5, label='Elderly (65+ years)')
plt.plot(years_proj, pop_65_plus_proj, color='red', linewidth=2.5, linestyle='--')

# Plot Young (under-15s) - Orange line
plt.plot(years_hist, pop_0_14_hist, color='orange', linewidth=2.5, label='Young (under-15s)')
plt.plot(years_proj, pop_0_14_proj, color='orange', linewidth=2.5, linestyle='--')

# Add labels at the end of each line
# Working age label
plt.text(2095, pop_15_64_proj.iloc[-1], 'Working age (15–64 years)', 
         color='green', fontsize=10, va='center')

# Elderly label  
plt.text(2095, pop_65_plus_proj.iloc[-1], 'Elderly (65+ years)', 
         color='red', fontsize=10, va='center')

# Young label
plt.text(2095, pop_0_14_proj.iloc[-1], 'Young (under-15s)', 
         color='orange', fontsize=10, va='center')

# Customize the chart
plt.title('Co cau dan so Vietnam theo do tuoi (1950-2100)', fontsize=16, fontweight='bold')
plt.xlabel('Nam', fontsize=12)
plt.ylabel('Dan so (trieu nguoi)', fontsize=12)

# Set x-axis to show every 10 years
plt.xticks(np.arange(1950, 2101, 10), rotation=45)

# Set y-axis limits
plt.ylim(0, 80)

# Add grid with light horizontal lines
plt.grid(True, alpha=0.3, axis='y')
plt.grid(False, axis='x')

# Set white background
plt.gca().set_facecolor('white')
plt.gcf().set_facecolor('white')

# Add vertical line to separate historical from projection
plt.axvline(x=2023, color='gray', linestyle=':', alpha=0.5)

# Add annotation for historical vs projection
plt.text(1980, 75, 'Historical', fontsize=10, alpha=0.7)
plt.text(2050, 75, 'Projection', fontsize=10, alpha=0.7)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart
plt.savefig('vietnam_population_line_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("Bieu do duong da duoc tao va luu thanh cong!")
print(f"Tong so nam du lieu: {len(df_clean)}")
print(f"Khoang thoi gian: {df_clean['Year'].min()} - {df_clean['Year'].max()}")
print(f"Du lieu lich su (1950-2023): {len(historical_data)} nam")
print(f"Du lieu du bao (2024-2100): {len(projection_data)} nam")
