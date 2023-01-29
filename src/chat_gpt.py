import os
import openai
import logging

openai.organization = os.getenv("OPENAI_API_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")
# list all available models
# openai.Model.list()


def ask_chat_gpt(the_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=the_text,
        max_tokens=100,
        temperature=0
    )
    answers = []
    logging.debug(response)
    for answer in response['choices']:
        answers.append(answer['text'])
    final_answer = " or ".join(answers)
    return final_answer
