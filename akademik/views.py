from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import MataKuliah

def krs(request):
    return render(request, "krs.html")

@api_view(['GET'])
def cari_semester(request):
    if request.method == 'GET':
        semester = request.GET.get("semester", "")
        try:
            semester = Semester.objects.get(semester=semester)
            matakuliah = semester.matakuliahs.all()
            serializers = MatakuliahSerializer(matakuliah, many=True)
            return Response(serializers.data)
        except Semester.DoesNotExist:
            return Response({"pesan": "tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def matakuliah(request):
    if request.method == 'GET':
        data_matakuliah = MataKuliah.objects.all()
        serializers = MatakuliahSerializer(data_matakuliah, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def cari_mahasiswa(request):
    if request.method == 'GET':
        nim = request.GET.get('nim', '')
        try:
            data_mahasiswa = Mahasiswa.objects.get(nim=nim)
            print(data_mahasiswa)
            serializers = MahasiswaSerializer(data_mahasiswa, many=False)
            return Response(serializers.data)
        except Mahasiswa.DoesNotExist:
            return Response({"detail": "nim tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def mahasiswa(request):
    if request.method == 'GET':
        data_mahasiswa = Mahasiswa.objects.all()
        serializer = MahasiswaSerializer(data_mahasiswa, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        serializer = MatakuliahSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        matakuliah = MataKuliah.objects.all()
        serializer = MatakuliahSerializer(matakuliah, many=True)
        return Response(serializer.data)