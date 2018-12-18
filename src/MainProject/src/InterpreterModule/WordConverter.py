#author: Cézan von Meijenfeldt
#!/usr/bin/env python

from keras.preprocessing.text import Tokenizer
import numpy as np
import pickle


class WordConverterClass:

    tokenWords = Tokenizer()
    tokenClasses = Tokenizer
    reverse_word_map_classes = []

    def loadTokenizers(self, wordTokenizerPath, classTokenizerPath):
        with open(wordTokenizerPath, 'rb') as handle:
            self.tokenWords = pickle.load(handle)

        with open(classTokenizerPath, 'rb') as handle:
            self.tokenClasses = pickle.load(handle)

        self.reverse_word_map_classes = dict(
            map(reversed, self.tokenClasses.word_index.items()))

        print("Tokenizers loaded")

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
