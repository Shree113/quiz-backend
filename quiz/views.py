from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Question
from .models import User
from .models import Score
from .serializers import QuestionSerializer, ScoreSerializer

@api_view(['GET'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # User must be logged in
def submit_score(request):
    user = request.user
    score_value = request.data.get('score')

    # Store the score in the database
    Score.objects.create(user=user, score=score_value)

    return Response({'message': 'Score submitted successfully!'})

@api_view(['GET'])
def leaderboard(request):
    total_users = Score.objects.count()  # ✅ Count total users who took the quiz
    scores = Score.objects.values('username', 'score').order_by('-score')  # ✅ Get scores only

    return Response({
        "total_users": total_users,
        "scores": list(scores)  # Convert to list to ensure JSON format
    })