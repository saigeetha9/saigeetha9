import requests
import os

USERNAME = "saigeetha9"
TOKEN = os.getenv("GH_TOKEN")  # Stored securely in GitHub Secrets

headers = {"Authorization": f"token {TOKEN}"}
url = "https://api.github.com/user/repos?sort=updated&per_page=100"
repos = requests.get(url, headers=headers).json()

projects_md = "### íº€ Featured Projects\n\n"
for repo in repos:
    if repo['description']:
        projects_md += f"#### [{repo['name']}]({repo['html_url']})\n> {repo['description']}\n\n"

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

start_tag = "<!-- AUTO-GENERATED:START (projects) -->"
end_tag = "<!-- AUTO-GENERATED:END -->"

start = readme.find(start_tag) + len(start_tag)
end = readme.find(end_tag)

new_readme = readme[:start] + "\n" + projects_md + readme[end:]

with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_readme)

