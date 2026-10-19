import matplotlib.pyplot as plt
import seaborn as sns


def generate_graph_5():
  from app import load_and_preprocess_data

  df = load_and_preprocess_data()
  plt.figure(figsize=(6, 4))
  corr_matrix = df[[
      "gdp_per_capita",
      "people_fully_vaccinated_per_hundred",
      "total_mortality_per_million",
  ]].corr()
  sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=1)
  plt.title("Correlation Heatmap")
  plt.savefig("plot5_correlation_heatmap.png")
  plt.close()
  print("✅ Graph 5 generated!")


if __name__ == "__main__":
  generate_graph_5()