import os
import time
import socket
import requests
import getpass
from colorama import Fore, init

init()

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
C = Fore.CYAN
W = Fore.WHITE

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

def banner():
    os.system("clear")
    print(f"""{G}
╔════════════════════════════╗
║     {B}DTool Terminal Tool     {G}║
╚════════════════════════════╝
""")

def cek_koneksi():
    print(f"{C}Mengecek koneksi internet...")
    try:
        requests.get("https://www.google.com", timeout=5)
        print(f"{G}Koneksi aktif!")
    except:
        print(f"{R}Tidak ada koneksi!")

def ping_website():
    target = input(f"{G}Masukkan domain/IP: ")
    print(f"{B}")
    os.system(f"ping -c 4 {target}")

def dns_lookup():
    domain = input(f"{G}Masukkan domain: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{G}IP Address: {ip}")
    except:
        print(f"{R}Domain tidak ditemukan.")

def ip_tracker():
    ip = input(f"{G}Masukkan IP Address: ")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res["status"] == "success":
            print(f"{C}Negara   : {res['country']}")
            print(f"{C}Kota     : {res['city']}")
            print(f"{C}ISP      : {res['isp']}")
            print(f"{C}Timezone : {res['timezone']}")
        else:
            print(f"{R}IP tidak valid.")
    except:
        print(f"{R}Gagal menghubungi API.")

def youtube_download():
    url = input(f"{G}Masukkan URL YouTube: ")
    print(f"{B}Downloading...")
    os.system(f"yt-dlp -f mp4 {url}")

def tiktok_download():
    url = input(f"{G}Masukkan URL TikTok: ")
    print(f"{B}Mendownload video TikTok...")
    os.system(f"yt-dlp {url}")

def hack_simulasi():
    target = input(f"{G}Masukkan target domain/IP: ")
    print(f"{R}Scanning {target}...")
    for i in range(1, 6):
        print(f"{B}Scanning port {i*111}...")
        time.sleep(0.5)
    print(f"{G}Exploit berhasil ditemukan! (simulasi)")

def cek_balance_safelinku_api():
    print(f"{B}Cek saldo SafelinkU...")
    api_key = "da4ae834895612183fff0f17ade10311afa99c47"  # ← API KEY kamu

    try:
        res = requests.get(f"https://api.safelinku.com/v1/user/info?api_token={api_key}")
        data = res.json()

        if "user" in data:
            name = data["user"]["name"]
            balance = data["user"]["balance"]
            print(f"{G}Nama Pengguna: {name}")
            print(f"{G}Saldo       : ${balance}")
        else:
            print(f"{R}Gagal mengambil data. Periksa API key!")
    except Exception as e:
        print(f"{R}Terjadi kesalahan: {e}")

def main():
    login()
    while True:
        banner()
        print(f"""{W}
[1] Cek Koneksi Internet
[2] Ping Website
[3] DNS Lookup
[4] IP Tracker
[5] Download Video YouTube
[6] Download TikTok
[7] Hack Tool Simulasi
[8] Cek Balance SafelinkU
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
            youtube_download()
        elif pilih == "6":
            tiktok_download()
        elif pilih == "7":
            hack_simulasi()
        elif pilih == "8":
            cek_balance_safelinku_api()
        elif pilih == "0":
            print(f"{C}Keluar...")
            break
        else:
            print(f"{R}Pilihan tidak valid.")
        input(f"\n{C}Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
