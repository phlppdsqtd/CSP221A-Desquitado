print("Git Notes")

r"""
DOWNLOADING

cd C:\Users\YourUsername\Documents
git clone https://github.com/phlppdsqtd/EXISTING-REPO-NAME.git
cd EXISTING-REPO-NAME

[POWERSHELL] FOR NEW PC:
[INSTALL UV] powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" 
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path" 
uv python install 3.12.11

[VS CODE] FOR EACH NEW PROJECT:
create new folder
open folder in VS code
do below in terminal:
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path" 
uv venv --python 3.12.11 .venv (or py -3.12 -m venv .venv)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\activate 

python --version 

Press Ctrl + Shift + P
Type and select Python: Select Interpreter
Select the interpreter pointing to .\.venv\Scripts\python.exe

UPLOADING (EXISTING REPO)
git add .
git commit -m "Desquitado"
git push 

UPLOADING (NEW REPO)
git init
echo .venv > .gitignore 
git add .
git commit -m "Desquitado"
git branch -m main
git remote add origin https://github.com/phlppdsqtd/NEW-REPO-NAME.git
git push -u origin main

SAMPLE: BRANCH
git checkout -b feature-drone-camera
git add .
git commit -m "Added take_photo method to DroneRobot"
git checkout main
git merge feature-drone-camera
git push origin main
git push origin feature-drone-camera

SAMPLE: REVERT
git add .
git commit -m "Added speak method to Robot base class"
git revert HEAD --no-edit
git log --oneline
git push origin main

SAMPLE: TAG
git tag v1.0.0
git push origin v1.0.0
"""