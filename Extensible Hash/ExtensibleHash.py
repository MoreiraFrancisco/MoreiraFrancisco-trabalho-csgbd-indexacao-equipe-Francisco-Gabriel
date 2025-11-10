class Bucket:
    def __init__(self, local_depth, size):
        self.local_depth = local_depth
        self.size = size
        self.kv_pairs = {}

    def is_full(self):
        return len(self.kv_pairs) >= self.size

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


class ExtensibleHash:
    def __init__(self, bucket_size):
        self.global_depth = 1
        self.bucket_size = bucket_size
        # Diretório inicial com 2^global_depth buckets
        self.directory = [Bucket(local_depth=1, size=bucket_size) for _ in range(2)]

    def hash(self, key):
        return hash(key) & ((1 << self.global_depth) - 1)

    def double_directory(self):

      #  Duplica o diretório quando todos os bits atuais não são suficientes.
        print("🔁 Diretório cheio — duplicando o diretório...")
        # Dobra a lista do diretório (concatena ela consigo mesma)
        self.directory += self.directory.copy()
        self.global_depth += 1
        print(f"✅ Nova profundidade global: {self.global_depth}. Tamanho do diretório: {len(self.directory)}")

    def split_bucket(self, index):
       
        # Cria um novo bucket, redistribui as chaves entre os dois buckets e atualiza a profundidade local e o diretório
     
        old_bucket = self.directory[index]
        print(f"⚠️  Bucket no índice {index} está cheio. Iniciando divisão...")

        old_bucket.local_depth += 1
        print(f"🔹 Nova profundidade local do bucket: {old_bucket.local_depth}")

        # Se a profundidade local exceder a global, o diretório precisa ser duplicado
        if old_bucket.local_depth > self.global_depth:
            self.double_directory()

        # Cria um novo bucket com a mesma profundidade local do antigo
        new_bucket = Bucket(local_depth=old_bucket.local_depth, size=self.bucket_size)

        # Calcula o padrão de bits que diferencia os dois buckets
        mask = 1 << (old_bucket.local_depth - 1)

        # Atualiza o diretório: redistribui ponteiros entre antigo e novo bucket
        for i in range(len(self.directory)):
            # Se a posição do diretório aponta para o bucket antigo
            if self.directory[i] is old_bucket:
                # E o bit relevante é 1, ele deve apontar para o novo bucket
                if (i & mask) != 0:
                    self.directory[i] = new_bucket

        # Redistribui as chaves do bucket antigo
        all_items = list(old_bucket.kv_pairs.items())
        old_bucket.kv_pairs.clear()  # limpa o bucket antigo
        for key, value in all_items:
            # Recalcula o índice do diretório com base no novo global_depth
            new_index = self.hash(key)
            self.directory[new_index].insert(key, value)
        print(f"✅ Bucket dividido com sucesso! Reorganizados {len(all_items)} itens.")

    def insert(self, key, value):
        index = self.hash(key)
        bucket = self.directory[index]

        print(f"Tentando inserir chave '{key}' no bucket {index} (Profundidade local: {bucket.local_depth})")

        # Se a chave já existe, apenas atualiza
        if key in bucket.kv_pairs:
            bucket.insert(key, value)
            print(f"🔁 Chave '{key}' atualizada no bucket {index}.")
            return

        # Se o bucket estiver cheio, precisa ser dividido
        if bucket.is_full():
            self.split_bucket(index)
            # Após dividir, tenta inserir novamente (recursivamente)
            self.insert(key, value)
        else:
            # Caso contrário, insere normalmente
            bucket.insert(key, value)
            print(f"✅ Chave '{key}' inserida com sucesso no bucket {index}.")

    def search(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        value = bucket.search(key)

        if value is not None:
            print(f"🔍 Chave '{key}' encontrada no bucket {index}: {value}")
        else:
            print(f"❌ Chave '{key}' não encontrada (bucket {index}).")
        return value

    def remove(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        print(f"Tentando remover chave '{key}' do bucket {index}...")

        if bucket.remove(key):
            print(f"🗑️  Chave '{key}' removida com sucesso do bucket {index}.")
        else:
            print(f"⚠️  Chave '{key}' não encontrada no bucket {index}.")

    def display(self):
        print("\n📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘")
        print(f"Profundidade global: {self.global_depth}")
        seen = set()
        for i, bucket in enumerate(self.directory):
            if id(bucket) not in seen:
                print(f"Índice {i:02b}: {bucket.display()}")
                seen.add(id(bucket))
        print("───────────────────────────────")