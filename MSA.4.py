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
print("##############################################################")
print("Analysis of Protein Families for Specific Taxonomic Groups")
print("WARNING: Entrez Direct (EDirect) is needed for this programme to run")
print("##############################################################") 

# Define a function for the rest of the script
def no_answer():
	print("-------------------------------")
	print("Please answer yes or no.") 
# Ask User whether they need to install the Entrez
# Might Later want to change the while loop 
answer = input("Do you have EDirect installed in this environment? [Yes/No]").upper()

# If the answer is yes then print "This programme will continue"
if answer=="YES":
	print("##########################################################################")
	print("Initiating this Analysis of Protein Families for Specific Taxonomic Groups")
	print("###########################################################################")
# If the answer is no then print "Edirect will now be downloaded to this system" (could ask if that is ok) and install programme
elif answer=="NO":
	print("################################################")
	print("EDirect will now be downloaded to this system")
	print("###############################################")
	# Install EDirect to the OS
	cmd = 'sh -c "$(wget -q ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh -O -)"'
	subprocess.call(cmd, shell=True)
	# Set the PATH for the current terminal session
	cmd_2 = 'export PATH=${PATH}:${HOME}/edirect'
	subprocess.call(cmd_2, shell=True)
else:
	
	print("-------------------------------------")
	print("Please answer yes or no.")
	print("Re-run the programme if you would like to run this analysis.")
	print("Programme terminating...")
	print("--------------------------------------")
	sys.exit()

#Ask user for NCBI account and API key 
print("------------------------------")
print("WARNING: An NCBI account and API key are required for this programme to be excuted")
print("Without an NCBI account and API key the programme may throw an error if there are too many requests")
print("------------------------------")

NCBI = input("Do you have an NCBI account and API key? [Yes/No]").upper()

# If the answer is yes then prompted for the email associated with the NCBI account and the API key
if NCBI=="YES":
	# Ask user for their email associated with their NCBI account and their API key
	email, API_key = input("Please enter your email associated with your NCBI account and API key").split()
	# Print the email associated with their NCBI account
	print("NCBI Email: " + email)
	# Print their API Key
	print("API Key: " + API_key)
	# Define the inputted API key as an OS variable
	os.environ["API_key"]= API_key

# If the answer is no the open up the NCBI website on the page where you set up an account and exit 
elif NCBI=="NO":
	print("Set up an NCBI account and API Key before excuting this programme again")
        # Print that the user must set up API key and that the programme will be terminated.
	print("--------------------------------------")
	print("Please set up NCBI Account and API key before re-running this programme again")
	print("Terminating this programme...")
	print("--------------------------------------")
	#Open up the URL for the NCBI website in default browser
        #Open a seperate browser tab for the URL (new=1)
        #Raise the window (autoraise=True)
	webbrowser.open('https://account.ncbi.nlm.nih.gov/signup/?back_url=https%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fmyncbi%2F', new=1, autoraise=True)
	# Exit the script
	sys.exit()

else: 
	print("--------------------------------------")
	print("Please answer yes or no")
	print("Terminating this programme...")        
	print("--------------------------------------")
	sys.exit()

# Ask your what database they want to use
db = input("What database would you like to use for the analysis?").lower()

# Make python variable a variable in BASH 
os.environ['db'] = db

#Ask if they want information on this database
ans_db = input("Would you like information on this database?").upper()

if ans_db=="YES":
	print("######################################")
	print("Information on the database selected")
	print("#######################################")
	
	# Use EInfo to gather information on the user-inputted database
	cmd3 = 'einfo -db $db > "$db".txt'
	subprocess.call(cmd3, shell=True)

	# Print contents of file to the screen
	file_db= open("%s.txt" % db)
	file_db_contents = file_db.read()
	print(file_db_contents)
	file_db.close()

	# Ask user if they wish to continue
	continue1 = input("Would you like to continue? [Yes|No]").upper()
	# Define a function to ask user if they wish to continue
	def continue_or_not(answer):
		if answer=="YES":
			print("------------------------------")
			print("Continuing the programme.....")
			print("-----------------------------")
		else:
			print("-----------------------------")
			print("Exiting the programme.....")
			print("-----------------------------")	
			sys.exit()
	continue_or_not(continue1)
elif ans_db=="NO":
	print("--------------------------------------")
	print("Continuing with the analysis.....")
	print("--------------------------------------")

