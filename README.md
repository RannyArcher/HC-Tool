## THIS IS A HASHING AND CRACKING (TOOL ALL IN ONE)



#### MODES:
	crack :	this make you able to crack a hash using wordlist file or stdin program.
	hash:	this make you able to creat your own hash.


#### OPTIONS in crack:
	[-a/--algorithm]	it specifies what algorithm you want to use while cracking.
				put unknow in the value if you dont know.
				the unknow value will try all avaible algorithms.

	[-x/--hash]		this specifies what whash you want to crack.

	[-w/--wordlist]		this specifies what wordlist you want to use while cracking.
				you can sepecify a stdin program using hyphen or 'stdin'
				in the value.

	BE CAREFULL ALL VALUES ABOVE ARE REQUIRED IN THE CRACK MODE !



#### OPTIONS in hash :
	[-a/--algorithm]	it specifies your hash's algorithm.

	[-s/--string]		it specifies what string you want to hash it.
				be carefull char escape is required in the long string.

	BE CAREFULL ALL VALUE ABOVE ARE REQUIRED IN THE HASH MODE !



#### Available Algorithms:

	sha224		blake2s		sha3_384

	sha3_224	blake2b		sha3_512

	sha1		md5		sha384

	sha256		sha3_256	sha512


	BE CAREFULL IF YOU USE UNAVAILABLE ALGORITHM YOU'LL GET AN ERROR !



#### EXAMPLE for hash:
	``` ./hc_tool.py hash --string "YOUR_STRING" --algorithm md5 ```

#### EXMAPLE for crack:
	USING file:
		```./hc_tool.py crack --hash "YOUR_HASH" --algorithm md5 --wordlist FILE.TXT```

	USING stdin:
		```cat FILE.txt | ./h_too.py crack --hash "YOUR_HASH" -algorithm md5 --wordlist - ```

	YOU CAN USE stdin WORD INSTEAD THE HYPHEN IT WILL GIVE YOU THE SAME RESULT.
	AND YOU CAN USE OPTIONS LIKE THAT :
		-x	or	-hash		or	--hash
		-s	or	-string		or	--string
	AND SO ON.
