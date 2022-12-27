# `ConvAA2lig`

The `ConvAA2lig` is a simple program for converting PDB file from Amino acid name to your Ligand name.

# Install program
chmod +x install.sh

./install.sh

source ~/.bashrc

# Run test
cd test

python test_ConvAA2lig.py

# Usage: 
ConvAA2lig -n [Name] -i [Input] -o [Output] --atom [False]

# Optional argruments:
    -h, --help      show this help message and exit
    -n [Name]       ligand name that you want to change
    -i [Input]      input file path (.pdb)
    -o [Output]     output directory path
    -a, --atom      Turn on/off for sorting atom number (default False; True)
    -v, --version   the lastest version of ConvAA2lig
    
# Uninstall program
chmod +x UNINSTALL.sh

./UNINSTALL.sh
    
# Author's email:
    moo_sutthittha@hotmail.com (Moonipur)

# The lastest version:
    ConvAA2lig v1.0.2    

** Please contact us if you have any questions or problems with the program.
