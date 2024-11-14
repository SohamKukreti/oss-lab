from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

import pandas as pd

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
print(df.head(10))

print(f"Number of samples: {df.shape[0]}")
print(f"Number of features: {df.shape[1] - 1}")
print(f"Number of classes: {len(df['target'].unique())}")


X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.3, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



df.hist(bins=20, figsize=(10, 10))
# plt.title("Before Scaling")
plt.show()

scaled_df = pd.DataFrame(X_train_scaled, columns=wine.feature_names)
scaled_df.hist(bins=20, figsize=(10, 10))
# plt.title("After Scaling")
plt.show()


clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_scaled, y_train)

y_pred = clf.predict(X_test)
#print(y_pred)
#print(clf.predict_proba(X_test_scaled))


cm = confusion_matrix(y_test, y_pred)
print(cm)
