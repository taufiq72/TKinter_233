import tkinter as tk

def proses_prediksi():
    jendela_hasil = tk.Toplevel(root)
    jendela_hasil.title("Hasil Prediksi")
    jendela_hasil.geometry("300x150") # Ukuran jendela hasil
    
    label_hasil = tk.Label(jendela_hasil, text=f"Prediksi Prodi: {variabel_prodi.get()}", 
                           font=("Helvetica", 12, "bold"), fg="blue")
    
    label_hasil.pack(expand=True) 