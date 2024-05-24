# import sqlite3

# baglanti = sqlite3.connect("1000kitap.db")
# kursor = baglanti.cursor()

# def cedvel_yarat():
#     kursor.execute("""
#     CREATE TABLE IF NOT EXISTS kitaplar(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ad TEXT, 
#         muellif TEXT, 
#         nesriyyat TEXT, 
#         sehife_sayi INT
#     )""")
#     baglanti.commit()

# def melumat_elave_et():
#     kursor.execute("INSERT INTO kitaplar (ad, muellif, nesriyyat, sehife_sayi) VALUES ('Göytəpə', 'Süleyman Əlisa', 'Qanun', 240)")
#     baglanti.commit()

# def dinamik_melumat_elave_et(ad, muellif, nesriyyat, sehife_sayi):
#     kursor.execute("INSERT INTO kitaplar (ad, muellif, nesriyyat, sehife_sayi) VALUES (?, ?, ?, ?)", (ad, muellif, nesriyyat, sehife_sayi))
#     baglanti.commit()

# def melumatlari_goster():
#     kursor.execute("SELECT * FROM kitaplar")  
#     data = kursor.fetchall()
#     for row in data:
#         print(row)

# def dinamik_goster(muellif):
#     kursor.execute("SELECT ad FROM kitaplar WHERE muellif=?", (muellif, ))  
#     data = kursor.fetchall()
#     for row in data:
#         print(row)

# def muellif_duzelt(kohne_muellif, yeni_muellif):
#     kursor.execute("UPDATE kitaplar SET muellif=? WHERE muellif=?", (yeni_muellif, kohne_muellif))
#     baglanti.commit()

# def nesriyyat_duzelt(kohne_nesriyyat, yeni_nesriyyat):
#     kursor.execute("UPDATE kitaplar SET nesriyyat=? WHERE nesriyyat=?", (yeni_nesriyyat, kohne_nesriyyat))
#     baglanti.commit()

# def melumat_sil(muellif):
#     kursor.execute("DELETE FROM kitaplar WHERE muellif=?", (muellif,))
#     baglanti.commit()

# cedvel_yarat()
# melumat_elave_et()
# dinamik_melumat_elave_et('Yeni Kitab', 'Yeni Yazar', 'Yeni Nəşriyyat', 200)
# melumatlari_goster()
# dinamik_goster('Süleyman Əlisa')
# muellif_duzelt('Süleyman Əlisa', 'Süleyman')
# nesriyyat_duzelt('Qanun', 'Qanun nəşriyyat')
# melumat_sil('Yeni Yazar')

# baglanti.close()
