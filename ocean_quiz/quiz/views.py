from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import QuizQuestion


def get_quiz(request):
    """
    Fetch a paginated list of quiz questions filtered by category.
    Supports `limit`, `offset`, and `category` query parameters.
    """
    # Get query parameters with defaults
    limit = int(request.GET.get('limit', 5))  # Default to 5 questions per page
    offset = int(request.GET.get('offset', 0))  # Default starting point
    category = request.GET.get('category', "Ocean Biodiversity")  # Default category filter

    # Filter questions by category
    questions_queryset = QuizQuestion.objects.filter(category__icontains=category)
    total_questions = questions_queryset.count()  # Total number of questions in this category

    # Paginate the questions
    questions = questions_queryset[offset:offset + limit]

    # Format the response data
    data = {
        "data": [
            {
                "question": question.question_text,
                "answer": [
                    {"answer": answer.text, "is_correct": answer.is_correct}
                    for answer in question.answers.all()
                ],
                "uid": question.id,
            }
            for question in questions
        ],
        "pagination": {
            "total": total_questions,
            "limit": limit,
            "offset": offset,
            "next_offset": offset + limit if offset + limit < total_questions else None,
            "prev_offset": offset - limit if offset - limit >= 0 else None,
        },
    }

    # Return the JSON response
    return JsonResponse(data)

