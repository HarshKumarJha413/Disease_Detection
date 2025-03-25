import pickle
import pandas as pd
import numpy as np

# Load the pickle file
print("Loading pickle file...")
with open('disease_prediction_system.pkl', 'rb') as f:
    data = pickle.load(f)

# Load the training data
print("Loading Training.csv...")
df = pd.read_csv('Training.csv')
print(f"Original columns: {len(df.columns)}")

# Remove unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(f"After removing unnamed columns: {len(df.columns)}")

# Check the features that the model was trained on
if "final_rf_model" in data:
    rf_model = data["final_rf_model"]
    print(f"RF model expects {rf_model.n_features_in_} features")
    
    # If the model has feature names (sklearn >= 1.0)
    if hasattr(rf_model, 'feature_names_in_'):
        print("Model has feature names:")
        print(rf_model.feature_names_in_)
        
        # Compare with our dataframe
        symptoms = list(df.columns)
        symptoms.remove('prognosis')  # Remove the target variable
        print(f"DataFrame has {len(symptoms)} features")
        
        # Check for missing or extra features
        model_features = set(rf_model.feature_names_in_)
        df_features = set(symptoms)
        
        missing_in_df = model_features - df_features
        extra_in_df = df_features - model_features
        
        if missing_in_df:
            print(f"Features missing in DataFrame: {missing_in_df}")
        
        if extra_in_df:
            print(f"Extra features in DataFrame: {extra_in_df}")
        
        # Save a fixed model that works with the current data
        X = df.drop('prognosis', axis=1)
        y = df['prognosis']
        
        print("Retraining models with current data...")
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.naive_bayes import GaussianNB
        
        # Train new models on current data
        new_rf_model = RandomForestClassifier(random_state=42)
        new_rf_model.fit(X, y)
        
        new_nb_model = GaussianNB()
        new_nb_model.fit(X, y)
        
        # Create a new dictionary with the updated models
        new_data = {
            "final_rf_model": new_rf_model,
            "final_nb_model": new_nb_model
        }
        
        # Save the new model
        print("Saving new model...")
        with open('new_disease_prediction_system.pkl', 'wb') as f:
            pickle.dump(new_data, f)
        
        print("New model saved to new_disease_prediction_system.pkl")
        
else:
    print("RF model not found in pickle file") 