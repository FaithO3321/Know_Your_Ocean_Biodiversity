from django.apps import AppConfig


class QuizConfig(AppConfig):
    """
   Configuration class for the Quiz application.
   Specifies the database field type and application name.
   """
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'quiz'
