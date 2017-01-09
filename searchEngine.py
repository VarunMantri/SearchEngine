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
    for file in os.listdir('D:\Python\webCrawling'):
        if file.endswith('.txt'):
            startLineFlag=0
            foundFlag=0
            counter=0
            link=''
            with open(file) as f:
                for line in f:
                    if startLineFlag==0:
                        link=line
                        startLineFlag=1
                    else:
                        if line.find(key) is not -1:
                            #counter will notify the number of times result was hit
                            #proximity=100
                            counter=counter+1
                            foundFlag=1
            if foundFlag == 1:
                searchresults=merger(link,counter,searchresults)
               # searchresults[counter]=link
    return searchresults

def merger(link,counter,searchresults):
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
        if item[1]>counter:
            newList.append([item[0],item[1]])
            rPointer=rPointer+1
        elif item[1]<counter:
            newList.append([link,counter])
            entryFlag=1
            for i in searchresults[rPointer:]:
                newList.append([i[0],i[1]])
            break
    if entryFlag!=1:
        newList.append([link,counter])
    return newList

if __name__ == '__main__':
    main()