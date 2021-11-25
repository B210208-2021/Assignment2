#!/usr/local/bin/python3
# Assignment Two
# Exam Number: B210208 

# The purpose of this script is to allow the user to specify protein family and taxonomic group.
# Once specified, the script will analyse these sequences using relevalent programmes.

# Import All Relevant Modules
import os, sys, subprocess
import numpy as np

# Print to the screen that Entrez Direct is needed for this proramme to work 
print("---------------------------------------------------------")
print("Warning!!!")
print("Entrez Direct (EDirect) is needed for this programme to run!!!")
print("---------------------------------------------------------") 

# Ask User whether they need to install the Entrez
# Might Later want to change the while loop 
answer = input("Do you have EDirect installed in this environment? [Yes/No]").upper()

# If the answer is yes then print "This programme will continue"
if answer=="YES":
	print("--------------------")
	print("This programme will continue")
	print("--------------------")
# If the answer is no then print "Edirect will now be downloaded to this system" (could ask if that is ok) and install programme
elif answer=="NO":
	print("--------------------")
	print("EDirect will now be downloaded to this system")
	print("This will download a number of scripts and several precoiled prgrams")
	print("These will be downloaded into an edirect folder in your home directory")
	print("It may print an additional command for updating the PATH environment variable in your configuration file")
	print("Answer y and press the Return key if you want it run.")
	print("If the PATH is already set correctly, or if you prefer to make any editing changes manually, just press Return.")
	print("--------------------")
	cmd = 'sh -c "$(wget -q ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh -O -)"'
	subprocess.call(cmd, shell=True)
	cmd_2 = 'export PATH=${PATH}:${HOME}/edirect'
	subprocess.call(cmd_2, shell=True)
else:
	print("This prompt requires a Yes or No answer!!")


#while input("Do you have EDirect installed in this environment? [Yes/No]") == "Yes"
		


