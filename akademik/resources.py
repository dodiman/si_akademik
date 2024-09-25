from import_export import resources
from .models import *

class MatakuliahResource(resources.ModelResource):
    class Meta:
        model = MataKuliah


class NilaiResource(resources.ModelResource):
    class Meta:
        model = Nilai

class MahasiswaResource(resources.ModelResource):
    class Meta:
        model = Mahasiswa

class DosenResource(resources.ModelResource):
    class Meta:
        model = Dosen

class KeteranganKuliahResource(resources.ModelResource):
    class Meta:
        model = KeteranganMataKuliah

class SemesterResource(resources.ModelResource):
    class Meta:
        model = Semester

class JadwalPenilaianResource(resources.ModelResource):
    class Meta:
        model = JadwalPenilaian

class BobotPenilaianResource(resources.ModelResource):
    class Meta:
        model = BobotPenilaian

class PesertaMataKuliahResorce(resources.ModelResource):
    class Meta:
        model = PesertaMataKuliah