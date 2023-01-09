
import speech_recognition as sr
import pyaudio
import wave
import requests as r


from googlesearch import search
import wikipedia as wiki
import pyttsx3

CHUNK = 1024  # определяет форму ауди сигнала
FRT = pyaudio.paInt16  # шестнадцатибитный формат задает значение амплитуды
CHAN = 1  # канал записи звука
RT = 44100  # частота
REC_SEC = 5  # длина записи
OUTPUT = "output.wav"
p = pyaudio.PyAudio()  # Создать интерфейс для PortAudio
stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True,
                frames_per_buffer=CHUNK, input_device_index=1)  # открываем поток для записи
print("rec")
frames = []  # формируем выборку данных фреймов
for i in range(0, int(RT / CHUNK * REC_SEC)):
    data = stream.read(CHUNK)
    frames.append(data)
print("done")

stream.stop_stream()  # останавливаем и закрываем поток
stream.close()
p.terminate()
w = wave.open(OUTPUT, 'wb')
w.setnchannels(CHAN)
w.setsampwidth(p.get_sample_size(FRT))
w.setframerate(RT)
w.writeframes(b''.join(frames))
w.close()
recognizer = sr.Recognizer()
audio_ex = sr.AudioFile("output.wav")
type(audio_ex)
with audio_ex as source:
    audiodata = recognizer.record(audio_ex)
    type(audiodata)
    text1 = recognizer.recognize_google(audio_data=audiodata, language='ru-RU')
text2 = text1.casefold()
print(text1)
print(text2)
tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию

tts.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос

for voice in voices:

    if voice.name == 'Timofey':

        tts.setProperty('voice', voice.id)
if "что такое" in text2:
    try:
        text = text2
        a = text.split(" ")
        list = a[2:]
        text_to_search = " ".join(list)
        print(text_to_search)
        wiki.set_lang("ru")
        search_result = wiki.search(text_to_search, results=5)
        for index, result in enumerate(search_result):
            print(f"{index}){result}")

        get_one = int(input(
            "выберите интересующий вас результат, если эти результаты вас не устраивают, то введите цифру 5"))
        if get_one == 5:
            for url in search(text2, num_results=5, lang="ru"):
                print(url)
        else:
            result = wiki.summary(search_result[get_one])
            print(result)
            tts.say(result)
            tts.runAndWait()

    except:
        for url in search(text2, num_results=5, lang="ru"):
            print(url)
elif "погода" in text2:
    text = text2
    a = text.split(" ")
    list = a[1:]
    if len(list) >= 1:
        city = " ".join(list)
        url = f"https://wttr.in/{city}?0T"
        headers = {"Accept-Language": "ru"}
        
        search_parameters = {"M": ""}
        response = r.get(url=url, headers=headers, params=search_parameters)
        text = response.text
        print(text)
        tts.say(text)
        tts.runAndWait()
    else:
        city = str(input("Введите город, в котором хотите узнать погоду"))
        url = f"https://wttr.in/{city}?0T"
        headers = {"Accept-Language": "ru"}
        search_parameters = {"M": ""}
        response = r.get(url=url, headers=headers, params=search_parameters)
        text = response.text
        print(text)
        tts.say(text)
        tts.runAndWait()



else:
    pass
