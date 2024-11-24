import os
from git import Repo

# Define repositories to clone
repositories = [
    "https://github.com/jfinal/jfinal.git",
    "https://github.com/novoda/android-demos.git",
    "https://github.com/bennidi/mbassador.git",
    "https://github.com/hierynomus/sshj.git",
    "https://github.com/zeromq/jeromq.git",
    "https://github.com/square/javapoet.git",
    "https://github.com/orfjackal/retrolambda.git",
    "https://github.com/scobal/seyren.git",
    "https://github.com/Netflix/zuul.git",
    "https://github.com/mrniko/redisson.git"
    # Replace with your 10 repositories
]

output_dir = "C:/Users/PMLS/Documents/SoftwareClonedProjects/cloned_repos"  # Path to save cloned repositories

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for repo_url in repositories:
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(output_dir, repo_name)
    if not os.path.exists(repo_path):
        print(f"Cloning {repo_name}...")
        Repo.clone_from(repo_url, repo_path)
    else:
        print(f"{repo_name} already exists.")
