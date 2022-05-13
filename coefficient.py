# Python code to demonstrate
# to split strings
# on uppercase letter

import re
def coefficient_gen(ini_str):  
# Printing Initial string
  #print ("Initial String", ini_str)

  global comp_d
  comp_d = {} 
# Splitting on UpperCase using re
  res_list = []
  res_list = re.findall('[A-Z][^A-Z]*', ini_str)
  #print(res_list)
 #this block assigns keys as indexes and coefficients as values in a dictionary. if no coefficient(1 is assigned) 
  for x in res_list:
      if x.isalpha():
        comp_d[res_list.index(x)] = 1
      for y in "".join(x):
          if y.isdigit():
              comp_d[res_list.index(x)] = int(y)
  return((comp_d))

