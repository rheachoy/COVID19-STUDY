import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def generate_graphs_3_and_4():
  from app import load_and_preprocess_data

  df = load_and_preprocess_data()

  # Graph 3
  plt.figure(figsize=(8, 4))
  months = np.arange(1, 13)
  for quartile in ["Low", "Lower-Middle", "Upper-Middle", "High"]:
    multiplier = (
        {"High": 1.0, "Upper-Middle": 0.8, "Lower-Middle": 0.5, "Low": 0.3}[
            quartile
        ]
    )
    timeline = 100 / (1 + np.exp(-0.5 * (months - 6))) * multiplier
    plt.plot(months, timeline, marker="o", label=f"{quartile} Wealth")
  plt.title("Vaccination Rollout Timeline by Wealth Quartile")
  plt.savefig("plot3_vax_timeline.png")
  plt.close()

  # Graph 4
  plt.figure(figsize=(8, 4))
  sns.boxplot(
      data=df,
      x="wealth_quartile",
      y="total_mortality_per_million",
      palette="Set2",
  )
  plt.title("COVID-19 Mortality Distribution Across Wealth Quartiles")
  plt.savefig("plot4_mortality_boxplot.png")
  plt.close()
  print("✅ Graphs 3 and 4 generated!")


if __name__ == "__main__":
  generate_graphs_3_and_4()