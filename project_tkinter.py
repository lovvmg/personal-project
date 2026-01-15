# KALKULATOR
import tkinter as tk
from tkinter import ttk

#init
kalkulator = tk.Tk()
kalkulator.geometry("500x300")
kalkulator.resizable(False,False)
kalkulator.configure(bg="pink")
kalkulator.title("Calculator Apps")

# input frame
input_frame = ttk.Frame(kalkulator)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#label 
#angka pertama
angka_pertama = ttk.Label(input_frame, text = "Masukkan Angka Pertama : ")
angka_pertama.pack(padx=10,fill="x",expand=True)

# entry angka pertama
ANGKA_PERTAMA = tk.StringVar()
angka_pertama_entry = ttk.Entry(input_frame, textvariable=ANGKA_PERTAMA)
angka_pertama_entry.pack(padx=10, fill="x",expand=True)

#angka kedua
angka_kedua = ttk.Label(input_frame, text = "Masukkan Angka Kedua     : ")
angka_kedua.pack(padx=10,fill="x",expand=True)

#entry angka kedua
ANGKA_KEDUA = tk.StringVar()
angka_kedua_entry = ttk.Entry(input_frame,textvariable=ANGKA_KEDUA)
angka_kedua_entry.pack(padx=10,fill="x",expand=True)

#operasi 
operasi = ttk.Label(input_frame, text = "Masukkan jenis operasi (+ * - /) :")
operasi.pack(padx=10,fill="x",expand=True)

# entry operasi
OPERASI = tk.StringVar()
operasi_entry = ttk.Entry(input_frame, textvariable=OPERASI)
operasi_entry.pack(padx=10,fill="x",expand=True)

HASIL_STRING = tk.StringVar()

#hasil 
def operation():
    x = float(ANGKA_PERTAMA.get())
    y= float(ANGKA_KEDUA.get())
    global HASIL
    HASIL = 0
    if OPERASI.get() == "+":
        HASIL = x + y

    elif OPERASI.get() == "-":
        HASIL = x - y

    elif OPERASI.get() == "*":
        HASIL = x*y
    elif OPERASI.get() == "/":
        if y  == 0 :
            HASIL_STRING.set("Error: Bagi 0")
            return # Stop agar tidak lanjut ke bawah
        else :
            HASIL = x/y

    HASIL_STRING.set(str(HASIL))
   

# --- TOMBOL (BUTTON) ---
# Tombol ini yang akan memanggil fungsi 'hitung' saat diklik
tombol_hitung = ttk.Button(input_frame, text="Hitung Hasil", command=operation)
tombol_hitung.pack(padx=10, pady=10, fill="x", expand=True)

hasil  = ttk.Label(input_frame, text= "Hasil Operasi :")
hasil.pack(padx=10, fill="x",expand=True)
hasil_entry = ttk.Entry(input_frame,textvariable=HASIL_STRING, state = "readonly")
hasil_entry.pack(padx=10, fill="x",expand=True)


kalkulator.mainloop()

'''note
jangan lupa pakai .get() untuk ambil valuenya '''