else:
	print("---------------------------------------")
	print("Please answer yes or no")
	print("Termnating this programme..")
	print("---------------------------------------")
	sys.exit()


# Ask for the protein family that the user wants to analyse
prot_fam = input("What Protein Family would you like to analyse?").lower() 

os.environ['pf'] = prot_fam

# Ask user if they would like information on this protein family
ans_prot = input("Would you like information on this protein family? [Yes/No]").upper()

if ans_prot=="YES":
	print("###########################################")
	print("Information on the protein family selected")
	print("##########################################")
	
	# Add in lines to fetch the pubmed info- wiki and then ask of they want the pubmed ids/pubs
	cmd4 = 'esearch -db pubmed -query $pf  | efetch -format medline | gzip  > "$pf".gz'
	subprocess.call(cmd4, shell=True)
	
	# Display results in a user-controlled manner
	cmd_p= 'zmore "$pf".gz'
	subprocess.call(cmd_p, shell=True)
	
	# Ask user if they wish to continue
	continue2 = input("Would you like to continue? [Yes|No]").upper()
	continue_or_not(continue2)

elif ans_prot=="NO":
	print("---------------------------------")
	print("Continuing with the analysis...")
	print("---------------------------------")
else: 
	print("---------------------------------")
	print("Answer yes or no")
	print("Terminating this programme....")
	print("----------------------------------")
	sys.exit()

#Ask the user to specify a taxonomic group 
tax_gr= input("Please specify a taxonomic group you would like to study:").lower()

os.environ['tax_gr'] = tax_gr

ans_tax = input("Would you like information on this taxonomic group? [Yes/No]").upper()

if ans_tax=="YES":
	print("#################################################")
	print("Information on the taxonomic group selected")
	print("#################################################")

	# Add lines to fetch the info from pubmed- Pull wiki and then ask if want pubmed ids stored 
	cmd5 = 'esearch -db pubmed -query $tax_gr | efetch -format medline | gzip > "$tax_gr".gz'
	subprocess.call(cmd5, shell=True)
	
	# Display results in a user controlled manner
	cmd_t = 'zmore "$tax_gr".gz'
	subprocess.call(cmd_t, shell=True)

        # Ask user if they wish to continue
	continue3= input("Would you like to continue? [Yes|No]").upper()
	continue_or_not(continue3)

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

# Let the user know what step of the analysis they are on
print("######################################################################################################")
print("Using EDirect to retrieve the relevant information for the specified protein family and taxonomic group")
print("#######################################################################################################") 

# Ask user to specify an output file 
outputfile = input("What name would you like to call the resulting output file from esearch?")

# Define the output file as an OS environment variable 
os.environ['outputfile'] = outputfile

# Ask if they would like to inculde partial sequences 
fmt_esearch= input("Would you like to include partial sequences in this analysis? [Yes|No]").upper()

if fmt_esearch=="YES":
	# Obtain the relevalent protein sequence data for the specified taxonomic group
	cmd_e = 'wget -qO $outputfile "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=$db&api_key=$API_key&term="$pf[PROT]+AND+$tax_gr[ORGN]"&usehistory=y"'
	subprocess.call(cmd_e, shell=True)
elif fmt_esearch=="NO":
	# Obtain the relevalent protein sequence data for the specified taxonomic group
	cmd_e2='wget -qO $outputfile "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=$db&api_key=$API_key&term="$pf[PROT]+AND+$tax_gr[ORGN]+NOT+PARTIAL"&usehistory=y"'
	subprocess.call(cmd_e2, shell=True)
else:
	print("--------------------------")
	print("Please answer yes or no")
	print("Terminating the analysis..")
	print("--------------------------")
	sys.exit()

# Obtain Query_key and Webenv from that command
with open(outputfile) as fd:
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
outputfile2 = input("What name would you like to call the resulting output file from efetch? (.fa)")

# Define the output file as an OS environment variable 
os.environ['outputfile2'] = outputfile2

# Ask if they would like to limit the number of downloaded sequences- Recommend no more than 1000
lim= input("What would you like to limit the number of downloads to?\nReccomendation: restrict the number of downloads to no more than 1000\n")

# Define the lim variable as an OS variable
os.environ["lim"]= lim
 
# Use efetch to retrieve the fasta files with specified limit on the number of downloads
cmd7 = 'wget -qO $outputfile2 "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=$db&api_key=$API_key&query_key=$query&WebEnv=$webenv&rettype=fasta&retmode=text&retmax=$lim"'
subprocess.call(cmd7, shell=True)

