#!/bin/bash

Loc=`find "$(cd ..; pwd)" -name "ConvAA2lig.py"`;

sed -z 's/alias ConvAA2lig='python3 ${Loc}\n//g' ~/.bashrc 