# !/bin/bash

if [ -f ~/.bashrc ];
then
   Loc=`find "$(pwd)" -name "ConvAA2lig.py"`;
   echo "alias ConvAA2lig='python3 ${Loc}'" >> ~/.bashrc;
   source ~/.bashrc;
   echo "Installation is already finished";
else
   echo "Your .bashrc does NOT exist";
fi
