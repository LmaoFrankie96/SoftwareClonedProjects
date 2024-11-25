import json
import os

# Define input and output paths
input_folder = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\refactoring results"
output_file = r"C:\Users\PMLS\Documents\SoftwareClonedProjects\outputs\RefactoringCommits\refactoring_commits.json"

def extract_commits(input_folder):
    commits = {}  # Dictionary to store extracted commits
    for file in os.listdir(input_folder):
        if file.endswith(".json"):  # Process only JSON files
            file_path = os.path.join(input_folder, file)
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)  # Load the JSON data
                    if "commits" in data and isinstance(data["commits"], list):
                        # Extract the SHA1 of commits with detected refactorings
                        repo_name = file.replace('.json', '')  # Use filename as repo name
                        commits[repo_name] = [
                            commit["sha1"]
                            for commit in data["commits"]
                            if commit.get("refactorings")  # Include only commits with refactorings
                        ]
                    else:
                        print(f"Unexpected structure in {file_path}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {file_path}: {e}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    return commits

if __name__ == "__main__":
    refactoring_commits = extract_commits(input_folder)
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Save the extracted commits to the output JSON file
    with open(output_file, "w") as f:
        json.dump(refactoring_commits, f, indent=4)
    print(f"Extracted commits saved to {output_file}")
