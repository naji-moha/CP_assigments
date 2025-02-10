import numpy as np
import matplotlib.pyplot as plt

# student scores
scores = [76, 10, 21, 61, 40, 65, 40, 95, 77, 92, 59, 81, 76, 98, 57, 51, 92, 35, 17, 61, 35]

bins = [0, 20, 40, 60, 80, 100]

# Plot the histogram
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=bins, edgecolor='black', alpha=0.7)
plt.xlabel("Score Ranges")
plt.ylabel("Frequency")
plt.title("Histogram of Student Scores")
plt.xticks(bins)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
