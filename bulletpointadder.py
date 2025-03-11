import pyperclip

text = pyperclip.paste()

#separate line and add stars

lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = "* " + lines[i]

text = "\n".join(lines)

newtext = pyperclip.copy(text)