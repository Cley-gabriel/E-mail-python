from string import Template
from datetime import datetime
from login import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib



with open('enviaemail/E-mail-python/template.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='', data=data_atual)

#CONFIGURAÇÃO DO ENVIO DA MENSAGEM
msg = MIMEMultipart()
msg['from'] = 'Nome de quem enviou o e-mail'
msg['to'] = 'E-mail de quem vai receber a mensagem'  
msg['subject'] = 'Assunto do e-mail'

#MENSAGEM QUE DESEJA ENVIAR
corpo = MIMEText('template.html', html)
msg.attach(corpo)


# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('O e-mail foi enviado com sucesso.')
    except Exception as erro:
        print('O e-mail foi não enviado...')
        print('Erro:', erro)