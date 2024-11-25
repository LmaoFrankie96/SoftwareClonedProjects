from pydriller import Repository
import os
import json

def extract_commit_data(repo_path):
    data = []
    for commit in Repository(repo_path).traverse_commits():
        data.append({
            "commit_hash": commit.hash,
            "commit_message": commit.msg
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
    
    # Extract commit data
    commit_data = extract_commit_data(repo_path)
    
    # Define the output file path (JSON file named after the repository)
    output_path = os.path.join(output_dir, f"{repo}.json")
    
    # Write the commit data to the JSON file
    with open(output_path, "w") as f:
        json.dump(commit_data, f, indent=4)
    
    print(f"Commit messages for '{repo}' saved to {output_path}")
    break
