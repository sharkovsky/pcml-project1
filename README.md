# pcml-project1
Hi guys! This is our git repository for sharing code and for writing the report.
I suggest the following directory structure, let me know if you have any suggestions:
### report
this directory contains the latex source files and the instructions to compile the report.
Also, this directory should contain minimal scripts to regenerate the figures in the report, just in case.
I'll update a template soon.
### submission-code
this directory contains the version of the code we plan to submit.
### personal development branches
Following Zhang's example, it might be better to use personal development branches instead of directories.
This reflects better the *standard* git workflow, so I guess it is a good exercise.
Therefore, let's all have a *development* branch (e.g. mine is called `cremones-devel`) and let's all submit pull requests when we think we have something good.
##### using development branches
To create a branch, execute the following lines on a terminal, from your personal clone of the git directory
```
git checkout -b <name of your branch>
<make some changes>
git add <files that were changed and that you want to commit>
git commit -m "my first changes"
git push origin <name of your branch>
```
The changes that you made while *inside* your development branch will not be visible to the master branch unless you submit a pull request (I usually do this via the github web interface, I'm unsure how to do this from the command line).
The last line in the given code is important, because it will setup your local development branch to *track* the remote branch (on github) with the same name.

Whenever you need to go back to master, simply type `git checkout master`, and obviously `git checkout <name of the branch> to go to whatever branch you want.

Since your development branch and the master are two separate entities, at some point you probably need to synchronize the changes that were in master with the ones in your local development branch.
You do this with the following code:
```
git checkout <name of your development branch>
git fetch origin master
git merge
```
There will likely be some conflicts, which you need to solve (look for strings like >>>> and ==== in the files that had conflicts).

~~ personal directories ~~
~~ A possibility is that each one of us has a personal directory where we can share code that is in intermediate state. ~~
~~ This might help us to avoid having to resolve many conflicts while merging, but in any case it would be best if each one of us also worked on a personal branch, and only put code in these repositories once the development is almost done. ~~
