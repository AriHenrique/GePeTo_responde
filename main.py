import openai
import os
from dotenv import load_dotenv

load_dotenv()

KEY_API = os.getenv('KEY_API')
MODEL = os.getenv('MODEL')


def generate_chat_response(rules: str, input_question: str, key_api: str = KEY_API, temperature: int = 7,
                           model: str = MODEL):
    """
    Gera uma resposta relacionada a pergunta do usuário em conjunto com as regras estabelecidas de como a IA deve responder
    :param model: Tipo do modelo do GPT usada
    :param rules: As regras da conversa, definidas pelo usuário.
    :param input_question:  A pergunta do usuário.
    :param key_api: chave API do usuário adquirida pela OpenAI
    :param temperature: Valor de parâmetro de quanto a resposta pode fugir da regra
    :return: A resposta gerada pela OpenAI com base na pergunta.
    """
    openai.api_key = key_api

    if temperature > 10 or temperature < 0:
        temperature = 10

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": rules.encode('utf-8')}, {"role": "user", "content": input_question.encode('utf-8')}],
        temperature=int(temperature // 10)
    )

    reply = response.choices[0].message.content.encode('utf-8')

    if reply:
        with open('resposta.txt', "+w", encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(reply)
        print("Resposta processada e salva em resposta.txt.")
    else:
        print("Ocorreu um erro ao processar a resposta.")

    return reply


if __name__ == "__main__":
    print("Digite 'q' para sair a qualquer momento")
    rules = input("Por favor, defina as regras do chat (tópico específico, formato das respostas, etc):\n\n")
    if rules.lower() == 'q':
        quit()
    while True:
        try:
            temperature = input("Em uma escala de 0 a 10, o quanto você deseja que a resposta se afaste das regras?"
                                    "Informe um numero : ")
            if temperature != 'q':
                temperature = int(temperature)
            else:
                quit()
            break
        except ValueError:
            print("Digite apenas numeros inteiros")
            continue
    question = input("Pergunta:\n\n")

    while question.lower() != 'q':
        resp = generate_chat_response(rules, question)
        print(resp, '\n\n')
        question = input("\n\nPergunta (digite 'q' para sair):\n\n")
