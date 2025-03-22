from django.shortcuts import render, redirect
from .models import SurveyResponse

def survey_view(request):
    if request.method == "POST":
        flight_number = request.POST.get("flight_number")
        rating = request.POST.get("rating")
        feedback = request.POST.get("feedback")

        SurveyResponse.objects.create(
            flight_number=flight_number,
            mark=rating,
            comments=feedback
        )

        # Перенаправляем пользователя, чтобы избежать повторной отправки формы
        return redirect("/?success=1")  

    success_message = "Спасибо! Ваш отзыв успешно отправлен." if request.GET.get("success") else ""
    
    return render(request, "survey.html", {"success_message": success_message})
