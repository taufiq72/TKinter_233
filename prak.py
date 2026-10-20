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

entries = []
for i in range(1, 11):
    label_mapel = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i}:")
    label_mapel.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry_mapel = tk.Entry(frame_input, width=15)
    entry_mapel.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry_mapel)

frame_dropdown = tk.Frame(root)
frame_dropdown.pack(pady=10)

label_dropdown = tk.Label(frame_dropdown, text="Pilihan Jurusan Anda:")
label_dropdown.pack(side="left", padx=5)

daftar_prodi = ["Teknologi Informasi", "Sistem Informasi", "Teknik Elektro", "Teknik Industri", "Teknik Sipil", "Farmasi", "Kedokteran"]
variabel_prodi = tk.StringVar(root)
variabel_prodi.set(daftar_prodi[0]) # Menetapkan nilai awal/default

dropdown_prodi = tk.OptionMenu(frame_dropdown, variabel_prodi, *daftar_prodi)
dropdown_prodi.config(width=15)
dropdown_prodi.pack(side="left", padx=5)