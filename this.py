a = input("Masukkan pilihan Player-1 : ").lower()
b = input("Masukkan pilihan Player-2 : ").lower()
arr = ['gunting', 'batu', 'kertas']

if(a and b in arr):
  if(a == arr[0] and b == arr[1]):
    print('Player-2 menang')
  elif(a == arr[1] and b == arr[2]):
    print('Player-2 menang')
  elif(a == arr[2] and b == arr[0]):
    print('Player-2 menang')
  elif(a == b):
    print('Pertandingan seri')
  else:
    print('Player-1 menang')
else:
  print("hanya gunting batu kertas yang di izinkan")


a = int(input("Masukkan banyaknya buku yang akan dibeli : "))
if(a > 1):
  if(a <= 10):
    a *= int(20000)
    print("Harga yang harus dibayar =", a, "Rupiah")
  elif(a <= 25):
    a *= int(18000)
    print("Harga yang harus dibayar =", a, "Rupiah")
  elif(a <= 50):
    a *= int(15000)
    print("Harga yang harus dibayar =", a, "Rupiah")
  elif(a > 50):
    a *= int(10000)
    print("Harga yang harus dibayar =", a, "Rupiah")
else:
  print("Tidak boleh kurang dari 1")

a = int(input("Masukkan sebuah bilangan bulat : "))
for i in range(a):
  if(i % 2 == 0):
    print("# "*a)
  else:
    print("$ "*a)
