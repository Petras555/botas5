import subprocess
import sys

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.check_call(cmd, shell=True)

# Step 1: Upgrade pip (optional but recommended)
run(f"{sys.executable} -m pip install --upgrade pip")

# Step 2: Install Playwright
run(f"{sys.executable} -m pip install playwright")

# Step 3: Install Playwright browsers
run(f"{sys.executable} -m playwright install")


# git status
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git push --set-upstream origin main