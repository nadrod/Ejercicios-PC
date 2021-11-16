import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
from tkinter import *
from tkinter import ttk


def sendEmail(sender_email, password, receiver_email, path_meme):
    msg = MIMEMultipart()
    mensaje = 'Jajaja miren este meme chicos!'  # Mensaje del email

    msg['From'] = sender_email  # Encabezado del email
    msg['To'] = receiver_email
    msg['Subject'] = 'MEME'

    msg.attach(MIMEText(mensaje, 'plain'))

    with open(path_meme, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name=os.path.basename(path_meme))
    msg.attach(image)

    p = MIMEBase('application', 'octet-stream')  # Posiciona el encabezado en su lugar
    p.add_header('Content-Disposition', "attachment; filename= %s" % str(os.path.basename(path_meme)))
    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com: 587')  # Ejecuta el protocolo simple de email de gmail
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def enviarMailApp():
    root = Tk()
    mainframe = ttk.Frame(root, padding="70 70 72 72")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    root.title('Enviar Meme por Email')
    sender_email = StringVar()
    password = StringVar()
    receiver_email = StringVar()
    image = StringVar()

    ttk.Label(mainframe, text="From:").grid(row=0, sticky=W)  # label
    ttk.Entry(mainframe, textvariable=sender_email).grid(row=0, column=1, sticky=E)  # entry textbox
    ttk.Label(mainframe, text="Password:").grid(row=1, sticky=W)  # label
    ttk.Entry(mainframe, textvariable=password, show="*").grid(row=1, column=1, sticky=E)  # entry textbox
    ttk.Label(mainframe, text="To:").grid(row=2, sticky=W)  # label
    ttk.Entry(mainframe, textvariable=receiver_email).grid(row=2, column=1, sticky=E)  # entry textbox
    ttk.Label(mainframe, text="Image Path:").grid(row=3, sticky=W)  # label
    ttk.Entry(mainframe, textvariable=image).grid(row=3, column=1, sticky=E)  # entry textbox

    enviar = ttk.Button(mainframe, text="Enviar", command=lambda:sendEmail(sender_email.get(), password.get(), receiver_email.get(), image.get())).grid(row=6, column=1)  # button
    root.mainloop()


if __name__ == '__main__':
    enviarMailApp()
    # sendEmail("pruebapiapc2021@gmail.com", "PIAPC2021", "pruebapiapc2021@gmail.com",
    #         "C:\\Users\\HP\\Downloads\\meme.jpg")
