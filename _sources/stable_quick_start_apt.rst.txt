==============================
Probe Basic APT Stable Install
==============================

**Probe Basic APT Installation Guide for use with Debian 12 Bookworm and LinuxCNC version 2.9 or Later**

Important Requirements
----------------------

    - Probe Basic is currently designed for 1920x1080 screen sizes only!
    - Probe Basic requires graphics hardware that supports OpenGL 3.2 and OpenGL Shading Language (GLSL) 1.50 or later
    - Probe Basic is tested on xfce4, during install of Debian 12 ISO:
    - DO NOT enter a Root password during installation, leave blank and skip this page.

    During installation, this screen below will appear, be sure to uncheck gnome and check xfce as pictured below. No other changes on this page are needed.

    .. image:: images/xfce_check_doc.png
        :align: center


Installation Steps
------------------


1. Download the Linux Debian 12 Bookworm ISO Image File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Download from: https://www.debian.org/download

    Select the Linux Debian 12 Bookworm Netinst CD ISO from the above link. You will need to make a bootable DVD or USB thumb drive depending on how you plan to install. The below software is extremely easy and works flawlessly with Linux Debian OS images:

    https://www.balena.io/etcher/?ref=etcher_update

    Once you have created your flash stick for LinuxCNC, proceed to install and boot the system. (Note: It is advised to have an ethernet cable internet connection during install). Select the graphical installation option. Follow the steps on screen to complete installation. When you are greeted by the Linux Desktop Selection Page, uncheck the GNOME option and check the XFCE4 option.


2. Update the System
^^^^^^^^^^^^^^^^^^^^

    After installation, run the following commands in the main terminal:

    .. code-block:: bash

        sudo apt update
        
        
        sudo apt upgrade


3. Install LinuxCNC (if not already installed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Amd64 Deb (for PC's):
   
      https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-uspace_2.9.3_amd64.deb

   
   Arm64 Deb (for Pi 4/5)

      https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-arm64/linuxcnc-uspace_2.9.3_arm64.deb



   In a terminal, enter the following lines one at a time and press enter after each:

      .. code-block:: bash

         cd ~
         
         cd Downloads
         
         sudo dpkg -i linuxcnc-uspace_2.9.3_amd64.deb


    Once you have installed LinuxCNC, open it and start the axis sim briefly and then shut it down to ensure the installation was successful.


4. Add the APT Repository for the Installation type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **AMD64 for PC Installation Repository:**
    
        Run the following commands in the main terminal one at a time:

        .. code-block:: bash

            sudo apt install curl


            echo 'deb [arch=amd64] https://repository.qtpyvcp.com/apt stable main' | sudo tee /etc/apt/sources.list.d/kcjengr.list


            curl -sS https://repository.qtpyvcp.com/repo/kcjengr.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kcjengr.gpg


            gpg --keyserver keys.openpgp.org --recv-key 2DEC041F290DF85A



    
    **ARM64 Raspberry Pi 4 and 5 Installation Repository:**
    
        Run the following commands in the main terminal one at a time:

        .. code-block:: bash

            sudo apt install curl


            echo 'deb [arch=arm64] https://repository.qtpyvcp.com/apt stable main' | sudo tee /etc/apt/sources.list.d/kcjengr.list


            curl -sS https://repository.qtpyvcp.com/repo/kcjengr.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kcjengr.gpg


            gpg --keyserver keys.openpgp.org --recv-key 2DEC041F290DF85A




5. Update the Repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt update


6. Install QtPyVCP and Probe Basic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash


        sudo apt install python3-qtpyvcp


        sudo apt install python3-probe-basic


    Congratulations! You have now installed Probe Basic. You should be able to launch the Probe Basic sim from within the LinuxCNC applications dropdown menu.


Updating and Configuration
--------------------------

    Updating of Probe Basic and QtPyVCP will occur when you run the normal "sudo apt update" and "sudo apt upgrade" commands. During updating, the Probe Basic sim configuration files will be overwritten. It is strongly recommended to create your machine configuration files with unique names to avoid having them overwritten during updates.
