import os

# Git commands to commit and push
os.system("git add .")
os.system('git commit -m "Updated GitHub Profile Website"')
os.system("git push origin main")

print("Website deployed successfully!")
