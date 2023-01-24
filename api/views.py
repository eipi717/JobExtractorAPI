from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from .serializers import JobSerializer
from jobsExtractor.models import Job
# from django_filters.rest_framework import FilterSet, filters
from django.db import transaction
from django_filters import rest_framework as filters

# Create your views here.

"""
Implement using functional way
"""
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List all jobs': '/listjobs',
        'List job by ID': '/listjob/<id>/',
        'Create job': '/createjob/',
        'Update job': '/updatejob/<id>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def listAllJob(request):
    if request.GET:
        # TODO: filter by other attributes
        jobs = Job.objects.filter(source=request.GET['source'])
    else:
        jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listJobByID(request, id):
    job = Job.objects.get(id=id)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createJob(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        print("Valid data!")
        serializer.save(user=request.user)

    return Response(serializer.data)


@api_view(['POST'])
def updateJob(request, id):
    job = Job.objects.get(id=id)
    serializer = JobSerializer(instance=job, data=request.data)

    if serializer.is_valid(raise_exception=True):
        job.updated = timezone.now()
        serializer.save(user=request.user)

    return Response(serializer.data)


@api_view(['GET'])
def deleteJobByID(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return Response("Item deleted!")



