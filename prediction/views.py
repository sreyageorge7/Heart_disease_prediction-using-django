from django.shortcuts import render
from .forms import HeartForm
import joblib
import os
from django.conf import settings

# Load the model from model folder
model_path = os.path.join(settings.BASE_DIR, 'prediction', 'model', 'heart_model.pkl')
model = joblib.load(model_path)

def predict(request):
    if request.method == 'POST':
        form = HeartForm(request.POST)
        if form.is_valid():
            data = list(form.cleaned_data.values())
            prediction = model.predict([data])
            result = "🔴 Heart Disease Detected" if prediction[0] == 1 else "🟢 No Heart Disease"
            return render(request, 'prediction/result.html', {'result': result})
    else:
        form = HeartForm()
    return render(request, 'prediction/form.html', {'form': form})

