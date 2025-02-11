# Projeto-Audios-com-IA
### Este é um projeto da disciplina de Sistemas Distribuídos que visa integrar dois agentes inteligentes (IA) a uma API

## Instalação do Projeto

### IMPORTANTE PARA EXECUÇÃO DE ALGUMAS FERRAMENTAS A VERSÃO DO PYTHON UTILIZADA DEVE SER A VERSÃO Python 3.9
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Maicon-Souza-Audios-com-IA.git
2. **Navegue até a pasta onde o projeto foi clonado:**
   ```bash
   cd endereco-repositorio
3 . **Entre na pasta do backend**

4. **Instale as dependências:**
   ```bash
   python install -r requirements.txt OU 
   python -m pip install -r requirements.txt

5. **INSTALE O PYTORCH PARA A VERSÃO 3.9 DO PYTHON:**
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

6. **INSTALE O GERENCIADOR DE ARQUIVO USADO PELO WHISPER:**
   (CASO NÃO TENHA É NECESSÁRIO INSTALAR O CHOCOLATTEY TAMBÉM, AMBOS PELO POWERSHELL)
   ```bash
   # on Windows using Chocolatey (https://chocolatey.org/)
   choco install ffmpeg

   
7. **Execute o programa:**
      ```bash
    python run.py
__________________________________________________________________________________________________________

## Regras de Commit
- **Mensagens de Commit**: Para organizar melhor o histórico do projeto e garantir uma compreensão mais clara dos commits, será utilizado um formato de mensagem que identifica o tipo do commit:

  **Tipos**:
  - `feat`: Nova funcionalidade
  - `fix`: Correção de bug
  - `docs`: Alterações na documentação
  - `style`: Alterações que não afetam o funcionamento do código (formatação, espaços, etc.)
  - `refactor`: Refatoração de código sem alterar funcionalidades
  - `test`: Adição ou correção de testes
  - `chore`: Alterações administrativas e de manutenção do projeto

  **Exemplos de Mensagens para commit**:
  - `"[feat]: implementado o método para buscar cliente por CPF"`
  - `"[fix]: correção do erro na consulta de clientes ativos"`
  - `"[docs]: atualização no Documento de Requisitos (Dicionário de Dados) - todos os tipos DATE se tornaram TIMESTAMP"`
  - `"[docs]: adicionadas informações sobre novos requisitos no README"`
  - `"[style]: ajuste na formatação e indentação no código do controller"`
  - `"[refactor]: reorganização de métodos de manipulação de clientes"`
  - `"[test]: correção de testes para consulta de clientes ativos"`
  - `"[chore]: atualização das dependências do projeto para as versões mais recentes"`
 
## Relatório
O relatório detalhado do projeto pode ser acessado em: [Relatório do Projeto](https://docs.google.com/document/d/1G1SCv8qc4ozA8WvCNqMl6gWgwXUbTai6G4CXvlkGAKc/edit?pli=1&tab=t.0#heading=h.aczyuw2yex2w)
