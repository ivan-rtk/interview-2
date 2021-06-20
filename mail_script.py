import email
from smtplib import SMTP_SSL
import imaplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_SMTP = 'smtp.gmail.com'
GMAIL_IMAP = 'imap.gmail.com'
SSL_port = 465

LOGIN = 'vedroidtsd.085@gmail.com'
PWD = ''
recipients = ['homutovan@live.com', 'elenar63@yandex.ru']


class Email_client:

    def __init__(self, SMTP_server, IMAP_server, SSL_port, LOGIN, PWD):
        self.LOGIN = LOGIN
        self.PWD = PWD
        self.context = ssl.create_default_context()
        self.server = SMTP_SSL(SMTP_server, SSL_port, context=self.context)
        self.server.login(self.LOGIN, self.PWD)
        self.mail = imaplib.IMAP4_SSL(IMAP_server)
        self.mail.login(LOGIN, PWD)
        self.msg = MIMEMultipart()

    def create_msg(self, msg_to, msg_subj, msg_text):
        self.msg['From'] = self.LOGIN
        self.msg['To'] = ', '.join(msg_to)
        self.msg['Subject'] = msg_subj
        self.msg.attach(MIMEText(msg_text))

    def send_msg(self):
        self.server.sendmail(self.LOGIN, self.msg['To'], self.msg.as_string())

    def receive_mail(self, folder='inbox', header=None):
        # self.mail.list()
        self.mail.select(folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = self.mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = self.mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1].decode('utf8')
        return email.message_from_string(raw_email[1:])

    def close_email(self):
        self.server.quit()
        self.mail.logout()


if __name__ == '__main__':
    gmail = Email_client(GMAIL_SMTP, GMAIL_IMAP, SSL_port, LOGIN, PWD)
    gmail.create_msg(recipients, 'Python', 'Hello!')
    gmail.send_msg()
    print(gmail.receive_mail(header=''))