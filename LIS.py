import math

def compare(p1, p2):
    # Fungsi perbandingan khusus untuk mengurutkan pasangan
    # Jika elemen pertama sama, pasangan dengan elemen kedua lebih kecil
    if p1[0] == p2[0]:
        return p1[1] < p2[1]
    return p1[0] < p2[0]

def buildTree(tree, pos, low, high, index, value):
    # Fungsi untuk membangun pohon segmen
    # Secara rekursif memperbarui pohon dengan panjang LIS untuk setiap indeks
   
	if index < low or index > high:
		return
	if low == high:
		tree[pos] = value
		return
	mid = (high + low) // 2
	buildTree(tree, 2 * pos + 1, low, mid, index, value)
	buildTree(tree, 2 * pos + 2, mid + 1, high, index, value)
	tree[pos] = max(tree[2 * pos + 1], tree[2 * pos + 2])

def findMax(tree, pos, low, high, start, end):
    # Fungsi untuk mengambil nilai maksimum dari pohon segmen untuk rentang tertentu
    
	if low >= start and high <= end:
		return tree[pos]
	if start > high or end < low:
		return 0
	mid = (high + low) // 2
	return max(findMax(tree, 2 * pos + 1, low, mid, start, end),
			findMax(tree, 2 * pos + 2, mid + 1, high, start, end))


def findLIS(arr):
    # Fungsi untuk menemukan panjang Subsequence Peningkatan Terpanjang (LIS)
    n = len(arr)
    # Membuat pasangan elemen dengan indeks asli
    p = [(arr[i], i) for i in range(n)]
    # Mengurutkan pasangan berdasarkan elemen pertama dan kemudian elemen kedua secara terbalik
    p.sort(key=lambda x: (x[0], -x[1]))
    # Menghitung panjang pohon segmen
    len_tree = 2 * (2 ** (int(math.ceil(math.log2(n)))) - 1)
    # Menginisialisasi pohon segmen dengan nilai nol
    tree = [0] * len_tree
    # Membangun pohon segmen dengan memperbarui panjang LIS untuk setiap indeks
    for i in range(n):
        buildTree(tree, 0, 0, n - 1, p[i][1],
                  findMax(tree, 0, 0, n - 1, 0, p[i][1]) + 1)
    # Mengembalikan panjang LIS untuk seluruh array
    return tree[0]


# Main
arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
print("Panjang LIS:", findLIS(arr))
print("Salah satu array yang memenuhi: 1, 2, 8, 11")
