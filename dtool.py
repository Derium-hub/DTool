import os
import socket
import base64
from cryptography.fernet import Fernet

# Direktori penyimpanan hasil enkripsi/dekripsi
DOWNLOAD_DIR = "/storage/emulated/0/Download/termux"

def banner():
    print(r"""
     ____  _______       _     
    |  _ \|__   __|/\   | |    
    | | | |  | |  /  \  | |    
    | |_| |  | | / /\ \ | |___ 
    |____/   |_|/_/  \_\|_____|

        DTool - Termux Edition v1
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
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[✓] Port {port} terbuka")
            sock.close()
    except Exception as e:
        print(f"Error: {e}")

# ================================
# 2. DNS Lookup
# ================================
def dns_lookup():
    domain = input("Masukkan nama domain (contoh: google.com): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[✓] IP dari {domain}: {ip}")
    except socket.gaierror:
        print("[!] Domain tidak ditemukan")

# ================================
# 3. Ping Host
# ================================
def ping_host():
    host = input("Masukkan host/IP yang ingin di-ping: ")
    os.system(f"ping -c 4 {host}")

# ================================
# 4. Encrypt File
# ================================
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return key

def encrypt_file():
    filepath = input("Masukkan path file yang ingin dienkripsi: ")
    if not os.path.exists(filepath):
        print("[!] File tidak ditemukan.")
        return

    key = generate_key()
    fernet = Fernet(key)

    with open(filepath, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    filename = os.path.basename(filepath)
    output_path = os.path.join(DOWNLOAD_DIR, f"enc_{filename}")

    with open(output_path, "wb") as enc_file:
        enc_file.write(encrypted)

    print(f"[✓] File terenkripsi disimpan di: {output_path}")
    print(f"[!] Simpan kunci ini untuk dekripsi:\n{key.decode()}")

# ================================
# 5. Decrypt File
# ================================
def decrypt_file():
    key_input = input("Masukkan kunci enkripsi (Base64): ")
    try:
        fernet = Fernet(key_input.encode())
        filepath = input("Masukkan path file terenkripsi: ")

        if not os.path.exists(filepath):
            print("[!] File tidak ditemukan.")
            return

        with open(filepath, "rb") as file:
            encrypted = file.read()

        decrypted = fernet.decrypt(encrypted)

        filename = os.path.basename(filepath).replace("enc_", "")
        output_path = os.path.join(DOWNLOAD_DIR, f"dec_{filename}")

        with open(output_path, "wb") as dec_file:
            dec_file.write(decrypted)

        print(f"[✓] File didekripsi disimpan di: {output_path}")
    except Exception as e:
        print("[!] Gagal mendekripsi:", e)

# ================================
# Menu Utama
# ================================
def menu():
    banner()
    print("""
[1] Port Scanner
[2] DNS Lookup
[3] Ping Host
[4] Encrypt File
[5] Decrypt File
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
        encrypt_file()
    elif choice == "5":
        decrypt_file()
    elif choice == "0":
        print("Keluar dari DTool...")
        exit()
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    while True:
        menu()
        input("\nTekan Enter untuk kembali ke menu...")
        os.system("clear")