# Would they like a summary of their data?
summary = input("Would you like a summary of the downloaded data? [Yes|No]").upper()

if summary=='YES':
	print("#############################################################")
	print("Summary of the dowloaded data")
	print("#############################################################")
	
	# Open file and print the number of sequences
	file_efetch = open(outputfile2, "r")
	file_contents_efetch = file_efetch.read()
	seq_count = file_contents_efetch.count(">")
	print("Sequence Count: " + seq_count)

	# Average length of the sequences
	
	# Number of protein sequences per species


	# Ask user to specify filename 
	outputfile_I = input("What name would you like to call the resulting output file? (.infoseq)")  
        # Define python variable as OS variable
	os.environ["outputfile_I"]= outputfile_I


	# Print Basic info about the file 
	cmd_i_d = 'infoseq $outputfile2 -nousa > $outputfile_I'
	subprocess.call("cmd_i_d", shell=True)

	# Print file contents to screen
	f_I= open(outputfile_I)
	fc_I= f_I.read()
	print(fc_I)
	f_I.close()

	#Ask if they want to continue
	continue4 = input("Would you like to continue? [Yes|No]").upper()
	continue_or_not(continue4)

elif summary=='NO':
	print("-----------------------------")
	print("Continuing with the programme...")
	print("-----------------------------")
else:
	print("----------------------------")
	print("Please answer yes or no")
	print("Terminating the analysis")
	print("----------------------------")
	sys.exit()

# Would they like to trim their data?
trim_data= input("Would you like to filter sequences by a minimum and maximum length? [Yes|No]").upper()

if trim_data=="YES":
	installed =  input("Do you have pullseq installed? [Yes|No]/n If not please refer to the user manual and the pullseq github repository").upper() 	

	min_l,max_l = input("What minimum and maximum length would you like to filter your sequences by? [Min|Max]").split()
	print("The minimum length is " + min_l + "the maximum length is " + max_l)
	os.environ["min_l"] = min_l
	os.environ["max_l"] = max_l
	#Maybe ask if this is correct
	outputfile3 = input("What name would you like to call the resulting output file from pullseq?")
	os.environ['outputfile3'] =outputfile3
	cmd8= 'pullseq -i $outputfile2  -m $min_l  -a $max_l > $outputfile3' 
	subprocess.call(cmd8, shell=True)
	# Ask if they would like a summary of the trimmed data
	summary2 = imput("Would you like a summary of the trimmed data? [Yes|No]").upper()
	if summary2=="YES":
		print("----------------------------------")
		print("Displaying the trimmed data....")
		print("------------------------------")
		#Think of some way to display the data
		file_trimmed = open(outputfile3, "r")
		file_trimmed_contents = file_trimmed.read()
		seq_count_t = file_trimmed.count(">")
		print(seq_count)
		cmd_i_t = 'infoseq $outputfile3 -nousa > "$db"_"$pf"_"$tax_gr"_trimmed.infoseq'
		subproces.call(cmd_i_t, shell=True)
		#Ask if they want to continue
		continue_t= input("Would you like to continue? [Yes|No]")
		if continue_t=="YES":
			print("-----------------------------")
			print("Continuing with the programme")
			print("-----------------------------")
			# Let the user know what step they are on of the analysis 
			print("#################################################")
			print("Generating the Sequence Alignments")
			print("#################################################") 
			# Ask what name they would like to give to the output file
			outputfile4= input("What name would you like to call the resulting output file from clustalo? [.msf]")
			os.environ['outputfile4']= outputfile4
			# Run Clustalo
			cmd_ct = 'clustalo -i $outputfile3 -o $outputfile4 --outfmt msf -v'
			subprocess.call(cmd_ct, shell=True)
		else:
			print("----------------------------")
			print("Terminating the programme...")
			print("-----------------------------")
			sys.exit()
	
	elif summary2=="NO":
		print("----------------------------")
		print("Continuing the programme....")
		print("----------------------------")
		# Let the user know what step they are on of the analysis
		print("###################################################")
		print("Generating the Sequence Alignments")
		print("####################################################")
		# Ask what name they would like to give to the output file
		outputfile4= input("What name would you like to call the resulting output file from clustalo? [.msf]")
		os.environ['outputfile4']= outputfile4
		# Run Clustalo
		cmd_t= 'clustalo -i $outputfile3 -o $outputfile4 --outfmt msf -v'
		subprocess.call(cmd_t, shell=True)
	else:
		print("----------------------------")
		print("Answer yes or no")
		print("Terminating the programme...")
		print("-----------------------------")
		sys.exit()
