## THIS IS A HASHING AND CRACKING (TOOL ALL IN ONE)



#### MODES:
	__crack__ :	this make you able to crack a hash using wordlist file or stdin program.
	**hash**:	this make you able to creat your own hash.



#### OPTIONS in crack:
	__[-a/--algorithm]__	it specifies what algorithm you want to use while cracking.
				put unknow in the value if you dont know.
				the unknow value will try all avaible algorithms.

	__[-x/--hash]__		this specifies what whash you want to crack.

	__[-w/--wordlist]__		this specifies what wordlist you want to use while cracking.
				you can sepecify a stdin program using hyphen or 'stdin'
				in the value.

	__BE CAREFULL ALL VALUES ABOVE ARE REQUIRED IN THE CRACK MODE !__



#### OPTIONS in hash :
	__[-a/--algorithm]__	it specifies your hash's algorithm.

	__[-s/--string]__		it specifies what string you want to hash it.
				be carefull char escape is required in the long string.

	__BE CAREFULL ALL VALUE ABOVE ARE REQUIRED IN THE HASH MODE !__



#### Available Algorithms:

**	sha224		blake2s		sha3_384**

**	sha3_224	blake2b		sha3_512**

**	sha1		md5		sha384**

**	sha256		sha3_256	sha512**


	__BE CAREFULL IF YOU USE UNAVAILABLE ALGORITHM YOU'LL GET AN ERROR !__



#### EXAMPLE for hash:
	```./hc_tool.py hash --string "YOUR_STRING" --algorithm md5```

#### EXMAPLE for crack:
	__USING file:__
		```./hc_tool.py crack --hash "YOUR_HASH" --algorithm md5 --wordlist FILE.TXT```

	__USING stdin:__
		```cat FILE.txt | ./h_too.py crack --hash "YOUR_HASH" -algorithm md5 --wordlist - ```

	__YOU CAN USE stdin WORD INSTEAD THE HYPHEN IT WILL GIVE YOU THE SAME RESULT.__
	__AND YOU CAN USE OPTIONS LIKE THAT :__
__		-x	or	-hash		or	--hash__
__		-s	or	-string		or	--string__
__	AND SO ON.__



