import os
import json
import subprocess

def getGitRepos(directory, output={}):
    # get all folders in directory
    allFolders = os.listdir(directory)
    joinedFolders = []
    for folder in allFolders:
        # ignore hidden folders
        if not folder.startswith('.') and os.path.isdir(os.path.join(directory, folder)):
            joinedFolders.append(os.path.join(directory, folder))
    # loop through all folders
    for folder in joinedFolders:
        actualFolder = folder.split('/')[-1]
        parentFolder = folder.split('/')[-2]
        if output.get(parentFolder) == None:
            output[parentFolder] = {}
            output[parentFolder][actualFolder] = {}
        else:
            output[parentFolder][actualFolder] = {}
        # check if the folder is a git repository
        if os.path.isdir(folder + "/.git"):
            # get the git information
            gitInfo = subprocess.check_output(
                ["git", "remote", "-v"], cwd=folder)
            # split the git information into an array
            gitInfo = str(gitInfo).split()
            try:
                # get the git url
                gitUrl = gitInfo[1]
                # add the git url to the output
                output[parentFolder][actualFolder]["gitUrl"] = "git@"+gitUrl.split('@')[-1]
            except:
                print("no remote repository found")
        else:
            # recursively get the git repositories
            getGitRepos(folder, output[parentFolder])
    return output

# get current directory
currentDirectory = os.getcwd()
with open('gitInfo.json', 'w') as outfile:
    json.dump(getGitRepos(currentDirectory), outfile, indent=4)

#GitStructureDump
