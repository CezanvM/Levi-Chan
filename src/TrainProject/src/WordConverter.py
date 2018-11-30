# import sentences
# import clasification(intents)

#prepare both lists with the keras tokenizer (fit_on_texts)

#split data in train and test data 80/20
import json
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import numpy as np
import pickle


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
    tokenClasses = Tokenizer

    def importData(self, Path):
        with open(Path) as json_data:
            Data = json.load(json_data)
            for intent in Data['Data']:
                for pattern in intent['Pattern']:
                    self.words.append(pattern)
                    self.classes.append(intent["Tag"])
            #add pattern to pattern list
            #add Tag to tag list

        return self.tokenizeData()

    def creatTokenizers(self, path):
        self.tokenWords = Tokenizer()
        self.tokenClasses = Tokenizer()
        return self.importData(path)

    def loadTokenizers(self, wordTokenizerPath, classTokenizerPath):
        with open(wordTokenizerPath, 'rb') as handle:
            self.tokenWords = pickle.load(handle)

        with open(classTokenizerPath, 'rb') as handle:
            self.tokenClasses = pickle.load(handle)

        self.reverse_word_map_classes = dict(
            map(reversed, self.tokenClasses.word_index.items()))

    def tokenizeData(self):

        self.tokenWords.fit_on_texts(self.words)
        self.tokenClasses.fit_on_texts(self.classes)

        #print(self.tokenWords.word_counts)
        #print(tokenClasses.word_counts)

        self.encodedWords = self.tokenWords.texts_to_matrix(
            self.words, mode='count')
        self.encodedClasses = self.tokenClasses.texts_to_matrix(
            self.classes, mode='count')

        #print(self.encodedWords)
        #print(self.encodedClasses)

        reverse_word_map_words = dict(
            map(reversed, self.tokenWords.word_index.items()))
        self.reverse_word_map_classes = dict(
            map(reversed, self.tokenClasses.word_index.items()))

        return self.splitTrainTest()

    def convertSentenceToTokens(self, sentence):
        sentence = sentence.lower()
        words = sentence.split()
        sentenceBag = np.zeros(len(self.tokenWords.word_index) + 1)
        for s in words:
            for i, w in enumerate(self.tokenWords.word_index):
                if w == s:
                    sentenceBag.itemset(self.tokenWords.word_index.get(w), 1)

        return sentenceBag

    def tokenToClasses(self, ClassificationIndex):
        intention = self.reverse_word_map_classes[ClassificationIndex]
        return (intention)

    def saveClassTokenizer(self, path):
        print("saving class tokenizer")
        #classFile = open(path, "w+")
        with open(path, 'wb') as handle:
            pickle.dump(
                self.tokenClasses, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def saveWordTokenizer(self, path):
        with open(path, 'wb') as handle:
            pickle.dump(
                self.tokenWords, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def splitTrainTest(self):
        self.train_x, self.test_x, self.train_y, self.test_y = train_test_split(
            self.encodedWords, self.encodedClasses, test_size=0)
        print("train length  ", len(self.train_x))
        print("test length ", len(self.test_x))

        return self.train_x, self.test_x, self.train_y, self.test_y
