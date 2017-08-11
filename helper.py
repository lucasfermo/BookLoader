#Helper function for bookloader.py
import os,sys
import urllib,os,bs4,webbrowser,requests,re,sys,math,decimal

def getIdFunction(soup,n=10):
    getId=soup.findAll('a',attrs={"class","bookTitle"})
    getId=getId[:10]
    bookId=[]

    for i in getId:
        ID=str(i).replace("-",".")
        ID=ID.split("show/")
        ID=ID[1].split(".")[0]
        bookId.append(ID)

    return bookId

def getTitleFunction(soup):
    titles=[]

    getTitle=soup.findAll("a", {"class":'bookTitle'})
    getTitle=getTitle[:10]

    #Get book titles
    for i in getTitle:
        title=str(i).split("name\">")
        title=title[1].split("</")
        titles.append(title[0])

    titles=list(map(lambda x:x.capitalize(),titles))

    return titles

def getYearsFunction(soup):
    getYears=soup.findAll('span',attrs={"class":'greyText smallText uitext'})
    getYears=getYears[0:10]

    years=[]

    for i, c in enumerate(getYears):
        try:
            tmp=str(c).split("published")
            tmp=tmp[1][:20].strip()
            years.append(tmp)
        except:
            years.append("0000")
            continue

    return years

def getRatingsFunction(soup):
    #Get average rating
    avgRate=[]
    #Total ratings
    ratings=[]

    getRating=soup.findAll('span',attrs={'class','minirating'})
    getRating=getRating[:10]

    for i,c in enumerate(getRating):
        tmp=str(c).split('avg')
        #Get average rating
        avgRate.append(str(tmp[0][-6:]).strip())
        #Get amount of ratings
        ratings.append(tmp[1].split(" ")[3].replace(",",""))

    return avgRate,ratings

def inputStringFunction(bid,au,t,years,avg,rat):
    tmp=""
    for i,c in enumerate(t):
        try:
            tmp+=bid[i]+"\t"+au+'\t'
            tmp+=t[i]+'\t'+years[i]+'\t'
            tmp+=avg[i]+'\t'+rat[i]+'\n'

        except:
            continue

    return tmp
