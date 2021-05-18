from sklearn.neighbors import KNeighborsClassifier


def model_knn(sg, al, hemo, htn, dm, appet):
    import pickle
    x = [[sg, al, hemo, htn, dm, appet]]
    knn = pickle.load(open('CKDModel.sav', 'rb'))
    predictions = knn.predict(x)
    if predictions == 1:
        predictions = 'CKD'
    elif predictions == 0:
        predictions = 'NOT-CKD'
    else:
        predictions = 'Error'
    return predictions
