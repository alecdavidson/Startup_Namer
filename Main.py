import random
import re
import sys
import flask


def get_random_line(rsv):
    file_h = open(rsv)
    limit = file_h.readline()
    limit = limit.replace('\n', '' )
    limit = int(limit)
    line = random.randint(0, limit - 1)
    
    for x in range(line):
        file_h.readline()
    phrase = file_h.readline()
    phrase = phrase.replace('\n', '')
    
    return(phrase)
	

def main():
	choice = random.randint(1,2)
	
	if choice == 1:
		flask.flash(get_random_line('Eng_Verb.txt') + " " + get_random_line('Eng_Noun.txt'))
		#print(get_random_line('Eng_Verb.txt') + " " + get_random_line('Eng_Noun.txt'))
	elif choice == 2:
		flask.flash(get_random_line('Advyrbs.txt'))
		#print(get_random_line('Advyrbs.txt'))
	else:
		flask.flash(get_random_line('Swahili.txt'))
		#print(get_random_line('Swahili.txt'))
		
#main()