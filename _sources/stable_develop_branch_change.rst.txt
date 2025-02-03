====================================
Changing Stable <-> Develop Versions
====================================

Probe Basic STABLE and DEVELOP Version Information
--------------------------------------------------

    Probe Basic now has STABLE and DEVELOP repositories from which users can select for apt updates. You can switch between repositories to test new and upcoming features, but must understand that the development repository will be a testing version. As such, it may be subject to bugs. If you select the develop branch, please be sure to report any bugs either on the forum or on git.

Step-by-Step Guide to Change the Sources List for Stable and Develop APT Repository
-----------------------------------------------------------------------------------

1. Edit the sources list
^^^^^^^^^^^^^^^^^^^^^^^^

    Type or copy and paste the following line in a terminal, press ENTER, and type in your sudo password when prompted:

    .. code-block:: bash

       sudo nano /etc/apt/sources.list.d/kcjengr.list

    .. image:: images/pb_sources_list.png
       :align: center
       :scale: 80%

    |

2. Modify the repository
^^^^^^^^^^^^^^^^^^^^^^^^

    Edit the source list line to set the apt repository for either STABLE or DEVELOP version of Probe Basic:

    .. image:: images/nano_sources_list.png
       :align: center
       :scale: 80%

    |

    .. image:: images/nano_sources_list_edited.png
       :align: center
       :scale: 80%

    |

3. Save changes
^^^^^^^^^^^^^^^

    Exit and save the changes by pressing CTRL + X, then Y, then ENTER:

    .. image:: images/yes_nano_to_save.png
       :align: center
       :scale: 80%

    |

    .. image:: images/enter_nano_file_save_name.png
       :align: center
       :scale: 80%

    |

4. Uninstall current Probe Basic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Run the following commands in terminal to uninstall the current installation of Probe Basic:

    .. code-block:: bash

       sudo dpkg -P python3-probe-basic
       sudo dpkg -P python3-qtpyvcp

5. Install Probe Basic and QtPyVCP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Run the following commands in terminal to install Probe Basic and QtPyVCP:

    .. code-block:: bash

       sudo apt install python3-qtpyvcp
       sudo apt install python3-probe-basic

6. Update and upgrade
^^^^^^^^^^^^^^^^^^^^^

    Run apt update/upgrade by copying the following commands in the main terminal one line at a time. Select Y for yes if asked at any point during the update:

    .. code-block:: bash

       sudo apt update
       sudo apt upgrade

7. Important Note
^^^^^^^^^^^^^^^^^

    The development versions will likely require edits, additions or updates to config files. These include but are not limited to the yaml, ini, hal, subroutine, python, and any other supporting configuration files. These changes may not always be fully documented as we test them and are making changes, so we urge users to be aware that the development version should be used in a testing environment only. Those wishing to retain stability in operational use should change to the STABLE version.

Troubleshooting and Support
---------------------------

    For bug reporting, general assistance, or troubleshooting, visit the QtPyVCP section of the LinuxCNC forum:

    https://forum.linuxcnc.org/qtpyvcp
