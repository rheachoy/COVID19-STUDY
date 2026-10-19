import matplotlib.pyplot as plt
import seaborn as sns


def generate_graph_2():
  from app import load_and_preprocess_data

  df = load_and_preprocess_data()
  plt.figure(figsize=(8, 4))
  sns.scatterplot(
      data=df,
      x="gdp_per_capita",
      y="total_mortality_per_million",
      hue="wealth_quartile",
      palette="viridis",
      s=70,
  )
  plt.title("GDP per Capita vs. Total COVID-19 Mortality per Million")
  plt.savefig("plot2_gdp_vs_mortality.png")
  plt.close()
  print("✅ Graph 2 generated!")


if __name__ == "__main__":
  generate_graph_2()