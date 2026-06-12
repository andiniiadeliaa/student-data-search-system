data = []

file = open("data.txt", "r")
for baris in file:
    isi = baris.strip().split(",")
    mhs = {
        "nim": isi[0],
        "nama": isi[1],
        "jurusan": isi[2],
        "ipk": float(isi[3])
    }
    data.append(mhs)
file.close()

index_jur = {}
for d in data:
    jur = d["jurusan"]
    if jur in index_jur:
        index_jur[jur].append(d)
    else:
        index_jur[jur] = [d]

index_nama = {}
for d in data:
    nm = d["nama"]
    index_nama[nm] = d

def cari_jurusan(jur):
    if jur in index_jur:
        return index_jur[jur]
    else:
        return []

def cari_nama(nama):
    if nama in index_nama:
        return [index_nama[nama]]
    else:
        return []

print("=== Cari Jurusan SI ===")
hasil_jur = cari_jurusan("SI")

if hasil_jur:
    for m in hasil_jur:
        print(f"{m['nim']} | {m['nama']} | {m['jurusan']} | IPK: {m['ipk']}")
else:
    print("Data tidak ditemukan")


print("\n=== Cari Nama Eka ===")
hasil_nama = cari_nama("Eka")

if hasil_nama:
    for m in hasil_nama:
        print(f"{m['nim']} | {m['nama']} | {m['jurusan']} | IPK: {m['ipk']}")
else:
    print("Data tidak ditemukan")