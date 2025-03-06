import os

def ensure_ansible_sign_manifest():
    if not os.path.isfile("MANIFEST.in"):
        with open("MANIFEST.in", "w") as f:
            f.write("""
# Include all
global-include *

# Exclude dynamic or external stuff
global-exclude *.swp *.pyc
recursive-exclude .git *
""")

if __name__ == "__main__":
    ensure_ansible_sign_manifest()
