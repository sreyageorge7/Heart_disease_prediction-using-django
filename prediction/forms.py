from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.IntegerField()
    cp = forms.IntegerField(label="Chest Pain Type")
    trestbps = forms.IntegerField(label="Resting BP")
    chol = forms.IntegerField(label="Cholesterol")
    fbs = forms.IntegerField(label="Fasting Blood Sugar")
    restecg = forms.IntegerField(label="Resting ECG")
    thalach = forms.IntegerField(label="Max Heart Rate")
    exang = forms.IntegerField(label="Exercise Induced Angina")
    oldpeak = forms.FloatField()
    slope = forms.IntegerField()
    ca = forms.IntegerField()
    thal = forms.IntegerField()
