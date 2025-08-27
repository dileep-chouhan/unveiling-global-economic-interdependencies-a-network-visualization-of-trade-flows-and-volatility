import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
num_countries = 20
countries = [f'Country {i}' for i in range(1, num_countries + 1)]
dates = pd.to_datetime(pd.date_range(start='2020-01-01', periods=12))
# Generate random trade volume data
trade_volume = np.random.randint(100, 1000, size=(len(countries), len(countries), len(dates)))
trade_volume = np.triu(trade_volume, k=1) + trade_volume.transpose() # make it symmetric
# Generate random volatility index
volatility = np.random.rand(len(countries), len(dates)) * 10  # values between 0 and 10
#Create DataFrame for trade volume
trade_df = pd.DataFrame(trade_volume.reshape(len(countries)*len(countries),len(dates)),
                        columns=dates)
trade_df['Country1'] = np.repeat(countries, len(countries))
trade_df['Country2'] = np.tile(countries, len(countries))
trade_df = trade_df.melt(id_vars=['Country1','Country2'], var_name='Date', value_name='TradeVolume')
trade_df['Date'] = pd.to_datetime(trade_df['Date'])
#Create DataFrame for volatility
volatility_df = pd.DataFrame(volatility, columns=dates, index=countries)
volatility_df = volatility_df.melt(var_name='Date', value_name='Volatility')
volatility_df['Date'] = pd.to_datetime(volatility_df['Date'])
volatility_df = volatility_df.reset_index().rename(columns={'index':'Country'})
# --- 2. Data Cleaning and Analysis ---
#Calculate average trade volume and volatility over the period
avg_trade = trade_df.groupby(['Country1', 'Country2'])['TradeVolume'].mean().reset_index()
avg_volatility = volatility_df.groupby('Country')['Volatility'].mean().reset_index()
# --- 3. Visualization ---
# Create a network graph
G = nx.Graph()
for index, row in avg_trade.iterrows():
    G.add_edge(row['Country1'], row['Country2'], weight=row['TradeVolume'])
# Node size based on average volatility
node_sizes = [avg_volatility[avg_volatility['Country'] == node]['Volatility'].values[0] * 100 for node in G.nodes()]
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G) # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color='skyblue', width=[d['weight']/100 for u,v,d in G.edges(data=True)], edge_color='gray')
plt.title('Global Trade Network Visualization', fontsize=16)
plt.savefig('global_trade_network.png')
print("Plot saved to global_trade_network.png")
plt.figure(figsize=(10,6))
plt.bar(avg_volatility['Country'], avg_volatility['Volatility'])
plt.xlabel('Country')
plt.ylabel('Average Volatility')
plt.title('Average Volatility per Country')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('average_volatility.png')
print("Plot saved to average_volatility.png")