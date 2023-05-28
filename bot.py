import requests
from instagram_private_api import Client, ClientCompatPatch

# Instagram API ayarları
username = 'KULLANICI_ADINIZ'
password = 'ŞİFRENİZ'
api = Client(username, password)

# Deprem API'si ayarları
deprem_api_url = 'https://api.orhanaydogdu.com.tr/deprem/kandilli/live'

# Deprem verilerini alma ve hikaye paylaşma işlemi
def get_deprem_verileri():
    # Deprem API'sinden verileri al
    response = requests.get(deprem_api_url)
    data = response.json()
    deprem_verileri = data['result']
    
    # İlk deprem verisini al
    deprem = deprem_verileri[0]
    
    # Deprem bilgilerini al
    deprem_buyuklugu = deprem['mag']
    deprem_yeri = deprem['location_properties']['epiCenter']['name']
    tarih_zaman = deprem['date']
    
    # Hikaye metnini oluştur
    hikaye_metni = f"Yeni bir deprem! 🌍\n\nBüyüklük: {deprem_buyuklugu}\nYer: {deprem_yeri}\nTarih ve Zaman: {tarih_zaman}"
    
    # Hikayeyi paylaş
    api.post_photo(photo='hikaye_gorseli.jpg', caption=hikaye_metni, options={'story_duration': 24 * 60 * 60})

# Botu çalıştırma
if __name__ == '__main__':
    get_deprem_verileri()
