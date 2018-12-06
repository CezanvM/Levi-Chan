from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, SGD
from sklearn.metrics import accuracy_score
import numpy as np
import operator
from keras.models import model_from_json


class TrainClass:
    model = Sequential()

    def trainModel(self, train_x, test_x, train_y, test_y):

        print("output length ", len(train_y[0]))
        print("Input length ", len(train_x[0]))

        self.model = Sequential()
        self.model.add(
            Dense(
                len(train_y[0]),
                input_shape=(len(train_x[0]), ),
                activation='sigmoid'))
        self.model.compile(
            Adam(lr=0.5), 'binary_crossentropy', metrics=['accuracy'])

        print("training started!")
        self.model.fit(train_x, train_y, epochs=5000, verbose=1)

        print("training done!")

    def predictModel(self, input, wordConverter):
        matrix = np.array([np.asarray(input)])
        output = self.model.predict(matrix)
        return self.getClass(output, wordConverter, input)

    def getModel(self):
        return self.model

    def saveModel(self, path):
        model_json = self.model.to_json()
        with open(path, "w") as json_file:
            json_file.write(model_json)

    def saveWeights(self, path):
        self.model.save_weights(path)

    def loadModel(self, JSON, weights):
        json_file = open(JSON, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        #   load weights into new model
        loaded_model.load_weights(weights)
        print("Loaded model from disk")

        self.model = loaded_model
        # evaluate loaded model on test data
        self.model.compile(
            Adam(lr=0.5), 'binary_crossentropy', metrics=['accuracy'])
        print("model compiled")

    def getClass(self, networkOutput, wordConverter, input):
        # for i in networkOutput.
        for result in networkOutput:
            # array = np.asarray(result)
            maxValue = max(result)
            maxValueIndex = result.tolist().index(max(result))

            intention = wordConverter.tokenToClasses(maxValueIndex)

        return intention, maxValue

    def trainModel2(self, train_x, test_x, train_y, test_y):

        print("output length ", len(train_y[0]))
        print("Input length ", len(train_x[0]))

        self.model = Sequential()
        self.model.add(Dense(10, input_shape=(len(train_x[0]), )))
        self.model.add(Activation('relu'))
        self.model.add(Dense(len(train_y[0])))
        self.model.add(Activation('softmax'))

        self.model.compile(
            loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])
        self.model.summary()

        self.model.fit(train_x, train_y, epochs=4000, validation_split=0.1)