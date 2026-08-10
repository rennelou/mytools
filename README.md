# Configuração Acesso ao GitHub via HTTPS (PAT)

Este guia ensina como configurar o acesso aos seus repositórios do GitHub utilizando um **Personal Access Token (PAT)**.
---

## Passo 1: Gerar o Personal Access Token (PAT) no GitHub

Como o GitHub não aceita mais senhas pessoais para operações na linha de comando, você deve gerar uma chave de acesso (PAT):

1. Acesse o GitHub e vá em **Settings** (no menu da sua foto de perfil).
2. No menu lateral esquerdo, selecione **Developer settings**.
3. Acesse **Personal access tokens** $\rightarrow$ **Tokens (classic)**.
4. Clique em **Generate new token** $\rightarrow$ **Generate new token (classic)**.
5. Preencha os campos:
   * **Note:** Dê um nome descritivo (ex: `PC-Faculdade`).
   * **Expiration:** Defina o prazo de validade desejado.
   * **Scopes:** Marque a caixa **`repo`** (concede acesso a repositórios públicos e privados).
6. Clique no botão verde **Generate token** no final da página.
7. ⚠️ **Copie e guarde o token gerado (`ghp_...`).** Ele será exibido uma única vez.

---

## Passo 2: Configurar o Assistente de Credenciais do Sistema

```bash
git config credential.helper store
```

---

## Passo 3: Clonar e Autenticar o Repositório
Clone seu repositório usando a URL HTTPS limpa e padrão:

```bash
git clone [https://github.com/USUARIO/NOME_DO_REPOSITORIO.git]
cd NOME_DO_REPOSITORIO
```

Realize uma operação de teste (ex: pull ou push):

```bash
git pull origin main
```

Insira as credenciais quando solicitado:

Username: Digite seu nome de usuário do GitHub.

Password: Cole o seu PAT (ghp_...) copiado no Passo 1.

Pronto! As credenciais serão salvas com segurança no cofre do seu sistema. Nas próximas operações de git push ou git pull, o acesso será automático e sem solicitar senha.

# Pre-Commit e Gitleaks

## Passo 1: Instalar o Pre-Commit
O pre-commit é um gerenciador de hooks feito em Python. Instale-o na sua máquina:

```bash
pip install pre-commit
```

## Passo 2: Criar o Arquivo de Configuração .pre-commit-config.yaml
Na raiz do seu repositório, crie um arquivo chamado .pre-commit-config.yaml e cole a configuração do GitLeaks:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.2
    hooks:
      - id: gitleaks
```

## Passo 3: Instalar o Hook no Repositório Git
No terminal, dentro da pasta do projeto, execute o comando para registrar o script no Git local:

```bash
pre-commit install
```

Saída esperada: pre-commit installed at .git/hooks/pre-commit

## Pass 4: Testando a Configuração

```bash
pre-commit run --all-files
```
