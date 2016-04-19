# Wednesday - Command line & Git

## Materials for this day
  - https://www.codecademy.com/learn/learn-the-command-line
  - https://try.github.io

## Please install git on your system:
  - Windows:
    - http://cmder.net/ or https://git-scm.com/download/win
  - Linux
    - `sudo apt-get install git` (Ubuntu)
    - `sudo yum install git` (Fedora)
  - Mac
    - http://git-scm.com/download/mac or `brew install git`

## Tasks for this day
  - Command Line
    - setup the environment
    - basic terminal operations
    - manipulations
    - redirections
    - scripts

  - Git
    - git basics
    - branches
    - git tools
    - pull requests
    - rebase

## Tasks in detail
  - Open a terminal
  - Basic terminal operations
    - Check the current working directory
    - Check the files and directories in your working directory
    - Create a Greenfox directory
    - Change into the Greenfox directory
    - Check the files and directories in your working directory
    - Create an empty index.html file
    - Create an imges directory
    - Create a css directory
    - Change into the images directory
    - Go back to the parent directory
    - Create at least one file to every directory

  - Open a terminal
    - Fork this git repository: https://github.com/greenfox-academy/syllabus-2015-Nov.git
    - Clone your greenfox repository
    - Change into week-1/3-command-line/ directory

  - Manipulations
    - Change into the project directory
    - List the detailed file and directory informations
    - Copy the index.html into about.html
    - Create a temp_images directory
    - Copy 1.jpg and 2.jpg into temp_images directory
    - Copy every jpg file into temp_images directory
    - Move 6.jpg file from css into images directory
    - Delete 7.jpg from css directory
    - Navigate up one directory from project/css/ to project/

  - Redirections
    - Echo a string to a file
    - cat a file content and redirect the content to another file
    - redirect a file content to cat command
    - count the words in index.html
    - cat a file content and pipe to wc
    - sort a file
    - sort a file and redirect the input to a file
    - remove the duplicated lines from tasks.txt
    - cat task.txt and filter basic tasks
    - cat task.txt and filter out with -v the basic tasks

  - Git basics
    - setup your environtment
    - git config --global user.name "Your Name"
    - git config --global user.email yourname@example.com

    - create a repo on github
    - clone it on your system using command line

    - create 5 directory and 5 file with content
    - see the changes
    - add these files as staged files
    - use git status to check
    - commit it with commit message
    - change the content of two file
    - set to staged
    - use git status
    - commit it with commit message
    - git pull
    - git push -u origin my_branch
    - check it on github

    - change the content of two file
    - use git status
    - remove from staged git reset HEAD file

    - change the content of two file
    - use git status
    - set to staged
    - git diff --staged or --cached
    - commit it
    - check it on github


  - Branches
    - git branch fix
    - git branch
    - git checkout fix
    - git commit
    - git push
    - check it on github

    - git checkout master
    - git merge fix
    - git branch -d fix
    - git push


## Other:
    git remote show origin

    set the original remote in case of forked repo:
    git remote -v
    git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
    git remote -v

    sync your forked repo:
    git fetch upstream
    git checkout master
    git merge upstream/master

    git log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
