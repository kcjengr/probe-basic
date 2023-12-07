#!/bin/bash

source ~/dev/venv/bin/activate
cd ~/dev/probe_basic/linuxcnc/configs/probe_basic_manual_sim
linuxcnc probe_basic.ini
