# import sentences
# import clasification(intents)

#prepare both lists with the keras tokenizer (fit_on_text)

#split data in train and test data 80/20
import json

bag = []
words = []
classes = []
documents = []


def importData(Path):
    with open(Path) as json_data:
        Data = json.load(json_data)
        for intent in Data['Data']:
            for pattern in intent['Pattern']:
                words.append(pattern)
                classes.append(intent["Tag"])
                #add pattern to pattern list
                #add Tag to tag list

        print(words)
        print(classes)


import keras


def tokenizeData():
    print("kek")


importData('src\TrainProject\Data.json')
