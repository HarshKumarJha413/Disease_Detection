import pickle
import sys

# Load the pickle file
try:
    with open('disease_prediction_system.pkl', 'rb') as f:
        data = pickle.load(f)
    
    # Print the structure
    print("Type of data:", type(data))
    
    # If it's a dictionary, print the keys
    if isinstance(data, dict):
        print("\nKeys in the dictionary:")
        for key in data.keys():
            print(f"- {key} (type: {type(data[key])})")
    
    # If it's a tuple or list, print the structure
    elif isinstance(data, (list, tuple)):
        print(f"\nLength of the {type(data).__name__}: {len(data)}")
        for i, item in enumerate(data[:3]):  # Print info about first 3 items
            print(f"Item {i} type: {type(item)}")
    
    # Try to extract training data columns as symptoms
    try:
        import pandas as pd
        # Check if this is the training data file
        test_data = pd.read_csv('Training.csv')
        print("\nColumns from Training.csv (potential symptoms):")
        symptom_columns = [col for col in test_data.columns if col != 'prognosis']
        print(symptom_columns[:20])  # Print first 20 symptom columns
    except Exception as e:
        print("Could not read Training.csv:", e)
    
except Exception as e:
    print(f"Error loading or processing the pickle file: {e}")
    sys.exit(1) 