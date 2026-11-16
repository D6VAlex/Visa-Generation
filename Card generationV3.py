import random
import requests
import time
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from bs4 import BeautifulSoup

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def generate_card(bin_prefix, length=16):
    card_number = bin_prefix
    while len(card_number) < (length - 1):
        card_number += str(random.randint(0, 9))
    for i in range(10):
        test_card = card_number + str(i)
        if luhn_checksum(test_card) == 0:
            month = str(random.randint(1, 12)).zfill(2)
            year = str(random.randint(2025, 2030))
            cvv = str(random.randint(100, 999))
            return f"{test_card}|{month}|{year}|{cvv}"
    return None

def api_binlist_net(bin_8, proxy):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        r = requests.get(f"https://lookup.binlist.net/{bin_8}", headers={"Accept-Version": "3"}, proxies=proxies, timeout=5)
        if r.status_code == 200:
            d = r.json()
            return f"{d.get('scheme','?').upper()} | {d.get('type','?').upper()} | {d.get('bank',{}).get('name','?')} | {d.get('country',{}).get('name','?')}"
    except: pass
    return None

def api_binlist_io(bin_8, proxy):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        r = requests.get(f"https://binlist.io/lookup/{bin_8}/", proxies=proxies, timeout=5)
        if r.status_code == 200:
            d = r.json()
            return f"{d.get('scheme','?').upper()} | {d.get('type','?').upper()} | {d.get('bank',{}).get('name','?')} | {d.get('country',{}).get('name','?')}"
    except: pass
    return None

def api_bincheck_io(bin_8, proxy):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        r = requests.get(f"https://bincheck.io/api/check/{bin_8}", proxies=proxies, timeout=5)
        if r.status_code == 200:
            d = r.json()
            if 'data' in d:
                return f"{d['data'].get('scheme','?').upper()} | {d['data'].get('bank_name','?')}"
    except: pass
    return None

def api_freebinchecker(bin_8, proxy):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        url = f"https://www.freebinchecker.com/bin-checker/{bin_8}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, proxies=proxies, timeout=5)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            bank = soup.find(string="Bank").find_next("td").text.strip()
            brand = soup.find(string="Brand").find_next("td").text.strip()
            return f"{brand.upper()} | {bank}"
    except: pass
    return None

def api_bintable(bin_8, proxy):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        r = requests.get(f"https://lookups.bintable.com/v1/{bin_8}", proxies=proxies, timeout=5)
        if r.status_code == 200:
            d = r.json()
            return f"{d.get('scheme','?').upper()} | {d.get('bank','?')}"
    except: pass
    return None

API_LIST = [api_binlist_net, api_binlist_io, api_bincheck_io, api_freebinchecker, api_bintable]

def check_bin_multi(card_number, proxy):
    bin_8 = card_number[:8]
    random.shuffle(API_LIST)
    for api in API_LIST:
        result = api(bin_8, proxy)
        if result:
            return result
        time.sleep(random.uniform(0.5, 1.5))
    return "Valid Format"

class App:
    def __init__(self, root):
        self.root = root
        root.title("CC Generator")
        root.geometry("700x600")
        root.configure(bg="#1e1e1e")
        
        tk.Label(root, text="By D6VAlex", fg="#00ff00", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame1 = tk.Frame(root, bg="#1e1e1e")
        frame1.pack(pady=5)
        tk.Label(frame1, text="BIN:", fg="white", bg="#1e1e1e", font=("Arial", 11)).pack(side="left")
        self.bin_entry = tk.Entry(frame1, font=("Arial", 12), width=15)
        self.bin_entry.pack(side="left", padx=10)
        self.bin_entry.insert(0, "453201")
        
        frame2 = tk.Frame(root, bg="#1e1e1e")
        frame2.pack(pady=5)
        tk.Label(frame2, text="Proxy:", fg="white", bg="#1e1e1e", font=("Arial", 11)).pack(side="left")
        self.proxy_entry = tk.Entry(frame2, font=("Arial", 12), width=30)
        self.proxy_entry.pack(side="left", padx=10)
        
        self.btn_gen = tk.Button(root, text="Generate", bg="#00aa00", fg="white", font=("Arial", 12, "bold"), command=self.start_thread)
        self.btn_gen.pack(pady=10, ipadx=20, ipady=5)
        
        self.text_box = scrolledtext.ScrolledText(root, width=80, height=22, bg="black", fg="#00ff00", font=("Consolas", 11))
        self.text_box.pack(pady=10)

    def log(self, msg):
        self.text_box.insert(tk.END, msg + "\n")
        self.text_box.see(tk.END)

    def start_thread(self):
        self.btn_gen.configure(state="disabled", text="Working...")
        self.text_box.delete(1.0, tk.END)
        threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        bin_prefix = self.bin_entry.get().strip()
        proxy = self.proxy_entry.get().strip()
        
        if len(bin_prefix) < 6:
            messagebox.showerror("Error", "BIN must be at least 6 digits.")
            self.reset_btn()
            return
            
        self.log(f"Generating 10 Cards for BIN: {bin_prefix}")
        self.log(f"Proxy: {proxy if proxy else 'None'}\n")
        
        saved_cards = []
        
        for i in range(10):
            card_data = generate_card(bin_prefix)
            if not card_data:
                continue
                
            card_parts = card_data.split('|')
            card = card_parts[0]
            
            bin_info = check_bin_multi(card, proxy)
            
            self.log(f"Card: {card_data}")
            self.log(f"Info: {bin_info}\n")
            
            saved_cards.append(f"{card_data} | {bin_info}")
            
        try:
            with open("cards.txt", "a") as f:
                for c in saved_cards:
                    f.write(c + "\n")
            self.log("Saved to cards.txt")
        except:
            self.log("Failed to save file")
            
        self.log("Done.")
        self.reset_btn()

    def reset_btn(self):
        self.btn_gen.configure(state="normal", text="Generate")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()