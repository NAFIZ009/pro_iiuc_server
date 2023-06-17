from django.shortcuts import render

# Create your views here.
import mysql.connector
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import StudentInfo
from myapp.serializers import StudentInfoSerializer


def get_credentials(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    # You can add your custom logic here, such as validating the credentials
    # and returning an appropriate response.

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host='127.0.0.1',
        user='a@mail.com',
        password='(4C7H8p6UwdVEb2',
        database='mysqldb'
    )

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Execute a SELECT query to check if the provided credentials exist in the database
    query = "SELECT * FROM myapp_usercredentials WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    # Fetch the result of the query
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    db.close()

# Check if the credentials match and return the appropriate response
    if result is not None:
        data = {
            'message': 'Credentials are valid.'
        }
        return JsonResponse(data)
    else:
        data = {
            'message': 'Invalid credentials.'
        }
        return JsonResponse(data)

    # For demonstration purposes, we will simply return the credentials in the response.
    # un = "jabin"
    # pas = "nafizerbow"

    # if (username == un and password == pas):
    #     data = {"access": "allowed"}
    # else:
    #     data = {"access": "cancelled"}

    # return JsonResponse(data)

# url = http://localhost:8000/api/credentials/?username=johndoe&password=secretpassword


class StudentInfoView(APIView):
    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data uploaded successfully'}, status=201)
        return Response(serializer.errors, status=400)


class StudentInfoDetailView(APIView):
    def get(self, request, name):
        try:
            student_info = StudentInfo.objects.get(name=name)
            serializer = StudentInfoSerializer(student_info)
            return Response(serializer.data)
        except StudentInfo.DoesNotExist:
            return Response(status=404)