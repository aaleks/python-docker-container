#example usage of the script this can be used for quick comparaison of two lists 

#examples : 
#python substractlist.py -l1 $(ls -al |awk '{print $9}') -l2 test tessst
#python substractlist.py -l1 "$(ls -al)" -l2 "$(ls -al)"  
#python substractlist.py -l1 $(ls -al |awk '{print $9}') -l2 $(ls -al |awk '{print $9}') -d=0
#python substractlist.py -l1 $(echo "test test2") -l2 $(echo "testl") -d=0

import argparse

#def check_contains(a, b):
#     diff = a - b
#     if not diff:
#         # All elements from a are present in b
#         return True
#     print('Some elements are missing: {}'.format(diff))
#     return False

parser = argparse.ArgumentParser(description='Check the missing elements from the first list in the second list.')
parser.add_argument('-l1','--list-one', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument('-l2','--list-two', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument("-d", "--debug", type=int, default=0,help="Debug mode")
args = parser.parse_args()

# To show the results of the given option to screen.
if args.debug:
	for _, value in parser.parse_args()._get_kwargs():
	    if value is not None:
	        print(value)
	print("\n**** list arguments ****")    
	print(args.list_one)
	print(args.list_two)

print ("\nList 1 - List 2")
print list(set(set(args.list_one) - set(args.list_two)))

print ("\nThe elements that are present in the second AND not in the first list :")
print list(set(set(args.list_two) - set(args.list_one)))
