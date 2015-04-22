#pdb parser
import re

outfile = open("defb28_parsed.pdb", "w")

#this is where we want to start inserting our "chain identifier"
pdb_index = 20
chain_length = 6

with open("defb28_chimera.pdb", "r") as fh:
	for line in fh:
		lst = line.split(" ")
		new_lst = []
		
		for i in lst:
			#an empty string evaluates to False
			if i: 
				new_lst.append(i)

		if len(new_lst) > 1:
			if re.search("ATOM", new_lst[0]):

				#parse the atom
				chain_identifier = new_lst[4]

				#mess around with this to add or remove a character... 
				new_line = line[:pdb_index] +" A"+str(1000+int(chain_identifier))+ line[pdb_index+chain_length+1:]
				#print new_line.strip()
				outfile.write(new_line)
			else:
				outfile.write(line)
		else:
			outfile.write(line)