from django import forms
from .models import SurveyResponse

class FlightSurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = '__all__'