import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
data = pd.read_csv('hand_data.csv', header=None)
X = data.iloc[:, :-1]  
y = data.iloc[:, -1]   
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
print("Training the AI Brain... please wait.")
model = RandomForestClassifier() 
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)
print(f"Training Complete! Accuracy: {score * 100}%")
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
print("Model saved as 'model.p'!")