#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:55:46 2022

@author: QI
"""

import smtplib
import email.mime.multipart import MIMEMultipart
import email.mime.text import MIMEText
import email.mime.base import MIMEBase
import emaail import encoders

def add_pdf_to_email(msg, data_path, filename, num, ftype=('application','pdf')):
    """

    Parameters
    ----------
    msg : MIMEMultipart object
    data_path : str
        path to the file.
    filename : str
        file name.
    num : int
        the unique number assigned to the file to be used latter.
    ftype : tuple of str. Choose from ('image','png'), optional
        The default is 'pdf'.
    -------

    """
    with open(os.path.join(data_path, filename), 'rb') as f:
        # set attachment mime and file name, the type is specified
        mime = MIMEBase(ftype[0], ftype[1], filename=filename)
        # add required header data
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        mime.add_header('X-Attachment-Id', str(num))
        mime.add_header('Content-ID', f'<{num}>')
        # read attachment life content into the MIMBase object
        mime.set_payload(f.read())
        # encode with base64
        encoders.encode_base64(mime)
        # add MIMEBase object to MIMEMultipart object
        msg.attach(mime)

def send_email(data_path):
    sender = 'wangqikelly@hotmail.com'
    receivers = ['wangqikelly@hotmail.com']
    
    msg = MIMEMultipart()
    
    add_pdf_to_email(msg, data_path, 'results.pdf', 1)
    
    message = f"""
    <html><body>
    <h1> The Title of the Email </h1>
    <p> The details lie here. </p>
    <p> <img src="cid:{1}"> </p>
    </body></html>
    """
    msg.attach(MIMEText(message, 'html'))
    
    msg['Subject'] = "Subject of the Email"
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    
    s = smtplib.SMTP('hostname')
    
    s.ehlo()
    s.starttls()
    s.ehlo()
    # s.login(user, password)
    
    s.send_message(msg)
    s.quit()
    
if __name__=='__main__':
    send_email('./files')
    