elif trim_data=="NO":
	print("----------------------------")
	print("Continuing with the programme")
	print("-----------------------------")
	# Let the user know what step of the analysis they are on
	print("##########################################################")
	print("Generating the Sequence Alignments")
	print("#########################################################")
	# Ask what name they would like to give to the output file
	outputfile4= input("What name would you like to call the resulting output file from clustalo? [.msf]")
	os.environ['outputfile4']= outputfile4
	# Run Clustalo
	cmd_nt = 'clustalo -i $outputfile2 - o $outputfile4 --outfmt msf -v'
	subprocess.call(cmd_nt, shell=True)
else:
	print("----------------------------")
	print("Answer yes or no")
	print("Terminating the programme")
	print("--------------------------")
	sys.exit()


# Ask the user if they would like a pairwise or multiple sequence alignment

# Information on the MSA
msa = input("Would you like to see information on these multiple sequence alignments? [Yes|No]").upper()

if msa=="YES":
	outputfile5 = input("What name would you like to call the resulting output file? (.infoalign)")
	# Define the python variable as an OS variable
	os.environ["outputfile5"] = outputfile5
	# Generate an infoalign file
	cmd_info = 'infoalign $outputfile4 -nousa -outfile $outputfile5'
	subprocess.call(cmd_info, shell=True)
	# Print the generated file to the screen
	f5 = open(outputfile5)
	fc5 = f.read()
	print(fc5)
	f.close()
	# Ask the user do they wish to continue
	continue5= input("Would you like to continue? [Yes|No]")
	continue_or_not(continue5)

elif msa=="NO":
	print("------------------------")
	print("Continuing the programme...")
	print("------------------------")
else:
	print("------------------------")
	print("Please Answer Yes or No")
	print("Terminating the programme....")
	print("------------------------")
	sys.exit()

# Show alignments 
show_a = input("Would you like to see and store the multiple sequence alignments in order of similarity? [Yes|No]").upper()

if show_a=="YES":
        outputfile6 = input("What name would you like to call the resulting output file? (.showalign)")
      	# Define python variable as OS variable
        os.environ["outputfile6"] = outputfile6
	# Generate MSA showalign in order of similarity
        cmd_s = 'showalign -order=s $outputfile4 -outfile $outputfile6'
        subprocess.call(cmd_s, shell=True)
	# Print the contents of the file to the screen
        f6 = open(outputfile6)
        fc6 = f.read()
        print(fc6)
        f6.close()
	# Ask the user if they wish to continue
	continue6= input("Would you like to continue? [Yes|No]").upper()
	continue_or_not(continue6)

elif show_a=="NO":
        print("------------------------")
        print("Continuing the programme...")
        print("------------------------")
else:
        print("------------------------")
        print("Please Answer Yes or No")
        print("Terminating the programme")
        print("------------------------")
        sys.exit()

# Could ask for similarities and dissimilarities 
show_s_d = input("Would you like to see and store the similarities AND/OR dissimilarities? [S|D|B|N]").upper()

if show_s_d=="S":
	print("--------------------------")
	print("Similarities in Multiple Sequence Alignments")
	print("--------------------------")

	# Similarities
	# User input for filename
	outputfile_S = input("What name would you like to call the resulting output file? (.showalign)")
	# Define python variable as OS variable
	os.environ["outputfile_S"]= outputfile_S
	# Run the showaign cmd for similarities
	cmd_s_d= 'showalign -show=s $outputfile4 -outfile $outputfile_S'
	subprocess.call(cmd_s_d, shell=True)
	# Print contents of the file generated to the screen 
	fs= open(outputfile_S)
	fcs= fs.read()
	print(fcs)
	fs.close()
	# Ask if they would like to continue
	continue7= input("Would you like to continue? [Yes|No]")
	continue_or_not(continue7)

