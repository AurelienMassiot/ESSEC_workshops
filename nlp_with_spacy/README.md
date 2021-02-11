# NLP with spaCy

### What is it ?

NLP workshop  which took place during February 2021. The objective was to describe the main features of the [spaCy](https://spacy.io/) library and propose use case examples.

### notebooks

* **basic_features.ipynb**: expose the main functionalities of spaCy.
* **spaCy_analytics.ipynb**: analysis of the book _Pride and Prejudice_
* **text_classification.ipynb**: pre-processing with spaCy for text classfication task.

### Requirements

Python libraries:
```bash
$ pip install spacy numpy pandas scikit-learn matplotlib
$ python -m spacy download en_core_web_sm
$ python -m spacy download en_core_web_lg
```

**Datasets**

* [Amazon Alexa reviews](https://www.kaggle.com/sid321axn/amazon-alexa-reviews)
* [Pride and Prejudice raw text](https://www.gutenberg.org/ebooks/42671.txt.utf-8)
