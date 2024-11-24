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

repos_dir = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\cloned_repos"
output_path = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\commit_diffs.json"

diff_data = {}
for repo in os.listdir(repos_dir):
    repo_path = os.path.join(repos_dir, repo)
    diff_data[repo] = extract_diff_data(repo_path)
    break

with open(output_path, "w") as f:
    json.dump(diff_data, f, indent=4)
