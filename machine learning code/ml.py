import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import change_to_categorical


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

# data preprocessing
# label encode 0 ~ 4
label_mapping = {'walking': 0, 'sitting': 1, 'falling': 2, 'standing': 3, 'none': 4}
y = np.array([label_mapping[label] for label in y])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# standardization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# change data into categorical label
y_train = change_to_categorical(y_train, num_classes=5)
y_test = change_to_categorical(y_test, num_classes=5)