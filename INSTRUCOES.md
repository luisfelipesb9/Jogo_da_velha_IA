# Instruções de Instalação e Execução

Parece que você não tem o Python instalado em sua máquina. Para rodar o Jogo da Velha com IA, siga os passos abaixo:

## 1. Instalar o Python

1.  Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  Clique no botão amarelo **"Download Python 3.x.x"**.
3.  Execute o instalador baixado.
4.  **IMPORTANTE:** Na primeira tela do instalador, marque a opção **"Add Python to PATH"** (Adicionar Python ao PATH). Isso é crucial para que você possa rodar o comando `python` no terminal.
5.  Clique em **"Install Now"**.

## 2. Verificar a Instalação

Após a instalação, abra um novo terminal (Prompt de Comando ou PowerShell) e digite:

```bash
python --version
```

Se aparecer a versão do Python (ex: `Python 3.12.0`), a instalação foi bem-sucedida!

## Solução de Problemas Comuns

### "Python não foi encontrado" mas aparece no `where python`?
Se você rodar `where python` e ver um caminho como `C:\Users\Luis\AppData\Local\Microsoft\WindowsApps\python.exe`, mas o comando `python` der erro ou abrir a Microsoft Store, isso é normal do Windows.

**O que está acontecendo:** Esse arquivo é apenas um "atalho" (alias) que o Windows cria para te incentivar a instalar via loja. Ele **não** é o Python real.

**Como resolver:**
1.  Siga a instalação do passo 1 acima (baixando do python.org).
2.  Após instalar, se o erro persistir, digite "Gerenciar aliases de execução do aplicativo" no menu Iniciar do Windows.
3.  Desative as chaves para "App Installer" (python.exe e python3.exe).
4.  Feche e abra o terminal novamente.

## 3. Rodar o Jogo

Navegue até a pasta do projeto no terminal e execute o seguinte comando para abrir a interface gráfica:

```bash
python main.py
```

Divirta-se jogando contra a IA invencível!
