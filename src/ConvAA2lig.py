#! /usr/bin/python3

import os
import sys

help_description = '''usage: ConvAA2lig -n [Name] -i [Input] -o [Output] --atom [False]

optional argruments:
    -h, --help      show this help message and exit
    -n [Name]       ligand name that you want to change
    -i [Input]      input file path (.pdb)
    -o [Output]     output directory path
    -a, --atom      Turn on/off for sorting atom number (default False; True)
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
        file.close()

def clean(key, nu1, out_path):
    data = []
    with open(out_path, 'r') as file:
        for line in file:
            insert = nu1
            if line[12:16] == key:
                if len(insert) == 2:
                    file = line[:12] + " " + insert + " " + line[16:]
                    data.append(file)
            else:
                file = line[:]
                data.append(file)
    
    with open(out_path, 'w') as py:
        py.writelines(data)
        py.close()


def sort(key, nu1, out_path):
    data = []
    num = 1
    with open(out_path, 'r') as file:
        for line in file:
            insert = nu1 + str(num)
            if line[12:16] == key:
                if len(insert) == 2:
                    file = line[:12] + " " + insert + " " + line[16:]
                    # print(file)
                    data.append(file)
                    num += 1
                elif len(insert) == 3:
                    file = line[:12] + " " + insert + line[16:]
                    # print(file)
                    data.append(file)
                    num += 1
                elif len(insert) == 4:
                    file = line[:12] + insert + line[16:]
                    data.append(file)
                    num += 1
                elif len(insert) == 5:
                    file = line[:11] + insert + line[16:]
                    data.append(file)
                    num += 1
                else:
                    print('** Your input file is too large for sorting atom.')
                    return False ; break
            else:
                file = line[:]
                data.append(file)
                       
    with open(out_path, 'w') as py:
        py.writelines(data)
        py.close()


def ATOM(out_before, name, boole):
    if boole == 'False':
        print('>> The processing is finished')
    elif boole == 'True':
        print('** Use --atom command with the [True] value')
        output = out_before + name + '.pdb'
        clear = {
            ' NE1': ['NE'],
            ' NE2': ['NE'],
            ' NH1': ['NH'],
            ' NH2': ['NH'],
            ' ND1': ['ND'],
            ' ND2': ['ND'],
            ' OD1': ['OD'],
            ' OD2': ['OD'],
            ' OE1': ['OE'],
            ' OE2': ['OE'],
            ' OG1': ['OG'],
            ' OG2': ['OG'],
            ' CG1': ['CG'],
            ' CG2': ['CG'],
            ' CD1': ['CD'],
            ' CD2': ['CD'],
            ' CE1': ['CE'],
            ' CE2': ['CE'],
            ' CE3': ['CE'],
            ' CH2': ['CH'],
            ' CZ2': ['CZ'],
            ' CZ3': ['CZ'],
        }

        atom = {
            ' N  ': ['N'],
            ' NE ': ['NE'],
            ' NZ ': ['NZ'],
            ' C  ': ['C'],
            ' O  ': ['O'],
            ' OE ': ['OE'],
            ' OG ': ['OG'],
            ' OH ': ['OH'],
            ' CA ': ['CA'],
            ' CB ': ['CB'],
            ' CG ': ['CG'],
            ' CD ': ['CD'],
            ' CE ': ['CE'],
            ' CH ': ['CH'],
            ' CZ ': ['CZ'],
            ' SD ': ['SD'],
            ' SG ': ['SG'],
        }

        for j, key in enumerate(clear.keys()):
            clean(key, clear[key][0], output)

        for i, key in enumerate(atom.keys()):
            t = sort(key, atom[key][0], output)
        if t == False:
            os.remove(output)
            print("   Please try again with other file")
        else:
            print('>> The processing is finished')

        

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
                                    if len(sys.argv) >= 8:
                                        if sys.argv[7] == '-a' or sys.argv[7] == '--atom':
                                            if len(sys.argv) >= 9:
                                                if sys.argv[8] == 'True' or sys.argv[8] == 'False':
                                                    boole =  sys.argv[8]
                                                    ATOM(output_file, Lig_name, boole)
                                                else:
                                                    print("** Your value '{}' is NOT boolean".format(sys.argv[8]))
                                                    print('   Please input boolean value [True/False]')
                                            else:
                                                print('** Please input boolean value [True/False]')
                                        else:
                                            print('ERROR: unrecognized arguments: {}'.format(sys.argv[7]))
                                            print('** Plese check with HELP command:\nConvAA2lig --help or ConvAA2lig -h')
                                    else:
                                        print('** Use --atom command with the default value [False]')
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


