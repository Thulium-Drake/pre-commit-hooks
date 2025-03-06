#!/bin/bash
# Check if MANIFEST.in exists, create if not
if ! test -f MANIFEST.in
then
  cat << EOF > MANIFEST.in
# Include all
global-include *

# Exclude dynamic or external stuff
global-exclude *.swp *.pyc
recursive-exclude .git *
EOF
fi
