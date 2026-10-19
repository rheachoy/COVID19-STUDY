import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def generate_graph_1():
  from app import load_and_preprocess_data

  df = load_and_preprocess_data()
  plt.figure(figsize=(8, 4))
  sns.regplot(
      data=df,
      x="gdp_per_capita",
      y="people_fully_vaccinated_per_hundred",
      scatter_kws={"alpha": 0.6},
      line_kws={"color": "red"},
  )
  plt.title("GDP per Capita vs. Vaccination Rate")
  plt.savefig("plot1_gdp_vs_vax.png")
  plt.close()
  print("✅ Graph 1 generated!")


if __name__ == "__main__":
  generate_graph_1()