from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI(title="Chatbot Itaú com Guardrails (sem LLM)")

# =========================
# [1] INPUT GUARDRAIL
# =========================

PALAVRAS_PROIBIDAS = [
    "ignore as regras",
    "burlar",
    "hackear",
    "quebrar o sistema",
    "bypass",
    "fraude"
]

def input_guardrail(texto: str) -> bool:
    texto_lower = texto.lower()
    for palavra in PALAVRAS_PROIBIDAS:
        if palavra in texto_lower:
            return False
    if len(texto) > 300:
        return False
    return True


# =========================
# [2] ANALISADOR DE INTENÇÃO & RISCO
# =========================

def analisar_intencao(texto: str) -> dict:
    texto_lower = texto.lower()

    if re.search(r"(burlar|fraude|hack|ignorar regras)", texto_lower):
        return {
            "intencao": "evasao_de_controle",
            "risco": "alto"
        }

    if re.search(r"(pix|saldo|transferência|boleto)", texto_lower):
        return {
            "intencao": "consulta_financeira",
            "risco": "baixo"
        }

    return {
        "intencao": "desconhecida",
        "risco": "medio"
    }


# =========================
# [3] POLICY ENGINE (REGRAS)
# =========================

def policy_engine(analise: dict) -> bool:
    """
    Retorna True se a resposta generativa for permitida
    """
    if analise["risco"] == "alto":
        return False
    return True


# =========================
# [4] ORQUESTRADOR DE PROMPT
# =========================

def orquestrador(texto_usuario: str) -> str:
    """
    Decide o que fazer com a requisição
    """

    # Input Guardrail
    if not input_guardrail(texto_usuario):
        return "Solicitação bloqueada por regras de segurança."

    # Análise de intenção
    analise = analisar_intencao(texto_usuario)

    # Policy Engine
    permitido = policy_engine(analise)

    if not permitido:
        return (
            "Não posso ajudar com esse tipo de solicitação. "
            "Para dúvidas sobre segurança, procure os canais oficiais do Itaú."
        )

    # Aqui entraria o LLM (simulado)
    return resposta_segura(texto_usuario)


# =========================
# [5] RESPOSTA SEGURA (simula LLM)
# =========================

def resposta_segura(texto: str) -> str:
    return (
        "Posso ajudar com informações gerais sobre produtos e serviços do Itaú, "
        "como Pix, contas e educação financeira."
    )


# =========================
# MODELO DE ENTRADA
# =========================

class Pergunta(BaseModel):
    mensagem: str


# =========================
# ENDPOINTS
# =========================

@app.get("/")
def home():
    return {"mensagem": "API Chatbot Itaú com Guardrails ativa 111"}

@app.post("/chat")
def chat(pergunta: Pergunta):
    resposta = orquestrador(pergunta.mensagem)
    return {"resposta": resposta}

@app.get("/status")
def status():
    return {"status": "Sistema seguro em execução"}
