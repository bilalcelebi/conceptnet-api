### ConceptNet API ###

I maked this API because Original API is so much complicated. Bu this more basic and understandable. You can search words, relations and concepts and you can download it too. Let me explains url types:

***/word/{language_code}/{word}/{amount_of_retrieve_data}/?download={True|False}***  

This url will return you the information of a requested word. What is this information, it returns synonyms and antonyms of this word both in its own language and other languages, its equivalents in other words, the roots it derives from in its own language and in other languages, and related words in both its own and other languages that are derived from or contain a part of itself.

***/related/{language_code}/{word}/{amount_of_retrieve_data}/?download={True|False}***

This url will return the equivalent of a word you have given in other languages, as well as the words in which it is rooted in its own language.

***/example***

This will return information about example word in english. Example word roots, equivalents in other languages. This is example batch you can understand structure of dataset with looking this.

***/get_relation***

This will return a large amount of data giving information about the relationships between the words. One of the most famous is ***'RelatedTo'***. You need give parameters in the body element. Like download if you wanna download result as a json file and relation_type like RelatedTo and Synonyms and last one is amount parameters that refers how big data you want.


***For Use***

- First Clone the Repository.
- Download required libraries. [Flask and Requests just thats.]
- Go to the src/ folder and run wsgi.py file.
- And ta da! you gonna see localhost url working on 5000th port and you can use your API now.
