# GePeTo

Este script utiliza a inteligência artificial da OpenAI (GPT-3) para gerar respostas com base em uma pergunta do usuário e regras específicas da conversa.
Ele também inclui uma animação de processamento enquanto a resposta está sendo gerada.

## Pré-requisitos
- Python (versão 3.6 ou superior)
- OpenAI Python SDK
- python-dotenv
- Chave API OpenAI

## Instalando as Bibliotecas

Certifique-se de que você possui as bibliotecas necessárias instaladas. Você pode usar o gerenciador de pacotes Python, como pip ou poetry, para instalá-las. Os arquivos `requirements.txt` e `pyproject.toml` incluem as bibliotecas necessárias. Para instalá-las, execute um dos seguintes comandos:

```bash
pip install -r requirements.txt
```
ou
```bash
poetry install
```
## Configuração

Antes de usar o script, configure suas variáveis de ambiente no arquivo .env. Você deve fornecer a sua chave de API da OpenAI e especificar o modelo GPT a ser utilizado.

__Exemplo do arquivo ```.env```:__
```dotenv
KEY_API=sua_chave_api
MODEL=gpt-3.5-turbo-16k
```
## Uso do Script

1. Execute o script em um ambiente Python compatível.
2. Siga as instruções no console para definir as regras da conversa, o grau de criatividade da resposta e fazer perguntas.
3. A resposta gerada pela IA será armazenada em um arquivo chamado ``resposta.txt`` e também será exibida no console.

Lembre-se de que você pode digitar 'q' a qualquer momento para sair.

## Como Obter uma Chave de API do GPT-3 da OpenAI

A OpenAI fornece uma API para acessar o GPT-3, um poderoso modelo de linguagem. Para começar a usar a API, você precisa obter uma chave de API. Aqui estão os passos para conseguir uma:

1. **Crie uma Conta OpenAI**: Se você ainda não tiver uma conta, acesse o site da OpenAI em [https://www.openai.com](https://www.openai.com) e crie uma conta.

2. **Faça Login na Sua Conta**: Após criar a conta, faça o login.

3. **Acesse a Página de Conta**: Uma vez logado, vá para a página da sua conta. Você pode encontrar essa opção no menu ou no seu painel de usuário.

4. **Crie uma Nova Chave de API**:
    - Dentro da sua conta, navegue até a seção de API.
    - Lá, você encontrará a opção para criar uma nova chave de API.
    - Clique para criar uma nova chave.
    - Você pode escolher o nome da chave e definir permissões específicas, se necessário.

5. **Guarde a Sua Chave com Cuidado**: Após criar a chave, ela será exibida na sua conta. Copie a chave e mantenha-a em um local seguro. Trate sua chave de API com sigilo, pois ela é usada para autenticar suas solicitações à API do GPT-3.

Agora você tem uma chave de API da OpenAI que pode ser usada para acessar o GPT-3 em seus próprios projetos e aplicativos.

Lembre-se de seguir as políticas de uso da OpenAI ao utilizar a API para garantir um uso adequado e ético.

Divirta-se explorando o poder do GPT-3!

## Preços e Cálculos de Uso da API GPT-3 da OpenAI

A API GPT-3 da OpenAI é uma ferramenta poderosa para o processamento de linguagem natural, mas seu uso tem custos associados. A OpenAI oferece preços flexíveis para a API, e é importante entender como esses preços são calculados.

### Preços

Os preços da API GPT-3 são baseados em duas métricas principais:

1. **Custo por Token**: Você é cobrado com base na quantidade de tokens utilizados em uma solicitação. Um token pode ser uma única palavra ou um caractere, por exemplo. O custo por token depende do modelo específico que você está usando. Modelos maiores têm um custo por token maior.

2. **Tempo de Processamento**: Além do custo por token, você também será cobrado com base no tempo de processamento da solicitação. Isso é medido em milissegundos e depende da quantidade de tempo que a solicitação leva para ser concluída.

### Cálculos de Uso

Para calcular o custo de uma solicitação à API GPT-3, você precisa considerar duas partes:

1. **Custo dos Tokens**: Primeiro, calcule o número de tokens em sua solicitação. Você pode usar a biblioteca OpenAI Python SDK para fazer isso. Lembre-se de que ambos os dados de entrada e saída contam como tokens. O cálculo pode ser feito com o seguinte código:

```python
import openai

response = openai.Completion.create(
    engine="davinci",
    prompt="Escreva algo interessante.",
    max_tokens=50
)

# Obtenha o número de tokens na resposta
num_tokens = response['usage']['total_tokens']
```

2. **Custo do Tempo de Processamento**: Em seguida, calcule o tempo que a solicitação leva para ser concluída. Você pode usar bibliotecas em Python, como time, para medir o tempo decorrido.

3. **Custo Total**: Com o número de tokens e o tempo de processamento, você pode calcular o custo total usando a seguinte fórmula:
    - _Custo Total = (Custo por Token * Número de Tokens) + (Custo por Milissegundo * Tempo de Processamento)_

É importante entender essas métricas e fazer cálculos de uso ao trabalhar com a API GPT-3 da OpenAI para controlar seus custos e otimizar o uso.

### Exemplo de Cálculo de Uso

Suponha que você está usando o mecanismo "davinci" e envia uma solicitação com 50 tokens e um tempo de processamento de 100 milissegundos. Se o custo por token for $0,01 e o custo por milissegundo for $0,00001, o cálculo de uso seria:
- _Custo Total = (0,01 * 50) + (0,00001 * 100) = $0,50 + $0,001 = $0,501_

Este é um exemplo simples de cálculo de uso da API GPT-3. Lembre-se de consultar a documentação oficial da OpenAI para obter informações atualizadas sobre preços e cálculos de uso.


# Autor
[AriHenrique](https://github.com/AriHenrique)

# Licença
Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para obter detalhes.

