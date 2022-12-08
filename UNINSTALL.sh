#!/bin/bash

comm=`find "$(cd ..; pwd)" -name "ConvAA2lig.py"`

Loc=`grep -n "alias ConvAA2lig='python3 ${comm}'" ~/.bashrc | cut -b 1-3`

sed -i sed -i "${Loc}d" ~/.bashrc ~/.bashrc 
