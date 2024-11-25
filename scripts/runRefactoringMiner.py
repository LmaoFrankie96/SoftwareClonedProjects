import os
import subprocess

def run_refactoring_miner(repo_path, output_path):
    miner_path = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\RefactoringMiner\build\libs\RM-fat.jar"  # Update with your actual path
    command = [
        "java",
        "-jar",
        miner_path,
        "-a",  # Analyze all commits in the repo
        repo_path,  # Path to the repo
        "-json",  # Output in JSON format
        output_path  # Output file path for the JSON results
    ]
    subprocess.run(command, check=True)

repos_dir = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\cloned_repos"
output_dir = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\refactoring results"

for repo in os.listdir(repos_dir):
    repo_path = os.path.join(repos_dir, repo)
    output_path = os.path.join(output_dir, f"{repo}.json")
    os.makedirs(output_dir, exist_ok=True)
    run_refactoring_miner(repo_path, output_path)
    
