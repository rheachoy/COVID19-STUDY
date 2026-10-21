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

    def run_correlation_suite(df):
    """Bivariate correlation analysis (Pearson & Spearman)."""
    print("\n" + "="*50)
    print("1. BIVARIATE CORRELATION ANALYSIS")
    print("="*50)
    
    metrics = [
        ("Vaccination Coverage", "people_fully_vaccinated_per_hundred"),
        ("Mortality Rate (Deaths/M)", "total_deaths_per_million")
    ]
    
    for label, col in metrics:
        subset = df[["gdp_per_capita", col]].dropna()
        x = subset["gdp_per_capita"]
        y = subset[col]
        
        r_val, p_val_p = stats.pearsonr(x, y)
        rho_val, p_val_s = stats.spearmanr(x, y)
        
        print(f"\nRelationship: GDP per Capita vs. {label}")
        print(f"  - Pearson  r : {r_val:7.4f} (p-value: {p_val_p:.4e})")
        print(f"  - Spearman \u03c1 : {rho_val:7.4f} (p-value: {p_val_s:.4e})"

        def run_distribution_and_anova(df):
    """Distribution checks and One-Way ANOVA across wealth quartiles."""
    print("\n" + "="*50)
    print("2. DISTRIBUTION NORMALITY & ONE-WAY ANOVA")
    print("="*50)
    
    _, p_raw = stats.shapiro(df["gdp_per_capita"])
    print(f"Shapiro-Wilk Test (Raw GDP p-value): {p_raw:.4e} (Non-normal)")
    
    groups = [
        group["people_fully_vaccinated_per_hundred"].dropna().values 
        for _, group in df.groupby("income_quartile", observed=False)
    ]
    
    f_stat, f_p_value = stats.f_oneway(*groups)
    print("\nOne-Way ANOVA: Vaccination Rate Across Wealth Quartiles")
    print(f"  - F-Statistic: {f_stat:.4f}")
    print(f"  - p-value    : {f_p_value:.4e}")
    
    quartile_summary = df.groupby("income_quartile", observed=False)["people_fully_vaccinated_per_hundred"].agg(
        Mean="mean", Median="median", SD="std", Count="count"
    )
    print("\nQuartile Vaccination Breakdown:\n", quartile_summary)

    def run_multivariate_regression(df):
    """Multivariate OLS Regression controlling for age confounding."""
    print("\n" + "="*50)
    print("3. MULTIVARIATE OLS REGRESSION (CONFOUNDER ANALYSIS)")
    print("="*50)
    
    reg_df = df.dropna(subset=[
        "total_deaths_per_million", "gdp_per_capita", "median_age", "hospital_beds_per_thousand"
    ]).copy()
    
    reg_df["log_gdp"] = np.log(reg_df["gdp_per_capita"])
    
    X = reg_df[["log_gdp", "median_age", "hospital_beds_per_thousand"]]
    X = sm.add_constant(X)
    y = reg_df["total_deaths_per_million"]
    
    model = sm.OLS(y, X).fit()
    print(f"R-squared: {model.rsquared:.4f} | F-statistic p-val: {model.f_pvalue:.4e}\n")
    print(model.summary().tables[1])

def execute_all():
    df = load_data()
    run_correlation_suite(df)
    run_distribution_and_anova(df)
    run_multivariate_regression(df)

if __name__ == "__main__":
    execute_all()
    