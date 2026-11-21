from disco import *

print("""=============================
  Bem vindo ao lumen OS 1.0
=============================""")

def quebrar_linha(linha):
    palavras = []
    atual = ""
    texto = False
    for letra in linha:
        if letra == "'":
            texto = not texto
            atual += letra
        elif letra == " " and not texto:
            if atual:
                palavras.append(atual)
                atual = ""
        else:
            atual += letra
    if atual:
        palavras.append(atual)
    return palavras

def rodar(cod):
	print(repr(cod))
	if isinstance(cod, str):
		cod = cod.splitlines()
		print("ok")
	for linha in cod:
		ps = quebrar_linha(linha)
		print(ps)
		if len(ps) == 0:
			continue
		cmd = ps[0]
	
		if cmd == "editar" and len(ps) == 4:
			arquivo = ps[1]
			if ps[2] == "=":
				if arquivo in HD:
					HD[arquivo] = ps[3]
			elif ps[2] == "+=":
				if arquivo in HD:
					HD[arquivo] += ps[3]
			elif ps[2] == "-=":
				if arquivo in HD:
					HD[arquivo] -= ps[3]
			salvar_memoria(HD)
	
		elif cmd == "rodar" and len(ps) == 2:
			print(HD.keys())
			print(ps[1])
			if ps[1] in HD:
				print("Executando...")
				rodar(HD[ps[1]])
			else:
				print("Arquivo não encontrado")
		
		elif cmd == "criar" and len(ps) == 3:
			criar(ps[1], ps[2])
			salvar_memoria(HD)
		
		elif cmd == "help":
			print("""
=================
 lista de comandos
=================
editar    edita um arquivo

rodar   roda um arquivo

criar    cria um arquivo

help   mostra essa janela""")
	salvar_memoria(HD)
	
while True:
	cmd = input(">>")
	cod = [cmd]
	rodar(cod)
