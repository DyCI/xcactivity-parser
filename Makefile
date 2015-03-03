all: test


test:
	py.test ./tests/*

testpython3:
	/usr/local/bin/python3 /usr/local/bin/py.test ./tests/* 

testvv:
	py.test ./tests/* -vv

testwithspaces:	
	py.test -k "with_spaces" -vv ./tests/*

