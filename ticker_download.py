import pandas as pd
import json

# Specify the path to your CSV file
csv_file = "/Users/giacomomaggiore/Desktop/flat-ui__data-Sun Dec 15 2024.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)
list_tickers = df["Symbol"].tolist()
# Print the DataFrame
print(list_tickers)

# Specify the path to your JavaScript file
js_file = "ticker_list.js"

# Convert the list to a JSON string
json_data = json.dumps(list_tickers)

# Write the JSON string to the JavaScript file
with open(js_file, "w") as file:
    file.write(f"const list_tickers = {json_data};")