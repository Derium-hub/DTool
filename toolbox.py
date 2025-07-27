import os import sys import time import requests import socket import validators import subprocess import qrcode import speedtest import json from pytube import YouTube from bs4 import BeautifulSoup from colorama import Fore, init from fake_useragent import UserAgent import instaloader from yt_dlp import YoutubeDL

init(autoreset=True)

PASSWORD = "Derium289" VERSION = "1.0.0"

def slow(text): for c in text: sys.stdout.write(c) sys.stdout.flush() time.sleep(0.01) print()

def login(): os.system("clear") print(Fore.CYAN + "LOGIN AKSES TOOL") import getpass pw = getpass.getpass("Masukkan password: ") if pw != PASSWORD: print(Fore.RED + "Password salah!") sys.exit() print(Fore.GREEN + "Login berhasil!") time.sleep(1)

def banner(): os.system("clear") print(Fore.RED + "╔═╗╔═╗╔╦╗╔═╗╔╦╗╦╔═╗") print(Fore.GREEN + "║ ╦║╣  ║ ║ ║ ║ ║║  ") print(Fore.CYAN + "╚═╝╚═╝ ╩ ╚═╝ ╩ ╩╚═╝") print(Fore.YELLOW + f"Versi {VERSION}") print(Fore.YELLOW + "-"*35)

def menu(): print(Fore.YELLOW + """ [1]  Cek IP & Lokasi [2]  Download TikTok [3]  Download YouTube [4]  Download Instagram Reel [5]  Download Facebook Video [6]  Download Twitter/X Video [7]  Screenshot Web Page [8]  Email Verifier [9]  Fake Identity Generator [10] DDoS Simulasi [11] WA Number Checker [12] Generate QR Code [13] Speed Test [00] Keluar """)

def cek_ip(): try: ip = requests.get("https://api.ipify.org").text info = requests.get(f"http://ip-api.com/json/{ip}").json() print(f"\nIP Anda: {ip}") print(f"Negara: {info['country']}") print(f"Kota: {info['city']}") print(f"ISP: {info['isp']}") except: print("Gagal mengambil data IP")

def tiktok_download(): url = input("Masukkan URL TikTok: ") try: opts = {'outtmpl': '%(title)s.%(ext)s'} with YoutubeDL(opts) as ydl: ydl.download([url]) except: print("Gagal download video TikTok")

def youtube_download(): url = input("Masukkan URL YouTube: ") try: yt = YouTube(url) stream = yt.streams.get_highest_resolution() stream.download() print("Download selesai.") except: print("Gagal download video YouTube")

def insta_download(): url = input("Masukkan URL Instagram: ") try: loader = instaloader.Instaloader() loader.download_url(url, "insta_download.mp4") print("Download selesai.") except: print("Gagal download Instagram reel")

def facebook_download(): url = input("Masukkan URL Facebook: ") try: opts = {'outtmpl': '%(title)s.%(ext)s'} with YoutubeDL(opts) as ydl: ydl.download([url]) except: print("Gagal download video Facebook")

def twitter_download(): url = input("Masukkan URL Twitter: ") try: opts = {'outtmpl': '%(title)s.%(ext)s'} with YoutubeDL(opts) as ydl: ydl.download([url]) except: print("Gagal download video Twitter/X")

def screenshot_web(): url = input("Masukkan URL: ") try: api = f"https://image.thum.io/get/fullpage/{url}" r = requests.get(api) with open("screenshot.jpg", "wb") as f: f.write(r.content) print("Screenshot berhasil disimpan.") except: print("Gagal mengambil screenshot.")

def email_verifier(): email = input("Masukkan alamat email: ") try: res = requests.get(f"https://api.eva.pingutil.com/email?email={email}") data = res.json() if data['data']['deliverable']: print("Email valid dan bisa dikirim.") else: print("Email tidak valid.") except: print("Gagal memverifikasi email.")

def fake_identity(): try: ua = UserAgent() r = requests.get("https://randomuser.me/api/", headers={'User-Agent': ua.random}) data = r.json()['results'][0] print(f"Nama: {data['name']['first']} {data['name']['last']}") print(f"Gender: {data['gender']}") print(f"Email: {data['email']}") print(f"Negara: {data['location']['country']}") except: print("Gagal mengambil identitas palsu")

def ddos_simulasi(): target = input("Masukkan target (IP/domain): ") try: print(f"Mengirim paket simulasi ke {target}...") for i in range(10): print(f"Packet #{i+1} sent to {target}") time.sleep(0.5) print("Simulasi selesai.") except: print("Gagal melakukan simulasi DDoS")

def wa_checker(): number = input("Masukkan nomor WA (62xxx): ") try: print(f"[!] Menyamar jadi WhatsApp...") res = requests.get(f"https://wa.me/{number}") if "Use WhatsApp" in res.text: print("Nomor WA aktif!") else: print("Tidak diketahui atau tidak aktif.") except: print("Gagal mengecek nomor WA.")

def generate_qr(): text = input("Masukkan teks atau URL: ") img = qrcode.make(text) img.save("qrcode.png") print("QR Code berhasil disimpan.")

def speed_test(): try: st = speedtest.Speedtest() print(f"Unduh: {round(st.download() / 1_000_000, 2)} Mbps") print(f"Unggah: {round(st.upload() / 1_000_000, 2)} Mbps") print(f"Ping: {st.results.ping} ms") except: print("Gagal menjalankan speedtest")

def main(): login() while True: banner() menu() choice = input("Pilih menu: ")

if choice == "1": cek_ip()
    elif choice == "2": tiktok_download()
    elif choice == "3": youtube_download()
    elif choice == "4": insta_download()
    elif choice == "5": facebook_download()
    elif choice == "6": twitter_download()
    elif choice == "7": screenshot_web()
    elif choice == "8": email_verifier()
    elif choice == "9": fake_identity()
    elif choice == "10": ddos_simulasi()
    elif choice == "11": wa_checker()
    elif choice == "12": generate_qr()
    elif choice == "13": speed_test()
    elif choice == "00":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid!")
    input("\nTekan Enter untuk kembali ke menu...")

if name == "main": main()

