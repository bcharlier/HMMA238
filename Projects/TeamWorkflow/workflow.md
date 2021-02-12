# Common workflow


## Configuration phase
Go to a directory of our choice and open a terminal from it. (Or open a terminal and go to a directory of your choice from it.)
Now we want our teammates to be able to identify who made each contribution.
For this purpose, we need to set up a name and an e-mail :

```
$ git config --global user.name "Your Name"
$ git config --global user.email "your@email"
```

Since we want to track a remote repository (we assume here the repository already exist).
We want to *get a local copy* on our machine.

  * clone repo

```
$ git clone <url> .

# or if you want to use SSH cloning, see
# https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account
# You can copy the url by first clicking on the "Code" button and then on the "copy-to-clipboard" icon.
```

## Working phase

Assuming we are in the corresponding directory, we can perform an `ls -la` to see the cloned files.
We want now to create a new branch and start working off from it

  * create branch

```
git branch my_new_branch
```

Typing `git branch` will display local existing branches.
The branch we just created is the branch we want to work with.

  * select branch

```
$ git checkout my_new_branch
```
We can type `git branch` , we will see that the new branch has been selected(highlighted and marked by a symbol `*`)

```
anas@sakhr:~/studies/practicals$ git branch
  master
* my_new_branch
```


**We are now ready to start working on the code files. The changes will be local changes and will not affect other branches.**

## Committing changes, merging & cleaning
### Committing changes

By now, let us say we are done working on the task and want to share the results with the rest of the team.
While working on the code, `git` was tracking the changes.

  * check status
```
$ git status
```
It will say that there are changes not staged for commits and will show what changes have occurred.
So we want to add those changes to the staging area and do a commit explaining what changes have been made using the following :

  * add & commit
```
$ git add -A
$ git commit -am "explain your contributions"
```

By now we successfully committed the changes to the local 'my_new_branch' branch. This had no effect on the master branch and no effect on the remote repository.
After the commit, we  want to push the branch to the remote directory:
  * push to remote
```
$ git push -u origin my_new_branch
```

Remember, we already configured our name at the start and we pushed our branch to remote.
This means our team can now see the new branch and check if the code runs well before it is merged into the master branch.

### Merging & cleaning

Let us say our team reviewed the code and validates it and the branch is ready to be merged into the `master` branch.
The roadmap is as follows:
select `master` branch ==> pull  ==> merge (local) ==> push (remote) ==> delete (local) ==> delete (remote).


  * merge and push
```
$ git checkout master

# always pull in case any changes were made while working locally
$ git pull origin master

$ git merge my_new_branch
$ git push origin master
```


Finally, we want to delete `my_new_branch` (local and remote).
  * delete
```
git branch -d my_new_branch

git push origin --delete my_new_branch
```


## Essentials

Let us wrap up the whole thing and recap important steps :

clone ==> create branch  ==> work on it ==> check status ==> add & commit ==> push to remote ==> select `master` ==> pull ==> merge local ==> push ==> delete local ==> delete remote


# Resources

- https://git-scm.com/book/en/v2
- https://www.youtube.com/c/Coreyms/playlists
- https://www.atlassian.com/fr/git/tutorials/learn-git-with-bitbucket-cloud (french)
- https://docs.github.com/en

