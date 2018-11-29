# import sentences
# import clasification(intents)

#prepare both lists with the keras tokenizer (fit_on_texts)

#split data in train and test data 80/20
import json
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import numpy as np


class WordConverterClass:
    bag = []
    words = []
    classes = []
    documents = []

    encodedWords = []
    encodedClasses = []

    reverse_word_map_classes = []

    train_x = []
    train_y = []
    test_x = []
    test_y = []

    tokenWords = Tokenizer()

    def importData(self, Path):
        with open(Path) as json_data:
            Data = json.load(json_data)
            for intent in Data['Data']:
                for pattern in intent['Pattern']:
                    self.words.append(pattern)
                    self.classes.append(intent["Tag"])
            #add pattern to pattern list
            #add Tag to tag list

            print(self.words)
            print(self.classes)

        return self.tokenizeData()

    def tokenizeData(self):
        self.tokenWords = Tokenizer()
        self.tokenWords.fit_on_texts(self.words)
        tokenClasses = Tokenizer()
        tokenClasses.fit_on_texts(self.classes)

        print(self.tokenWords.word_counts)
        print(tokenClasses.word_counts)

        self.encodedWords = self.tokenWords.texts_to_matrix(
            self.words, mode='count')
        self.encodedClasses = tokenClasses.texts_to_matrix(
            self.classes, mode='count')

        print(self.encodedWords)
        print(self.encodedClasses)

        reverse_word_map_words = dict(
            map(reversed, self.tokenWords.word_index.items()))
        self.reverse_word_map_classes = dict(
            map(reversed, tokenClasses.word_index.items()))

        #print(self.reverse_word_map_classes)
        return self.splitTrainTest()

    #def tokenToWords(list_of_indices):
    #        words = [reverse_word_map_words.get(letter) for letter in list_of_indices]
    #    return(words)

    def convertSentenceToTokens(self, sentence):
        sentence = sentence.lower()
        words = sentence.split()
        sentenceBag = np.zeros(len(self.tokenWords.word_index) + 1)
        for s in words:
            for i, w in enumerate(self.tokenWords.word_index):
                if w == s:
                    sentenceBag.itemset(self.tokenWords.word_index.get(w), 1)

    # matrix = np.matrix(np.array(sentenceBag))
        return sentenceBag

    def tokenToClasses(self, ClassificationIndex):
        intention = self.reverse_word_map_classes[ClassificationIndex]
        return (intention)

    def splitTrainTest(self):
        self.train_x, self.test_x, self.train_y, self.test_y = train_test_split(
            self.encodedWords, self.encodedClasses, test_size=0)
        print("train length  ", len(self.train_x))
        print("test length ", len(self.test_x))

        return self.train_x, self.test_x, self.train_y, self.test_y
