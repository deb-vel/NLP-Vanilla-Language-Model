# NLP-Vanilla-Language-Model

# Assignment Specification
(i) Pick a corpus;
(ii) check corpus and see what sort of processing you need to do - if you are using the BNC, you do not need to build a perfect tokeniser, an imperfect but practical one will do - of course, the errors will propagate into your language model, but that is ok;
(iii) decide on how you will store the information (i.e. plan ahead);
(iv) split the data into 80/20 (keep the same split for later - i.e. split only once)
(v) first build Unigram frequencies/probabilities, then Bigram and then Trigram; 
(vi) consider storage options so that you build your n-gram models only once;

Corpora choices:
Maltese Corpus: http://mlrs.research.um.edu.mt/index.php?page=downloads
(Baby) British National Corpus: http://ota.ox.ac.uk/desc/2553

# Implementation
## Corpus
 I chose a Maltese corpus called malti03.academic.1.txt. For this corpus, I took the first word of every line in the text file and stored it inside a list. Therefore, each element of the list contains tokens which are words or punctuation. To read this file I made use of the utf-8 decoding so that the Maltese letters are not changed into random symbols.
 
## Storage
### Lists and arrays
As mentioned above, I stored the words of the corpus inside a list, one after the other. This list was then used to get all sentences and created a 2D array having each row being a sentence and each column storing words. This was then shuffled randomly and split it 80/20. I used the training data to calculate the N-Grams upon.
An array for each N-gram model was created to store the unique permutations found. I also created arrays to store the frequencies of the unigram and the bigram models. These arrays are populated every time a new unique N-gram is met. E.g the word “għalliema” is stored at index 0 in the unigram array and its respective frequency is stored at index 0 in the unigram’s separate frequency array.
By storing the frequencies, the program can make use of them when calculating the probabilities later on, instead of calculating the frequency again. E.g to calculate the probability of a trigram, for the denominator it accesses the bigram’s frequency which would have been previously calculated.

### Text Files
For each N-Gram model I created a text file to store the details in. Once again the utf-8 encoding/decoding was used, this time to write to the files.
The first column consists of unique unigrams/bigrams/trigram depending which one of them is being analyzed. The second column consits of the frequency of the N-Gram, and the last column is the probability. These are separated with a space character. I chose this character because no token contains a space characters, therefore, it is not confused with an actual token (e.g. if the delimiter is a comma it can be confused with a token from the corpus).
The below is a snippet from the trigram text file
    
## Time to build
It took the program about 23 seconds to finish running when using my laptop.

## Running the program
You can double click on the RunMe.cmd file to run the program. When it finishes you can press enter to close the window

