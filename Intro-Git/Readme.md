Introduction to git
====================

Git is a [Version Control System (VCS)](https://en.wikipedia.org/wiki/Version_control). 

# References

- https://fr.slideshare.net/ThomasRausch4/git-introduction-tutorial
- https://git-school.github.io/visualizing-git/
- https://github.com/HMMA238-2020/git-tutorial

# Objectives

During this session you will learn how to:

1. **clone** a remote repository and to register the versions of a local folder
2. save snapshot of your work: **commit**
5. create **branches** to isolate some modifications
3. interact with a remote repository: **push** your modifications and **pull** the modifications of others
4. resolve simple conflicts with **merge**

# Setting up your **local** git identity

## Git

On a terminal, specify the email address with which you will make your commits:
```
$ git config --global user.email "prenom.nom@domaine.fr"
```

## Create a SSH key

The SSH is needed to get a smooth authentification procedd to the remode repository. In a terminal:
```
$ ssh-keygen -t rsa -b 4096 -C "prenom.nom@domaine.fr"
```
Accept the default option (keys saved in `~/.ssh` and no passphrase)

```
ssh-add
```
Ref: https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

# Github

GitHub is a web hosting service for remote repositories using git. GitHub includes additional features for collaboration, such as bug tracking, requests to add features, or task management. Unfortunately GitHub do not include natively a Continuous Integration system. Note that there are other git-based hosting websites such as GitLab or BitBucket.

### Create a GitHub account

Please go to https://github.com/ and follow the instructions for creation and activation for your account.

### Add your SSH key

In a terminal
```
$ cat ~/.ssh/id_rsa.pub
```
copy the result into the clipboard and follow the instruction [here](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).

To check your installation, please follow [this](https://help.github.com/en/github/authenticating-to-github/testing-your-ssh-connection)

## Create a Repository

Let's create a remote repository hosted on your GitHub account. 

On GitHub, click on the `+` symbol at the top right of the page, then `New repository`. Give the name `FirstRepo` to your new project and a short description. 

Create a **public** repo, meaning that everyone can access to your code (read only). Finish by clicking on `Create repository`. 


Follow the instructions provided by GitHub to create your local copy of the repository:
1. Create a new folder called `FirstRepo` in your `/home` directory and `cd` to it
2. Then execute the following command
```
echo "# FirstRepo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:XXXXXXXXXXXXXXXXXX/FirstRepo.git
git push -u origin master
```


**Exercice:** 

Create a text file called `.gitignore` with the following content:
```
*.pdf
*~
```
Create a commit and push it to your repo. What is the purpose of this file?

# Interact with other users

The purpose of this exercise is to learn how to the use git as a collaboration tool for software development.

## Using an existing repository

Browse the repository at https://github.com/HMMA238-2020/git-tutorial. What is this module able to do?

**Exercice:**

Fork the repository by following these steps: 
  1. On GitHub, click on the fork icon. 
  2. A copy is added to your GitHub space. Clone it (this copy!) to get a local repository. 
  3. In a terminal, inspect the output of the command `git remote get-url origin`

## Debuging

A bug has appeared into the python module after some commit. An issue has been opened inin the bug tracking system at https://github.com/HMMA238-2020/git-tutorial/issues . Your goal is to find the problem... and then to fix it on your **forked repo**. Finally, you will be able submit a Pull Request to the original repository to share your fix.

### Identification of the bad commit

Your goal is to identify the commit(s) that caused the bug. Use `git log`, `git diff`, `git checkout` to identify the commit responsible for the problem.

### Create a new branch to fix the problem

In order to fix a complex bug or add a new feature, it is often necessary to modify several parts of the code. We create a branch, where we make all the commits dedicated to solve the bug. The idea is to maintain a stable version, in the branche `master`, separated from the developing version, which may contain bugs.

**Exercice:** 

1. Create a local branch `Fix_EOL_Error`
2. Push this local branch to your remote repo.
3. Checkout to the `Fix_EOL_Error` branch, fix the bugs. The branch `master` will not be affected.
4. Merge the fix into the branch `master`
5. suppress the local branch `Fix_EOL_Error` and the remote `origin/Fix_EOL_Error` branch

### Pull request

Your work about bug fixing may interest the original author of the project. On GitHub, open a pull-request. Pull-requests are a set of commits which can be integrated directly by the author of the project in its repository, and are thus a powerful tool for working with others.

## Branch Merging and Solving conflict

**Exercice:**

  1. Checkout to the branch `NonGaussian`. Try to figure out what has changed compared to the master branch. 
  2. Try to merge the branch `NonGaussian` to the branch `master`. 
  3. Where are located the conflicts? They are shown with the following decorator
```python
      <<<<<<< HEAD
      some code on current branch
      =======
      some code on branch to be merged
      >>>>>>> NonGaussian
```
   
  4. Resolve them by plotting the two histogram on a same plot. Namely produce a figure like this:![plot](plot.png)


# To go further

Please visit https://learngitbranching.js.org/ 
