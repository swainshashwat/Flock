import os
import sys
import site

def setup_python_path():

    # TBD : Setup log for symlinks 

    # Add the project root directory to the Python path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))
    if project_root not in sys.path:
        sys.path.append(project_root)

    # Get the site-packages directory
    site_packages = site.getsitepackages()[0]

    # Create a symlink to the project root directory in site-packages
    symlink_name = os.path.join(site_packages, "flock")
    if not os.path.exists(symlink_name):
        os.symlink(os.path.abspath(os.path.dirname(__file__)), symlink_name)
    

    # TBD : setup yml file to setup the site-packages
    

# Automatically set up the Python path and create symlink when this script is imported
if __name__ == "__main__":
    setup_python_path()
