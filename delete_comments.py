#!/usr/bin/env python

"""
	This script will delete all of the template comments from an XCode project.
	It will remove all of the comments from the top of *m *h and *.mm. It will
	traverse the <DIRECTORY> searching for these files, then remove the comments.
	
	By Joe Misiti joseph.misiti@gmail.com
"""

import os
import glob
import sys

global pathstocheck
pathstocheck = []

def get_file_list(directory):
	global pathstocheck
	files = glob.glob(directory + '/*')
	for file in files:
		if os.path.isdir(file):
			pathstocheck.append(file)
			get_file_list(file)

def get_source_files(paths):
	files = [];
	for path in paths:
		localfiles = glob.glob(path + '/*m')
		if len(localfiles) > 0:
			for f in localfiles:
				files.append(f)
		localfiles = glob.glob(path + '/*h')
		if len(localfiles) > 0:     		
			for f in localfiles:
				files.append(f)
		localfiles = glob.glob(path + '/*mm')
		if len(localfiles) > 0:
			for f in localfiles:
				files.append(f)
					
	return files
				
def delete_all_comments(topdir):
	get_file_list(topdir)
	files = get_source_files(pathstocheck)
	for file in files:
		print "removing comments from: ", file
		fin = open(file,'r')
		lines = fin.readlines()
		fin.close()
		
		fout = open(file,'w')
		indx = 0
		for line in lines:
			if indx < 7 and "//" in line:
				indx += 1
				continue
			fout.write( line )
		fout.close()
			
	
if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "usage: delete_comments.py <DIRECTORY>"
	else:
		delete_all_comments(sys.argv[1])