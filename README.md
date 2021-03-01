# Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)


## Deskripsi
Topological sort ini merupakan suatu kasus pengurutan, dimana pengurutan dilakukan terhadap elemen-elemen pada suatu himpunan, dengan mempertimbangkan keterurutan parsial dari elemen-elemen tersebut.
Algoritma Decrease and Conquer terdiri dari dua tahapan:
1.	Decrease: mereduksi persoalan menjadi beberapa persoalan yang lebih kecil (biasanya dua upa-persoalan).
2.	Conquer: memproses satu upa-persoalan secara rekursif.
      Tidak ada tahap combine dalam decrease and conquer, karena hanya satu upa-persoalan yang diselesaikan.

## Contoh Persoalan
Sebagai contoh, Mata kuliah Matematika Teknik memiliki prerequisite berupa Mata Kuliah Kalkulus IA. Sehingga untuk mengambil mata kuliah matematika teknik seseorang harus mengambil mata kuliah kalkulus IA terlebih dahulu. Namun untuk kasus lain, mata kuliah Struktur diskrit tidak memiliki prerequisite sehingga bisa diambil bersamaan dengan Mata Kuliah Matematika Teknik ataupun setelah atau sebelum mengambil Mata Kuliah Matematika Teknik, sehingga terdapat beberapa alternatif posisi pengurutan Mata Kuliah Struktur Diskrit. Pada kasus ini hasil pengurutan yang didapat berupa urutan mata pelajaran yang bisa diambil secara linear.

## Bahasa Pemrograman
Python 3

## Cara menggunakan program (file executable)
Masuk Ke folder bin
jalankan file main.exe

## Cara menggunakan program (file python)
Masuk Kedalam termiminal dengan alamat file Tucil2_13519136 berada
Masuk ke folder src
jalankan file main.py

## Alur Main Program
Meminta inpuntan Nama dan NIM (formalitas)
Menampilkan list file test dalam forder test
Memasukkan Nama File yang sesuai (contoh: paket_2.txt)
Menampilkan output program
Menampilkan Pesan "Proses Selesai"


## Menambahkan File Test
Untuk semua file test harus berada adalam folder test.
Apabila ingin menguji dengan file baru, file tersebut harus berada di folder test yang satu tingkat dengan folder src/bin.

## Spesifikasi file input
File harus berada dalam forder test dan setiap matakuliah terdapat pembeda (spasi) antara matakuliah dengn prasyaratnya.

<kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah
prasyarat - 3>.

<kode_kuliah_2>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.

<kode_kuliah_3>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah
prasyarat - 3>, <kode kuliah prasyarat - 4>.

<kode_kuliah_4>.

.

.
## Contoh isi file teks:
Logkom.

Alstrukdat.

RPL, TBFO.

AI, Logkom, Algeo, Stima.

WBD, RPL.

Orkom.

OOP, Alstrukdat.

Stima, Matdis.

Probstat, Matdis, Algeo.

OS, Orkom.

Basdat, Alstrukdat.

MachineLearning, AI, Probstat, Algeo, Stima.

Sispar, OS, Orkom, Jarkom.

PPL, RPL, MRPL.

Grafkom, IMK, Algeo.

SocioIF, AI, MRPL.

Jarkom, OS, Orkom.

SI, Basdat.

MRPL, RPL.

MBD, Basdat.

IMK, OOP, Probstat.

PDA, WBD, MRPL.

Matdis.

TBFO.

Algeo.

KP, Alstrukdat, OOP, AI, PDA.

TA1, SocioIF.

TA2, TA1.

## Contact
[Muhammad Rizal Muhaimin](https://github.com/MrizalMuhaimin)
NIM: 13519136



