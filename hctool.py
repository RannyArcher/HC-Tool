#!/bin/python3
from sys import argv, stderr, stdin
from hashlib import *
from os import path

options = argv
available_algorithms = ['sha224','blake2s','sha3_384','sha3_224','blake2b','sha3_512','sha1','md5','sha384','sha256','sha3_256','sha512']


def hctool_usage():
    print("""Usage:     hctool [MODE] [OPTIONS]""")




def hashing(string, hash_algorithm):
    hash_algorithm = hash_algorithm.lower()
    if hash_algorithm in available_algorithms:
        if hash_algorithm == 'md5':
            print(md5(string.encode("utf-8")).hexdigest())
            exit()
        elif hash_algorithm == 'sha1':
            print(sha1(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha224':
            print(sha224(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'blake2s':
            print(blake2s(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha3_384':
            print(sha3_384(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha3_224':
            print(sha3_224(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'blake2b':
            print(blake2b(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha3_512':
            print(sha3_512(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha384':
            print(sha384(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha256':
            print(sha256(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha3_256':
            print(sha3_256(string.encode('utf-8')).hexdigest())
            exit()
        elif hash_algorithm == 'sha512':
            print(sha512(string.encode('utf-8')).hexdigest())
            exit()
    else:
        print('[!] Unavailable Algorithm.', file=stderr)


def hctool_help():
    print("""Usage: hctool [MODE] [OPTIONS]
                            hash  [-s/--string] [-a/--algorithm] 
                            crack [-w/--wordlist] [-x/--hash] [-a/--algorithm]
                            list
                            help / [-h/--help]
    
Modes:
        help                show help and usage.
        hash                hashing mode (hash a string).
        crack               cracking mode (crack a hash).
        list                list all available algorithms.


Options:
        MODE                select which mode (hash, crack, list, help), read the Modes above.
        -s/--string         this option for hash mode, specify the string which you want to hash it.
        -x/--hash           this option for crack mode, specify the hash which you want to crack. 
            
                             __in hash mode___ specify which algorithm you want to hash with it.
        -a/--algorithm      |
                            |__in crack mode__ specify which algorithm to crack hash using it (put `all` if you dont know).
            
        -w/--wordlist       this option for crack mode, specify wordlist filename or put `-` or `stdin` for stdin.


Examples:
        Hashing :   hctool hash -a md5 -s \"hello\"
                    this will hash the `hello` string to be like that (5d41402abc4b2a76b9719d911017c592).
        
        Cracking :  EX1:    hctool crack -a md5 -x \"5d41402abc4b2a76b9719d911017c592\" -w wordlist.txt
                            this will try crack this hash `5d41402abc4b2a76b9719d911017c592` using every line
                            in wordlist.txt with md5 hashing for every line.

                    EX2:    hctool crack -a all -x \"5d41402abc4b2a76b9719d911017c592\" -w wordlist.txt
                            it's like before but this will try to crack the hash using every line in wordlist.txt
                            with all available algorithms.

Note:              for hashing mode, if the string includes spaces you need to put the string between quotes `'`
                   or double quotes `\"`, else the hctool will note read all of the string!
                   and if the string includes quote(s) `'` put it between double quotes `"` and also
                   if the string includes double quotes `"` put it between quotes `'`.
""")


def list_algos():
    for i in available_algorithms:
        print(i, end=' | ')
    print("")
    exit()


def cracking(user_hash, hash_algorithm, wordlist) :
    hash_algorithm = hash_algorithm.lower()
    if hash_algorithm in available_algorithms:
        if (wordlist == '-') or (wordlist == 'stdin') or (wordlist == 'STDIN'):
            print('')
            for word in stdin :
                word = word.replace('\n', '')
                print(f"[!] Trying [{word}]", end='\r')
                if hash_algorithm == 'md5':
                    virtual = md5(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha1':
                    virtual = sha1(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha224':
                    virtual = sha224(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'blake2s':
                    virtual = blake2s(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha3_384':
                    virtual = sha3_384(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha3_224':
                    virtual = sha3_224(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'blake2b':
                    virtual = blake2b(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha3_512':
                    virtual = sha3_512(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha384':
                    virtual = sha384(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha256':
                    virtual = sha256(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha3_256':
                    virtual = sha3_256(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass
                elif hash_algorithm == 'sha512':
                    virtual = sha512(word.encode("utf-8")).hexdigest()
                    if virtual == user_hash:
                        print('')
                        print(f"[+] Cracked: {word}")
                        exit()
                    else:
                        pass

            print('')
            print("[-] Sorry We can't crack this hash.")
            exit()


        else:
            if path.exists(wordlist):
                wordlist = open(wordlist, 'r')
                for word in wordlist :
                    word = word.replace('\n', '')
                    print(f"[!] Trying [{word}]", end='\r')
                    if hash_algorithm == 'md5':
                        virtual = md5(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha1':
                        virtual = sha1(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha224':
                        virtual = sha224(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'blake2s':
                        virtual = blake2s(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha3_384':
                        virtual = sha3_384(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha3_224':
                        virtual = sha3_224(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass

                    elif hash_algorithm == 'blake2b':
                        virtual = blake2b(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha3_512':
                        virtual = sha3_512(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha384':
                        virtual = sha384(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha256':
                        virtual = sha256(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha3_256':
                        virtual = sha3_256(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                    elif hash_algorithm == 'sha512':
                        virtual = sha512(word.encode("utf-8")).hexdigest()
                        if virtual == user_hash:
                            print('')
                            print(f"[+] Cracked: {word}")
                            exit()
                        else:
                            pass
                print('')
                print("[-] Sorry We can't crack this hash.")
                exit()
                

    elif hash_algorithm == 'all':
        if wordlist == '-' or wordlist == 'stdin' or wordlist == 'STDIN' :
            print('')
            for word in stdin:
                word = word.replace('\n', '')
                print(f'[!] Trying [{word}]', end='\r')
                if md5(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was md5.')
                    exit()
                elif sha224(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha224.')
                    exit()

                elif blake2s(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was blake2s.')
                    exit()

                elif sha3_384(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_384.')
                    exit()

                elif sha3_224(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_224.')
                    exit()

                elif blake2b(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was blake2b.')
                    exit()

                elif sha3_512(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')                    
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_512.')
                    exit()

                elif sha1(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha1.')
                    exit()

                elif md5(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was md5.')
                    exit()

                elif sha384(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha384.')
                    exit()

                elif sha256(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha256.')
                    exit()

                elif sha3_256(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_256.')
                    exit()

                elif sha512(word.encode('utf-8')).hexdigest() == user_hash:
                    print('')
                    print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha512.')
                    exit()
                else:
                    pass
            print('[!] Sorry We can\'t crack this hash.', file=stderr)
            exit()
                ######
        else:
            if path.exists(wordlist):
                wordlist = open(wordlist, 'r')
                for word in wordlist :
                    word = word.replace('\n', '')
                    print(f"[!] Trying [{word}]", end='\r')
                    if md5(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was md5.')
                        exit()
                    elif sha224(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha224.')
                        exit()

                    elif blake2s(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was blake2s.')
                        exit()

                    elif sha3_384(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_384.')
                        exit()

                    elif sha3_224(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_224.')
                        exit()

                    elif blake2b(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was blake2b.')
                        exit()

                    elif sha3_512(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')                    
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_512.')
                        exit()

                    elif sha1(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha1.')
                        exit()

                    elif md5(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was md5.')
                        exit()

                    elif sha384(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha384.')
                        exit()

                    elif sha256(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha256.')
                        exit()

                    elif sha3_256(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha3_256.')
                        exit()

                    elif sha512(word.encode('utf-8')).hexdigest() == user_hash:
                        print('')
                        print(f'[+] Cracked: {word}\n[+] Hash Algorithm was sha512.')
                        exit()
                    else:
                        pass
                print('[!] Sorry We can\'t crack this hash.', file=stderr)
                exit()

    else :
        print("[!] Unvailable Algorithm.", file=stderr)
        exit()


if len(options) != 1:
    options[1] = options[1].lower()
    if ('hash' in options) or ('list' in options) or ('crack' in options):
        if options[1] == "hash":
            if (('-s' in options) or ('--string' in options)) and (('-a' in options) or ('--algorithm' in options)):
                if '-s' in options and '-a' in options:
                    hashing(options[options.index('-s') + 1 ], options[options.index('-a') + 1 ])
                elif '--string' in options and '--algorithm' in options:
                    hashing(options[options.index('--string') + 1 ], options[options.index('--algorithm') + 1 ])
                elif '-s' in options and '--algorithm' in options:
                    hashing(options[options.index('-s') + 1 ], options[options.index('--algorithm') + 1 ])
                elif '--string' in options and '-a' in options:
                    hashing(options[options.index('--string') + 1 ], options[options.index('-a') + 1 ])
            else:
                print("[!] Please add all hash options with their values.", file=stderr)
                exit()



        elif options[1] == "crack":
            if (('-w' in options) or ('--wordlist' in options)) and (('-x' in options) or ('--hash' in options)) and (('-a' in options) or ('--algorithm' in options)):
                if ('-x' in options) and ('-w' in options) and ('-a' in options):
                    cracking(options[options.index('-x') + 1 ], options[options.index('-a') + 1 ], options[options.index('-w') + 1 ])
                elif ('--hash' in options) and ('--wordlist' in options) and ('--algorithm' in options):
                    cracking(options[options.index('--hash') + 1 ], options[options.index('--algorithm') + 1 ], options[options.index('--wordlist') + 1 ])
                elif ('--hash' in options) and ('--wordlist' in options) and ('-a' in options):
                    cracking(options[options.index('--hash') + 1 ], options[options.index('-a') + 1 ], options[options.index('--wordlist') + 1 ])
                elif ('-a' in options) and ('-x' in options) and ('--wordlist' in options):
                    cracking(options[options.index('-x') + 1 ], options[options.index('-a') + 1 ], options[options.index('--wordlist') + 1 ])
                elif ('-a' in options) and ('--hash' in options) and ('-w' in options):
                    cracking(options[options.index('--hash') + 1 ], options[options.index('-a') + 1 ], options[options.index('-w') + 1 ])
                elif ('--algorithm' in options) and ('-x' in options) and ('-w' in options):
                    cracking(options[options.index('-x') + 1 ], options[options.index('--algorithm')], options[options.index('-w') + 1 ])
                elif ('--algorithm' in options) and ('--hash' in options) and ('-w' in options):
                    cracking(options[options.index('--hash') + 1 ], options[options.index('--algorithm') + 1 ], options[options.index('-w') + 1])
                elif ('--algorithm' in options) and ('-x' in options) and ('--wordlist' in options):
                    cracking(options[options.index('-x') + 1 ], options[options.index('--algorithm') + 1 ], options[options.index('--wordlist') + 1 ])
            else :
                print("[!] Please add all crack options with their values.", file=stderr)
                exit()
        elif options[1] == 'list':
            list_algos()



    elif (options[1] == 'help') or ('-h' in options) or ('-help' in options) or ('--help' in options) :
        hctool_help()
    else :
        print(f"[!] Sorry there is no {options[1]} mode.", file=stderr)
        exit()


else :
    hctool_usage()
    exit()
