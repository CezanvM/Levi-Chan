#author: Cézan von Meijenfeldt

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, SGD
from keras.models import model_from_json
import numpy as np


class NeuralNetClass:
    model = Sequential()

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

    def predictModel(self, input, wordConverter):
        matrix = np.array([np.asarray(input)])
        output = self.model.predict(matrix)
        return self.getClass(output, wordConverter, input)

    def getClass(self, networkOutput, wordConverter, input):
        # for i in networkOutput.
        for result in networkOutput:
            # array = np.asarray(result)
            maxValue = max(result)
            maxValueIndex = result.tolist().index(max(result))

            intention = wordConverter.tokenToClasses(maxValueIndex)

        return intention, maxValue