#!/usr/local/bin/python3
# Assignment Two
# Exam Number: B210208 

# The purpose of this script is to allow the user to specify protein family and taxonomic group.
# Once specified, the script will analyse these sequences using relevalent programmes.

# Import All Relevant Modules
import os, sys, subprocess
import numpy as np
import re
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
	#Put the API_key into the bash.profile if not there already*
	#export NCBI_API_KEY=API_key
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
	#cmd3 = 'einfo -db  db'
	#subprocess.call(cmd3, shell=True)
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
	#cmd4 = 'esearch -db pubmed -query prot_fam  | efetch -format abstract'
	#subprocess.call(cmd4, shell=True)
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
	#cmd5 = 'esearch -db pubmed -query tax_gr | efetch -format abstract'
	#subprocess.call(cmd5, shell=True)
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


#Define the local python varaiables as OS environment variables
os.environ['pf'] = prot_fam
os.environ['tx_g'] = tax_gr
os.environ['db'] = db

# Ask user to specify an output file 
outputfile = input("What name would you like to call the resulting output file?")

# Define the output file as an OS environment variable 
os.environ['outputfile'] = outputfile

# Obtain the relevalent protein sequence data for the specified taxonomic group
cmd6 = 'wget -qO $outputfile "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=$db&term="$pf[PROT]+AND+$tx_g[ORGN]"&usehistory=y"'
subprocess.call(cmd6, shell=True)

# Obtain Query_key and Webenv from that command
with open("esearch.txt") as fd:
	for line in fd:
		m1= re.search(r'(<QueryKey>)(\w+)',line)
		m2= re.search(r'(<WebEnv>)(\w+)', line)
		if m1:
			query= m1.group(2)
			print(query)	
		if m2:
			webenv= m2.group(2)
			print(webenv)

#Define the local python variables as OS environment variables
os.environ['query'] = query
os.environ['webenv'] = webenv

# Ask user to specify an output file name
outputfile2 = input("What name would you like to call the resulting output file?")

# Define the output file as an OS environment variable 
os.environ['outputfile2'] = outputfile2

# Use efetch
cmd7 = 'wget -qO $outputfile2 "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=$db&query_key=$query&WebEnv=$webenv&rettype=fasta&retmode=text"'
subprocess.call(cmd7, shell=True)

# Would they like a summary of their data?
summary = input("Would you like a summary of the data downloaded? [Yes|No]").upper()

if summary=='YES':
	print("-----------------------------")
	print("Summary of the dowloaded data")
	print("-----------------------------")
	#Think of some way of displaying the data
	#Ask if they want to continue
elif summary=='NO':
	print("-----------------------------")
	print("Continuing with the programme...")
	print("-----------------------------")
else:
	print("----------------------------")
	print("Answer yes or no")
	print("Terminating the  programme")
	print("----------------------------")
	sys.exit()

# Would they like to trim their data?
trim_data= input("Would you like to filter sequences by a minimum and maximum length? [Yes|No]").upper()

# Could ask if pullseq is installed

if trim_data=="YES":
	min_l,max_l = input("What minimum and maximum length would you like to filter your sequences by? [Min|Max]").split()
	print("The minimum length is " + min_l + "the maximum length is " + max_l)
	os.environ["min_l"] = min_l
	os.environ["max_l"] = max_l
	cmd_c = 'echo $min_l'
	subprocess.call(cmd_c, shell=True)
	cmd_c2 = 'echo $max_l'
	subprocess.call(cmd_c2, shell=True)
	#Maybe ask if this is correct
	outputfile3 = input("What name would you like to call the resulting output file?")
	os.environ['outputfile3'] =outputfile3
	cmd8= 'pullseq -i $outputfile2  -m $min_l  -a $max_l > $outputfile3' 
	subprocess.call(cmd8, shell=True)
elif trim_data=="NO":
	print("----------------------------")
	print("Continuing with the programme")
	print("-----------------------------")
else:
	print("----------------------------")
	print("Answer yes or no")
	print("Terminating the programme")
	print("--------------------------")
	sys.exit() 
# Ask if they would like a summary of the sequences

# Ask what name they would like to give to the output file
outputfile4 = input("What name would you like to call the resulting output file?") 
os.environ['outputfile4'] =outputfile4
# Run Clustal
cmd9 = 'clustalo -i $outputfile3 -o $outputfile4 -t $db --outfmt msf  -v'
subprocess.call(cmd9, shell=True)
# Determine Level of Protein Conservation

# Plot the Level of Protein Conservation- display it and save it
cmd10 = 'plotcon -sformat msf $outputfile4  -graph x11'
cmd11  = ' plotcon -sformat msf plotcon.msf -graph ps'
subprocess.call(cmd10, shell=True)
subprocess.call(cmd11, shell=True)

# Ask if they would like to run a BLAST 

# Scan PROSITE database for any known motifs known to be associated with the subset of sequences

 

#while input("Do you have EDirect installed in this environment? [Yes/No]") == "Yes"
		


