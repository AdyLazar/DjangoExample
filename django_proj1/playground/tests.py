from django.test import TestCase
import json
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.serializers import PostSerializer
from .models import LogMessage 
# Create your tests here.
#Testing for the REST API
class Creation_TestCase (APITestCase): # testing for the creation of LogMessage 
    def test_CreateLogMessage(self):
        data = {"message":"massage1", "log_date": datetime.now}
        response = self.client.post("api/log/create",data) # we provide the n-point and the data we want to test
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)