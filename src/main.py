#Nama       : Muhammad Rizal Muhaimin
#Nim        : 13519136
#Deskripsi  : Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)


import os

def Tampilan_Awal():
    print(
    """
===================================================================
         Penyusunan Rencana Kuliah dengan Topological Sort 
                 (Penerapan Decrease and Conquer)
             Tugas Kecil 2 IF2211 Strategi Algoritma
                   Semester II tahun 2020/2021
===================================================================\n""" 
            )

def Tampilan_login():
    Nama = input("Masukkan Nama :> ")
    NIM =  input("Masukkan NIM  :> ")
    print("\nHai", Nama, NIM)
    print("Berikut daftar paket kuliah khusus buat kamu (^_^) ")
    

def List_file_test ():
    #membaca list file yang ada di file test
    print("\nDaftar file paket kuliah :\n")
    path = "../test"
    Dir_test = os.listdir(path)
    for namefile in Dir_test:
        print(namefile)


def Retrun_List_Graf():
    nfile = input("\nMasukkan Nama File\n:> ")
    try:
        path = "../test/"+str(nfile)
        File = open(path, 'r')
        Line = File.readline()
        list_graf = list()
        List_DAG = list()
        while Line:
            #MANIPULASI STRING
            s = Line
            s = s.replace("."," ")
            s = s.replace(",", " ")
            s = s.replace("\n"," ")
            s = s.split(" ")
            
            #MENJADIKAN LIST OF LIST
            for i in range(len(s)):
                if s[i] != "":
                    List_DAG.append(s[i])
            list_graf.append(List_DAG[:len(List_DAG)])
            List_DAG.clear()
            Line = File.readline()
        return list_graf
    except:
        print("\n================= ============================== =================\n")
        print("Maaf Nama File salah")
        print("\n================= ============================== =================\n")


# Bagian dari Topological Sort
def retrun_graf_not_pre(list_graf, list_baru, n, len_list_graf):
    #MENGEMBALIKAN LIST GRAF YANG TIDAK MEMILIKI PRASYARAT
    if n == len_list_graf:
        return list_baru 
    else :
        if (len(list_graf[n])== 1):
            list_baru.append(list_graf[n][0])
            list_graf.remove(list_graf[n])
            n -= 1
        n += 1
        return retrun_graf_not_pre(list_graf,list_baru,n,len(list_graf))


# Bagian dari Topological Sort
def retrun_list_per_semester(list_graf,list_baru, list_semester):
    #MENGEMBALIKAN LIST PER SEMSETER
    if  len(list_graf) == 0: #basis
        #penambahan list matakuliah tinggkat akhir
        list_semester.append(list_baru[0:len(list_baru)])
        return list_semester
    else:
        #menhapus matakulia yang sudah di ambil
        for j in range(len(list_graf)):
            pop_list = list_graf.pop()
            for k in list_baru:
                if k in pop_list: 
                    pop_list.remove(k) 
            list_graf.insert(0,pop_list)
        list_semester.append(list_baru[0:len(list_baru)])
        list_baru.clear()
        list_baru = retrun_graf_not_pre(list_graf,list_baru, 0, len(list_graf))
        #rekursif
        return retrun_list_per_semester(list_graf,list_baru, list_semester)


def Menampilkan_Matkul_Semester(list_semester):
    print("\n================= Daftar Matakuliah per Semester =================\n")
    
    semester = 1
    for List_matkul in list_semester:
        print("Semester ", semester,": ", end="")
        for i in range(len(List_matkul)):
        

            if  semester == len(list_semester) and i+1 == len(List_matkul):
                print(List_matkul[i] +str("."), end="")
            else:
                print(List_matkul[i] +str(", "), end="")
        print("\n")
        semester += 1
    print("================= ============================== =================\n")


def main():
    #inisualisasi variabel
    list_semester = list()
    list_baru = list()
    list_graf = Retrun_List_Graf()
    list_semester = retrun_list_per_semester(list_graf, retrun_graf_not_pre(list_graf,list_baru, 0, len(list_graf)), list_semester)    
    Menampilkan_Matkul_Semester(list_semester)
 
  
#MAIN PROGRAM
run = True
Tampilan_Awal()
Tampilan_login()
while run:
    List_file_test ()
    main()
    N = input("Mau lihat paket lain? (Y) :> ")
    print("\n================= ============================== =================\n")
    if N != "Y":
        run = False
        print("Anda keluar dari sistem")


