import tkinter as tk

def proses_prediksi():
    jendela_hasil = tk.Toplevel(root)
    jendela_hasil.title("Hasil Prediksi")
    jendela_hasil.geometry("300x150") # Ukuran jendela hasil
    
    label_hasil = tk.Label(jendela_hasil, text=f"Prediksi Prodi: {variabel_prodi.get()}", 
                           font=("Helvetica", 12, "bold"), fg="blue")
    
    label_hasil.pack(expand=True) 

root = tk.Tk()
root.title("Aplikasi Prediksi")
root.geometry("400x650")

label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 14, "bold"))
label_judul.pack(pady=20)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)