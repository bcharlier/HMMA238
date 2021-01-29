# How to fix "Le terme «conda» n'est pas reconnu comme nom d'applet de commande...".

### Step 1 : Uninstall anaconda, then install again.

When this window appear : 
<!-- <img src="files/images/python-screenshot.jpg" width="600"> -->

<img src="https://raw.github.com/Poncheele/doc/master/Anaconda.png" width="600">

Check the box "Add Anaconda to my Path environment variable"

### step 2 : Create your environment 

#### Open Anaconda Prompt

Write the following commands :

    conda create -n hmma238 matplotlib

    conda activate hmma238

### Step 3 : Check if it works

Try to launch in VsCode the file test_python.py (located in the git repository HMMA238 (Courses-IDE))

