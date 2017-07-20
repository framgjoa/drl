#!/usr/bin/python
#Documentation Reference Layer main generator

import sys
import getopt

#Input format for DRL:
# Py drl schema predoc format

def main(argv):
   schemafile = ''
   predocfile = ''
   formatfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["sfile=","pfile=", "ffile="])
   except getopt.GetoptError:
      print 'drl.py -s <schemafile> -p <predocfile> -f <formatfile>'
      sys.exit(2)
   # print 'Options: ', opts
   # print 'Arguments: ', args
   (schemafile, predocfile, formatfile) = args
   for opt, arg in opts:
	   if opt == '-h':
	         print 'drl.py -s <schemafile> -p <predocfile> -f <formatfile>'
	         sys.exit()

	   # To-do: Add flags into options
'''
	   elif opt in ("-s", "--sfile"):
	       	schemafile = arg
	   elif opt in ("-p", "--pfile"):
	        predocfile = arg
	   elif opt in ("-f", "--ffile"):
	        formatfile = arg
'''

'''
   print 'Schema file is ', schemafile
   print 'Predoc file is ', predocfile
   print 'Format file is ', formatfile
'''

if __name__ == "__main__":
   main(sys.argv[1:])


