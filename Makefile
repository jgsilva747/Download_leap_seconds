# -------------------------------------------------------------------------
# type "make" command in the Linux terminal to retrieve data from celestrak
# -------------------------------------------------------------------------

all:
	# this line gives the file permission to execute
	chmod +x download.sh
	# run the bash file to retrieve files
	./download.sh
	# Generate files with useful information
	python3 read_files.py
	# Type "make clean" to delete generated files.

make clean:
	rm -f *.dat
