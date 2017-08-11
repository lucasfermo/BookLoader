import os,sys
import urllib,os,bs4,webbrowser,requests,re,sys,math,decimal
from helper import getIdFunction,getTitleFunction,getYearsFunction
from helper import getRatingsFunction,inputStringFunction



os.chdir("C:\\users\\lucasfermo\\atomMain\\books")

#sys.argv
try:
    n=str(sys.argv[1]).capitalize()+" "+str(sys.argv[2].capitalize())
    print(n)
    n=n.split(" ")
except:
    n="Donald Trump".split(" ")

url="https://www.goodreads.com/search? \
    q={}+{}&search_type=books&search%5Bfield%5D=author".format(n[0],n[1])
while " " in url:
    url=url.replace(" ","")

res=requests.get(url)

soup=bs4.BeautifulSoup(res.text,'html.parser')

bookId=getIdFunction(soup)

titles=getTitleFunction(soup)


#Get years
years=getYearsFunction(soup)

avgRate,ratings=getRatingsFunction(soup)

author=" ".join(n)

kwargs=dict(bid=bookId,au=author,t=titles,years=years,
        avg=avgRate, rat=ratings)

inputString=inputStringFunction(**kwargs)

f=open(author.replace(" ","_")+".txt",'w')

f.write(inputString)
f.close()

print("Done","{} books loaded to {}.txt".format(len(years),author.replace(" ", "_")))
