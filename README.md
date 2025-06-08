# Interpolasi Lagrange
## Kode Program

    # rumus Interpolasi Lagrange:
    def LI(x, x_vs, y_vs):
        n = len(x_vs)
        result = 0

        for i in range(n):
            temp = y_vs[i]
            for j in range(n):
                if i != j:
                    temp *= (x - x_vs[j]) / (x_vs[i] - x_vs[j])
            result += temp

        return result

    # data:
    x_vs = [6, 9, 12, 15]
    y_vs = [234, 960, 2280, 4356]

    # f(x) saat:
    x = 11
    # f(11):
    f_x = LI(x, x_vs, y_vs)
    print(f"f({x}) ≈ {f_x:.2f}")

## Penjelasan Kode

  * Fungsi `LI` menerima parameter:

    * `x`: titik yang ingin dicari nilai fungsi interpolasi.
    * `x_vs`: daftar nilai x dari titik data.
    * `y_vs`: daftar nilai y dari titik data.
  * Fungsi menghitung nilai interpolasi dengan rumus polinomial Lagrange:

  <img width="842" alt="Rumus" src="https://github.com/user-attachments/assets/89740255-a134-4757-ba7e-7189dfd0ed64" />


  * `for i in range(n)`: mengiterasi tiap titik data untuk menghitung basis polinomial Lagrange.
  * `for j in range(n)`: menghitung produk untuk `Li(x)` dengan mengalikan pecahan `(x - xj) / (xi - xj)` untuk setiap `j ≠ i`.

  * Variabel `result` menjumlahkan hasil tiap basis dikalikan nilai `yi`.

## Anggota R08

  * Krisna Anugrah Arianto Heru Putro (5053241002)
  * Rafian Dany Azadirahta (5053241008)
  * Sofia Elsa Mahera (5053241011)
