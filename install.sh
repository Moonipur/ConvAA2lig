# !/bin/bash

if [ -f ~/.bashrc ];
then
   Loc=`find "$(cd ..; pwd)" -name "ConvAA2lig.py"`;
   echo "alias ConvAA2lig='python3 ${Loc}'" >> ~/.bashrc;
   echo "Installation already finished";
else
   echo "Your .bashrc does NOT exist";
fi
