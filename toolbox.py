import os
import socket
import requests
from colorama import Fore, init

# Inisialisasi warna
init(autoreset=True)
B = Fore.BLUE
G = Fore.GREEN
R = Fore.RED

# Banner simpel
def banner():
    os.system("clear")
    print(f"{G}╔══════════════════════════╗")
    print(f"{B}║      DTool Terminal      ║")
    print(f"{R}╚══════════════════════════╝\n")

# Fungsi 1: Cek koneksi internet
def cek_koneksi():
    print(f"{B}Mengecek koneksi internet...")
    try:
        requests.get("https://www.google.com", timeout=5)
        print(f"{G}[✓] Internet aktif")
    except:
        print(f"{R}[✗] Tidak terhubung ke internet")

# Fungsi 2: Ping Website
def ping_website():
    target = input(f"{G}Masukkan URL/IP: ")
    print(f"{B}Ping ke {target}...\n")
    os.system(f"ping -c 4 {target}")

# Fungsi 3: DNS Lookup
def dns_lookup():
    domain = input(f"{G}Masukkan nama domain: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{G}Alamat IP: {ip}")
    except socket.gaierror:
        print(f"{R}Domain tidak ditemukan!")

# Fungsi 4: IP Tracker (lokasi)
def ip_tracker():
    ip = input(f"{G}Masukkan IP target: ")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            print(f"""
{G}Negara   : {res['country']}
Kota     : {res['city']}
ISP      : {res['isp']}
Lokasi   : {res['lat']}, {res['lon']}
""")
        else:
            print(f"{R}IP tidak ditemukan atau diblokir.")
    except:
        print(f"{R}Gagal mengambil data lokasi IP.")

# Fungsi 5: Download video YouTube (yt-dlp harus terinstal)
def download_youtube():
    url = input(f"{G}Masukkan URL YouTube: ")
    print(f"{B}Mengunduh video...")
    os.system(f"yt-dlp -f mp4 {url}")

# Menu utama
def main():
    while True:
        banner()
        print(f"""{B}
[1] Cek Koneksi Internet
[2] Ping Website
[3] DNS Lookup
[4] IP Tracker
[5] Download Video YouTube
[0] Keluar
""")
        pilih = input(f"{G}Pilih menu: ")
        if pilih == "1":
            cek_koneksi()
        elif pilih == "2":
            ping_website()
        elif pilih == "3":
            dns_lookup()
        elif pilih == "4":
            ip_tracker()
        elif pilih == "5":
            download_youtube()
        elif pilih == "0":
            print(f"{R}Keluar...")
            break
        else:
            print(f"{R}Pilihan tidak valid.")
        input(f"{B}\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
