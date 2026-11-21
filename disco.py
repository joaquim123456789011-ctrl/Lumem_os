import json
import os

ARQUIVO = "HD.json"

# ===== CARREGAR MEMÓRIA =====
def carregar_memoria():
    if not os.path.exists(ARQUIVO):
        return {}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# ===== SALVAR MEMÓRIA =====
def salvar_memoria(HD):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(HD, f, indent=4)

# ===== CRIAR/MUDAR ARQUIVO =====
def criar(nome, dado):
    global HD
    HD[nome] = dado


HD = carregar_memoria()

with open("lumen_kernel.py", "r", encoding="utf-8") as a:
    sistema = a.read()

def dowload(os):
	criar("sistema.sys", os)
	salvar_memoria(HD)