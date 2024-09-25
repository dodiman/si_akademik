from rest_framework import serializers
from .models import *

class MatakuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataKuliah
        fields = "__all__"

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = "__all__"

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"