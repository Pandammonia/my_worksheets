def count_words(filename):

	"""count number of words in a file"""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has {num_words} words.")

filename = ['New Text Document.txt', 'pi.txt', 'pi_million_digits.txt'] #this would stop the function at "wert.txt and rturn the error
# unless we use pass in the except block
for file in filename:
	count_words(file)