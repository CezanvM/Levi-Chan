from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, SGD
from sklearn.metrics import accuracy_score


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
            SGD(lr=0.5), 'binary_crossentropy', metrics=['accuracy'])
        self.model.summary()

        self.model.fit(train_x, train_y, epochs=5000, validation_split=0.2)

        print("The train accuracy score is {:0.3f}".format(
            accuracy_score(
                train_y, self.model.predict(train_x).round(),
                normalize=False)))
        print("The test accuracy score is {:0.3f}".format(
            accuracy_score(
                test_y, self.model.predict(test_x).round(), normalize=False)))

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