# setup a dev environment
$ python -m pip install -e .

# install setup.py
$ python setup.py install

#to merge with master
$ git checkout master
$ git pull
$ git merge my-feature-branch
$ git log

# to convert jupyter notebook to html
$ jupyter nbconvert --to html {}.ipynb

# updating forked branches
    # Add the remote, call it "upstream":

    git remote add upstream https://github.com/whoever/whatever.git

    # Fetch all the branches of that remote into remote-tracking branches

    git fetch upstream

    # Make sure that you're on your master branch:

    git checkout master

    # Rewrite your master branch so that any commits of yours that
    # aren't already in upstream/master are replayed on top of that
    # other branch:

git rebase upstream/master