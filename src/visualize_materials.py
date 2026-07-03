# Import pandas for data analysis
# WHY: Used to read and manipulate the CSV dataset
import pandas as pd

# Import matplotlib for plotting
# WHY: Used to create and save figures
import matplotlib.pyplot as plt

# Import seaborn for heatmaps
# WHY: Seaborn provides a professional heatmap function
import seaborn as sns

# Read dataset from CSV file
# WHY: Load our materials data into memory
data = pd.read_csv("data/materials_data.csv")

# Calculate correlation matrix
# WHY: Measure relationships between all numerical variables
correlation = data.corr(numeric_only=True)

# Save correlation matrix
# WHY: Keep a permanent record of the analysis
correlation.to_csv(
    "results/correlation_matrix.csv"
)

# Create figure window
# WHY: Prepare a canvas for the heatmap
plt.figure(figsize=(8,6))

# Create heatmap
# WHY: Visualize all correlations at once
sns.heatmap(
    correlation,
    annot=True,      # Show correlation values
    cmap="coolwarm"  # Color scale
)

# Add title
# WHY: Explain what the figure represents
plt.title("Correlation Heatmap")

# Save figure
# WHY: Store the figure in the repository
plt.savefig(
    "figures/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

# Display figure
# WHY: Let us inspect the heatmap immediately
plt.show()

# Confirmation message
print("Correlation heatmap saved successfully.")

# Select correlations with the target variable
# WHY: We only care about variables related to Overpotential
target_correlation = correlation["Overpotential_mV"]

# Remove the target's correlation with itself
# WHY: Overpotential is always perfectly correlated with itself (=1)
target_correlation = target_correlation.drop(
    "Overpotential_mV"
)

# Convert all values to absolute values
# WHY: We want strength, not direction
feature_ranking = target_correlation.abs()

# Sort from strongest to weakest
# WHY: Makes interpretation easier
feature_ranking = feature_ranking.sort_values(
    ascending=False
)

# Print ranking
# WHY: Display results immediately
print()
print("FEATURE RANKING")
print(feature_ranking)

# Save ranking to CSV
# WHY: Keep permanent results
feature_ranking.to_csv(
    "results/feature_ranking.csv"
)

print()
print("Feature ranking saved successfully.")

# Create a new figure for feature ranking
# WHY: We need a separate graph for feature importance
plt.figure(figsize=(8, 6))

# Create a bar chart of ranked features
# WHY: Bar charts are best for comparing feature strengths
feature_ranking.plot(kind="bar")

# Label the x-axis
# WHY: Readers need to know these are catalyst/material features
plt.xlabel("Feature")

# Label the y-axis
# WHY: This shows the strength of correlation with overpotential
plt.ylabel("Absolute Correlation with Overpotential")

# Add a title
# WHY: The title explains the scientific purpose of the graph
plt.title("Feature Ranking Based on Correlation Strength")

# Rotate x-axis labels
# WHY: Prevents long feature names from overlapping
plt.xticks(rotation=45, ha="right")

# Add grid
# WHY: Makes the bar values easier to read
plt.grid(True)

# Save the graph
# WHY: Stores the feature ranking figure in the repository
plt.savefig(
    "figures/feature_ranking.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph
# WHY: Allows us to inspect the figure immediately
plt.show()

# Print confirmation message
# WHY: Confirms that the feature ranking graph was created
print("Feature ranking graph saved successfully.")