import openai
import os
from dotenv import load_dotenv
import sys
import time
import threading

load_dotenv()

KEY_API = os.getenv('KEY_API')
MODEL = os.getenv('MODEL')
RESPONSE_READY = False

def generate_response(rules: str, question: str, temperature: int, result: list, key_api: str = KEY_API, model: str = MODEL):
    """
    Gera uma resposta da inteligência artificial da OpenAI com base em uma pergunta do usuário e regras específicas da conversa.

    :param rules: As regras da conversa, orientando a resposta da IA.
    :param question: A pergunta do usuário para a qual você quer uma resposta.
    :param temperature: Controla a criatividade da resposta (0 para conservadora, 10 para mais criativa - fugindo mais da regra ou assunto).
    :param result: Uma lista onde a resposta gerada será armazenada.
    :param key_api: A chave de API para autenticação com a OpenAI.
    :param model: O modelo GPT específico a ser utilizado para gerar a resposta.
    :return:
    """
    openai.api_key = key_api

    if temperature > 10 or temperature < 0:
        temperature = 10
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": rules}, {"role": "user", "content": question}],
            temperature=int(temperature / 10)
        )
    except openai.error.ServiceUnavailableError:
        print("\n\nERRO: GPT congestionado, tente novamente mais tarde")
        return

    reply = response.choices[0].message.content

    if reply:
        with open('resposta.txt', "w", encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(reply)
        result.append(reply)
    print('\n\n',reply)


def animation():
    movement_chars = "-\|/"
    while not RESPONSE_READY:
        for char in movement_chars:
            if not RESPONSE_READY:
                sys.stdout.write(f"\r{char} Processando")
                sys.stdout.flush()
                time.sleep(0.1)


if __name__ == "__main__":

    print("Digite 'q' a qualquer momento para sair.")
    rules = input("Por favor, defina as regras do chat (tópico específico, formato das respostas, etc):\n\n")
    if rules.lower() == 'q':
        quit()
    while True:
        try:
            temperature = input("\nEm uma escala de 0 a 10, o quanto você deseja que a resposta se afaste das regras? "
                                "Informe um número: ")
            if temperature.lower() == 'q':
                quit()
            temperature = int(temperature)
            if 0 <= temperature <= 10:
                break
            else:
                print("Por favor, insira um valor entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um valor numérico.")
    while True:
        response = list()
        question = input("\nPergunta (digite 'q' para sair):\n")
        if question.lower() == 'q':
            break

        animation_thread = threading.Thread(target=animation)
        animation_thread.start()
        response_thread = threading.Thread(target=generate_response, args=(rules, question, temperature, response))
        response_thread.start()

        response_thread.join()
        RESPONSE_READY = True
        animation_thread.join()
