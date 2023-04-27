from rest_framework import serializers
from .models import Candidate, Vote, Voters

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class VotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = '__all__'

class reportSerializer(serializers.Serializer):
    name = serializers.CharField()
    number = serializers.IntegerField()
    votes = serializers.IntegerField()