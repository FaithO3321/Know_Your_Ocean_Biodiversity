from django.db import models

class QuizQuestion(models.Model): # Represents a question in a quiz
    category = models.CharField(max_length=100, default="Ocean Biodiversity")
    question_text = models.TextField()
    
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
