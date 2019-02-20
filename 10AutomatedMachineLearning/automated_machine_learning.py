import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
# データセット
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_iris
# アルゴリズム
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
# 評価指標
from sklearn.metrics import accuracy_score

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Automated Machine Learning'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 200
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # メインで使用するverticalBox
        self.mainVerticalBox = QVBoxLayout()
        self.setupComboTitleLabel()
        self.setupComboBox()
        self.setupButtonTitleLabel()
        self.setupButton()

    def setupComboTitleLabel(self):
        self.comboBoxLabel = QLabel("STEP1: Please select the data to be used!", self)
        self.comboBoxLabel.move(135, 20)

    def setupComboBox(self):
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Breast Cancer")
        self.comboBox.addItem("Iris Classificaiton")
        self.comboBox.move(175, 40)

    def setupButtonTitleLabel(self):
        self.buttonLabel = QLabel("STEP2: Click the button to execute ", self)
        self.buttonLabel.move(135, 120)

    def setupButton(self):
        self.button = QPushButton('Fit!', self)
        self.button.clicked.connect(self.on_click)
        self.button.resize(150, 35)
        self.button.move(175, 140)

    def on_click(self):
        print('button pushed!')
        resultWindow = ResultWindow()
        print(self.comboBox.currentIndex())
        resultWindow.show(self.comboBox.currentIndex())

class ResultWindow(QWidget):
    def __init__(self, parent=None):
        self.dialog = QDialog(parent)
        self.label = QLabel()
        self.label.setText('Result Window')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.dialog.setLayout(self.layout)

    def show(self, currentIndex):
        print(currentIndex)
        if currentIndex == 0:
            self.label.setText("【Result of Breast Cancer - Accuracy Score】")
            self.classifyBreastCancer()
        else:
            self.label.setText("【Result of Iris - Accuracy Score】")
            self.classifyIris()
        self.dialog.exec_()

    def classifyBreastCancer(self):
        print('classify Breast Cancer!')
        dataset = load_breast_cancer()
        # データの整形
        X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
        y = pd.DataFrame(dataset.target, columns=['y'])
        X.join(y).head()

        # Holdout法
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20, random_state=1)
        pipe_knn_50 = Pipeline([('scl',StandardScaler()),('est',KNeighborsClassifier(n_neighbors=50))])
        pipe_logistic = Pipeline([('scl',StandardScaler()),('est',LogisticRegression(random_state=1))])

        # K近傍法とロジスティック回帰で分類する
        pipe_knn_50.fit(X_train,y_train.as_matrix().ravel())
        pipe_logistic.fit(X_train,y_train.as_matrix().ravel())

        # KNN - Train
        self.knnTrainLabel = QLabel("KNN - Nearest 50 - Train: %.3f" % accuracy_score(y_train, pipe_knn_50.predict(X_train)))
        self.layout.addWidget(self.knnTrainLabel)
        # KNN - Test
        self.knnTestLabel = QLabel("KNN - Nearest 50 - Test: %.3f" % accuracy_score(y_test, pipe_knn_50.predict(X_test)))
        self.layout.addWidget(self.knnTestLabel)
        # Logistic Regression - Train
        self.logisticTrainLabel = QLabel("Logistic Regression - Train: %.3f" % accuracy_score(y_train, pipe_logistic.predict(X_train)))
        self.layout.addWidget(self.logisticTrainLabel)
        # Logistic Regression - Test
        self.logisticTestLabel = QLabel("Logistic Regression - Test: %.3f" % accuracy_score(y_test, pipe_logistic.predict(X_test)))
        self.layout.addWidget(self.logisticTestLabel)

    def classifyIris(self):
        print('classify Iris!')
        dataset = load_iris()
        # データの整形
        X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
        y = pd.DataFrame(dataset.target, columns=['y'])
        X.join(y).head()

        # Holdout法
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20, random_state=1)
        pipe_knn_50 = Pipeline([('scl',StandardScaler()),('est',KNeighborsClassifier(n_neighbors=50))])
        pipe_logistic = Pipeline([('scl',StandardScaler()),('est',LogisticRegression(random_state=1))])

        # K近傍法とロジスティック回帰で分類する
        pipe_knn_50.fit(X_train,y_train.as_matrix().ravel())
        pipe_logistic.fit(X_train,y_train.as_matrix().ravel())

        # KNN - Train
        self.knnTrainLabel = QLabel("KNN - Nearest 50 - Train: %.3f" % accuracy_score(y_train, pipe_knn_50.predict(X_train)))
        self.layout.addWidget(self.knnTrainLabel)
        # KNN - Test
        self.knnTestLabel = QLabel("KNN - Nearest 50 - Test: %.3f" % accuracy_score(y_test, pipe_knn_50.predict(X_test)))
        self.layout.addWidget(self.knnTestLabel)
        # Logistic Regression - Train
        self.logisticTrainLabel = QLabel("Logistic Regression - Train: %.3f" % accuracy_score(y_train, pipe_logistic.predict(X_train)))
        self.layout.addWidget(self.logisticTrainLabel)
        # Logistic Regression - Test
        self.logisticTestLabel = QLabel("Logistic Regression - Test: %.3f" % accuracy_score(y_test, pipe_logistic.predict(X_test)))
        self.layout.addWidget(self.logisticTestLabel)

def main():
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
