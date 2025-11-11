class Bucket:
    def __init__(self, local_depth, size):
        self.local_depth = local_depth
        self.size = size
        self.kv_pairs = {}

    def is_full(self):
        return len(self.kv_pairs) >= self.size

    def is_empty(self):
    # Verifica se o bucket está vazio (usado para merge).
        return len(self.kv_pairs) == 0

    def insert(self, key, value):
        self.kv_pairs[key] = value

    def search(self, key):
        return self.kv_pairs.get(key, None)

    def remove(self, key):
        if key in self.kv_pairs:
            del self.kv_pairs[key]
            return True
        return False

    def display(self):
        return f"Depth {self.local_depth}, Items: {self.kv_pairs}"

    def get_all_items(self):
        return list(self.kv_pairs.items())

    def clear(self):
        self.kv_pairs.clear()


class ExtensibleHash:
    def __init__(self, bucket_size):
        
        #Inicial: 2 buckets (2^1), global_depth=1

        self.global_depth = 1
        self.bucket_size = bucket_size
        self.directory = [
            Bucket(local_depth=1, size=bucket_size),
            Bucket(local_depth=1, size=bucket_size)
        ]
        self._split_attempts = {}

    def hash(self, key):

        # Calcula hash(key) usando hash() built-in do Python
        # Aplica máscara de bits: & ((1 << global_depth) - 1)

        return hash(key) & ((1 << self.global_depth) - 1)

    def _validate_invariants(self):
        
      # Valida que a estrutura mantém as propriedades de hash extensível.

        expected_size = 1 << self.global_depth
        if len(self.directory) != expected_size:
            raise RuntimeError(f"Tamanho do diretório inválido: {len(self.directory)}, esperado {expected_size}")
        for i, bucket in enumerate(self.directory):
            if bucket.local_depth > self.global_depth:
                raise RuntimeError(f"Bucket no índice {i} tem local_depth={bucket.local_depth} maior que global_depth={self.global_depth}")
        return True

    def double_directory(self):
        print("🔁 Diretório cheio — duplicando o diretório...")
        old_directory = self.directory
        self.directory = []
        for bucket in old_directory:
            self.directory.append(bucket)
        for bucket in old_directory:
            self.directory.append(bucket)
        self.global_depth += 1
        print(f"✅ Nova profundidade global: {self.global_depth}")
        print(f"✅ Tamanho do diretório: {len(self.directory)}")
        self._validate_invariants()

    def split_bucket(self, index):
        old_bucket = self.directory[index]
        print(f"⚠️ Bucket no índice {index:0{self.global_depth}b} está cheio. Iniciando divisão...")

        old_bucket.local_depth += 1
        print(f"🔹 Nova profundidade local do bucket: {old_bucket.local_depth}")

        if old_bucket.local_depth > self.global_depth:
            self.double_directory()

        new_bucket = Bucket(local_depth=old_bucket.local_depth, size=self.bucket_size)
        mask = 1 << (old_bucket.local_depth - 1)

        for i in range(len(self.directory)):
            if self.directory[i] is old_bucket:
                if (i & mask) != 0:
                    self.directory[i] = new_bucket

        all_items = old_bucket.get_all_items()
        old_bucket.clear()
        for key, value in all_items:
            local_index = hash(key) & ((1 << old_bucket.local_depth) - 1)
            if (local_index & mask) != 0:
                new_bucket.insert(key, value)
            else:
                old_bucket.insert(key, value)
        print(f"✅ Bucket dividido! Reorganizados {len(all_items)} itens entre dois buckets.")
        self._validate_invariants()

    def merge_buckets(self, index):

        bucket = self.directory[index]
        if bucket.local_depth <= 0:
            return False
        mask = 1 << (bucket.local_depth - 1)
        buddy_index = index ^ mask
        buddy_bucket = self.directory[buddy_index]
        if buddy_bucket.local_depth != bucket.local_depth:
            return False
        if bucket.is_empty() and buddy_bucket.is_empty():
            buddy_items = buddy_bucket.get_all_items()
            for key, value in buddy_items:
                bucket.insert(key, value)
            bucket.local_depth -= 1
            buddy_bucket.local_depth -= 1
            print(f"✅ Buckets {index:0{self.global_depth}b} e {buddy_index:0{self.global_depth}b} mesclados! Nova local_depth: {bucket.local_depth}")
            for i in range(len(self.directory)):
                if self.directory[i] is buddy_bucket:
                    self.directory[i] = bucket
            return True
        return False

    def contract_directory(self):
        max_local_depth = max(bucket.local_depth for bucket in self.directory)
        if max_local_depth < self.global_depth:
            print("📉 Contraindo diretório...")
            mid = len(self.directory) // 2
            self.directory = self.directory[:mid]
            self.global_depth -= 1
            print(f"✅ Diretório contraído! Nova profundidade global: {self.global_depth}")
            print(f"✅ Novo tamanho do diretório: {len(self.directory)}")
            self._validate_invariants()
            return True
        return False

    def insert(self, key, value):

        index = self.hash(key)
        bucket = self.directory[index]
        print(f"Tentando inserir chave '{key}' no bucket {index:0{self.global_depth}b} (Profundidade local: {bucket.local_depth})")
        if key in bucket.kv_pairs:
            bucket.insert(key, value)
            print(f"🔁 Chave '{key}' atualizada no bucket {index:0{self.global_depth}b}.")
            return
        if bucket.is_full():
            split_key = (id(bucket), bucket.local_depth)
            if split_key not in self._split_attempts:
                self._split_attempts[split_key] = 0
            self._split_attempts[split_key] += 1
            if self._split_attempts[split_key] > 3:
                print(f"⚠️ AVISO: Ciclo de divisão detectado no bucket {index:0{self.global_depth}b}. Possível problema com função hash ou colisões excessivas.")
                if not bucket.is_full():
                    bucket.insert(key, value)
                    print(f"✅ Chave '{key}' inserida após tratamento de ciclo.")
                else:
                    print(f"❌ Não foi possível inserir '{key}' - bucket permanece cheio!")
                return
            self.split_bucket(index)
            self._split_attempts.clear()
            self.insert(key, value)
        else:
            bucket.insert(key, value)
            print(f"✅ Chave '{key}' inserida com sucesso no bucket {index:0{self.global_depth}b}.")
            self._split_attempts.clear()

    def search(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        value = bucket.search(key)
        if value is not None:
            print(f"🔍 Chave '{key}' encontrada no bucket {index:0{self.global_depth}b}: {value}")
        else:
            print(f"❌ Chave '{key}' não encontrada (bucket {index:0{self.global_depth}b}).")
        return value

    def remove(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        print(f"Tentando remover chave '{key}' do bucket {index:0{self.global_depth}b}...")
        if bucket.remove(key):
            print(f"🗑️ Chave '{key}' removida com sucesso do bucket {index:0{self.global_depth}b}.")
            self.merge_buckets(index)
            self.contract_directory()
        else:
            print(f"⚠️ Chave '{key}' não encontrada no bucket {index:0{self.global_depth}b}.")

    def display(self):
        print("\n📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘")
        print(f"Profundidade global: {self.global_depth}")
        print(f"Tamanho do diretório: {len(self.directory)}")
        bucket_indices = {}
        for i, bucket in enumerate(self.directory):
            bucket_id = id(bucket)
            if bucket_id not in bucket_indices:
                bucket_indices[bucket_id] = []
            bucket_indices[bucket_id].append(i)
        seen = set()
        for i, bucket in enumerate(self.directory):
            bucket_id = id(bucket)
            if bucket_id not in seen:
                indices = bucket_indices[bucket_id]
                indices_str = ", ".join(f"{idx:0{self.global_depth}b}" for idx in indices)
                print(f"Índices [{indices_str}]: {bucket.display()}")
                seen.add(bucket_id)
        print("───────────────────────────────")



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

