# Probe Basic subroutines

This folder contains 4 sub directories with the various subroutines used by Probe Basic, details about each are further below or in the README.md in each.

When installed/updated via apt Probe Basic will install the latests version of the of its subroutines to `/usr/share/probe_basic/nc_files`

These files are also copied to `~/linuxcnc/nc_files`.  How ever it will not overwrite existing files but will add any new files.  
This ensures that any changes you make to the files at `~/linuxcnc/nc_files` are preserved during updates but new routines will be added. After updates you may wish to compare the difference between the routines at `/usr/share/probe_basic/nc_files` and `~/linuxcnc/nc_files` to see if any change have been made to existing routines.  
One quick way to view a summary of changes is with `diff` and `diffstat` (this may require `sudo apt-get install -Y diff diffstat`)  
`diff -u ~/linuxcnc/nc_files/probe_basic /usr/share/probe_basic/nc_files/probe_basic | diffstat`

For a mill your INI `[RS274NGC]SUBROUTINE_PATH` should include `subroutines`, `probe` and `atc_carousel`  
`SUBROUTINE_PATH = ../../nc_files/probe_basic/subroutines:../../nc_files/probe_basic/probe:../../nc_files/probe_basic/atc_carousel`

For a lathe you should include the `lathe` folder as-well at the start  
`SUBROUTINE_PATH = ../../nc_files/probe_basic/lathe:../../nc_files/probe_basic/subroutines:../../nc_files/probe_basic/probe:../../nc_files/probe_basic/atc_carousel`

## subroutines
This folder contains some basic subroutines called from various parts of the UI  
It does include the tool_touch_off routine that is used with a tool setter

## probe
This folder contains the probing subroutines that are called form the PROBING tab

## atc_carousel
This folder contains carousel style ATC subroutines  
These routines are all called form the ATC tab in the main UI or as part of M6 remap.  
They automatically support any of the of the sizes currently available (8, 10, 12, 14, 16, 18, 20, 21, 24) based on your INI's `\[ATC\]POCKETS` setting  

If you have an ATC these are the files that you most likely will need to adjust to your needs, see the README.md in the directory for more details

## lathe
This folder contains lathe subroutines for probe_basic_lathe  
Some of these are unique to the lathe UI and some are tweaked versions of routines in the other folders that override there normal behaviour
