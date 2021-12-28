import os
import smtplib
# Добавляем необходимые подклассы - MIME-типы
# Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
import mimetypes
import email
from email import encoders  # Импортируем энкодер
from email.header import decode_header
from email.mime.base import MIMEBase  # Общий тип
from email.mime.text import MIMEText  # Текст/HTML
from email.mime.image import MIMEImage  # Изображения
from email.mime.audio import MIMEAudio  # Аудио
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект


class Email:
    addr_from = 'testTest7771115@gmail.com'
    password = 'test5111777'

    def send_email(self, addr_to, msg_subj, msg_text, files):
        msg = MIMEMultipart()  # Создаем сообщение
        msg['From'] = self.addr_from  # Адресат
        msg['To'] = addr_to  # Получатель
        msg['Subject'] = msg_subj  # Тема сообщения

        body = msg_text  # Текст сообщения
        msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

        self.process_attachement(msg, files)

        # ======== Этот блок настраивается для каждого почтового провайдера отдельно ===============================================
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
        server.starttls()  # Начинаем шифрованный обмен по TLS
        # server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
        server.login(self.addr_from, self.password)  # Получаем доступ
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Выходим
        # ==========================================================================================================================

    # Функция по обработке списка, добавляемых к сообщению файлов
    def process_attachement(self, msg, files):
        for f in files:
            if os.path.isfile(f):  # Если файл существует
                self.attach_file(msg, f)  # Добавляем файл к сообщению.
            elif os.path.exists(f):  # Если путь не файл и существует, значит - папка
                dir = os.listdir(f)  # Получаем список файлов в папке
                for file in dir:  # Перебираем все файлы и...
                    # ...добавляем каждый файл к сообщению
                    self.attach_file(msg, f + "/" + file)

    # Функция по добавлению конкретного файла к сообщению
    def attach_file(self, msg, filepath):
        filename = os.path.basename(filepath)  # Получаем только имя файла
        # Определяем тип файла на основе его расширения
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:  # Если тип файла не определяется
            ctype = 'application/octet-stream'  # Будем использовать общий тип
        maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
        if maintype == 'text':  # Если текстовый файл
            with open(filepath) as fp:  # Открываем файл для чтения
                # Используем тип MIMEText
                file = MIMEText(fp.read(), _subtype=subtype)
                fp.close()  # После использования файл обязательно нужно закрыть
        elif maintype == 'image':  # Если изображение
            with open(filepath, 'rb') as fp:
                file = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'audio':  # Если аудио
            with open(filepath, 'rb') as fp:
                file = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
        else:  # Неизвестный тип файла
            with open(filepath, 'rb') as fp:
                filename, file_extension = os.path.splitext(filepath)
                file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
                # Добавляем содержимое общего типа (полезную нагрузку)
                file.set_payload(fp.read())
                fp.close()
                # Содержимое должно кодироваться как Base64
                encoders.encode_base64(file)
        file.add_header('Content-Disposition', 'attachment',
                        filename='Этот_файл_принадлежит_тебе' + file_extension)  # Добавляем заголовки
        msg.attach(file)  # Присоединяем файл к сообщению
