import os
import socket

def banner():
    print(r"""
     ____  _______       _     
    |  _ \|__   __|/\   | |    
    | | | |  | |  /  \  | |    
    | |_| |  | | / /\ \ | |___ 
    |____/   |_|/_/  \_\|_____|

       DTool - Termux Edition v2
    """)

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

def dns_lookup():
    domain = input("Masukkan domain (contoh: google.com): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[✓] IP dari {domain}: {ip}")
    except Exception:
        print("[!] Domain tidak ditemukan")

def ping_host():
    host = input("Masukkan host/IP: ")
    os.system(f"ping -c 4 {host}")

def download_video():
    url = input("Masukkan URL YouTube video: ")
    dest = "/storage/emulated/0/Download/ytvideo"
    os.makedirs(dest, exist_ok=True)
    os.system(f"yt-dlp -o '{dest}/%(title)s.%(ext)s' '{url}'")
    print("[✓] Video berhasil di-download ke folder ytvideo.")

def download_audio():
    url = input("Masukkan URL YouTube video: ")
    dest = "/storage/emulated/0/Download/ytaudio"
    os.makedirs(dest, exist_ok=True)
    os.system(f"yt-dlp -x --audio-format mp3 -o '{dest}/%(title)s.%(ext)s' '{url}'")
    print("[✓] Audio berhasil di-download (MP3) ke folder ytaudio.")

def menu():
    banner()
    print("""
[1] Port Scanner
[2] DNS Lookup
[3] Ping Host
[4] Download YouTube Video
[5] Download YouTube Audio (MP3)
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
    elif choice == "0":
        print("Terima kasih sudah menggunakan DTool!")
        exit()
    else:
        print("[!] Pilihan tidak valid!")

if __name__ == "__main__":
    while True:
        menu()
        input("\nTekan Enter untuk kembali ke menu...")
        os.system("clear")
