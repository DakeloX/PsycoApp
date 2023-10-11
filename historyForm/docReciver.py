# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:34:32 2023

@author: Miguel
"""
import formAdvance
from docxtpl import DocxTemplate

doc = DocxTemplate("templateTest.docx")

def capturar_datos():
    
    app = formAdvance.HistoriaClinicaApp()
    app.mainloop()

    context = app.obtener_datos()

    doc.render(context)
    
    doc.save("documento generado.docx")


if __name__ == "__main__":
    capturar_datos()