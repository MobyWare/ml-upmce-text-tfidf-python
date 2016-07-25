# Investigating the use of TF-IDF scores to identity PHI in documents.

## Goal
I want to re-familiarize myself with TF-IDF and experiment with how the score can help me identify PHI in documents. The institution is the PHI will me more prominent in a particular document than other words given a corpus.

## Method
I am attempting to calculate TF-IDF scores for documents in a tabular form for further analysis. I am interested in seeing how we can exploit to ID PHI in docs. I got the code [here](http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/)

## Set up
1. The code uses textblob which you can install using: 
 pip install -U textblob
2. Run test to see that libraries are installed or run main to it your corpus of documents using:
	python main.py <path to your file> <optional output path>