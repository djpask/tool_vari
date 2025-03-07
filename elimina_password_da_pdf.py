import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def remove_password():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    password = password_entry.get(show="DGNPQL76M14L259C")
    password="DGNPQL76M14L259C"
    if not password:
        messagebox.showerror("Errore", "Inserisci la password del PDF.")
        return

    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                reader.decrypt(password)
                writer = PyPDF2.PdfWriter()
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])

                output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                if output_path:
                    with open(output_path, "wb") as output_file:
                        writer.write(output_file)
                    messagebox.showinfo("Successo", "La password è stata rimossa con successo.")
            else:
                messagebox.showinfo("Informazione", "Il file PDF non è protetto da password.")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

app = tk.Tk()
app.title("Rimuovi Password da PDF")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Inserisci la password del PDF:")
label.pack(pady=5)

password_entry = tk.Entry(frame, show="*")
password_entry.pack(pady=5)

remove_button = tk.Button(frame, text="Seleziona PDF e Rimuovi Password", command=remove_password)
remove_button.pack(pady=10)

app.mainloop()