all_lines = []                                   #defined as name of file
file_name = input("What's the file name with extension?: ")
with open (f'{file_name}', 'r') as file:    #opens a Gaussian text file
    for each_line in file:
        all_lines.append(each_line.strip())

i=0
j=0
for s in range (len(all_lines)):                  #Reads the Input orientation information
    if "Input orientation:" in all_lines[s]:
        start = s
        i = i + 1
for e in range (start + 5, len(all_lines)):
    if "----" in all_lines[e]:
        end = e
        break
    j=j+1


# Converts the atomic number to element symbol
atomic_number = {
    '1':'H', '2':'He', '3':'Li', '4':'Be', '5':'B', '6':'C', '7':'N', '8':'O', '9':'F', '10':'Ne',
    '11':'Na', '12':'Mg', '13':'Al', '14':'Si','15':'P','16':'S','17':'Cl','18':'Ar','19':'K',
    '20':'Ca'
    }
print(f'''
Number of geometry optimization steps: {i}
Number of atoms: {j}

Element           X            Y            Z''')

coordinates = []                          #Reads the coordinates data
elements = []
xyz_angs =[]
xyz_bohr =[]
for line in all_lines[start + 5 : end]:
    words = line.split()
    elements.append(atomic_number.get(words[1]))
    xyz_angs.append(words[3:])

import numpy as np                                    #converting angstroms to Bohrs

xyz_angs = np.array(xyz_angs,float)
xyz_bohr=list(xyz_angs/0.529177)

coordinates= list(zip(elements,xyz_bohr))
coordinates.sort(key=lambda coordinates: coordinates[0][0])  # sorts the same elements together


print(*coordinates, sep='\n')                                  #print the last Input Orientation table











