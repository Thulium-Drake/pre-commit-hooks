# Pre-commit hooks
This repo contains custom pre-commit hooks

## ansible-sign
This hook will verify if a role is signed with ansible-sign and fail the check if it isn't

## terramate-fmt and terramate-generate
This hook will ensure that your terramate configuration has been generated and formatted correctly


# Adding new hooks
Adding new hooks requires the following steps:

  * Start with the following python skeleton:
```
import os

def my_stuff()

def main():
    my_stuff()

if __name__ == "__main__":
    raise SystemExit(main())
```
  * Add the python script to the `pre_commit_hooks` folder, e.g. `my_stuff.py`
  * Add the script in `setup.cfg`
```
[options.entry_points]
console_scripts =
    my-stuff = pre_commit_hooks.my_stuff:main
```
  * Add the hook config in `.pre-commit-hooks.yaml`
```
- id: my-stuff
  name: Do stuff!
  description: This hook does stuff
  entry: my-stuff
  language: python
  pass_filenames: false
  always_run: true
```
  * Bump the version of the version in `setup.cfg`
  * Commit to git and make a new tag
