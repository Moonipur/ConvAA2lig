# !/bin/bash

if [ -f ~/.bash_profile ];
then
   Loc=`find "$(cd ..; pwd)" -name "ConvAA2lig.py"`;
   echo "alias ConvAA2lig='python3 ${Loc}'" >> ~/.bash_profile;
else
   echo "Your .bash_profile does NOT exist";
fi
