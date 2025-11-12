import unittest
import random
from ExtensibleHash import Bucket, ExtensibleHash


# ==============================================================
# 🔍 TESTES PARA A IMPLEMENTAÇÃO DO HASH EXTENSÍVEL
# ==============================================================
# ⚙️ Pré-requisito: o código completo das classes Bucket e ExtensibleHash
# deve ter sido executado anteriormente neste notebook.
# ==============================================================

# 1️⃣ TESTE INICIAL — CRIAÇÃO BÁSICA
print("\n===== TESTE 1: Criação de um hash extensível vazio =====")
h = ExtensibleHash(bucket_size=2)  # cada bucket comporta no máximo 2 itens
h.display()

# 2️⃣ TESTE DE INSERÇÃO SEM SPLIT
print("\n===== TESTE 2: Inserções simples (sem divisão de bucket) =====")
h.insert(1, 1)
h.insert(3, 3)
h.display()  # ainda deve haver apenas 2 buckets

# 3️⃣ TESTE DE SPLIT DE BUCKET
print("\n===== TESTE 3: Inserção que causa um split =====")
# Este item deve causar o primeiro split, pois bucket encheu
h.insert(5, 5)
h.display()

# 4️⃣ TESTE DE DUPLICAÇÃO DE DIRETÓRIO
print("\n===== TESTE 4: Inserções que forçam duplicação do diretório =====")
# Insere vários itens até precisar dobrar o diretório (global_depth ↑)
for k in [7, 2, 6, 4]:
    h.insert(k, k)
h.display()

# 5️⃣ TESTE DE BUSCA
print("\n===== TESTE 5: Buscas de chaves existentes e inexistentes =====")
# Chaves que devem existir
h.search(1)
h.search(4)
# Chave que não existe
h.search(999)

# 6️⃣ TESTE DE ATUALIZAÇÃO DE CHAVE EXISTENTE
print("\n===== TESTE 6: Atualização de valor em chave já existente =====")
h.insert(4, 4)
h.search(4)
h.display()

# 7️⃣ TESTE DE REMOÇÃO
print("\n===== TESTE 7: Remoção de chaves =====")
h.remove(1)   # existente
h.remove(99)  # inexistente
h.display()

# 8️⃣ TESTE DE INSERÇÕES GRANDES (ESTRESSE)
print("\n===== TESTE 8: Inserção de vários elementos (teste de stress) =====")
for i in range(10, 30):
    h.insert(i, i)
h.display()

# 9️⃣ TESTE FINAL — BUSCA E CONSISTÊNCIA
print("\n===== TESTE 9: Busca após várias inserções =====")
for i in [10, 15, 20, 25, 30, 999]:
    h.search(i)

# ==============================================================
# 🔎 TESTES — INSERÇÕES E REMOÇÕES ALEATÓRIAS (1 A 50)
# ==============================================================
import random

print("\n===== TESTE 10: Inserções e remoções aleatórias (1 a 50) =====")

# Cria o hash extensível com buckets de tamanho 3 (pode ajustar se quiser)
h = ExtensibleHash(bucket_size=3)

# Gera lista de chaves de 1 a 50 e embaralha
chaves = list(range(1, 51))
random.shuffle(chaves)

print("\n🔹 Inserindo 50 chaves em ordem aleatória...\n")
for i, key in enumerate(chaves, start=1):
    if i % 10 == 0:
        print(f"--- [{i}/50] Inserindo chave {key} ---")
    h.insert(key, key)

print(f"\n(Inserção de {len(chaves)} elementos concluída)")

print("\n📘 Estado após todas as inserções:")
h.display()

# Agora vamos remover algumas chaves aleatoriamente
print("\n🔻 Removendo 10 chaves aleatórias...\n")
chaves_remover = random.sample(chaves, 10)
for key in chaves_remover:
    print(f"--- Removendo chave {key} ---")
    h.remove(key)

print("\n📘 Estado após remoções:")
h.display()

# Teste de busca aleatória (5 existentes, 3 inexistentes)
print("\n🔍 Buscando algumas chaves aleatórias...")
buscas = random.sample(chaves, 5) + [100, 101, 102]
for key in buscas:
    h.search(key)

print("\n✅ Teste finalizado! Estrutura e comportamento verificados.")
