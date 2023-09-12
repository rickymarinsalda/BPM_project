import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Importa ttk per la progress bar
import shutil
import os
import subprocess
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from chart_data import calculate_chart_data
import matplotlib.pyplot as plt



# Dichiarare label, entry, filepath, text_widget, progress_bar e save_button come variabili globali
# Dichiarare le variabili globali
label = None
entry = None
filepath = None
text_widget = None
progress_bar = None
save_button = None
window = None

# Cartella di destinazione per i file
destination_folder = "review"



# Crea una funzione per generare il grafico
def generate_chart():
    # Calcola i dati del grafico utilizzando la funzione importata
    global chart_frame
    original_scores, corrected_scores, summary_scores, review_scores = calculate_chart_data()

    # Genera il grafico con i dati calcolati
    plt.figure(figsize=(6, 4))
    plt.scatter(original_scores, corrected_scores, color='purple', alpha=0.5)
    plt.title("Confronto Sentiment Scores Prima e Dopo la Correzione")
    plt.xlabel("Sentiment Scores Originali")
    plt.ylabel("Sentiment Scores Corretti")
    plt.grid(True)

    # Incorpora il grafico nel frame
    canvas = FigureCanvasTkAgg(plt.gcf(), master=chart_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    labels = ['Negativity', 'Neutrality', 'Positivity']
    summary_values = summary_scores
    review_values = [sum(i) / len(i) for i in zip(*review_scores)]  # Media dei punteggi delle recensioni

    x = list(range(len(labels)))  # Converto il range in una lista
    width = 0.35

    fig, ax = plt.subplots(figsize=(6, 4))
    rects1 = ax.bar([i - width / 2 for i in x], summary_values, width, label='Summary')
    rects2 = ax.bar([i + width / 2 for i in x], review_values, width, label='Reviews')

    ax.set_ylabel('Scores')
    ax.set_title('Confronto Punteggi VADER tra Riassunto e Recensioni')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Incorpora il grafico nel frame
    canvas = FigureCanvasTkAgg(plt.gcf(), master=chart_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def center_window(window):
    # Ottieni le dimensioni della finestra
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    # Ottieni le dimensioni dello schermo
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcola le coordinate x e y per centrare la finestra
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Imposta la posizione della finestra
    window.geometry("+{}+{}".format(x, y))
def button_click():
    global label  # Dichiarare label come variabile globale
    selected_file = filedialog.askopenfilename(filetypes=[("File di testo", "*.txt")])
    if selected_file:
        global filepath  # Dichiarare filepath come variabile globale
        filepath = selected_file
        label.config(text="Hai selezionato il file: " + filepath)
    else:
        label.config(text="Nessun file selezionato")
def update_summary_on_gui():
    try:
        with open("summary.txt", "r") as summary_file:
            summary_text = summary_file.read()

        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, summary_text)

    except Exception as e:
        label.config(text=f"Errore nell'aggiornamento del riassunto: {str(e)}")

def save_file():
    if filepath:
        try:
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            file_name = os.path.basename(filepath)
            destination_path = os.path.join(destination_folder, file_name)

            shutil.move(filepath, destination_path)

            label.config(text=f"File salvato in {destination_path}")
            save_button.config(state="disabled")

            subprocess.Popen(["python", "summary_generator.py", destination_path])

            for i in range(21):
                progress_bar["value"] = (i / 20) * 100
                window.update_idletasks()
                window.after(1000)

            save_button.config(state="normal")
            update_summary_on_gui()

        except Exception as e:
            label.config(text=f"Errore nel salvataggio del file: {str(e)}")
    else:
        label.config(text="Nessun file selezionato")
def main():
    global chart_frame,label, entry, filepath, text_widget, progress_bar, save_button, window  # Utilizza le variabili globali label, entry, filepath, text_widget, progress_bar, save_button e window

    # Creare una finestra
    window = tk.Tk()
    window.title("Summary generator v1.0")

    # Aggiungi un nuovo frame per il grafico
    chart_frame = tk.Frame(window)
    chart_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
    # Creazione di un frame per i pulsanti a sinistra
    button_frame = tk.Frame(window)
    button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    # Creazione di un frame per il testo a destra
    text_frame = tk.Frame(window)
    text_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    # Creazione di un frame per il titolo
    title_frame = tk.Frame(window)
    title_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    # Configura il grid per espandersi uniformemente
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # Inizializza la variabile label
    label = tk.Label(button_frame, text="", font=("Helvetica", 12))
    label.pack(padx=5, pady=5)

    # Creazione del titolo centrato
    title_label = tk.Label(title_frame, text="Summary Review generator v1.0", font=("Helvetica", 20))
    title_label.pack()

    #dimensioni
    window.geometry("1600x900")
    # Centra la finestra nello schermo
    center_window(window)

    # Add the guide label
    guide_label = tk.Label(button_frame,
                           text="Instructions for Use:\n\n"
                                "1. Select a text file containing a set of reviews related to a product (preferably not more than 25 for technical reasons).\n\n"
                                "2. Click 'Select a file' to choose the file.\n\n"
                                "3. Click 'Generate summary' to obtain a summary of the reviews.\n\n"
                                "4. You can also click 'Generate Chart' to create a sentiment score chart.\n\n"
                                "Note: The window may take some time during summary generation.",
                           font=("Helvetica", 14),
                           wraplength=400,
                           justify="left")
    guide_label.pack(padx=5, pady=5)

    # Creare un pulsante per selezionare un file
    file_button = tk.Button(button_frame, text="Select a file", command=button_click)
    file_button.pack(padx=5, pady=5)

    # Creare un pulsante per salvare il file
    save_button = tk.Button(button_frame, text="Generate summary", command=save_file)
    save_button.pack(padx=5, pady=5)

    # Aggiungi un pulsante per generare il grafico
    chart_button = tk.Button(button_frame, text="Generate Chart", command=generate_chart)
    chart_button.pack(padx=5, pady=5)

    # Creare una progress bar
    progress_bar = ttk.Progressbar(text_frame, orient="horizontal", length=600, mode="determinate")
    progress_bar.pack(padx=5, pady=5, fill="both")

    # Creare un widget Text per visualizzare il riassunto
    text_widget = tk.Text(text_frame, wrap=tk.WORD, height=10, width=30 ,font=("Helvetica", 18))
    text_widget.pack(padx=5,pady=5, fill="both", expand=True )

    text_widget.configure(padx=25, pady=25)
    # Eseguire la finestra
    window.mainloop()

if __name__ == "__main__":
    main()
