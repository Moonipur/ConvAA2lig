inputf = '6M0J.pdb'
ligname = 'ACE'

#Processing
def Processing(input, ligname):
    output = ligname + '.pdb'

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

print('Test input name: {}'.format(inputf))
print('Test output name: {}.pdb'.format(ligname))
print("\t|--|\n\t|--|\n\t|--|\n\t|--|\n\t|--|\n\t \/\nTest process let's start")
Processing(inputf, ligname)
print("\t|--|\n\t|--|\n\t|--|\n\t|--|\n\t|--|\n\t \/\nProcess is already finished")
