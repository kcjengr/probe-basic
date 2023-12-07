#!/bin/bash

source ~/dev/venv/bin/activate
cd ~/dev/probe_basic/linuxcnc/configs/probe_basic_lathe_sim
linuxcnc probe_basic_lathe.ini
