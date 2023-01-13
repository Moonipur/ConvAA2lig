#! /usr/bin/python3

from __init__ import *

current_dir = os.getcwd()

Usage = '''usage: ConvAA2lig -n [Name] -i [Input] -o [Output] --atom {True, False}
'''

Epilog = "** Please contact us if you have any questions or problems with the program."

parser = argparse.ArgumentParser(
    prog = 'ConvAA2lig',
    usage= f'{Usage}',
    description = "ConvAA2lig is a simple program for converting PDB file from Amino acid name to your Ligand name. Author's email: moo_sutthittha@hotmail.com (https://github.com/Moonipur)",
    epilog = f'{Epilog}'
)

parser.add_argument('-n', metavar='Name', type=str, required=True, help="Ligand name that you want to change")
parser.add_argument('-i', metavar='Input', type=str, required=True, help="Input file path (.pdb)")
parser.add_argument('-o', metavar='Output', type=str, required=False, help='Output directory path (default: current directory)', default=current_dir)
parser.add_argument('-a','--atom', metavar='False', type=str, required=False, help='Turn on/off for sorting atom number (default: False)', default=False)
parser.add_argument('--version', help='ConvAA2lig v2.0', action='version', version='%(prog)s v2.0')
args = parser.parse_args()

#Processing
def Processing(input, output, ligname):
    output = os.path.join(output, ligname + '.pdb')
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
    if boole == False:
        print('>> The processing is finished')
    elif boole == True:
        print('** Use --atom command with the [True] value')
        output = os.path.join(out_before, name + '.pdb')
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


def check_agrs(name, inpath, outpath, atom):
    if os.path.exists(inpath):
        fil = inpath
        if fil[-4:] == '.pdb':
            In_PATH = os.path.abspath(inpath)
            print(f'Input path: {In_PATH}')
        else:
            print(f'Error: Input path: {In_PATH} is NOT PDB format')
    else:
        print(f'Error: Input path: {inpath} is NOT exist')

    if os.path.isdir(outpath):
        out_path = os.path.abspath(outpath)
        Out_PATH = out_path
        print(f'Output path: {Out_PATH}')
    else:
        print(f'Error: Output path: {outpath} is NOT directory')

    if len(name) == 3 and name.isupper() == True and name.isalpha() == True:
        Lig_Name = name
        print(f'Ligand name: {Lig_Name}')
    else:
        print(f'Your ligand name "{name}" is NOT appropriate\n** should have only 3 characters and all are UPPERCASE alphabets')
    
    if atom == "False":
        Atom = False
    elif atom == "True":
        Atom = True
    else:
        print(f'Your atom option {atom} is NOT boolean')

    return Lig_Name, In_PATH, Out_PATH, Atom


if __name__ == "__main__":
    try:
        Check_list = check_agrs(args.n, args.i, args.o, args.atom)
        Lig_Name = Check_list[0]
        In_PATH = Check_list[1]
        Out_PATH = Check_list[2]
        Atom = Check_list[3]

        if Atom == False:
            print('** Use --atom command with the [False] value')
            Processing(In_PATH ,Out_PATH, Lig_Name)
            print('>> The processing is finished')
        elif Atom == True:
            Processing(In_PATH ,Out_PATH, Lig_Name)
            ATOM(Out_PATH, Lig_Name, Atom)
    except BrokenPipeError as b:
        print(b)