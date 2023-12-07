#!/bin/bash

source ~/dev/venv/bin/activate
cd ~/dev/probe_basic/linuxcnc/configs/probe_basic_atc_sim
linuxcnc vmc_index_inch.ini
