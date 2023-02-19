import numpy as np
import pandas as pd

undead = pd.read_csv("Undead.csv")
undead_groups = {}
num_undead = len(undead)

undead_names = undead['Name']

for i in range(num_undead):
    undead_groups[undead_names[i]] = undead.iloc[i,1:]

cont = True

while(cont):

    while True:
        print("Which Undead Are You Using? \n")
        for i in range(len(undead_names)):
            print(str(i) + ": " + str(undead_names[i]))
        try:
            current_ud = int(input("Input the Corresponding Number: "))
            
        except:
            print("\nPlease Input a Number Instead of a Character \n ")
            continue
            
        else:
            if(current_ud<num_undead):
                break
            else:
                print("\nPlease input a valid number from the given list \n")

    current_ud = undead.iloc[current_ud,:]
