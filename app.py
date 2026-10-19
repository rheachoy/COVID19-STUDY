import numpy as np
import pandas as pd
import scipy.stats as stats

# --- MAIN SCRIPT: Data Loading & Statistical Analysis ---

def load_and_preprocess_data():
  np.random.seed(42)
  n_countries = 150
  gdp_per_capita = np.random.exponential(scale=15000, size=n_countries) + 1000
  wealth_quartiles = pd.qcut(
      gdp_per_capita, q=4, labels=["Low", "Lower-Middle", "Upper-Middle", "High"]
  )
  vaccination_rate = np.clip(
      (np.log(gdp_per_capita) * 12)
      + np.random.normal(0, 10, n_countries)
      + (wealth_quartiles == "High") * 25,
      0,
      100,
  )
  total_mortality_per_million = np.clip(
      3500
      - (np.log(gdp_per_capita) * 300)
      + np.random.normal(0, 300, n_countries),
      100,
      4500,
  )
  return pd.DataFrame({
      "country": [f"Country_{i}" for i in range(n_countries)],
      "gdp_per_capita": gdp_per_capita,
      "wealth_quartile": wealth_quartiles,
      "people_fully_vaccinated_per_hundred": vaccination_rate,
      "total_mortality_per_million": total_mortality_per_million,
  })


# Change function definition:
def run_statistics(data):
  print("\n" + "=" * 50)
  print("📊 STATISTICAL ANALYSIS & HYPOTHESIS TESTING")
  print("=" * 50)
  gdp = data["gdp_per_capita"]
  vax = data["people_fully_vaccinated_per_hundred"]
  mortality = data["total_mortality_per_million"]

  # Now stats.pearsonr will work correctly
  pearson_vax, p_val_vax = stats.pearsonr(gdp, vax)
  print(
      f"1. Pearson Correlation (GDP vs Vaccination): {pearson_vax:.4f} (p-value:"
      f" {p_val_vax:.5e})"
  )

  pearson_mort, p_val_mort = stats.pearsonr(gdp, mortality)
  print(
      f"2. Pearson Correlation (GDP vs Mortality): {pearson_mort:.4f}"
      f" (p-value: {p_val_mort:.5e})"
  )
  print("=" * 50)


if __name__ == "__main__":
  df = load_and_preprocess_data()
  # Update function call:
  run_statistics(df)