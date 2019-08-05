def Input(text):
	try: 
		return int(input(text))
	except:
		print("Numbers Only! Try again.")
		return Input(text)
def con(brd):
	text = ""
	for unit in brd[0]:
		text += "-"
	text += "\n"
	for row in brd:
		for unit in row:
			text += str(unit)
		text += "|\n"
	for unit in brd[0]:
		text += "-"
	return text