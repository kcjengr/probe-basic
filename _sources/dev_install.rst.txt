Probe Basic Development Installation
====================================


This Dev install method uses an installer script and will install QtPyVCP and Probe Basic into a virtual environment (venv) which is now a requirement for pip installations on systems running python version 3.11 which is what comes on Linux Debian 12 Bookworm. This has been tested to work on a clean install of debian 12 bookworm using the xfce4 option and nonfree firmware cdnetinst iso. Download and install the bookworm iso from the link below for your pc type, typically the amd64 on normal pc's:


https://www.debian.org/releases/bookworm/debian-installer/

.. important::
   During Linux Bookworm installation, DO NOT set a root password when prompted, just press continue to move to the next section in the visual installer. Once installed, run all of your updating.


Installation Steps
------------------

   1. Download and Install linuxcnc from deb file choose Amd64 (PC's) or Arm64 (Pi 4/5):
   
   Amd64 Deb (for PC's):
   
      https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-uspace_2.9.3_amd64.deb

   
   Arm64 Deb (for Pi 4/5)

      https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-arm64/linuxcnc-uspace_2.9.3_arm64.deb


   In a terminal, enter the following lines one at a time and press enter after each:

      .. code-block:: bash

         cd ~
         
         cd Downloads
         
         sudo dpkg -i linuxcnc-uspace_2.9.3_amd64.deb


   2. Next restart your computer

   3. Ensure git is installed:

      .. code-block:: bash

         sudo apt install git

   4. Ensure zenity is installed:

      .. code-block:: bash

         sudo apt install zenity

   5. Create a directory and clone the repo to it. Either clone or download a zip file:

      .. code-block:: bash

         cd ~
         mkdir dev
         cd dev
         git clone https://github.com/Lcvette/qtpyvcp-bookworm-installer.git
         cd qtpyvcp-bookworm-installer
         ./install_for_qtpyvcp.sh


Getting Started with Probe Basic DEVELOPMENT
--------------------------------------------

    You should now see a series of icons on your desktop, 3 probe basic mill instances consisting of an inch/metric/atc sim and 1 lathe sim instance.  There should also be 2 qtpyvcp icons, one for mill and one for lathe. These icons must be used to enter QTdesigner for your develpment work.  To test your edits in QTdesigner you must use the desktop launcher icons provided to start and run your instance of probe basic sim.  This is required due to python3 requiring to be run in a VENV (virtual environment).  Do not use the application drop down to run linuxcnc or you will not see your changes from your dev efforts.  The changes will be saved in the dev folder files.  When you have completed your edits and wish to create a .deb build file, you can follow the instructions under creating a .deb installation file in the probe basic instruction docs. (coming soon).


Updating QtPyVCP and Probe Basic
--------------------------------

   To update QtPyVCP and Probe Basic, from terminal in the installer directory file, run the following script command:

   .. code-block:: bash

      ./updater.sh


Uninstalling QtPyVCP and Probe Basic
------------------------------------

   To uninstall QtPyVCP and Probe Basic, delete the **/home/(your_pc_name)/dev** folder. Since this is a venv run in place install, it is removed once the directory is deleted.


Note
----

   Files that must be executable:

   - install_for_qtpyvcp.sh
   - sudo_helper.sh
   - updater.sh
