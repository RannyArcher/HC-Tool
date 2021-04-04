#!/bin/python3
from sys import argv, stderr, stdin
from hashlib import *
from os import path

is_file = path.exists
options = argv
modes = ('hash', 'crack')
algorithms = [sha224, blake2s, sha3_384, sha3_224, blake2b, sha3_512, sha1, md5, sha384, sha256, sha3_256, sha512]



def show_summary():
	print('./hc_tool.py [mode] [option] [value] ...\n\nrun hc_tool.py with a help option [-h/-help/--help] to read more about the tool.')


def show_full_help():
	print('MODES:\n\tcrack:\tthis make you able to crack a hash using wordlist file or stdin program.\n\thash:\tthis make you able to creat your own hash.\n\n\n\nOPTIONS in crack:\n\t[-a/--algorithm]\tit specifies what algorithm you want to use while cracking.\n\t\t\t\tput unknow in the value if you dont know.\n\t\t\t\tthe unknow value will try all avaible algorithms.\n\n\t[-x/--hash]\t\tthis specifies what whash you want to crack.\n\n\t[-w/--wordlist]\t\tthis specifies what wordlist you want to use while cracking.\n\t\t\t\tyou can sepecify a stdin program using hyphen or \'stdin\'\n\t\t\t\tin the value.\n\n\tBE CAREFULL ALL VALUES ABOVE ARE REQUIRED IN THE CRACK MODE !\n\n\n\nOPTIONS in hash :\n\t[-a/--algorithm]\tit specifies your hash\'s algorithm.\n\n\t[-s/--string]\t\tit specifies what string you want to hash it.\n\t\t\t\tbe carefull char escape is required in the long string.\n\n\tBE CAREFULL ALL VALUE ABOVE ARE REQUIRED IN THE HASH MODE !\n\n\n\nAvailable Algorithms:\n\n\tsha224\t\tblake2s\t\tsha3_384\n\n\tsha3_224\tblake2b\t\tsha3_512\n\n\tsha1\t\tmd5\t\tsha384\n\n\tsha256\t\tsha3_256\tsha512\n\n\n\tBE CAREFULL IF YOU USE UNAVAILABLE ALGORITHM YOU\'LL GET AN ERROR !\n\n\n\nEXAMPLE for hash:\n\t./hc_tool.py hash --string "YOUR_STRING" --algorithm md5\n\nEXMAPLE for crack:\n\tUSING file:\n\t\t./hc_tool.py crack --hash "YOUR_HASH" --algorithm md5 --wordlist FILE.TXT\n\n\tUSING stdin:\n\t\tcat FILE.txt | ./h_too.py crack --hash "YOUR_HASH" -algorithm md5 --wordlist -\n\n\tYOU CAN USE stdin WORD INSTEAD THE HYPHEN IT WILL GIVE YOU THE SAME RESULT.\n\tAND YOU CAN USE OPTIONS LIKE THAT :\n\t\t-x\tor\t-hash\t\tor\t--hash\n\t\t-s\tor\t-string\t\tor\t--string\n\tAND SO ON.\n\n\n')
	exit()


def get_value_of(*args):
	for arg in args:
		if arg in options:
			try:
				return options[options.index(arg) + 1]
			except IndexError:
				return ''

	return False


def check_value_of(value, option_name, help_options):
	if value or value == '':
		return value
	else:
		print(option_name ,'Option/Value is Needed.', help_options, file=stderr)
		exit()


def hash_of(string, algorithm):
	try:
		print(eval(algorithm)(string.encode("utf-8")).hexdigest())
	except NameError:
		print("[!] Unavailable Algorithm.", file=stderr)
	exit()


def crack_of(Hash, algorithm_of_hash, wordlist):
	if algorithm_of_hash.lower() != 'unknown':
		for word in wordlist:
			word = word.replace("\n","")
			print(f"[-] Trying [{word}]", end='\r')
			if Hash == eval(algorithm_of_hash)(word.encode("utf-8")).hexdigest():
				print(f"\n[+] Cracked: {word}")
				exit()
		print("\n[!] Sorry We Can't Crack This Hash.")
		exit()

	else:
		for word in wordlist:
			word = word.replace("\n","")
			print(f"[-] Trying [{word}]", end='\r')
			for algorithm in algorithms:
				if Hash == algorithm(word.encode("utf-8")).hexdigest():
					print(f"\n[+] Cracked: {word}\n[+] Using: {algorithm.__name__}")
					exit()














if len(options) > 1 and options[1] in modes:
	mode = options[1].lower()

	if mode == modes[0]:

		string = check_value_of(get_value_of('-s','-string','--string'),'String','[-s/--string]')
		algorithm = check_value_of(get_value_of('-a','-algorithm','--algorithm'),'Algorithm','[-a/--algorithm]')

		hash_of(string, algorithm)






	elif mode == modes[1]:
		wordlist = check_value_of(get_value_of('-w','-wordlist','--wordlist'),'Wordlist','[-w/--wordlist]')
		Hash = check_value_of(get_value_of('-x','-hash', '--hash'),'Hash','[-x/--hash]')
		algorithm_of_hash = check_value_of(get_value_of('-a','-algorithm','--algorithm'),'Algorithm of Hash','[-a/--algorithm]')

		if wordlist == '-' or wordlist.lower() == 'stdin':
			wordlist = stdin
		elif not is_file(wordlist):
			print('[!] File is Not Exists.')
			exit()

		crack_of(Hash, algorithm_of_hash, wordlist)



elif len(options) == 1:
	show_summary()



elif '-h' in options or '--help' in options or '-help' in options:
	show_full_help()



elif options[1] not in modes:
	print('[!] Unavailable Mode.', file=stderr)
