import requests
import json

# URL endpoint untuk mencari acara TV berdasarkan nama
api_url = "https://api.tvmaze.com/singlesearch/shows"

n = int(input("n: "))

for i in range(n):
    # Parameter yang akan dikirimkan ke API, misalnya nama acara TV
    title = input("Tite: ")
    params = {
        "q": title, # Ganti dengan nama acara TV yang ingin dicari
    }

    # Mengirim permintaan GET ke API
    response = requests.get(api_url, params=params)
    print(response.url);

    # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        # Mengambil data JSON dari hasil API
        show_data = response.json();
        for i in show_data:
            if type(show_data[i]) ==  dict:
                print(i, "==> ", end=' ');
                for j in show_data[i]:
                    print(f'{j}\t: {show_data[i][j]}, ',end="");
            else:
                print(f'{i}\t\t: {show_data[i]}')
        # print(show_data);
        
        # jjsn = json.dumps(show_data); #convert  dictionary ke json
        # print(jjsn);
        # print(type(jjsn));
        
        # Menampilkan informasi acara TV
        # print("--------------------")
        # print(f"Judul Acara: {params['q']}")
        # print(f"Deskripsi: {show_data['summary'].strip('<p>').strip('</p>')}")
        # print(f"Status: {show_data['status']}")
        # print(f"Tanggal Premier: {show_data['premiered']}")
        # print(f"Skor: {show_data['rating']['average']}")
        # print(f"Link: {show_data['officialSite']}")
    else:
        print(f"Terjadi kesalahan: {response.status_code}")
        print("--------------------")
