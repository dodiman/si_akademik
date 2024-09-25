from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.
# class MahasiswaAdmin(admin.ModelAdmin):
#     pass

# class MatakuliahAdmin(admin.ModelAdmin):
#     pass

# class NilaiAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Mahasiswa, MahasiswaAdmin)
# admin.site.register(MataKuliah, MatakuliahAdmin)
# admin.site.register(Nilai, NilaiAdmin)


@admin.register(MataKuliah)
class MatakuliahAdmin1(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MatakuliahResource

@admin.register(Mahasiswa)
class MahasiswaAdmin1(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MahasiswaResource

@admin.register(Nilai)
class NilaiAdmin1(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = NilaiResource

@admin.register(Dosen)
class DosenAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DosenResource

@admin.register(KeteranganMataKuliah)
class KeteranganMataKuliahAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = KeteranganMataKuliah

@admin.register(Semester)
class SemesterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Semester

@admin.register(JadwalPenilaian)
class JadwalPenilaianAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JadwalPenilaian

@admin.register(BobotPenilaian)
class BobotPenilaianAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BobotPenilaian

@admin.register(PesertaMataKuliah)
class PesertaMataKuliahAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PesertaMataKuliah