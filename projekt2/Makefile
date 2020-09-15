AUTOR = xskuto00
CC = python3
	
decipher : decipher.py
	@$(CC) decipher.py "$(publicKey)"
	
clean:
	rm -f *.tgz *~

pack:
	tar -cvzf $(AUTOR).tgz decipher.py Makefile
	
unpack:
	tar -xzvf $(AUTOR).tgz