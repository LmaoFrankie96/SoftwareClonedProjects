import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load the JSON data (replace this with your actual file path)
with open(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\metrics.json', 'r') as file:
    data = json.load(file)

# Flatten the JSON structure and load into a Pandas DataFrame
rows = []
for repo, commits in data.items():
    for commit in commits:
        row = {
            "Repository": repo,
            "Commit Hash": commit["commit_hash"],
            "AGE": commit["AGE"],
            "FIX": commit["FIX"],
            "OWN": commit["OWN"],
            "OEXP": commit["OEXP"],
            "NADEV": commit["NADEV"],
            "NDDEV": commit["NDDEV"],
            "NCOMM": commit["NCOMM"]
        }
        rows.append(row)

df = pd.DataFrame(rows)

# Show first few rows
print(df.head())

# Visualization 1: Distribution of `AGE`
plt.figure(figsize=(10, 6))
sns.histplot(df['AGE'], bins=20, kde=True, color='blue')
plt.title('Distribution of Commit Age (AGE)')
plt.xlabel('Age (Days)')
plt.ylabel('Frequency')
# Save the figure
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\commit_age_distribution.png')
plt.close()  # Close the plot to avoid overlapping with the next one

# Visualization 2: Relationship between `OWN` (Ownership) and `AGE`
plt.figure(figsize=(10, 6))
sns.scatterplot(x='AGE', y='OWN', data=df, hue='Repository', palette='viridis')
plt.title('Relationship between Ownership (OWN) and Commit Age (AGE)')
plt.xlabel('Age (Days)')
plt.ylabel('Ownership (%)')
plt.legend(title='Repository', bbox_to_anchor=(1.05, 1), loc='upper left')
# Save the figure
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\ownership_vs_age.png')
plt.close()

# Visualization 3: Average Ownership by Repository
plt.figure(figsize=(12, 6))
sns.barplot(x='Repository', y='OWN', data=df, estimator='mean', palette='Set2')
plt.title('Average Ownership (OWN) by Repository')
plt.xlabel('Repository')
plt.ylabel('Average Ownership (%)')
plt.xticks(rotation=45)
# Save the figure
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\avg_ownership_by_repo.png')
plt.close()

# Visualization 4: Fix Commit vs Non-Fix Commit (FIX)
plt.figure(figsize=(10, 6))
sns.countplot(x='FIX', data=df, palette='Blues')
plt.title('Number of Fix vs Non-Fix Commits')
plt.xlabel('Fix Commit')
plt.ylabel('Count')
plt.xticks([0, 1], ['Non-Fix', 'Fix'])
# Save the figure
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\fix_vs_nonfix_commits.png')
plt.close()

print("Visualizations saved successfully!")
