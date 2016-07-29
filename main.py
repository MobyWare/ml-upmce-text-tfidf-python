import sys
from tfidfLibDev import *


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # TODO proccess args
    pathToCorpus = argv
    resultPath = ""
    maxTermsPerDoc = 5

    fileBlobList = getBlobListByPath(pathToCorpus)

    resultFile = open(resultPath, mode='w')

    for blob in enumerate(fileBlobList):
        line = blob[0] # file Name.
        scores = {word: tfidf(word, blob, fileBlobList) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        for word, score in sorted_words[:maxTermsPerDoc]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
    

def getBlobListFromDirectory(path=""):
    pass

def getBlobListFromDelimetedFile(path="", regexDelim=""):
    pass

"""
This function gets the list of docs from either a directory with files to parse or a single delimited file
Returns a tuple of filename and text.
""""
def getBlobListByPath(path=""):
    pass


if __name__ == "__main__":
    main(sys.argv)