if show_s_d=="D":
	print("---------------------------")
	print("Disimilarities in Multiple Sequence Alignment")
	print("---------------------------")

	# Disimilarities
	# User input for filename
	outputfile_D= input("What name would you like to call the resulting output file? (.showalign)")
	# Define the python variable as an OS variable
	os.environ["outputfile_D"]= outputfile_D
	# Run the showalign command for disimilarities
	cmd_d='showalign -show=d $outputfile4 -outfile $outputfile_D'
	subproces.call(cmd_d, shell=True)
	# Print the contents of the file generated to the screen
	fd= open(outputfile_D)        
	fcd= fd.read()
	print(fcd)
	fd.close()
	# Ask if they wish to continue
	continue8= input("Would you like to continue? [Yes|No]")
	continue_or_not(continue8)

if show_s_d=="B":
	print("---------------------------")
	print("Similarities and Disimilarities in Multiple Sequence Alignment")
	print("---------------------------")

	# Similarities
	# User input for filename 
	outputfile_S2= input("What name would you like to call the resulting output file? (.showalign)")
	# Define python variable as OS variable
	os.environ["outputfile_S2"]= outputfile_S2
	# Run the showalign command for similarity
	cmd_s_d2= 'showalign -show=s $outputfile4 -outfile $outputfile_S2'
	subprocess.call(cmd_s_d2, shell=True)
	# Print the contents of the file generated to the screen
	fs2= open(outputfile_S2)
	fcs2= fs2.read()
	print(fcs2)
	fs2.close()

	# Disimilarities
	# User input for filename
	outputfile_D2= input("What name would you like to call the resulting output file? (.showalign)")
	# Define the Python variable as an OS variable 
	os.environ["outputfile_D2"]= outputfile_D2
	# Run the showalign command for dissimilarities
	cmd_s_d3= 'showalign -show=d $outputfile4 -outfile $outputfile_D2'
	subprocess.call(cmd_S_d3, shell=True)
	# Print the contents of the file generated to the screen
	fd2= open(outputfile_D2)
	fcd2= fd2.read()
	print(fcd2)
	fd2.close()
	# Ask user if they wish to continue
	continue9= input("Would you like to continue? [Yes|No]")
	continue_or_not(continue9)

if show_s_d=="N":
	print("--------------------------")
	print("Continuing the programme...")
	print("--------------------------")
else:
	print("---------------------------")
	print("Please answer S|D|B|N")
	print("Terminating the programme....")
	print("----------------------------")
	sys.exit()
# Determine Level of Protein Conservation

# Plot the Level of Protein Conservation- display it and save it
win_size = input("What window size would you like to generate the plot with?\nPlease refer to the manual for a description of the winsize parameter")
os.environ["win_size"]= win_size
cmd10 = 'plotcon -winsize $win_size -sformat msf $outputfile4  -graph x11'
subprocess.call(cmd10, shell=True)

save_plot = input("Would you like to save this plot to an output file?[Yes|No]")
if save_plot=="YES":
	plot_name= input("What would you like to name the output file for this plot?")
	os.environ["plot_name"] = plot_name
	cmd11  = ' plotcon -winsize $win_size -sformat msf $outputfile4 -graph ps -goutfile $plot_name'
	subprocess.call(cmd11, shell=True)
else:
	print("------------------------")
	print("The Plotcon plot will not be saved to an output file...")
	print("------------------------")

# Parse the fasta file into individual fasta files
cmd_split = 'seqretsplit $outputfile2 seqoutall'
subprocess.call(cmd_split, shell=True)

# Scan PROSITE database for any known motifs known to be associated with the subset of sequences- not looping regex
# Ask user if they want to report simple patterns
pat = input("Would you like to include simple patterns in this search? [Yes|No]/nPlease refer to the mannual for description of simple patterns.").upper()

if pat=="YES":
	print("###########################################################################")
	print("Scanning PROSITE Database for any known motifs inculding simple patterns...")
	print("############################################################################")
	cmd12 = 'for FILE in *.fasta; do patmatmotifs -full -sequence $FILE  -sformat1 fasta  "$(basename "$FILE" .fasta)".patmatmotifs; done'
	subprocess.call(cmd12, shell=True)
elif pat=="NO": 
	print("###########################################################################")
	print("Scanning PROSITE Database for any nown motifs ignoring simple patterns....")
	print("###########################################################################")
	cmd13 ='for FILE in *.fasta; do patmatmotifs -noprune -sequence $FILE  -sformat1 fasta  "$(basename "$FILE" .fasta)".patmatmotifs; done'
	subprocess.call(cmd13, shell=True)

else:
	print("-----------------------------------------------------")
	print("Please answer yes or no")
	print("Terminating the programme....")
	print("-----------------------------------------------------")
	sys.exit()


