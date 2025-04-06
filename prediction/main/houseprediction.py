
import os
import pandas as pd

from glob import glob
from category_encoders import OneHotEncoder
from sklearn.linear_model import Ridge
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def wrangle(filepath):
    # read file path
    df = pd.read_csv(filepath)
    
    # Filter to only apartments property type in buenos aires and drop the column
    df = df[df["property_type"] == "apartment"]
    df.drop(columns=["property_type"], inplace = True)
    
    # Filter to only Capital Federal district and drop place_with_parent_names column
    df = df[df["place_with_parent_names"].str.contains("Capital Federal")]
    
    # Filter to a price not more than $400000 
    df = df[df["price_aprox_usd"] <= 500000]
    
    # Split lat and lon from lat-lon and drop the lat-lon column
    df[["lat", "lon"]] = df["lat-lon"].str.split(",", expand=True).astype(float)
    df.drop(columns="lat-lon", inplace = True)
    
    # Drop features where more than half null values
    df.drop(columns=["expenses", "rooms", "floor"], inplace=True)
    
    # Split neighbourhood from place_with_parent_names and drop the column
    df["neighbourhood"] = df["place_with_parent_names"].str.split("|", expand=True)[3]
    df.drop(columns=["place_with_parent_names"], inplace=True)
    
    #Drop columns with high and low cardinality
    df.drop(columns=["operation", "currency", "properati_url"], inplace = True)
    
    # Drop columns with multicollinearlity
    df.drop(columns=[
        "surface_total_in_m2", 
        'price', 
        'price_aprox_local_currency', 
        'price_usd_per_m2', 
        'price_per_m2'], inplace=True)
    
    # Remove outliers from surface_covered_in_m2
    low, high = df["surface_covered_in_m2"].quantile([0.1, 0.9])
    df = df[df["surface_covered_in_m2"].between(low, high)]
    return df


static_dir = os.path.join(BASE_DIR, 'static')
files = glob(os.path.join(static_dir, 'buenos-aires-real-estate-*.csv'))

frames = []
for file in files:
    frames.append(wrangle(file))

df = pd.concat(frames)


y_train = df["price_aprox_usd"]
X_train = df.drop(columns=["price_aprox_usd"])


model = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    SimpleImputer(),
    Ridge()
)
model.fit(X_train, y_train)

def test_model(surface_covered_in_m2, lat, lon, neighbourhood):
    
    prediction = {
        "surface_covered_in_m2": surface_covered_in_m2,
        "lat": lat,
        "lon": lon,
        "neighbourhood": neighbourhood
    }
    df_prediction = pd.DataFrame(prediction, index=[0])
    predicted = model.predict(df_prediction)[0]
    return round(predicted, 2)