def text_printer(texts, printedtxts):
	while texts:
		text = texts.pop()
		printedtxt.append(text)

def text_show(printedtxt):
		for text in printedtxt:
			print(f"The text message read: {text}")




text_message_list = ['hey how are you doing luke', 'hey can i see you tomorrow', 'you have a meeting at 15:00 luke',
'hey luke ill see you tomorrow at 12'
]
printedtxt = []

text_printer(text_message_list[:], printedtxt)
text_show(printedtxt)
print(text_message_list)