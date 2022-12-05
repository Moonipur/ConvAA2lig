# !/bin/bash

if [ -f ~/.bashrc ];
then
   Loc=`find "$(cd ..; pwd)" -name "ConvAA2lig.py"`;
   echo "alias ConvAA2lig='python3 ${Loc}'" >> ~/.bashrc;
else
   echo "Your .bash_profile does NOT exist";
fi
