#!/bin/bash

# Pull the latest changes and arrange them for production.

set -x # Exit if one of these commands fails
set -e # Print each command as you run it

# Bring the changes from github
git fetch

# Move our own commit on top of them
# This should move our single special commit that changes debug to false
# while getting us the rest of the changes underneath it.
#
# If the git rebase fails, use 'git rebase --abort' to undo it
# and then do 'git diff origin/main' to try to figure out why it is so hateful
git rebase

# put the static files where django wants them
python manage.py collectstatic --noinput



