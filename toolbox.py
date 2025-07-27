import os
import sys
import time
import json
import socket
import requests
import validators
import subprocess
import qrcode
import speedtest
from bs4 import BeautifulSoup
from pytube import YouTube
from colorama import Fore, init
from fake_useragent import UserAgent
import instaloader
from yt_dlp import YoutubeDL
from getpass import getpass

init(autoreset=True)

PASSWORD = "Derium289"

def login():
    os.system("clear")
    print(Fore.CYAN + "DTool Login\n" + "-"*20)
    attempt = getpass("Masukkan password: ")
    if attempt != PASSWORD:
        print(Fore.RED + "Password salah!")
        sys.exit()
    print(Fore.GREEN + "Login berhasil!")
    time.sleep(1)

def show_menu():
    os.system("clear")
    print(Fore.BLUE + "="*40)
    print(Fore.GREEN + "        🔧 DTool Main Menu")
    print(Fore.BLUE + "="*40)
    print(Fore.RED + "[01]") ; print(Fore.WHITE + "Cek IP & Lokasi")
    print(Fore.RED + "[02]") ; print(Fore.WHITE + "Download TikTok (audio/video)")
    print(Fore.RED + "[03]") ; print(Fore.WHITE + "Download YouTube (audio/video)")
    print(Fore.RED + "[04]") ; print(Fore.WHITE + "Download Instagram Reel")
    print(Fore.RED + "[05]") ; print(Fore.WHITE + "Download Facebook Video")
    print(Fore.RED + "[06]") ; print(Fore.WHITE + "Download Twitter/X Video")
    print(Fore.RED + "[07]") ; print(Fore.WHITE + "Screenshot Halaman Web")
    print(Fore.RED + "[08]") ; print(Fore.WHITE + "Email Verifier")
    print(Fore.RED + "[09]") ; print(Fore.WHITE + "Fake Identity Generator")
    print(Fore.RED + "[10]") ; print(Fore.WHITE + "DDoS Simulasi (Non-Destruktif)")
    print(Fore.RED + "[11]") ; print(Fore.WHITE + "WhatsApp Number Checker")
    print(Fore.RED + "[12]") ; print(Fore.WHITE + "QR Code Generator")
    print(Fore.RED + "[13]") ; print(Fore.WHITE + "Speed Test")
    print(Fore.RED + "[00]") ; print(Fore.WHITE + "Keluar")
    print(Fore.BLUE + "="*40)

def cek_ip_lokasi():
    ip = requests.get("https://api.ipify.org").text
    info = requests.get(f"https://ipinfo.io/{ip}/json").json()
    print(Fore.GREEN + f"\nIP Anda: {ip}")
    for k, v in info.items():
        print(f"{k.capitalize()}: {v}")

def download_tiktok():
    url = input("Masukkan URL TikTok: ")
    if not validators.url(url):
        print(Fore.RED + "URL tidak valid!")
        return
    headers = {'User-Agent': UserAgent().random}
    r = requests.get(f"https://ssstik.io/abc?url={url}", headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    video = soup.find("a", attrs={"class": "download-link"})
    if video:
        print("Download link:", video["href"])
    else:
        print(Fore.RED + "Gagal mengambil video.")

def download_youtube():
    url = input("Masukkan URL YouTube: ")
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_instagram():
    url = input("Masukkan URL Reels Instagram: ")
    loader = instaloader.Instaloader()
    try:
        loader.download_post(instaloader.Post.from_shortcode(loader.context, url.split("/")[-2]), target="download")
        print(Fore.GREEN + "Download selesai.")
    except:
        print(Fore.RED + "Gagal mendownload.")

def download_facebook():
    url = input("Masukkan URL Facebook Video: ")
    headers = {"User-Agent": UserAgent().random}
    res = requests.get("https://fdown.net", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    # Simulasi saja karena scraping bisa berubah
    print(Fore.YELLOW + "Fitur ini bersifat simulasi. Link FB tidak diproses penuh.")

def download_twitter():
    url = input("Masukkan URL Twitter Video: ")
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def screenshot_web():
    url = input("Masukkan URL: ")
    api = f"https://image.thum.io/get/fullpage/{url}"
    img = requests.get(api)
    with open("screenshot.png", "wb") as f:
        f.write(img.content)
    print("Screenshot disimpan sebagai screenshot.png")

def email_verifier():
    email = input("Masukkan email: ")
    res = requests.get(f"https://api.eva.pingutil.com/email?email={email}")
    data = res.json()
    print(json.dumps(data, indent=2))

def fake_identity():
    res = requests.get("https://randomuser.me/api/").json()
    data = res["results"][0]
    print(f"Nama: {data['name']['first']} {data['name']['last']}")
    print(f"Email: {data['email']}")
    print(f"Telepon: {data['phone']}")
    print(f"Negara: {data['location']['country']}")

def ddos_simulasi():
    host = input("Target Host (IP/domain): ")
    try:
        for i in range(100):
            socket.gethostbyname(host)
            print(f"[{i}] Mengirim paket ke {host}")
    except:
        print(Fore.RED + "Host tidak valid.")

def wa_checker():
    num = input("Masukkan nomor HP (62xxx): ")
    url = f"https://wa.me/{num}"
    r = requests.get(url)
    if "WhatsApp" in r.text:
        print(Fore.GREEN + f"Nomor {num} terdaftar di WhatsApp.")
    else:
        print(Fore.RED + f"Nomor {num} tidak ditemukan.")

def qr_generator():
    text = input("Masukkan teks/URL: ")
    img = qrcode.make(text)
    img.save("qrcode.png")
    print("QR Code disimpan sebagai qrcode.png")

def run_speedtest():
    st = speedtest.Speedtest()
    print("Unduh:", round(st.download() / 1_000_000, 2), "Mbps")
    print("Unggah:", round(st.upload() / 1_000_000, 2), "Mbps")
    print("Ping:", st.results.ping, "ms")

def main():
    login()
    while True:
        show_menu()
        choice = input(Fore.YELLOW + "Pilih menu: ").strip()
        if choice == "1":
            cek_ip_lokasi()
        elif choice == "2":
            download_tiktok()
        elif choice == "3":
            download_youtube()
        elif choice == "4":
            download_instagram()
        elif choice == "5":
            download_facebook()
        elif choice == "6":
            download_twitter()
        elif choice == "7":
            screenshot_web()
        elif choice == "8":
            email_verifier()
        elif choice == "9":
            fake_identity()
        elif choice == "10":
            ddos_simulasi()
        elif choice == "11":
            wa_checker()
        elif choice == "12":
            qr_generator()
        elif choice == "13":
            run_speedtest()
        elif choice == "00":
            print("Keluar...")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid.")
        input(Fore.CYAN + "\nTekan ENTER untuk kembali ke menu...")

if __name__ == "__main__":
    main()
