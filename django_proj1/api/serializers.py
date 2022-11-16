from rest_framework import  serializers
from playground.models import Post
from playground.models import LogMessage

#Here we create serializers for our models (i.e tables from the database)

class PostSerializer (serializers.ModelSerializer) : # this class inherits from the ModelSerializer class
    class Meta: # set the meta data (data about data)
        model = Post # what we want to serialize
        fields = '__all__' # the list of fields we would like to serialize

class LogMessageSerializer (serializers.ModelSerializer) :
    class Meta:
        model = LogMessage
        fields = '__all__'