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
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\commit_age_distribution.png')
plt.close()

# Visualization 2: Relationship between `OWN` (Ownership) and `AGE`
plt.figure(figsize=(10, 6))
sns.scatterplot(x='AGE', y='OWN', data=df, hue='Repository', palette='viridis')
plt.title('Relationship between Ownership (OWN) and Commit Age (AGE)')
plt.xlabel('Age (Days)')
plt.ylabel('Ownership (%)')
plt.legend(title='Repository', bbox_to_anchor=(1.05, 1), loc='upper left')
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\ownership_vs_age.png')
plt.close()

# Visualization 3: Average Ownership by Repository
plt.figure(figsize=(12, 6))
sns.barplot(x='Repository', y='OWN', data=df, estimator='mean', palette='Set2')
plt.title('Average Ownership (OWN) by Repository')
plt.xlabel('Repository')
plt.ylabel('Average Ownership (%)')
plt.xticks(rotation=45)
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\avg_ownership_by_repo.png')
plt.close()

# Visualization 4: Fix Commit vs Non-Fix Commit (FIX)
plt.figure(figsize=(10, 6))
sns.countplot(x='FIX', data=df, palette='Blues')
plt.title('Number of Fix vs Non-Fix Commits')
plt.xlabel('Fix Commit')
plt.ylabel('Count')
plt.xticks([0, 1], ['Non-Fix', 'Fix'])
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\fix_vs_nonfix_commits.png')
plt.close()

# Visualization 5: Distribution of `OEXP` (Ownership Experience)
plt.figure(figsize=(10, 6))
sns.histplot(df['OEXP'], bins=20, kde=True, color='green')
plt.title('Distribution of Ownership Experience (OEXP)')
plt.xlabel('Ownership Experience')
plt.ylabel('Frequency')
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\ownership_experience_distribution.png')
plt.close()

# Visualization 6: Relationship between `NADEV` (New Developers) and `NDDEV` (Total Developers)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='NADEV', y='NDDEV', data=df, hue='Repository', palette='coolwarm')
plt.title('Relationship between New Developers (NADEV) and Total Developers (NDDEV)')
plt.xlabel('New Developers')
plt.ylabel('Total Developers')
plt.legend(title='Repository', bbox_to_anchor=(1.05, 1), loc='upper left')
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\new_vs_total_developers.png')
plt.close()

# Visualization 7: Distribution of `NCOMM` (Number of Commits)
plt.figure(figsize=(10, 6))
sns.histplot(df['NCOMM'], bins=20, kde=True, color='red')
plt.title('Distribution of Number of Commits (NCOMM)')
plt.xlabel('Number of Commits')
plt.ylabel('Frequency')
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\ncomm_distribution.png')
plt.close()

# Visualization 8: Average `OEXP` by Repository
plt.figure(figsize=(12, 6))
sns.barplot(x='Repository', y='OEXP', data=df, estimator='mean', palette='Blues')
plt.title('Average Ownership Experience (OEXP) by Repository')
plt.xlabel('Repository')
plt.ylabel('Average Ownership Experience')
plt.xticks(rotation=45)
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\avg_ownership_experience_by_repo.png')
plt.close()

# Visualization 9: Average Number of Developers (NADEV and NDDEV) by Repository
df_melted = df.melt(id_vars=["Repository"], value_vars=["NADEV", "NDDEV"], var_name="Developer Type", value_name="Number of Developers")
plt.figure(figsize=(12, 6))
sns.barplot(x='Repository', y='Number of Developers', data=df_melted, hue='Developer Type', estimator='mean', palette='muted')
plt.title('Average Number of Developers by Repository')
plt.xlabel('Repository')
plt.ylabel('Average Number of Developers')
plt.xticks(rotation=45)
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\avg_developers_by_repo.png')
plt.close()

# Visualization 10: Average Number of Commits (NCOMM) by Repository
plt.figure(figsize=(12, 6))
sns.barplot(x='Repository', y='NCOMM', data=df, estimator='mean', palette='viridis')
plt.title('Average Number of Commits (NCOMM) by Repository')
plt.xlabel('Repository')
plt.ylabel('Average Number of Commits')
plt.xticks(rotation=45)
# Save the figure with updated path
plt.savefig(r'C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\MetricsVisualizations\avg_commits_by_repo.png')
plt.close()

print("All visualizations saved successfully!")
