# Russian Propagenda Facebook Political Adverts Analyze > Computational Social Science

# Research Question:

“Are negative adverts more likely to be successful in Propaganda? “

How effective is an advert in relation to its positivity (negativity)?


## How do we measure effectiveness?

We have access to AD_Click and AD_Impression in our data and we can calculate Click Through Rate measure to compare the success or effect of the advert.
CTR = ClicksImpression

To measure campaigns’ success based on CTR  plus Amount of Money spent (In other words, which campaigns were more affordably successful).


## How to measure negativity?

We find a dictionary for labeling positive/ negative words or do supervised labeling to find negativity index for each row of our data. 


Finding a correlation between negativity Index vs effectiveness?  

Dictionary method for labeling using: SentiWordNet.

* Esuli, Andrea and Fabrizio Sebastiani. “SENTIWORDNET: A Publicly Available Lexical Resource for Opinion Mining.” LREC (2006).


## codes for using the dictionary:
https://github.com/aesuli/SentiWordNet
https://github.com/anelachan/sentimentanalysis


## Alternative Algorithms:

Too Naïve:
http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
Java code:
https://nlp.stanford.edu/sentiment/code.html


## Extras:

Compare the results for different groups based on followings and age. Does any obvious difference exist? 

Relate the Positivity/Negativity with the demographic measures.

Challenge:  Missing data exists in our columns; which is observable.

We must include the Demographics for clustering.
AD_TARGETING_INTERESTS, AD_TARGETING_EXCLUDED_CONNECTIONS

## Categorizations:

Age 
Platform (Instagram/ Facebook)

Which issues were more important for the Americans in comparison to topics for	 Russians Group? 


--------------------------------------------------------------------------------------------------------------------------------

# Contacts

* [Institute for Web Science and Technoloogies (WEST)](https://west.uni-koblenz.de), University of Koblenz-Landau


# License
All code is licensed under [MIT License](https://opensource.org/licenses/MIT) .
