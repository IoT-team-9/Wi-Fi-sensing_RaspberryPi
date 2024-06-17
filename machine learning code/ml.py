import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import change_to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# create db 
# connect to db file(csi-db.db)
connection = sqlite3.connect('csi-data.db')
cursor = connection.cursor()

# create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS csi-data (
    timestamp TEXT,
    label varchar(255)
)'''
)

# save to db
connection.commit()

#reading data
data = pd.read_csv('csi_data.csv')

X = data[['amplitude', 'phase']].values
y = data['label'].values  # label: walk, sit down, fall down, non

### data preprocessing ###
# label encode 0 ~ 4
label_mapping = {'walking': 0, 'sitting': 1, 'falling': 2, 'standing': 3, 'none': 4}
y = np.array([label_mapping[label] for label in y])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# standardization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# change data into categorical label
y_train = change_to_categorical(y_train, num_classes=5)
y_test = change_to_categorical(y_test, num_classes=5)


### model learning ###

learning_model = Sequential()

learning_model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
learning_model.add(Dropout(0.5))
learning_model.add(Dense(64, activation='relu'))
learning_model.add(Dropout(0.5))
learning_model.add(Dense(5, activation='softmax'))  

learning_model.compile(
    loss='categorical_crossentropy', 
    optimizer='adam', 
    metrics=['accuracy']
    )

data_history = learning_model.fit(
    X_train, 
    y_train, 
    epochs=50, 
    batch_size=32, 
    validate_data=(X_test, y_test)
    )

## model evaluation ##

loss, accuracy = learning_model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

y_pred = learning_model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

conf_matrix = confusion_matrix(y_true, y_pred_classes)
class_report = classification_report(
    y_true, 
    y_pred_classes, 
    target_names=['walking', 'sitting', 'falling', 'standing', 'none']
    )

print('Confusion Matrix')
print(conf_matrix)
print('\nClassification Report')
print(class_report)