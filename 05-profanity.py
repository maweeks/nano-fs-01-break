import urllib

def read_text():
	quotes = open("/Users/MattBP/Documents/Nano-FS/lessons/nano-fs-01-lesson/movie_quotes.txt")
	file_contents = quotes.read()
	quotes.close()
	check_profanity(file_contents)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
	output = connection.read()
	connection.close()
	if "true" in output:
		print("You got profanity!!")
	elif "false" in output:
		print("S'all good, send the text.")
	else:
		print("Document scan failed, you may not be safe...")

read_text()