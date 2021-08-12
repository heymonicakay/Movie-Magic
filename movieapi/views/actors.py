"""View module for handling requests about actors"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from movieapi.models import Actor


class ActorView(ViewSet):
    """Movie Server actors"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single actor

        Returns:
            Response -- JSON serialized actor
        """
        try:
            actor = Actor.objects.get(pk=pk)
            serializer = ActorSerializer(actor, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all actors

        Returns:
            Response -- JSON serialized list of actors
        """
        actors = Actor.objects.all()
        
        serializer = ActorSerializer(
            actors, many=True, context={'request': request})
        return Response(serializer.data)

class ActorSerializer(serializers.ModelSerializer):
    """JSON serializer for actors

    Arguments:
        serializers
    """
    class Meta:
        model = Actor
        fields = ('id', 'full_name')
