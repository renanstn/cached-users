# cached-users
Exercício do processo seletivo da Instruct

Candidato: **Renan Santana Desidério**

## O que é
Este programa recebe como entrada um **username**, e retorna o *e-mail*, *website*, e *hemisfério* do usuário buscado.

As buscas são feitas [nessa](https://jsonplaceholder.typicode.com/users) API.

## Como utilizar
Em seu terminal, siga os seguintes passos:
- Clone o projeto e o acesse
  - `git clone https://github.com/Doc-McCoy/cached-users.git`
  - `cd cached-users`
- Inicialize um ambiente virtual
  - `python -m venv .venv`
- Ative o ambiente virtual
  - Windows: `.venv\Scripts\activate`
  - Linux: `source .venv/bin/activate`
- Instale as dependências
  - `pip install -r requirements.txt`
- Execute os testes
  - `python -m unittest discover -s ./src/`
- Utilização do script
  - `python src/main.py <username>`

## Screenshot

![screenshot](https://github.com/Doc-McCoy/cached-users/blob/master/screenshot/print.png)
