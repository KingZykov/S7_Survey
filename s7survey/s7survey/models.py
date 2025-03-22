from django.db import models

class SurveyResponse(models.Model):
    flight_number = models.IntegerField()
    mark = models.CharField(max_length=12)
    comments = models.TextField(max_length=5000, blank=True, null=True)

    class Meta:
        db_table = "s7survey"  # Указываем, что модель соответствует таблице s7survey

    def __str__(self):
        return f"Flight {self.flight_number} - Mark: {self.mark}"