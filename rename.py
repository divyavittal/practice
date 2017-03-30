import os


def main(dir, old):
    os.chdir(dir)
    
    #old_files = os.listdir(dir)
    #i = 1
    for old_file in os.listdir("."):
       # new_file = old_file.replace(old, new)
		if old_file.endswith(old):
			index = old_file.find("_")
			os.rename(old_file, old_file[:index + 1]+"0"+old_file[index + 1:]) # replace "" by anything I want.
        #i = i + 1
if __name__ == '__main__':
    path = raw_input('Please enter the direction you want to go to: ')
    old_string = raw_input('Please enter the type of file: ') # type of file
    #new_string = raw_input('Please enter the new string you want: ')
    main(path, old_string)
	