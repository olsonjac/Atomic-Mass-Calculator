from weight import get_weight
from coefficient import coefficient_gen
#sets the name of the compound being calculated
print("This will work as long at the subscript does not exceed 9 for any given element \n")
ini_str = input("enter the compound: ")
#sets the variables from the exterior functions
comp_d = coefficient_gen(ini_str)
weights = get_weight(ini_str)

def solve():
  final = []
  #iterates through weights list and checks for presence of index in weights in keys of the coefficient dictionary
  #Then multipies each list object by the key:value from the dictionary "comp_d" that matches it
  for x in weights:
    if weights.index(x) in comp_d.keys():
      final.append((x) * comp_d.get(weights.index(x)))
  
  print(f"{final} grams/mole")
  
solve()  
