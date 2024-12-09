import numpy as np
import pandas as pd
import pickle

def ai_model( day:int, month:int, crop:str, district:str) -> str:
        # Load the scaler and model
        with open('scaler.pkl', 'rb') as f:
            loaded_scaler = pickle.load(f)

        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Convert 'day' and 'month' to cyclic features
        day_sin = np.sin(2 * np.pi * day / 31)
        day_cos = np.cos(2 * np.pi * day / 31)
        month_sin = np.sin(2 * np.pi * month / 12)
        month_cos = np.cos(2 * np.pi * month / 12)

        # Prepare the input data
        input_data = pd.DataFrame({
            'day_sin': [day_sin],
            'day_cos': [day_cos],
            'month_sin': [month_sin],
            'month_cos': [month_cos],
            'District Name_Chamrajnagar': [1 if district.lower() == 'ch' else 0],
            'District Name_Hassan': [1 if district.lower() == 'ha' else 0],
            'District Name_Mysore': [1 if district.lower() == 'my' else 0],
            'District Name_Tumkur': [1 if district.lower() == 'tu' else 0],
            'Commodity_Onion': [1 if crop.lower() == 'onion' else 0],
            'Commodity_Ragi (Finger Millet)': [1 if crop.lower() == 'ragi' else 0],
            'Commodity_Rice': [1 if crop.lower() == 'rice' else 0],
            'Commodity_Tomato': [1 if crop.lower() == 'tomato' else 0]
        })

        # Scale the input data
        ip = loaded_scaler.transform(input_data)

        # Make prediction
        predicted_price = model.predict(ip)

        return predicted_price
    
    

if __name__ == "__main__":
    # Example usage
   
    day = int(input("Enter the day (1-31): "))
    month = int(input("Enter the month (1-12): "))
    crop = input("Enter crop name (Ragi, Rice, Onion, Coconut, Tomato): ")
    district = input("Enter district (ba, ch, my, tu, ha): ")

    result = ai_model(day, month, crop, district)
    print(result)
