name: Update GitHub Projects

permissions:
  contents: write   # Gives permission to push changes

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
  workflow_dispatch:      # Allows manual run

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests

      - name: Update README with latest projects
        env:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}  # Your PAT for private repos
        run: python update_projects.py

      - name: Commit & push changes
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add README.md
          git commit -m "Update projects automatically" || echo "No changes"
          git push https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }} HEAD:main

