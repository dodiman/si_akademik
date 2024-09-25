from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=10, unique=True)
    JK = [
        ("l", "Laki - Laki"),
        ("p", "Perempuan"),
    ]
    jenis_kelamin = models.CharField(max_length=2, choices=JK)
    jurusan = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama} ({self.nim})"
    
class Dosen(models.Model):
    nama = models.CharField(max_length=100)
    nidn = models.CharField(max_length=20, unique=True)
    nuptk = models.CharField(max_length=20, unique=True)
    bidang_keahlian = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    no_hp = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    
class Semester(models.Model):
    SEMESTER = [
        ("I", "I"),
        ("II", "II"),
        ("III", "III"),
        ("IV", "IV"),
        ("V", "V"),
        ("VI", "VI"),
        ("VII", "VII"),
        ("VIII", "VIII"),
    ]
    semester = models.CharField(max_length=5, choices=SEMESTER)

    def __str__(self):
        return self.semester

class MataKuliah(models.Model):
    kode = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    sks = models.IntegerField()
    RUMPUN_MATAKULIAH = [
        ("Institusi", "Institusi"),
        ("Prodi", "Prodi"),
    ]
    rumpun = models.CharField(max_length=20, choices=RUMPUN_MATAKULIAH, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="matakuliahs", null=True, blank=True)

    def __str__(self):
        return self.nama
    
class KeteranganMataKuliah(models.Model):
    
    dosen_penanggung_jawab = models.ForeignKey(Dosen, on_delete=models.CASCADE, null=True, blank=True, related_name="keterangan_kuliahs")
    dosen_pembina = models.ForeignKey(Dosen, on_delete=models.CASCADE, null=True, blank=True)
    kelas = models.CharField(max_length=5, null=True, blank=True)
    matakuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, null=True, blank=True)
    tahun = models.IntegerField(null=True, blank=True)
    PERIODE = [
        ("Ganjil", "Ganjil"),
        ("Genap", "Genap")
    ]
    periode = models.CharField(max_length=10, choices=PERIODE, null=True, blank=True)

    def __str__(self):
        return f"{self.matakuliah} kelas {self.kelas} ({self.periode} {self.tahun})"
    


class Nilai(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    nilai = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.mahasiswa.nama} - {self.mata_kuliah.nama}: {self.nilai}'
    
class JadwalPenilaian(models.Model):
    tugas = models.DateField()
    uts = models.DateField()
    uas = models.DateField()
    dpna = models.DateField()

class BobotPenilaian(models.Model):
    kehadiran = models.IntegerField()
    tugas = models.IntegerField()
    uts = models.IntegerField()
    uas = models.IntegerField()

class PesertaMataKuliah(models.Model):
    matakuliah = models.ForeignKey(KeteranganMataKuliah, on_delete=models.CASCADE)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
