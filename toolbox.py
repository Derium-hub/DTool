import os
import socket
import requests
import time
import random
import getpass
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

# Fungsi login password
def login():
    password_benar = "Derium289"
    percobaan = 3
    while percobaan > 0:
        try:
            pw = getpass.getpass("Masukkan password: ")
        except Exception:
            print(f"{R}Terminal tidak mendukung getpass. Gunakan input biasa.")
            pw = input("Masukkan password: ")

        if pw == password_benar:
            print(f"{G}Akses diterima!\n")
            time.sleep(1)
            return True
        else:
            percobaan -= 1
            print(f"{R}Password salah. Sisa percobaan: {percobaan}")
    print(f"{R}Gagal login. Keluar...")
    exit()

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

# Fungsi 4: IP Tracker
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

# Fungsi 5: Download video YouTube
def download_youtube():
    url = input(f"{G}Masukkan URL YouTube: ")
    print(f"{B}Mengunduh video...")
    os.system(f"yt-dlp -f mp4 {url}")

# Fungsi 6: Download video & audio TikTok
def download_tiktok():
    url = input(f"{G}Masukkan URL TikTok: ")
    print(f"{B}Mengunduh video dan audio dari TikTok...\n")
    os.system(f"yt-dlp -f mp4 {url} -o '%(title)s.%(ext)s'")
    os.system(f"yt-dlp -x --audio-format mp3 {url} -o '%(title)s.%(ext)s'")

# Fungsi 7: Simulasi Hack Website Scanner
def hack_simulasi_scanner():
    target = input(f"{G}Masukkan target website (tanpa https): ")
    print(f"{B}Menjalankan simulasi hacking ke {target}...\n")

    print(f"{B}[•] Resolving domain...")
    time.sleep(1)
    try:
        ip = socket.gethostbyname(target)
        print(f"{G}[✓] IP ditemukan: {ip}")
    except:
        print(f"{R}[✗] Gagal resolve domain.")
        return
    time.sleep(1)

    print(f"{B}[•] Memindai port umum...")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{G}[OPEN] Port {port}")
        else:
            print(f"{R}[CLOSED] Port {port}")
        sock.close()
        time.sleep(0.2)

    print(f"{B}[•] Mengambil header web...")
    try:
        headers = requests.get(f"http://{target}", timeout=5).headers
        for key, value in headers.items():
            print(f"{G}{key}: {value}")
    except:
        print(f"{R}Gagal ambil header.")

    print(f"{B}[•] Menjalankan exploit dummy...\n")
    for i in range(5):
        print(f"{G}[*] Menginjeksi payload-{i}...")
        time.sleep(0.3)
    print(f"\n{G}[✓] Simulasi selesai. Tidak ada kerentanan ditemukan.\n")

# Menu utama
def main():
    login()
    while True:
        banner()
        print(f"""{B}
[1] Cek Koneksi Internet
[2] Ping Website
[3] DNS Lookup
[4] IP Tracker
[5] Download YouTube Video
[6] Download TikTok (Video & Audio)
[7] Simulasi Hack Tool (Website Scanner)
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
        elif pilih == "6":
            download_tiktok()
        elif pilih == "7":
            hack_simulasi_scanner()
        elif pilih == "0":
            print(f"{R}Keluar...")
            break
        else:
            print(f"{R}Pilihan tidak valid.")
        input(f"{B}\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
