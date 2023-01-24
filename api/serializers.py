from rest_framework import serializers
from jobsExtractor.models import Job

class JobSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()

    class Meta:
        model = Job
        fields = ['id', 'company', 'role', 'source', 'url', 'created', 'updated']