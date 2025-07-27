import os
import socket
import requests

def banner():
    print(r"""
     ____  _______       _     
    |  _ \|__   __|/\   | |    
    | | | |  | |  /  \  | |    
    | |_| |  | | / /\ \ | |___ 
    |____/   |_|/_/  \_\|_____|

       DTool - Termux Edition v2
    """)

# ================================
# 1. Port Scanner
# ================================
def port_scanner():
    target = input("Masukkan IP/Host target: ")
    try:
        for port in range(1, 101):
            sock = socket.socket()
            sock.settimeout(0.5)
            if sock.connect_ex((target, port)) == 0:
                print(f"[✓] Port {port} terbuka")
            sock.close()
    except Exception as e:
        print("[!] Error:", e)

# ================================
# 2. DNS Lookup
# ================================
def dns_lookup():
    domain = input("Masukkan domain (cth: google.com): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[✓] IP dari {domain}: {ip}")
    except socket.gaierror:
        print("[!] Domain tidak ditemukan")

# ================================
# 3. Ping Host
# ================================
def ping_host():
    host = input("Masukkan host/IP: ")
    os.system(f"ping -c 4 {host}")

# ================================
# 4. Download YouTube Video
# ================================
def download_video():
    url = input("Masukkan URL video YouTube: ")
    dest = "/storage/emulated/0/Download/ytvideo"
    os.makedirs(dest, exist_ok=True)
    os.system(f"yt-dlp -o '{dest}/%(title)s.%(ext)s' '{url}'")
    print("[✓] Video berhasil di-download ke folder ytvideo.")

# ================================
# 5. Download YouTube Audio (MP3)
# ================================
def download_audio():
    url = input("Masukkan URL video YouTube: ")
    dest = "/storage/emulated/0/Download/ytaudio"
    os.makedirs(dest, exist_ok=True)
    os.system(f"yt-dlp -x --audio-format mp3 -o '{dest}/%(title)s.%(ext)s' '{url}'")
    print("[✓] Audio berhasil di-download (MP3) ke folder ytaudio.")

# ================================
# 6. Scrape YouTube Download Info
# ================================
def scrape_youtube_download(url):
    try:
        print("[•] Menghubungi server...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
            'Accept': '*/*',
            'Referer': 'https://y2meta.mobi'
        }

        # Step 1: Ambil ID download
        api_url = f"https://p.oceansaver.in/ajax/download.php?copyright=0&format=mp3&url={url}&api=30de256ad09118bd6b60a13de631ae2cea6e5f9d"
        r1 = requests.get(api_url, headers=headers)
        r1.raise_for_status()
        id = r1.json().get("id")

        if not id:
            print("[!] Gagal mendapatkan ID unduhan.")
            return

        # Step 2: Ambil status & info file
        progress_url = f"https://p.oceansaver.in/api/progress?id={id}"
        r2 = requests.get(progress_url, headers=headers)
        r2.raise_for_status()
        data = r2.json()

        print("\n[✓] Info Berhasil Diambil:")
        print("Judul    :", data.get("title"))
        print("Ukuran   :", data.get("size"))
        print("Durasi   :", data.get("duration"))
        print("Download :", data.get("url"))

    except Exception as e:
        print("[!] Terjadi kesalahan:", e)

# ================================
# MENU UTAMA
# ================================
def menu():
    banner()
    print("""
[1] Port Scanner
[2] DNS Lookup
[3] Ping Host
[4] Download YouTube Video
[5] Download YouTube Audio (MP3)
[6] Scrape YouTube Download Info
[0] Keluar
""")
    choice = input("Pilih menu: ")
    if choice == "1":
        port_scanner()
    elif choice == "2":
        dns_lookup()
    elif choice == "3":
        ping_host()
    elif choice == "4":
        download_video()
    elif choice == "5":
        download_audio()
    elif choice == "6":
        url = input("Masukkan URL YouTube: ")
        scrape_youtube_download(url)
    elif choice == "0":
        print("Terima kasih telah menggunakan DTool!")
        exit()
    else:
        print("[!] Pilihan tidak valid!")

if __name__ == "__main__":
    while True:
        menu()
        input("\nTekan Enter untuk kembali ke menu...")
        os.system("clear")
