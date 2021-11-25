#!/usr/local/bin/python3
# Assignment Two
# Exam Number: B210208 

# The purpose of this script is to allow the user to specify protein family and taxonomic group.
# Once specified, the script will analyse these sequences using relevalent programmes.

# Import All Relevant Modules
import os, sys, subprocess
import numpy as np
import webbrowser

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
	print("-------------------------------------")
	print("Yes or No answer")
	print("Re-run the programme")
	print("Programme terminating...")
	print("--------------------------------------")
	sys.exit()

#Ask user for NCBI account and API key 
print("------------------------------")
print("An NCBI account and API key are required for this programme to be excuted well")
print("Without an NCBI account and API key the programme may throw an error if there are too many requests")
print("------------------------------")

NCBI = input("Do you have an NCBI account and API key? [Yes/No]").upper()

# If the answer is yes then prompted for the email associated with the NCBI account and the API key
if NCBI=="YES":
	email, API_key = input("Please enter your email associated with your NCBI account and API key").split()
	print("NCBI Email: " + email)
	print("API Key: " + API_key)
elif NCBI=="NO":
	print("Set up an NCBI account and API Key before excuting this programme again")
        #Open up the URL for the NCBI website in default browser
	#Open a seperate browser tab for the URL (new=1)
	#Raise the window (autoraise=True) 
	webbrowser.open('https://account.ncbi.nlm.nih.gov/signup/?back_url=https%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fmyncbi%2F',new=1, autoraise=True)
        #Exit Programme
	print("--------------------------------------")
	print("Please set up NCBI Account and API key")
	print("Programme terminating...")
	print("--------------------------------------")
	sys.exit()
else: 
	print("--------------------------------------")
	print("Yes or No answer!!")
	print("Please set up NCBI Account and API key OR re-run the programme")
	print("Programme termnating...")        
	print("--------------------------------------")
	sys.exit()

# Ask your what database they want to use
db = input("What database would you like to use for the analysis?").lower()

#Ask if they want information on this database
ans_db = input("Would you like information on this database?").upper()

if ans_db=="YES":
	print("--------------------------------------")
	print("Information on database selected")
	print("--------------------------------------")
	#Need to fix this!!!
	cmd_3 = 'einfo -db  db'
	subprocess.call(cmd_3, shell=True)
elif ans_db=="NO":
	print("--------------------------------------")
	print("Continuing the programme.....")
	print("--------------------------------------")
else:
	print("---------------------------------------")
	print("Answer yes or no")
	print("Programme terminated...")
	print("---------------------------------------")
	sys.exit()

# Ask user if they wish to continue

# Ask for the protein family that the user wants to analyse
prot_fam = input("What Protein Family would you like to analyse?") 

# Ask user if they would like information on this protein family
ans_prot = input("Would you like information on this protein family? [Yes/No]").upper()

if ans_prot=="YES":
	print("----------------------------------")
	print("Information on the protein family selected")
	print("-----------------------------------")
	# Add in lines to fetch the pubmed info
elif ans_prot=="NO":
	print("---------------------------------")
	print("Continuing the programme...")
	print("---------------------------------")
else: 
	print("---------------------------------")
	print("Answer yes or no")
	print("Programme terminated....")
	print("----------------------------------")
	sys.exit()

# Ask if they want to continue

#Ask the user to specify a taxonomic group 
tax_gr= input("Please specify a taxonomic group you would like to study:").lower()

ans_tax = input("Would you like information on this taxonomic group? [Yes/No]").upper()

if ans_tax=="YES":
	print("---------------------------------")
	print("Information on the taxonomic group selected")
	print("---------------------------------")
	# Add lines to fetch the info from pubmed
elif ans_tax=="NO":
	print("---------------------------------")
	print("Continuing the programme...")
	print("---------------------------------")
else:
	print("---------------------------------")
	print("Answer yes or no")
	print("Programme terminated....")
	print("------------------------")
	sys.exit()

# Ask if they want to continue       



#while input("Do you have EDirect installed in this environment? [Yes/No]") == "Yes"
		


