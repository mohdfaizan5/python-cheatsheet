#Git Config:

$ git --version
git version 2.38.0.windows.1
$ git config --global user.name "Mohammed Faizan"
$ git config --global user.email "mohdfaizan.zprb2@gmail.com"

---

> Note: Git is different from Github. Git is just a version control and it is offline in your local directory, but when you use platforms github, you can make a online backup of them

To create basic backup in local:

```
git init --> telling git to add/initialize this folder in git record
git add *
git commit -m "your message"
```
git log --> to view the log of commits
git status tells us about stage[what has be updated or added] and changed data



## Restoring the code 
    When we want to go to a particular commit

```
git checkout <hash_id> <what_you_want_to_recover or *>
```

local = refers to things on our computer
remote = refers to things on the online 
-v = verbose = give more details

# Github

## pushing code to github
```
git remote add <nick_name or origin> <github_url> --> links online
git remote -v --> get which url linked
git remote remove <nick_name or origin> --> removes the link

```
push = upload to github
pull = download from github

## Tell github that its you pushing
```
git config --global credential.username "<github_user_name>"
```




```
git remote add <where you want to push eg: main, master> <url>
```



cd --> change directory


---

## Branching:


> Situation: When you're working in some new feature and later you want to make some changes in your old code and still don't want to mess with current feature

>> Branching: working on multiple things at the same time

```terminal
git branch <branch_name>
```
How to visit that branch
```terminal
git checkout <branch_name>
``` 
fix the code and then commit


## Merging:
When we have 2 branches to fix, we use
```terminal
git merge <name_of_feature-to-merge_with>
```
>> Note: Git merges the branch and the branch you're in in[head]

 
## Feature Branch Workflow:

Feature Branches = A workflow.



```terminal

```