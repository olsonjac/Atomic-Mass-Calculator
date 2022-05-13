# Python code to demonstrate
# to split strings
# on uppercase letter

import re
def get_weight(ini_str):

# Dictionary of all elements matched with their atomic masses.
  elements_dict = {'H' : 1.008,'He' : 4.003, 'Li' : 6.941, 'Be' : 9.012,\
'B' : 10.811, 'C' : 12.011, 'N' : 14.007, 'O' : 15.999,\
'F' : 18.998, 'Ne' : 20.180, 'Na' : 22.990, 'Mg' : 24.305,\
'Al' : 26.982, 'Si' : 28.086, 'P' : 30.974, 'S' : 32.066,\
'Cl' : 35.453, 'Ar' : 39.948, 'K' : 39.098, 'Ca' : 40.078,\
'Sc' : 44.956, 'Ti' : 47.867, 'V' : 50.942, 'Cr' : 51.996,\
'Mn' : 54.938, 'Fe' : 55.845, 'Co' : 58.933, 'Ni' : 58.693,\
'Cu' : 63.546, 'Zn' : 65.38, 'Ga' : 69.723, 'Ge' : 72.631,\
'As' : 74.922, 'Se' : 78.971, 'Br' : 79.904, 'Kr' : 84.798,\
'Rb' : 84.468, 'Sr' : 87.62, 'Y' : 88.906, 'Zr' : 91.224,\
'Nb' : 92.906, 'Mo' : 95.95, 'Tc' : 98.907, 'Ru' : 101.07,\
'Rh' : 102.906, 'Pd' : 106.42, 'Ag' : 107.868, 'Cd' : 112.414,\
'In' : 114.818, 'Sn' : 118.711, 'Sb' : 121.760, 'Te' : 126.7,\
'I' : 126.904, 'Xe' : 131.294, 'Cs' : 132.905, 'Ba' : 137.328,\
'La' : 138.905, 'Ce' : 140.116, 'Pr' : 140.908, 'Nd' : 144.243,\
'Pm' : 144.913, 'Sm' : 150.36, 'Eu' : 151.964, 'Gd' : 157.25,\
'Tb' : 158.925, 'Dy': 162.500, 'Ho' : 164.930, 'Er' : 167.259,\
'Tm' : 168.934, 'Yb' : 173.055, 'Lu' : 174.967, 'Hf' : 178.49,\
'Ta' : 180.948, 'W' : 183.84, 'Re' : 186.207, 'Os' : 190.23,\
'Ir' : 192.217, 'Pt' : 195.085, 'Au' : 196.967, 'Hg' : 200.592,\
'Tl' : 204.383, 'Pb' : 207.2, 'Bi' : 208.980, 'Po' : 208.982,\
'At' : 209.987, 'Rn' : 222.081, 'Fr' : 223.020, 'Ra' : 226.025,\
'Ac' : 227.028, 'Th' : 232.038, 'Pa' : 231.036, 'U' : 238.029,\
'Np' : 237, 'Pu' : 244, 'Am' : 243, 'Cm' : 247, 'Bk' : 247,\
'Ct' : 251, 'Es' : 252, 'Fm' : 257, 'Md' : 258, 'No' : 259,\
'Lr' : 262, 'Rf' : 261, 'Db' : 262, 'Sg' : 266, 'Bh' : 264,\
'Hs' : 269, 'Mt' : 268, 'Ds' : 271, 'Rg' : 272, 'Cn' : 285,\
'Nh' : 284, 'Fl' : 289, 'Mc' : 288, 'Lv' : 292, 'Ts' : 294,\
'Og' : 294}

# Splitting on UpperCase using re
  res_list = []
  res_list = re.findall('[A-Z][^A-Z]*', ini_str)
  new_list = "".join(res_list)
  newer_list = list(new_list)
#this block removes the numbers from the list so tht it can be procssed with the elements dictionary
  for x in newer_list:
      if x.isdigit():
          newer_list.remove(x)
  trans_list = "".join(newer_list)  
  best_list = re.findall('[A-Z][^A-Z]*', trans_list)
  print(best_list)

  #This block takes the list and gets the atomic weights by comparing it against the dictionary and sets it to "weights"
  global weights
  weights = []
  for m in range(len(best_list)):
      if best_list[m]in elements_dict:
          weights.append((elements_dict[best_list[m]]))

  return(weights)  
