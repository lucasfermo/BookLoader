#Aggregates all author data into one text file
import os,sys
import urllib,os,bs4,webbrowser,requests,re,sys,math,decimal
print(os.getcwd())

os.chdir("C:\\users\\lucasfermo\\atomMain\\books\\authors")

files=[]
for i in os.listdir():
    if "master" not in i:
        files.append(i)


f=open("master.txt",'w')
for i in files:
    tmp=open(i,'r')
    f.write(tmp.read())


f.close()

print(len(files)," aggregated into master.txt")
