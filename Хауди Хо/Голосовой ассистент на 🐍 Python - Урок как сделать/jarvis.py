import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz  # нужен для нечёткого сравнения
import pyttsx3
import datetime

# для определения индекса записи устройства
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# распознаёт речь
# r = sr.Recognizer()
# with sr.Microphone(device_index=1) as source:
#     print("Скажите что-нибудь ...")
#     audio = r.listen(source)
#
# query = r.recognize_google(audio, language="ru-RU")
# print("Вы сказали: " + query.lower())

# Голосовой ассистент Кеша

# настройки
opts = {
    # имя ассистента
    "alias": ('кеша', 'кеш', 'инокентий', 'иннокентий', 'кишун', 'киш',
              'кишаня', 'кяш', 'кяша', 'кэш', 'кэша'),
    # удаляет из речевой команды слова
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    # команды ассистента
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты')
    }
}


# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


# вызывается каждый раз, когда запишит какую-то фразу, которую вы произнесли в микрофон
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice
            # удаляем в тексте имя ассистента и выделенные слова нами
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

# нечёткий поиск команды, которую получил ассистент


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC

# преобразование команды в действие


def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        # воспроизвести радио
        os.system("D:\\Jarvis\\res\\radio_record.m3u")

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

    else:
        print('Команда не распознана, повторите!')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    # в течение 1 секунды слушает фон, чтобы не путал шум с речью
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
# voices = speak_engine.getProperty('voices')
# # Каким голосом будет говорить
# speak_engine.setProperty('voice', voices[4].id)

# forced cmd test
# speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

speak("Добрый день, повелитель")
speak("Кеша слушает")

# слушает микрофон в фоне
stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop
