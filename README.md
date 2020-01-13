# cached-users
Exercício do processo seletivo da Instruct

## TODO
- [x] Implementar o código e fazer funcionar
- [x] Organizar o código
- [x] Verificar se o código está no padrão PEP8
- [x] Escrever os testes
- [x] Documentar e fazer um passo-a-passo de como instalar e utilizar
- [ ] Otimizar, se possível
- [ ] Adicionar o contribuinte

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
