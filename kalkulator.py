import tkinter as tk

# logic

angka_pertama = 0
operator_terpilih = ""
tipe_angka = int

# fungsi tekan angka
def tekan_angka(angka):
    # tambah angka ke layar
    isi_layar = layar.get()
    
    # batasi angka
    if len(isi_layar) >= 15:
        return
    
    layar.delete(0, tk.END)
    layar.insert(0, isi_layar + str(angka))
    
# fungsi tekan operator
def tekan_operator(operator):
    # angka pertama dan operator disimpan
    global angka_pertama, operator_terpilih, tipe_angka
    isi_layar = layar.get()
    
    # cek jika layar kosong
    if isi_layar == "":
        return
    
    # cek jika angka pertama int/float
    if "." in layar.get():
        tipe_angka = float
        angka_pertama = float(isi_layar)
    else:
        tipe_angka = int
        angka_pertama = int(isi_layar)
    
    operator_terpilih = operator
    layar.delete(0, tk.END)
    
# fungsi jika tombol titik desimal ditekan
def tekan_titik():
    # untuk menambahkan titik desimal
    isi_layar = layar.get()
    
    # cek jika sudah ada titik
    if "." not in isi_layar:
        # jika layar kosong, tambahkan "0."
        if isi_layar == "":
            layar.insert(0, "0.")
        else:
            layar.insert(tk.END, ".")

# fungsi hitung hasil
def hitung_hasil():
    # hitung hasil berdasarkan pilihan operator
    global operator_terpilih, tipe_angka
    angka_kedua = layar.get()
    
    # cek operator blm dipilih
    if operator_terpilih == "":
        return
    
    isi_layar = layar.get()
    
    # cek tipe angka
    if "." in isi_layar:
        angka_kedua = float(isi_layar)
        tipe_angka = float
    else:
        angka_kedua = int(isi_layar)
        tipe_angka = int

    # perhitungan
    if operator_terpilih == '+':
        hasil = angka_pertama + angka_kedua
    elif operator_terpilih == '-':
        hasil = angka_pertama - angka_kedua
    elif operator_terpilih == 'X':
        hasil = angka_pertama * angka_kedua
    elif operator_terpilih in ['/', '%']:
        try:
            if operator_terpilih == '/':
                hasil = angka_pertama / angka_kedua
            else:
                hasil = angka_pertama % angka_kedua
        except ZeroDivisionError:
            hasil = "Tidak Bisa Dibagi 0"
    else:
        hasil = "Operator Belum Dipilih"
        
    # tipe hasil
    if isinstance(hasil, float) and hasil.is_integer():
        hasil = int(hasil)
        tipe_angka = int
    elif isinstance(hasil, float):
        tipe_angka = float
    else:
        tipe_angka = int
    
    layar.delete(0, tk.END)
    layar.insert(0, str(hasil))
    
    #reset operator
    operator_terpilih = ""
    
#bersihkan layar
def bersihkan_layar():
    global angka_pertama, operator_terpilih, tipe_angka
    layar.delete(0, tk.END)
    angka_pertama = 0
    operator_terpilih = ""
    tipe_angka = int
    jendela.title("Kalkulator Sederhana")
    
# hapus satu karakter
def hapus_satu_karakter():
    global operator_terpilih
    isi_layar = layar.get()
    if len(isi_layar) > 0:
        # jika hapus semua, reset operator
        if len(isi_layar) == 1:
            operator_terpilih = ""
        layar.delete(len(isi_layar)-1, tk.END)
        
# GUI
jendela = tk.Tk()
jendela.title("Kalkulator Sederhana")
jendela.geometry("300x400")
jendela.resizable(False, False)
jendela.configure(bg="#f0f0f0")

layar = tk.Entry(
    jendela,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief="sunken",
    bg="#ffffff"
)
layar.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buat tombol
daftar_tombol = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('%', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('X', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# loop untuk membuat tombol
for (teks, baris, kolom) in daftar_tombol:
    #jika tombol adalah "="
    if teks == "=":
        warna_latar = "#4CAF50"
        warna_teks = "white"
        tombol = tk.Button(
            jendela,
            text=teks,
            font=("Arial", 16, "bold"),
            bg=warna_latar,
            fg=warna_teks,
            command=hitung_hasil
        )
    #jika adalah operator
    elif teks in ['+', '-', 'X', '%']:
        warna_latar = "#2196F3"
        warna_teks = "white"
        tombol = tk.Button(
            jendela,
            text=teks,
            font=("Arial", 16, "bold"),
            bg=warna_latar,
            fg=warna_teks,
            command=lambda op=teks: tekan_operator(op)
        )
    else:
        warna_latar = "#e0e0e0"
        warna_teks = "black"
        tombol = tk.Button(
            jendela,
            text=teks,
            font=("Arial", 16, "bold"),
            bg=warna_latar,
            fg=warna_teks,
            command=lambda angka=teks: tekan_angka(angka)
        )
        
    tombol.grid(
        row=baris,
        column=kolom,
        sticky="nsew",
        padx=5,
        pady=5  
    )

# tombol backspace
tombol_backspace = tk.Button(
    jendela,
    text='⌫',
    font=("Arial", 16, "bold"),
    bg="#e0e0e0",
    fg="black",
    command=hapus_satu_karakter
)
tombol_backspace.grid(
    row=5,
    column=1,
    sticky="nsew",
    padx=5,
    pady=5
)

# tombol clear
tombol_clear = tk.Button(
    jendela,
    text='C',
    font=("Arial", 16, "bold"),
    bg="#e0e0e0",
    fg="black",
    command=bersihkan_layar
)
tombol_clear.grid(
    row=5,
    column=0,
    sticky="nsew",
    padx=5,
    pady=5
)

# atur ukuran
for i in range(6): # 6 baris (0-5)
    jendela.grid_rowconfigure(i, weight=1)
for i in range(4): # 4 kolom (0-3)
    jendela.grid_columnconfigure(i, weight=1)
    
# keyboard bindings
def keyboard_handler(event):

    key = event.char
    if key in "0123456789":
        tekan_angka(key)
    elif key == ".":
        tekan_titik()
    elif key in "+-*/%":
        if key == "*" or key == "xX":
            tekan_operator("X")
        else:
            tekan_operator(key)
    elif key == "\r": #enter
        hitung_hasil()
    elif key == "\x08": #backspace
        hapus_satu_karakter()
    elif key in "cC" or key == "\x1b":
        bersihkan_layar()

jendela.bind("<Key>", keyboard_handler)

    
# jalankan aplikasi
jendela.mainloop()