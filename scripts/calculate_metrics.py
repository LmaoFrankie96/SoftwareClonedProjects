import os
import json
import git
from datetime import datetime, timedelta
import re

# Input paths
refactoring_commits_file = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\RefactoringCommits\refactoring_commits.json"
repos_folder = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\cloned_repos"
output_file = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\metrics.json"

def calculate_metrics(repo_path, commits):
    metrics = []
    repo = git.Repo(repo_path)

    for commit_hash in commits:
        try:
            commit = repo.commit(commit_hash)

            # **AGE** Metric
            file_mod_dates = []
            for file in commit.stats.files.keys():
                # Find the last commit modifying this file before the current commit
                blame = repo.git.log('--format=%ct', '-n', '1', '--', file, commit_hash + '^')
                if blame:
                    last_mod_time = datetime.fromtimestamp(int(blame))
                    file_mod_dates.append((commit.committed_datetime - last_mod_time).days)

            age = sum(file_mod_dates) / len(file_mod_dates) if file_mod_dates else 0

            # **FIX** Metric
            fix = bool(re.search(r'\b[A-Za-z]+-\d+\b', commit.message))

            # **OWN** Metric
            owner_modifications = []
            total_modifications = []
            for file in commit.stats.files.keys():
                blame_data = repo.git.blame('-e', commit_hash, '--', file).splitlines()
                authors = [line.split('(')[1].split(' ')[0] for line in blame_data if '(' in line]
                owner = max(set(authors), key=authors.count)
                owner_mods = authors.count(owner)
                owner_modifications.append(owner_mods)
                total_modifications.append(len(authors))

            own = (sum(owner_modifications) / sum(total_modifications) * 100) if total_modifications else 0

            # **OEXP** Metric
            total_changes = len(list(repo.iter_commits()))
            owner_changes = len(list(repo.iter_commits(author=commit.author.email)))
            oexp = (owner_changes / total_changes * 100) if total_changes else 0

            # **NADEV** and **NDDEV** Metrics
            time_window = commit.committed_datetime - timedelta(days=180)
            nadev = len(set(c.author.email for c in repo.iter_commits(since=time_window)))
            nddev = len(set(c.author.email for c in repo.iter_commits()))

            # **NCOMM** Metric
            modified_files = commit.stats.files.keys()
            previous_commits = list(repo.iter_commits(paths=modified_files, max_count=10))
            ncomm = len(previous_commits)

            # Collect metrics
            metrics.append({
                "commit_hash": commit_hash,
                "AGE": age,
                "FIX": fix,
                "OWN": own,
                "OEXP": oexp,
                "NADEV": nadev,
                "NDDEV": nddev,
                "NCOMM": ncomm,
            })

        except Exception as e:
            print(f"Error processing commit {commit_hash} in {repo_path}: {e}")

    return metrics

if __name__ == "__main__":
    with open(refactoring_commits_file, 'r') as f:
        refactoring_commits = json.load(f)

    all_metrics = {}

    for repo_name, commits in refactoring_commits.items():
        repo_path = os.path.join(repos_folder, repo_name)
        if os.path.exists(repo_path):
            print(f"Processing repository: {repo_name}")
            metrics = calculate_metrics(repo_path, commits)
            all_metrics[repo_name] = metrics
        else:
            print(f"Repository not found: {repo_name}")

    # Save metrics to output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(all_metrics, f, indent=4)
    print(f"Metrics saved to {output_file}")
