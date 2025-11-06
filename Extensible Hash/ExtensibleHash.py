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

    def insert(self, key, value):
         index = self.hash(key)
         bucket = self.directory[index]
         print(f"Tentando inserir chave {key} no bucket {index} que tem {len(bucket.kv_pairs)} itens.")
         if bucket.is_full():
               print(f"Erro: Bucket no índice {index} está cheio! Inserção de chave {key} não foi possível.")
            return
 
        bucket.insert(key, value)
        print(f"Chave {key} inserida com sucesso no bucket {index}.")

    
    
    def search(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        value = bucket.search(key)
        if value is not None:
            print(f"Encontrado na posição {index}: {value}")
        else:
            print(f"Chave {key} não encontrada na posição {index}.")
        return value

    def remove(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
       
        print(f"Tentando remover chave {key} do bucket {index}.")
        if bucket.remove(key):
            print(f"Chave {key} removida com sucesso do bucket {index}.")
        else:
            print(f"Chave {key} não encontrada no bucket {index} para remoção.")

    def display(self):
        print(f"Global depth: {self.global_depth}")
        print("Directory:")
        # Conjunto para evitar mostrar buckets duplicados
        seen = set()
        for i, bucket in enumerate(self.directory):
            if id(bucket) not in seen:
                print(f"Index {i}: {bucket.display()}")
                seen.add(id(bucket))


# TESTES PARA VERIFICAÇÃO

# Cria a hash extensível com tamanho 2 para cada bucket
eh = ExtensibleHash(2)

# Insere três registros diferentes
eh.insert(1001, {"nome": "Ana Silva", "email": "ana.silva@example.com"})
eh.insert(1002, {"nome": "Carlos Souza", "email": "carlos.souza@example.com"})
eh.insert(1003, {"nome": "Mariana Lima", "email": "mariana.lima@example.com"})

# Busca uma chave existente
print("\nBusca por chave existente (1001):")
eh.search(1001)

# Busca uma chave inexistente
print("\nBusca por chave inexistente (9999):")
eh.search(9999)

# Exibe a estrutura atual da hash extensível
print("\nEstrutura da hash:")
eh.display()

# Testa uma inserção que deve falhar por bucket cheio
print("\nTentativa de inserir em bucket cheio:")
eh.insert(1003, {"nome": "João Pedro", "email": "joao.pedro@example.com"})