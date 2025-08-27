# Unveiling Global Economic Interdependencies: A Network Visualization of Trade Flows and Volatility

## Overview

This project visualizes the intricate relationships within the global economic network by analyzing the correlation between international trade volumes and economic volatility.  The analysis aims to identify key economic relationships and potential vulnerabilities within this network.  By combining trade data with volatility indices for various countries, we generate interactive visualizations that highlight significant dependencies and patterns in global economic activity.

## Technologies Used

This project leverages the following Python libraries:

* **Pandas:** For data manipulation and analysis.
* **Matplotlib:** For creating static, interactive plots.
* **Seaborn:** For enhanced statistical data visualization.
* **NetworkX:** (Optional, add if used) For network graph creation and analysis.


## How to Run

1. **Install Dependencies:** Ensure you have Python 3 installed.  Navigate to the project directory in your terminal and install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script:** Execute the main script using:

   ```bash
   python main.py
   ```

## Example Output

The script will first print a summary of the analysis to the console, including key correlations and identified relationships between trade volumes and economic volatility.  Additionally, the script generates several visualization files:

* **`trade_network.png` (or similar):** A network graph visualizing the global trade network, with node size potentially representing trade volume and edge thickness representing correlation strength.  (Adjust filename according to your actual output)
* **`volatility_correlation.png` (or similar):** A visualization showing the correlation between trade volume and volatility indices across countries. (Adjust filename according to your actual output)

These visualizations provide an interactive way to explore the complex interplay of global trade and economic stability.  The specific output files and their contents may vary depending on the data used and the analysis performed.  Refer to the comments within the `main.py` script for detailed explanations.