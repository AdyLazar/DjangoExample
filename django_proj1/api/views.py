from rest_framework.response import Response # this respons class will take any data and render it out as json data
from rest_framework.decorators import api_view
from playground.models import Post
from playground.models import LogMessage
from .serializers import PostSerializer
from .serializers import LogMessageSerializer
from rest_framework import permissions

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'list/',
        'Create' : 'create/',
        'Update' : 'update/<str pk>/', #pk -- primary key of the object we want to update
        'Delete' : 'delete/<str pk>/', # --//-- delete
    }
    return Response(api_urls)

@api_view(['GET'])  # the request is to Read data
def getPost(request):
    posts = Post.objects.all() # get all the post from the database
    serializer = PostSerializer(posts, many=True), # we need to serialize our data before we can send it, 
    # many=True means we want to serialize multiple posts
    return Response(serializer.data)

@api_view(['GET'])
def getLogMessage (request):
    LogMessages = LogMessage.objects.all()
    serializer = LogMessageSerializer(LogMessages,many=True)
    return Response(serializer.data)

@api_view(['POST']) # the request is to Create data
def CreateLogMessage (request):
    serializer = LogMessage.Serializer(data=request.data) # raw data we got from the front-end
    if serializer.is_valid(): # make validations on the data
        serializer.save() # save the newly created item to the database
    return Response(serializer.data) # retrun the newly created post to the front-end