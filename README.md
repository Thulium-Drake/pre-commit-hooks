# Pre-commit hooks
This repo contains custom pre-commit hooks

## ansible-sign
This hook will verify if a role is signed with ansible-sign and fail the check if it isn't

## terramate-fmt and terramate-generate
This hook will ensure that your terramate configuration has been generated and formatted correctly


# Adding new hooks
Adding new hooks requires the following steps:

  * Add the python script to the `pre_commit_hooks` folder
  * Add the script in `setup.cfg`
  * Add the hook config in `.pre-commit-hooks.yaml'
