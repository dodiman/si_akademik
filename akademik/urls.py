from django.urls import path
from . import views

urlpatterns = [
    path("cari_mahasiswa", views.cari_mahasiswa, name="cari_mahasiswa_akademik"),
    path("cari_semester", views.cari_semester, name="cari_semester_akademik"),
    path("matakuliah", views.matakuliah, name="matakuliah_akademik"),
    path("mahasiswa", views.mahasiswa, name="mahasiswa_akademik"),
    path("krs", views.krs, name="krs_akademik"),
    path("", views.index, name="index_akademik"),
]