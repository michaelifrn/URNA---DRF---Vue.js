from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status

from .models import Candidate, Vote, Voters
from .serializers import CandidateSerializer, VoteSerializer, VotersSerializer, reportSerializer


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=False, methods=['post'])
    def create_candidate(self, request, *args, **kwargs):
        num = request.data.get('number')

        if Candidate.objects.filter(number=num).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
        candidate = self.get_serializer(data=request.data)
        candidate.is_valid(raise_exception=True)
        self.perform_create(candidate)
        return Response(status=status.HTTP_201_CREATED)
    
class VoteView(APIView):

    def get(self, request):
        query = Vote.objects.all()
        serializer = VoteSerializer(query, many = True)
        return Response(serializer.data)


    def post(self, request):
        reg = request.data.get('registration')

        if Voters.objects.filter(reg=reg).exists():
            voter = Voters.objects.get(reg=reg)
            if voter.status == False:
                serializer = VoteSerializer(data=request.data)
                if serializer.is_valid():
                    voter.status = True
                    voter.save()
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return JsonResponse({'error': 'Não foi possível encontrar essa chapa.'}, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({'error': 'Não é possível votar duas vezes.'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': 'Não foi possível encontrar sua matrícula.'}, status=status.HTTP_400_BAD_REQUEST)

class VotersView(APIView):

    def get(self, request):
        query = Voters.objects.all()
        serializer = VotersSerializer(query, many = True)
        return Response(serializer.data)


class reportView(APIView):

    def get(slef, request):
        candidates = Candidate.objects.all()
        candidate_data = []
        
        for candidate in candidates:
            votes = Vote.objects.filter(number=candidate.number).count()
            candidate_data.append({
                'name': candidate.name,
                'number': candidate.number,
                'votes': votes,
            })
        
        serializer = reportSerializer(candidate_data, many=True)
        return Response(serializer.data)