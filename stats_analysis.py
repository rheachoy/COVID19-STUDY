import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm

DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

def load_data():
    """Load OWID COVID-19 dataset and extract latest cross-sectional snapshot."""
    cols = [
        "iso_code", "continent", "location", "date", "total_deaths_per_million",
        "gdp_per_capita", "people_fully_vaccinated_per_hundred",
        "median_age", "hospital_beds_per_thousand", "population"
    ]
    df = pd.read_csv(DATA_URL, usecols=cols)
    df["date"] = pd.to_datetime(df["date"])
    
    country_df = df[~df["iso_code"].str.startswith("OWID")].copy()
    
    latest = (
        country_df.sort_values("date")
        .groupby("location")
        .last()
        .reset_index()
    )
    
    stats_df = latest.dropna(subset=[
        "gdp_per_capita", "people_fully_vaccinated_per_hundred", "total_deaths_per_million"
    ]).copy()
    
    stats_df["income_quartile"] = pd.qcut(
        stats_df["gdp_per_capita"], q=4, labels=["Low", "Lower-Middle", "Upper-Middle", "High"]
    )
    
    print(f"Data ingested: {len(stats_df)} countries available for hypothesis evaluation.")
    return stats_df

if __name__ == "__main__":
    df = load_data()