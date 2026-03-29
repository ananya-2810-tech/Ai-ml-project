from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Training data
expense_names = ["pizza", "burger", "restaurant", "uber", "bus", "train ticket", "notebook", "pen", "textbook", "movie ticket", "netflix"]
category = ["Food", "Food", "Food", "Travel", "Travel","Travel" ,"Education", "Education","Education", "Entertainment", "Entertainment"]

#Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(expense_names)

#Train model
model = MultinomialNB()
model.fit(X, category)

def predict_category(expense_name):
    test = vectorizer.transform([expense_name])
    prediction = model.predict(test)
    return prediction[0]

