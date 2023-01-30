
import os
# set the environment
os.environ['CA_ENV'] = 'dev'

import logging
from datetime import datetime
import config
from gtts import gTTS

from playsound import playsound
import speech_recognition as sr

import chat_gpt


MIC_TO_USE = 1


def list_microphones():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def speech_to_text():
    r = sr.Recognizer()
    logging.info("Talk!")
    with sr.Microphone(device_index=MIC_TO_USE) as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        the_text = r.recognize_google(audio2, language='en-IN')
        return the_text


def text_to_speech(the_text):
    language = 'en'
    file_location = config.DATA_DIR.joinpath('speech_from_text.mp3')
    tts_obj = gTTS(text=the_text, lang=language, slow=False)
    tts_obj.save(str(file_location))
    playsound(str(file_location))


def save_to_file(question, answer):
    question = question.replace('\n', '')
    answer = answer.replace('\n', '')
    with open(config.DATA_DIR.joinpath('QA.txt'), 'a+') as qa_file:
        qa_file.write(f"{datetime.now().strftime('%m/%d/%Y %H:%M:%S')}\n")
        qa_file.write(f"Q: {question}\n")
        qa_file.write(f"A: {answer}\n")
        qa_file.write(f"\n")


if __name__ == '__main__':
    # List all the microphones and use the correct one, update the constant MIC_TO_USE with the correct index
    # list_microphones()

    question = speech_to_text()
    logging.info(question)
    answer = chat_gpt.ask_chat_gpt(question)
    logging.info(answer)
    text_to_speech(answer)
    save_to_file(question, answer)

