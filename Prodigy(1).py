import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

file_path = "/Users/raghavender/Datasets:Research/Population.csv"

# Load the dataset while skipping metadata and empty rows
data = pd.read_csv(file_path, skiprows=5)

# Drop the 'Not classified' row
data = data[data['Country Name'] != 'Not classified']
data.columns=data.columns.str.strip()

# Drop specific columns, if needed (for example, 'Country Code' and 'Indicator Code')
columns_to_drop = ['Country Code', 'Indicator Name', 'Indicator Code']
data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])
data = data.set_index('Country Name')
data.index = data.index.str.strip()


# Choose a country to plot
if 'India' in data.index:
    # Transpose the dataset for easier plotting
    data = data.transpose()

    # Plot the data for 'India'
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data['India'], marker='o')

    # Customize the plot
    plt.title('Population Growth of India (1960-2022)')
    plt.xlabel('Year',fontsize=10)
    plt.ylabel('Population in Billions')
    plt.grid(True)
    plt.xticks(rotation=90,fontsize=5)

    # Show the plot
    plt.show()
else:
    print("Error: 'India' not found in the dataset.")