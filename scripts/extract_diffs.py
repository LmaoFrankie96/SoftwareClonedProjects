from pydriller import Repository
import os
import json

def extract_diff_data(repo_path):
    data = []
    for commit in Repository(repo_path).traverse_commits():
        for modified_file in commit.modified_files:
            data.append({
                "commit_hash": commit.hash,
                "previous_commit_hash": commit.parents[0] if commit.parents else None,
                "diff_stats": {
                    "additions": modified_file.added_lines,
                    "deletions": modified_file.deleted_lines
                },
                "diff_content": modified_file.diff
            })
    return data

# Path to the directory containing repositories
repos_dir = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\cloned_repos"
# Path to the directory where output JSON files will be saved
output_dir = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each repository
for repo in os.listdir(repos_dir):
    repo_path = os.path.join(repos_dir, repo)
    # Skip if it's not a directory
    if not os.path.isdir(repo_path):
        continue
    
    # Extract diff data for the repository
    diff_data = extract_diff_data(repo_path)
    
    # Define the output file path (JSON file named after the repository)
    output_path = os.path.join(output_dir, f"{repo}.json")
    
    # Write the diff data to the JSON file
    with open(output_path, "w") as f:
        json.dump(diff_data, f, indent=4)
    
    print(f"Diff data for '{repo}' saved to {output_path}")
    
