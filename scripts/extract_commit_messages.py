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

repos_dir = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\cloned_repos"
output_path = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\commit_messages.json"
commit_data = {}
for repo in os.listdir(repos_dir):
    repo_path = os.path.join(repos_dir, repo)
    commit_data[repo] = extract_commit_data(repo_path)
    break

with open(output_path, "w") as f:
    json.dump(commit_data, f, indent=4)
