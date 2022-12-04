#! /usr/bin/python3

import os
import sys

help_description = '''usage: ConvAA2lig -n [Name] -i [Input] -o [Output]

optional argruments:
    -h, --help      show this help message and exit
    -n [Name]       ligand name that you want to change
    -i [Input]      input file path (.pdb)
    -o [Output]     output directory path
    -v, --version   the lastest version of ConvAA2lig
    
author's email:
    moo_sutthittha@hotmail.com

The lastest version:
    ConvAA2lig v0.0.1    

** Please contact us if you have any questions or problems with the program.'''

version = 'ConvAA2lig v0.0.1'

#Processing
def Processing(input, output, ligname):
    output = output + ligname + '.pdb'

    with open(input, 'r', encoding='utf-8') as file:
        data = file.readlines()

    inx = 0    
    for line in data:
        if line[:4] == 'ATOM':
            data[inx] = line[:17] + ligname + line[20:]
        elif line[:3] == 'TER':
            data[inx] = line[:17] + ligname + line[20:]
        elif line[:6] == 'HETATM':
            data[inx] = line[:17] + ligname + line[20:]
        else:
            pass
        inx+=1

    ind = 0
    for line in data:
        if line[:4] == 'ATOM':
            data[ind] = line[:23] + '  1' + line[26:]
        elif line[:3] == 'TER':
            data[ind] = line[:23] + '  1' + line[26:]
        elif line[:6] == 'HETATM':
            data[ind] = line[:23] + '  1' + line[26:]
        else:
            pass
        ind+=1

    with open(output, 'w', encoding='utf-8') as file:
        file.writelines(data)


#Check Argumants
if len(sys.argv) >= 2:

    #Check Ligand name
    if sys.argv[1] == '-n':
        if len(sys.argv) >= 3:
            if len(sys.argv[2]) == 3 and sys.argv[2].isupper() == True and sys.argv[2].isalpha() == True:
                Lig_name = sys.argv[2]
                print('Ligand name: {}'.format(Lig_name))
                if sys.argv[3] == '-i':
                    #Check input file path
                    if len(sys.argv) >= 5:
                        if os.path.exists(sys.argv[4]):
                            fil = sys.argv[4]
                            if fil[-4:] == '.pdb':
                                input_file = sys.argv[4]
                                print('Input path: {}'.format(input_file))
                        else:
                            print('The file does NOT exist')

                        if sys.argv[5] == '-o':
                        #Check output file path
                            if len(sys.argv) >= 7:
                                if os.path.isdir(sys.argv[6]):
                                    output_file = sys.argv[6]
                                    print('Output path: {}'.format(output_file))
                                    Processing(input_file, output_file, Lig_name)
                                    print('>> The processing is finished')
                                else:
                                    print('The directory does NOT exist')
                            else:
                                print('ERROR: you did NOT provide a output file path.')
                        else:
                            print('ERROR: unrecognized arguments: {}'.format(sys.argv[5]))
                            print('** Plese check with HELP command:\nConvAA2lig --help or ConvAA2lig -h')

                    else:
                        print('ERROR: you did NOT provide a input file path.')
                else:
                    print('ERROR: unrecognized arguments: {}'.format(sys.argv[3]))
                    print('** Plese check with HELP command:\nConvAA2lig --help or ConvAA2lig -h')

            else:
                print('Your ligand name "{}" is NOT appropriate\n'.format(sys.argv[2])+'** should have only 3 characters and all are UPPERCASE alphabets')
        else:
            print('ERROR: you did NOT provide a ligand name.')
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print(help_description)
    elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print('The lastest version: {}'.format(version))
    else:
        print('ERROR: unrecognized arguments: {}'.format(sys.argv[1]))
        print('** Plese check with HELP command:\nConvAA2lig --help or ConvAA2lig -h')

elif len(sys.argv) < 2:
    print('** Plese check with HELP command:\nConvAA2lig --help or ConvAA2lig -h')


