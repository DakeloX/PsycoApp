import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(patient_data):
    doc = SimpleDocTemplate("historia_clinica.pdf", pagesize=letter)
    story = []

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    for key, value in patient_data.items():
        paragraph = Paragraph(f"<b>{key}:</b> {value}", style)
        story.append(paragraph)

    doc.build(story)
    print("Se ha generado el archivo historia_clinica.pdf")

def generate_pdf():
    patient_data = {
        "Nombre del Paciente": name_entry.get(),
        "Número de Documento": document_entry.get(),
        "Fecha": date_entry.get(),
        "Antecedentes": antecedents_entry.get(),
        "Motivo de la Consulta": reason_entry.get(),
    }

    create_pdf(patient_data)

# Crear la ventana principal de la interfaz
root = tk.Tk()
root.title("Generador de Historias Clínicas")

# Crear etiquetas y campos de entrada
name_label = tk.Label(root, text="Nombre del Paciente:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

document_label = tk.Label(root, text="Número de Documento:")
document_label.pack()
document_entry = tk.Entry(root)
document_entry.pack()

date_label = tk.Label(root, text="Fecha:")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

antecedents_label = tk.Label(root, text="Antecedentes:")
antecedents_label.pack()
antecedents_entry = tk.Entry(root)
antecedents_entry.pack()

reason_label = tk.Label(root, text="Motivo de la Consulta:")
reason_label.pack()
reason_entry = tk.Entry(root)
reason_entry.pack()

# Botón para generar el PDF
generate_button = tk.Button(root, text="Generar PDF", command=generate_pdf)
generate_button.pack()

# Iniciar la aplicación
root.mainloop()