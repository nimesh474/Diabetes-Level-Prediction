from django.shortcuts import render
import pickle
import numpy as np

# path of the model
path = r'D:/DeerWalk/diabetes_django/ml_model/diabetes_model.pkl'

# model loaded
model = pickle.load(open(path, 'rb'))

# logic to use linear regression model
def predict_diabetes(request):
    if request.method == 'GET':
        return render(request, 'data.html')
    else:
        age = float(request.POST['age'])
        gender = request.POST['gender']
        if gender == 'male':
            gender_value = 0.050680
        else:
            gender_value = -0.044642
        bmi = float(request.POST['bmi'])
        bp = float(request.POST['bp'])
        s1 = float(request.POST['s1'])
        s2 = float(request.POST['s2'])
        s3 = float(request.POST['s3'])
        s4 = float(request.POST['s4'])
        s5 = float(request.POST['s5'])
        s6 = float(request.POST['s6'])

        # django model
        # no need to get hyper

        # diabetes data 
        values = [age, gender_value, bmi, bp, s1, s2, s3, s4, s5, s6]
        reshape_array = np.array(values).reshape(1, -1)

        # make prediction
        prediction = model.predict(reshape_array)

        print(prediction)
        
        return render(request, 'data.html', {'prediction': prediction[0]})