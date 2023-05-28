# GitStructureDump
Dump local nested git repositories into json

## Project
Python script that helps you organize and clone your locally organized Git projects from a JSON file, 
allowing you to quickly set up your projects on a new machine. 
It generates a JSON file that captures the structure of your repositories, 
including nested folders, and stores the corresponding remote repository URLs.

## Project Idea
I organize all my github repositories in one big folder on my machine. They are organized into various subdirectories by personal projects,
coursework, etc. I wanted a way to preserve that structure in a way that it can be easily cloned on a new machine.

### First idea:
- Make the outermost folder a github repository itself.
- Use a `.gitignore` to ignore all directories so that nested git repositories aren't added.
- Use a `.gitkeep` in each project to keep the folder for the structure.
- Create a `gitInfo.txt` file for each repo to store it's remote URL.
- Problems:
    - Have to add each `.gitkeep` and `gitInfo.txt` into the `.gitignore` for each project's git repository.

### Second idea:
Basically the first idea but create a new folder which contains nested folders to preserve the file structure. This folder can be made
into a github repository since it won't actually have any git repositories so we don't need to worry about `.gitignores` for each project
in it.

### Final idea:
The second idea led to the solution of just creating a json file with all this data. Don't know why I didn't think of this in the first place.

## TODO:
Create another script to read the JSON and replicate it's sturcture with all remote repositories correctly cloned.
