import requests
import json

# URL endpoint untuk mencari acara TV berdasarkan nama
api_url = "https://api.tvmaze.com/singlesearch/shows"

n = int(input("n: "))

for i in range(n):
    # Parameter yang akan dikirimkan ke API, misalnya nama acara TV
    title = input("Tite: ")
    negara = input("country: ")
    params = {
        "q": title, # Ganti dengan nama acara TV yang ingin dicari
        "country": negara
    }

    # Mengirim permintaan GET ke API
    response = requests.get(api_url, params=params)

    # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        # Mengambil data JSON dari hasil API
        show_data = response.json()
        print(show_data)
        # Menampilkan informasi acara TV
        print(f"Judul Acara: {params['q']}")
        print(f"Deskripsi: {show_data['summary'].strip('<p>').strip('</p>')}")
        print(f"Status: {show_data['status']}")
        print(f"Tanggal Premier: {show_data['premiered']}")
        print(f"Negara dari params: {params['country']}")
        print(f"Skor: {show_data['rating']['average']}")
        print(f"Link: {show_data['officialSite']}")
        print("--------------------")
    else:
        print(f"Terjadi kesalahan: {response.status_code}")
        print("--------------------")
