#!/bin/bash

comm=`find "$(pwd)" -name "ConvAA2lig.py"`

Loc=`grep -n "alias ConvAA2lig='python3 ${comm}'" ~/.bashrc | cut -d: -f1`

sed -i "${Loc}d" ~/.bashrc 

source ~/.bashrc

echo "Uninstallation is already finished"
