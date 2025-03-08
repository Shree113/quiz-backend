from rest_framework import serializers
from .models import Question, Score

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField() 
    
    class Meta:
        model = Question
        fields = ['id', 'question', 'options', 'correct_option']

    def get_options(self, obj):
        return [obj.option_1, obj.option_2, obj.option_3, obj.option_4] 


class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Show username instead of ID

    class Meta:
        model = Score
        fields = '__all__'