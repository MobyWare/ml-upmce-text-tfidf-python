import sys
import ntpath
import re
from tfidfLibDev import *


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # TODO proccess args
    pathToCorpus = r"C:\Users\dickm\Documents\Projects\ML\DevProjects\ml-upmce-text-tfidf-python\testhydrateddocuments.txt"
    resultPath = r"C:\Users\dickm\Documents\Projects\ML\DevProjects\ml-upmce-text-tfidf-python\testhydrateddocuments_results.txt"
    maxTermsPerDoc = 5
    
    fileNames, fileBlobList = getBlobListByPath(pathToCorpus)

    resultFile = open(resultPath, mode='w')

    print("Writing report...")
    for i in range(len(fileBlobList)):
        #line = fileBlobList[i] # file Name.
        scores = {word: tfidf(word, fileBlobList[i], fileBlobList) for word in fileBlobList[i].words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        for word, score in sorted_words:
            resultFile.write("{},{},{}\n".format(fileNames[i], word, round(score, 5)))
    
    resultFile.close()
    
"""
This function gets the list of docs from either a directory with files to parse or a single delimited file
Returns a tuple of filename and text.
"""
def getBlobListByPath(path=""):
    # Todo add logic to decide if path is file or directory and call appropriate function. for now just call MIMIC
    return getBlobListFromMIMICText(path)


def getBlobListFromDirectory(path=""):
    
    pass

def getBlobListFromMIMICText(pathCorpus="", regexDelim=""):
    startFileDelim = r'[0-9]+,[0-9]+,"'
    endFileDelim = r'",'
    lines = open(pathCorpus, 'r').readlines()
    print("Read {} lines from MIMIC-formated file: {}.".format(len(lines), ntpath.basename(pathCorpus)))

    startIndex = -1
    documentNames = []
    documents = []
    documentName = ""
    for i in range(len(lines)):        
        if re.search(startFileDelim, lines[i]):   
            fileContent = ""
            startIndex = i+1
            documentName = getMimicFileName(lines[i])

        if startIndex > -1 and startIndex <= i and re.search(endFileDelim, lines[i]) :
            for j in range(startIndex,i):
                fileContent += lines[j] 
            documentNames.append(getMimicFileName(documentName))
            documents.append(tb(fileContent))
    
    print("Process complete.\nRead {} lines and identified {} documents in file: {}.".format(len(lines), len(documentNames), ntpath.basename(pathCorpus)))
    return documentNames, documents

def getMimicFileName(delimName=""):
    return delimName.strip().replace(',','-').replace('"', '')


if __name__ == "__main__":
    main(sys.argv)