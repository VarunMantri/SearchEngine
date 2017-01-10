__author__='Varun Rajiv Mantri'

#import statements

import os


def main():
    key=input('what would you like to search?')
    searchresults=searchEngine(key)
    print('Search results:')
    print(searchresults)

def searchEngine(key):
    '''
        this methods searches the crawled web pages and looks for the search parameter
        and shows the result in accordance with maximum hits
        :param key: parameter to be searched in the crawled pages
        :return: list of search result
        '''
    searchresults=[]
    wordsList=key.split()
    for file in os.listdir('D:\Python\webCrawling'):
        if file.endswith('.txt'):
            startLineFlag=0
            foundFlag=0
            counter1=0
            counter2=0
            proximity=0
            link=''
            with open(file) as f:
                for line in f:
                    if startLineFlag==0:
                        link=line
                        startLineFlag=1
                    else:
                        if line.find(key) is not -1:
                            #counter will notify the number of times result was hit
                            proximity=100
                            counter1=counter1+1
                            foundFlag=1
                        elif foundFlag!=1:
                            if len(wordsList)!=1:
                                returnedList=proximitySearch(wordsList,line)
                                returnedProximity=returnedList[0]
                                if returnedProximity>proximity:
                                    proximity=returnedProximity
                                elif returnedProximity==proximity:
                                    if returnedList[1]==1:
                                        counter2=counter2+1
                                foundFlag=2
            if foundFlag == 1:
                searchresults=merger(link,counter1,searchresults,100)
            elif foundFlag==2 and counter2!=0:
                searchresults=merger(link,counter2,searchresults,proximity)
               # searchresults[counter]=link
    return searchresults

def proximitySearch(wordList,line):
    '''
            this methods searches taking into consideration proximity of words in the entered search phrase
            :param wordlist: List of words to be searched
            :param line: variable that holds the phrase from crawled pages which needs to be searched
            :return: list containing the proximity value and the found flag
    '''
    counter=0
    proximity=0
    tempProximity=0
    foundFlag=0
    length=len(wordList)
    proximityConstant=100/(length-1)
    while counter!=length-1:
        tempCounter=counter
        absoluteCounter=0
        while tempCounter<=length-1:
            if tempCounter==0:
                currentSearch=wordList[tempCounter]
                tempProximity=proximityConstant * (absoluteCounter)
                if line.find(currentSearch) is not -1 and proximity <= tempProximity:
                    proximity=tempProximity
                    foundFlag=1
            else:
                currentSearch=currentSearch + " " + wordList[tempCounter]
                tempProximity = proximityConstant * (absoluteCounter)
                if line.find(currentSearch) is not -1 and proximity <= tempProximity:
                    proximity = tempProximity
                    foundFlag=1
            absoluteCounter=absoluteCounter+1
            tempCounter=tempCounter+1
        counter=counter+1

    return [proximity,foundFlag]


def merger(link,counter,searchresults,proximity):
    '''
        this methods merges the new link with the existing links depending upon number of hits
        :param link: the link that is to be included in the search result
        :param activeLinks: variable which holds the number of hits of the search phrase
        :param searchresults: list which internally contains lists that hold the links and the count of number of hits
        :return: merged list of links and number of hits
    '''
    rPointer=0
    newList=[]
    entryFlag=0
    for item in searchresults:
        if item[2]>proximity:
            newList.append([item[0],item[1],item[2]])
            rPointer=rPointer+1
        elif item[2]<proximity:
            newList.append([link,counter,proximity])
            entryFlag=1
            for i in searchresults[rPointer:]:
                newList.append([i[0],i[1],i[2]])
            break
        elif item[2]==proximity:
            if item[1] > counter:
                newList.append([item[0], item[1], item[2]])
                rPointer = rPointer + 1
            elif item[1] < counter:
                newList.append([link, counter,proximity])
                entryFlag = 1
                for i in searchresults[rPointer:]:
                    newList.append([i[0], i[1], i[2]])
                break
    if entryFlag!=1:
        newList.append([link,counter,proximity])
    return newList

if __name__ == '__main__':
    main()