# API de Controle e Reserva de Salas de Aula
Esta API em Django foi desenvolvida para facilitar o controle e reserva de salas de aula em uma instituição educacional. Abaixo estão as instruções sobre como iniciar e usar a API.

Como Iniciar a API:

- Instalação de Pré-requisitos:

Certifique-se de ter o Python instalado em seu sistema. Se não tiver, você pode baixá-lo em python.org.

É recomendável criar e ativar um ambiente virtual para instalar as dependências da API de forma isolada. Você pode usar o venv para isso.

- Clonar o Repositório:

Clone o repositório da API para o seu ambiente de desenvolvimento:

```python
git clone https://github.com/seu-usuario/api-salas-de-aula.git
```
- Instalar Dependências:

Navegue até o diretório do projeto e instale as dependências listadas no arquivo requirements.txt:

```pyton
cd api-salas-de-aula
pip install -r requirements.txt
```
- Por fim, inicie o servidor Django:

```python
python manage.py runserver
```
- Acessar a API:

Após iniciar o servidor, a API estará acessível em http://localhost:8000/.

- Descrição e uso da API:

A API tem como principal função a de gerenciar a reserv de salas, de forma que possa disponibilizar informações como o horário, nome da sala, disponibilidade, e descrição a respeito da mesma.

O uso da API é intuitivo e para executar as operações sera apenas necessário selecionar os botões e campos necessários, assim podendo fazer as operações CRD.
