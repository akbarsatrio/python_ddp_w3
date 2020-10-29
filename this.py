# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
a = input("Masukan pilihan Player-1 : ").lower()  #buat player1
b = input("Masukan pilihan Player-2 : ").lower()  #buat player2
arr = ['gunting', 'batu', 'kertas']	#array buat validasi input

#arr[0] = gunting
#arr[1] = batu
#arr[2] = kertas

#in arr dimaksudkan untuk membaca isi di dalam variabel arr
if a and b in arr:
  if  a == arr[0] and b == arr[1]:
    print("Player 2 menang")
  elif a == arr[1] and b == arr[2]:
    print("Player 2 menang")
  elif a == arr[2] and b == arr[0]:
    print("Player 2 menang")
  elif a == b in arr:
    print("Pertandingan seri")
	#Jika selain diatas,  bisa diambil keimpulan bahwa player 1 menang
  else:
    print("Player 1 menang")
else:
	#ini muncul jika kedua player memasukan value selain gunting batu kertas.bin
  print("Hanya boleh masukan gunting batu kertas")
print('\n')




# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
a = int(input("Masukkan banyaknya buku yang akan dibeli : "))

#validasi jika user input dibawah 1
if a > 1:
	#jika dibawah 10, harga menjadi 20ribu dikalikan dengan angka masuk di variabel a
  if a <= 10:
    a *= int(20000)
    print("Harga yang harus dibayar =", a, "Rupiah")

	#jika dibawah 25, harga menjadi 18ribu dikalikan dengan angka masuk di variabel a
  elif a <= 25:
    a *= int(18000)
    print("Harga yang harus dibayar =", a, "Rupiah")
	
	#jika dibawah 50, harga menjadi 15ribu dikalikan dengan angka masuk di variabel a
  elif a <= 50:
    a *= int(15000)
    print("Harga yang harus dibayar =", a, "Rupiah")
	
	#jika diatas 50, harga menjadi 10ribu dikalikan dengan angka masuk di variabel a
  elif a > 50:
    a *= int(10000)
    print("Harga yang harus dibayar =", a, "Rupiah")
else:
  print("Tidak boleh kurang dari 1")
print('\n')


# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
a = int(input("Masukkan sebuah bilangan bulat : "))

for i in range(1, a+1): #membaca dari angka 1, karena angka 1 merupakan bilangan ganjil.
  if i % 2 == 0:
    print("$ "*a ,i)
  else:
    print("# "*a ,i)



