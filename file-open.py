#---For appending the text---
f=open("helloworld.txt","a");
f.write("This is the sample text appending to the helloworld.txt.");
print(f.read());
f.close();
#---Reading the file content
f=open("helloworld.txt","r");
print(f.read());
f.close();
#------Wrinting the content to the file
f=open("helloworld.txt","w")
f.write("This is the last line added to the helloworld.txt file.")
f.close()
#---Reading the file content line by line

f=open("helloworld.txt","r")
print(f.readline(40))
f.close()
#----------------Finally removing the file from folder
import os
os.remove("deleted-file.txt")
print("File deleted successfully")
'''
import os
if os.path.exists("delete-file.txt"):
    os.remove("deleted-file.txt")
 else:
     print("File doesn't exist.")
     '''
