#Print only uniqu elements in the list

#examples : 
#python keepOnlyUniq.py -l test test1 test test1

import argparse
import json

parser = argparse.ArgumentParser(description='Check the missing elements from the first list in the second list.')
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument("-d", "--debug", type=int, default=0,help="Debug mode")
args = parser.parse_args()

# To show the results of the given option to screen.
if args.debug:
	for _, value in parser.parse_args()._get_kwargs():
	    if value is not None:
	        print(value)
	print("\n**** list arguments ****")    
	print(args.list)

myset = set(args.list)

data = {}
data['result'] = list(myset)

print ("\nUniq elements in the list\n")
print (list(myset))
#print json.dumps(data)
