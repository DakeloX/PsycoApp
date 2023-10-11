# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:45:06 2023

@author: Miguel
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class HistoriaClinicaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Historia Clínica")
        self.geometry("900x800")

        self.create_widgets()

    def create_widgets(self):
        row_num = 0
        
        # Nombre
        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.label_nombre.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Fecha de Nacimiento
        row_num += 1
        self.label_fecha_nacimiento = ttk.Label(self, text="Fecha de Nacimiento:")
        self.label_fecha_nacimiento.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.date_fecha_nacimiento = DateEntry(self)
        self.date_fecha_nacimiento.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Fecha de Registro
        row_num += 1
        self.label_fecha_registro = ttk.Label(self, text="Fecha de Registro:")
        self.label_fecha_registro.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.date_fecha_registro = DateEntry(self)
        self.date_fecha_registro.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Número de Identificación
        row_num += 1
        self.label_id = ttk.Label(self, text="Número de Identificación:")
        self.label_id.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_id = ttk.Entry(self)
        self.entry_id.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Edad
        row_num += 1
        self.label_edad = ttk.Label(self, text="Edad:")
        self.label_edad.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_edad = ttk.Entry(self)
        self.entry_edad.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Estado Civil
        row_num += 1
        self.label_estado_civil = ttk.Label(self, text="Estado Civil:")
        self.label_estado_civil.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.combo_estado_civil = ttk.Combobox(self, values=["Soltero(a)", "Casado(a)", "Divorciado(a)", "Viudo(a)", "Otro"])
        self.combo_estado_civil.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Sexo
        row_num += 1
        self.label_sexo = ttk.Label(self, text="Sexo:")
        self.label_sexo.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.var_sexo = tk.StringVar()
        self.radio_sexo_m = ttk.Radiobutton(self, text="Masculino", variable=self.var_sexo, value="Masculino")
        self.radio_sexo_m.grid(row=row_num, column=1, sticky=tk.W)
        self.radio_sexo_f = ttk.Radiobutton(self, text="Femenino", variable=self.var_sexo, value="Femenino")
        self.radio_sexo_f.grid(row=row_num, column=1, padx=90, sticky=tk.W)

        # Ocupación
        row_num += 1
        self.label_ocupacion = ttk.Label(self, text="Ocupación:")
        self.label_ocupacion.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_ocupacion = ttk.Entry(self)
        self.entry_ocupacion.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Escolaridad
        row_num += 1
        self.label_escolaridad = ttk.Label(self, text="Escolaridad:")
        self.label_escolaridad.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_escolaridad = ttk.Entry(self)
        self.entry_escolaridad.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Religión
        row_num += 1
        self.label_religion = ttk.Label(self, text="Religión:")
        self.label_religion.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_religion = ttk.Entry(self)
        self.entry_religion.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Teléfono
        row_num += 1
        self.label_telefono = ttk.Label(self, text="Teléfono:")
        self.label_telefono.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_telefono = ttk.Entry(self)
        self.entry_telefono.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Descripción de la consulta
        row_num += 1
        self.label_consulta = ttk.Label(self, text="Razón de la consulta:")
        self.label_consulta.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.text_consulta = tk.Text(self, height=5, width=40)
        self.text_consulta.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Antecedentes médicos
        row_num += 1
        self.label_antecedentes = ttk.Label(self, text="Antecedentes médicos:")
        self.label_antecedentes.grid(row=row_num, column=0, padx=10, pady=10, sticky=tk.W)
        self.text_antecedentes = tk.Text(self, height=5, width=40)
        self.text_antecedentes.grid(row=row_num, column=1, padx=10, pady=10, sticky=tk.W)

        # Botón enviar
        row_num += 1
        self.btn_enviar = ttk.Button(self, text="Guardar", command=self.guardar_datos)
        self.btn_enviar.grid(row=row_num, column=0, columnspan=2, pady=20)

    def guardar_datos(self):
        
        self.data= {
            'nombre' : self.entry_nombre.get(),
            'fecha_nacimiento' : self.date_fecha_nacimiento.get_date(),
            'fecha_registro' : self.date_fecha_registro.get_date(),
            'numero_id' : self.entry_id.get(),
            'edad' : self.entry_edad.get(),
            'estado_civil' : self.combo_estado_civil.get(),
            'sexo' : self.var_sexo.get(),
            'ocupacion' : self.entry_ocupacion.get(),
            'escolaridad' : self.entry_escolaridad.get(),
            'religion' : self.entry_religion.get(),
            'telefono' : self.entry_telefono.get(),
            'razon_consulta' : self.text_consulta.get("1.0", tk.END).strip(),
            'antecedentes' : self.text_antecedentes.get("1.0", tk.END).strip()
            }
        self.destroy()
        
    def obtener_datos(self):
        return self.data
    