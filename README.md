# 🤖 Chatbot Seguro com Guardrails – FastAPI

Este projeto implementa um **chatbot backend seguro**, desenvolvido em **FastAPI**, com **camadas de guardrails, análise de intenção e policy engine**, simulando um cenário real de atendimento bancário **sem uso de LLM externo**.

O foco do projeto é demonstrar **arquitetura segura, controle de risco e boas práticas de APIs**, e não apenas respostas conversacionais.

---

## 📌 Visão Geral

O chatbot recebe mensagens de usuários via API REST, aplica regras de segurança e controle de risco antes de decidir se a solicitação pode ser processada.

A solução simula um ambiente regulado (ex: setor financeiro), onde **nem toda pergunta pode gerar uma resposta livre**.

---

## 🧠 Arquitetura e Fluxo

Fluxo simplificado:

1. Usuário envia mensagem (`/chat`)
2. **Input Guardrail**
   - Bloqueio de palavras proibidas
   - Limite de tamanho
3. **Análise de Intenção e Risco**
   - Classificação da intenção do usuário
4. **Policy Engine**
   - Decide se a resposta é permitida
5. **Resposta Segura**
   - Retorna apenas informações autorizadas
6. Front-end simples em HTML é servido via FastAPI

---

## 🔐 Funcionalidades

- API REST com FastAPI
- Guardrails de entrada (input validation)
- Análise de intenção baseada em regex
- Classificação de risco (baixo / médio / alto)
- Policy engine para bloqueio de requisições sensíveis
- Simulação de resposta segura (sem LLM)
- Front-end estático simples (HTML)
- CORS habilitado
- Deploy pronto para Render

---

## 📂 Estrutura do Repositório

```text
ap_chatbot2/
├── main.py              # API FastAPI e lógica do chatbot
├── requirements.txt     # Dependências do projeto
├── render.yaml          # Configuração de deploy no Render
├── static/
│   └── index.html       # Interface simples do chatbot
└── README.md


