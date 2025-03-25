import pandas as pd

# Load the data
df = pd.read_csv('Training.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Check the prognosis data
print("Prognosis column data type:", df['prognosis'].dtype)
print("First 5 prognosis values:", df['prognosis'].head().tolist())

# Print unique disease values
unique_diseases = df['prognosis'].unique()
print("\nNumber of unique diseases:", len(unique_diseases))
print("First 5 unique disease values:", unique_diseases[:5].tolist()) 