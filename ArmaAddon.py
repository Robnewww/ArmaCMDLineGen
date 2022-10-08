import os

#if results file exists, its deleted
if os.path.exists("output/result.txt"):
	os.remove("output/result.txt")

# For printing which mod its on
count = 0

# Enables colour
os.system('color')

#ascii letters to remove
Disallowed = "#%&{}<>*?/$!:+`|='" 

#stores whole list of mods
total = []

#finds html ignoring desktop.ini
path = list(set(os.listdir('./input/')) - {'desktop.ini'} - {'.gitignore'})
print(f"\u001b[32mModlist found in: \u001b[1m{path}\u001b[0m")

try:
	#sets html path
	src_dir = './input/'+path[0]
	
	#sets html name to Mods.txt
	os.rename(src_dir, './input/Mods.txt')


	with open('./input/Mods.txt') as myfile:
		print('\u001b[32mStarting...\u001b[0m')
		
		for line in myfile:
			#line stores the whole text of line being read
			if '<td data-type="DisplayName">' in line:
				print(f"\u001b[35m{count}...\u001b[0m", end='' )
				count += 1
				line = line.replace('&amp;', "&")
				line = line.replace('</td>', ";")
				line = line.replace('@', "")
				line = line.replace('<td data-type="DisplayName">', "@")
				for character in Disallowed:
					line = line.replace(character, "")
				line = line.replace('"', '') # special for " because cant be in variable Disallowed
				#translate removes disallowed characters
				line = line.replace('          ', "")
				line = line.replace('\n', "")
				total.append(line)
				#total is a list of lines that have a mod name
	
	with open("output/result.txt", "a", newline='') as myfile2:
		myfile2.writelines(total)
	#writes total to a file, each element is wrote on the same line
	
	print("\n\u001b[1mOutput Created.\u001b[0m")
	os.rename('./input/Mods.txt', './input/Modslist.html')
	os.system("notepad.exe ./output/result.txt")
	input("Press any key to close...")
	
except:
	print("\u001b[31mException occured, did you put the html in '/input' ?\u001b[0m")
	input("Press any key to close...")
	quit()

myfile.close()
myfile2.close()
#redundant but still good to have

