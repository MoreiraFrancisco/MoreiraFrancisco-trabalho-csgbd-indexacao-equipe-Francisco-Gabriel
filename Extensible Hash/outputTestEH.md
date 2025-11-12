```

===== TESTE 1: Criação de um hash extensível vazio =====

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 1
Tamanho do diretório: 2
Índices [0]: Depth 1, Items: {}
Índices [1]: Depth 1, Items: {}
───────────────────────────────

===== TESTE 2: Inserções simples (sem divisão de bucket) =====
Tentando inserir chave '1' no bucket 1 (Profundidade local: 1)
✅ Chave '1' inserida com sucesso no bucket 1.
Tentando inserir chave '3' no bucket 1 (Profundidade local: 1)
✅ Chave '3' inserida com sucesso no bucket 1.

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 1
Tamanho do diretório: 2
Índices [0]: Depth 1, Items: {}
Índices [1]: Depth 1, Items: {1: 1, 3: 3}
───────────────────────────────

===== TESTE 3: Inserção que causa um split =====
Tentando inserir chave '5' no bucket 1 (Profundidade local: 1)
⚠️ Bucket no índice 1 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 2
🔁 Diretório cheio — duplicando o diretório...
✅ Nova profundidade global: 2
✅ Tamanho do diretório: 4
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '5' no bucket 01 (Profundidade local: 2)
✅ Chave '5' inserida com sucesso no bucket 01.

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 2
Tamanho do diretório: 4
Índices [00, 10]: Depth 1, Items: {}
Índices [01]: Depth 2, Items: {1: 1, 5: 5}
Índices [11]: Depth 2, Items: {3: 3}
───────────────────────────────

===== TESTE 4: Inserções que forçam duplicação do diretório =====
Tentando inserir chave '7' no bucket 11 (Profundidade local: 2)
✅ Chave '7' inserida com sucesso no bucket 11.
Tentando inserir chave '2' no bucket 10 (Profundidade local: 1)
✅ Chave '2' inserida com sucesso no bucket 10.
Tentando inserir chave '6' no bucket 10 (Profundidade local: 1)
✅ Chave '6' inserida com sucesso no bucket 10.
Tentando inserir chave '4' no bucket 00 (Profundidade local: 1)
⚠️ Bucket no índice 00 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 2
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '4' no bucket 00 (Profundidade local: 2)
✅ Chave '4' inserida com sucesso no bucket 00.

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 2
Tamanho do diretório: 4
Índices [00]: Depth 2, Items: {4: 4}
Índices [01]: Depth 2, Items: {1: 1, 5: 5}
Índices [10]: Depth 2, Items: {2: 2, 6: 6}
Índices [11]: Depth 2, Items: {3: 3, 7: 7}
───────────────────────────────

===== TESTE 5: Buscas de chaves existentes e inexistentes =====
🔍 Chave '1' encontrada no bucket 01: 1
🔍 Chave '4' encontrada no bucket 00: 4
❌ Chave '999' não encontrada (bucket 11).

===== TESTE 6: Atualização de valor em chave já existente =====
Tentando inserir chave '4' no bucket 00 (Profundidade local: 2)
🔁 Chave '4' atualizada no bucket 00.
🔍 Chave '4' encontrada no bucket 00: 4

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 2
Tamanho do diretório: 4
Índices [00]: Depth 2, Items: {4: 4}
Índices [01]: Depth 2, Items: {1: 1, 5: 5}
Índices [10]: Depth 2, Items: {2: 2, 6: 6}
Índices [11]: Depth 2, Items: {3: 3, 7: 7}
───────────────────────────────

===== TESTE 7: Remoção de chaves =====
Tentando remover chave '1' do bucket 01...
🗑️ Chave '1' removida com sucesso do bucket 01.
Tentando remover chave '99' do bucket 11...
⚠️ Chave '99' não encontrada no bucket 11.

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 2
Tamanho do diretório: 4
Índices [00]: Depth 2, Items: {4: 4}
Índices [01]: Depth 2, Items: {5: 5}
Índices [10]: Depth 2, Items: {2: 2, 6: 6}
Índices [11]: Depth 2, Items: {3: 3, 7: 7}
───────────────────────────────

===== TESTE 8: Inserção de vários elementos (teste de stress) =====
Tentando inserir chave '10' no bucket 10 (Profundidade local: 2)
⚠️ Bucket no índice 10 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
🔁 Diretório cheio — duplicando o diretório...
✅ Nova profundidade global: 3
✅ Tamanho do diretório: 8
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '10' no bucket 010 (Profundidade local: 3)
✅ Chave '10' inserida com sucesso no bucket 010.
Tentando inserir chave '11' no bucket 011 (Profundidade local: 2)
⚠️ Bucket no índice 011 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '11' no bucket 011 (Profundidade local: 3)
✅ Chave '11' inserida com sucesso no bucket 011.
Tentando inserir chave '12' no bucket 100 (Profundidade local: 2)
✅ Chave '12' inserida com sucesso no bucket 100.
Tentando inserir chave '13' no bucket 101 (Profundidade local: 2)
✅ Chave '13' inserida com sucesso no bucket 101.
Tentando inserir chave '14' no bucket 110 (Profundidade local: 3)
✅ Chave '14' inserida com sucesso no bucket 110.
Tentando inserir chave '15' no bucket 111 (Profundidade local: 3)
✅ Chave '15' inserida com sucesso no bucket 111.
Tentando inserir chave '16' no bucket 000 (Profundidade local: 2)
⚠️ Bucket no índice 000 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '16' no bucket 000 (Profundidade local: 3)
✅ Chave '16' inserida com sucesso no bucket 000.
Tentando inserir chave '17' no bucket 001 (Profundidade local: 2)
⚠️ Bucket no índice 001 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '17' no bucket 001 (Profundidade local: 3)
✅ Chave '17' inserida com sucesso no bucket 001.
Tentando inserir chave '18' no bucket 010 (Profundidade local: 3)
⚠️ Bucket no índice 010 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
🔁 Diretório cheio — duplicando o diretório...
✅ Nova profundidade global: 4
✅ Tamanho do diretório: 16
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '18' no bucket 0010 (Profundidade local: 4)
✅ Chave '18' inserida com sucesso no bucket 0010.
Tentando inserir chave '19' no bucket 0011 (Profundidade local: 3)
⚠️ Bucket no índice 0011 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '19' no bucket 0011 (Profundidade local: 4)
✅ Chave '19' inserida com sucesso no bucket 0011.
Tentando inserir chave '20' no bucket 0100 (Profundidade local: 3)
⚠️ Bucket no índice 0100 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '20' no bucket 0100 (Profundidade local: 4)
✅ Chave '20' inserida com sucesso no bucket 0100.
Tentando inserir chave '21' no bucket 0101 (Profundidade local: 3)
⚠️ Bucket no índice 0101 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '21' no bucket 0101 (Profundidade local: 4)
✅ Chave '21' inserida com sucesso no bucket 0101.
Tentando inserir chave '22' no bucket 0110 (Profundidade local: 3)
⚠️ Bucket no índice 0110 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '22' no bucket 0110 (Profundidade local: 4)
✅ Chave '22' inserida com sucesso no bucket 0110.
Tentando inserir chave '23' no bucket 0111 (Profundidade local: 3)
⚠️ Bucket no índice 0111 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 2 itens entre dois buckets.
Tentando inserir chave '23' no bucket 0111 (Profundidade local: 4)
✅ Chave '23' inserida com sucesso no bucket 0111.
Tentando inserir chave '24' no bucket 1000 (Profundidade local: 3)
✅ Chave '24' inserida com sucesso no bucket 1000.
Tentando inserir chave '25' no bucket 1001 (Profundidade local: 3)
✅ Chave '25' inserida com sucesso no bucket 1001.
Tentando inserir chave '26' no bucket 1010 (Profundidade local: 4)
✅ Chave '26' inserida com sucesso no bucket 1010.
Tentando inserir chave '27' no bucket 1011 (Profundidade local: 4)
✅ Chave '27' inserida com sucesso no bucket 1011.
Tentando inserir chave '28' no bucket 1100 (Profundidade local: 4)
✅ Chave '28' inserida com sucesso no bucket 1100.
Tentando inserir chave '29' no bucket 1101 (Profundidade local: 4)
✅ Chave '29' inserida com sucesso no bucket 1101.

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 4
Tamanho do diretório: 16
Índices [0000, 1000]: Depth 3, Items: {16: 16, 24: 24}
Índices [0001, 1001]: Depth 3, Items: {17: 17, 25: 25}
Índices [0010]: Depth 4, Items: {2: 2, 18: 18}
Índices [0011]: Depth 4, Items: {3: 3, 19: 19}
Índices [0100]: Depth 4, Items: {4: 4, 20: 20}
Índices [0101]: Depth 4, Items: {5: 5, 21: 21}
Índices [0110]: Depth 4, Items: {6: 6, 22: 22}
Índices [0111]: Depth 4, Items: {7: 7, 23: 23}
Índices [1010]: Depth 4, Items: {10: 10, 26: 26}
Índices [1011]: Depth 4, Items: {11: 11, 27: 27}
Índices [1100]: Depth 4, Items: {12: 12, 28: 28}
Índices [1101]: Depth 4, Items: {13: 13, 29: 29}
Índices [1110]: Depth 4, Items: {14: 14}
Índices [1111]: Depth 4, Items: {15: 15}
───────────────────────────────

===== TESTE 9: Busca após várias inserções =====
🔍 Chave '10' encontrada no bucket 1010: 10
🔍 Chave '15' encontrada no bucket 1111: 15
🔍 Chave '20' encontrada no bucket 0100: 20
🔍 Chave '25' encontrada no bucket 1001: 25
❌ Chave '30' não encontrada (bucket 1110).
❌ Chave '999' não encontrada (bucket 0111).

===== TESTE 10: Inserções e remoções aleatórias (1 a 50) =====

🔹 Inserindo 50 chaves em ordem aleatória...

Tentando inserir chave '23' no bucket 1 (Profundidade local: 1)
✅ Chave '23' inserida com sucesso no bucket 1.
Tentando inserir chave '35' no bucket 1 (Profundidade local: 1)
✅ Chave '35' inserida com sucesso no bucket 1.
Tentando inserir chave '12' no bucket 0 (Profundidade local: 1)
✅ Chave '12' inserida com sucesso no bucket 0.
Tentando inserir chave '4' no bucket 0 (Profundidade local: 1)
✅ Chave '4' inserida com sucesso no bucket 0.
Tentando inserir chave '38' no bucket 0 (Profundidade local: 1)
✅ Chave '38' inserida com sucesso no bucket 0.
Tentando inserir chave '6' no bucket 0 (Profundidade local: 1)
⚠️ Bucket no índice 0 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 2
🔁 Diretório cheio — duplicando o diretório...
✅ Nova profundidade global: 2
✅ Tamanho do diretório: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '6' no bucket 10 (Profundidade local: 2)
✅ Chave '6' inserida com sucesso no bucket 10.
Tentando inserir chave '26' no bucket 10 (Profundidade local: 2)
✅ Chave '26' inserida com sucesso no bucket 10.
Tentando inserir chave '13' no bucket 01 (Profundidade local: 1)
✅ Chave '13' inserida com sucesso no bucket 01.
Tentando inserir chave '39' no bucket 11 (Profundidade local: 1)
⚠️ Bucket no índice 11 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 2
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '39' no bucket 11 (Profundidade local: 2)
✅ Chave '39' inserida com sucesso no bucket 11.
--- [10/50] Inserindo chave 27 ---
Tentando inserir chave '27' no bucket 11 (Profundidade local: 2)
⚠️ Bucket no índice 11 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
🔁 Diretório cheio — duplicando o diretório...
✅ Nova profundidade global: 3
✅ Tamanho do diretório: 8
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '27' no bucket 011 (Profundidade local: 3)
✅ Chave '27' inserida com sucesso no bucket 011.
Tentando inserir chave '48' no bucket 000 (Profundidade local: 2)
✅ Chave '48' inserida com sucesso no bucket 000.
Tentando inserir chave '43' no bucket 011 (Profundidade local: 3)
✅ Chave '43' inserida com sucesso no bucket 011.
Tentando inserir chave '34' no bucket 010 (Profundidade local: 2)
⚠️ Bucket no índice 010 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '34' no bucket 010 (Profundidade local: 3)
✅ Chave '34' inserida com sucesso no bucket 010.
Tentando inserir chave '36' no bucket 100 (Profundidade local: 2)
⚠️ Bucket no índice 100 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '36' no bucket 100 (Profundidade local: 3)
✅ Chave '36' inserida com sucesso no bucket 100.
Tentando inserir chave '1' no bucket 001 (Profundidade local: 2)
✅ Chave '1' inserida com sucesso no bucket 001.
Tentando inserir chave '31' no bucket 111 (Profundidade local: 3)
✅ Chave '31' inserida com sucesso no bucket 111.
Tentando inserir chave '18' no bucket 010 (Profundidade local: 3)
✅ Chave '18' inserida com sucesso no bucket 010.
Tentando inserir chave '40' no bucket 000 (Profundidade local: 3)
✅ Chave '40' inserida com sucesso no bucket 000.
Tentando inserir chave '21' no bucket 101 (Profundidade local: 2)
✅ Chave '21' inserida com sucesso no bucket 101.
--- [20/50] Inserindo chave 33 ---
Tentando inserir chave '33' no bucket 001 (Profundidade local: 2)
⚠️ Bucket no índice 001 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 3
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '33' no bucket 001 (Profundidade local: 3)
✅ Chave '33' inserida com sucesso no bucket 001.
Tentando inserir chave '41' no bucket 001 (Profundidade local: 3)
✅ Chave '41' inserida com sucesso no bucket 001.
Tentando inserir chave '16' no bucket 000 (Profundidade local: 3)
✅ Chave '16' inserida com sucesso no bucket 000.
Tentando inserir chave '7' no bucket 111 (Profundidade local: 3)
⚠️ Bucket no índice 111 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
🔁 Diretório cheio — duplicando o diretório...
✅ Nova profundidade global: 4
✅ Tamanho do diretório: 16
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '7' no bucket 0111 (Profundidade local: 4)
✅ Chave '7' inserida com sucesso no bucket 0111.
Tentando inserir chave '20' no bucket 0100 (Profundidade local: 3)
⚠️ Bucket no índice 0100 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '20' no bucket 0100 (Profundidade local: 4)
✅ Chave '20' inserida com sucesso no bucket 0100.
Tentando inserir chave '3' no bucket 0011 (Profundidade local: 3)
⚠️ Bucket no índice 0011 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '3' no bucket 0011 (Profundidade local: 4)
✅ Chave '3' inserida com sucesso no bucket 0011.
Tentando inserir chave '44' no bucket 1100 (Profundidade local: 4)
✅ Chave '44' inserida com sucesso no bucket 1100.
Tentando inserir chave '19' no bucket 0011 (Profundidade local: 4)
✅ Chave '19' inserida com sucesso no bucket 0011.
Tentando inserir chave '28' no bucket 1100 (Profundidade local: 4)
✅ Chave '28' inserida com sucesso no bucket 1100.
Tentando inserir chave '29' no bucket 1101 (Profundidade local: 3)
✅ Chave '29' inserida com sucesso no bucket 1101.
--- [30/50] Inserindo chave 10 ---
Tentando inserir chave '10' no bucket 1010 (Profundidade local: 3)
⚠️ Bucket no índice 1010 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '10' no bucket 1010 (Profundidade local: 4)
✅ Chave '10' inserida com sucesso no bucket 1010.
Tentando inserir chave '11' no bucket 1011 (Profundidade local: 4)
✅ Chave '11' inserida com sucesso no bucket 1011.
Tentando inserir chave '46' no bucket 1110 (Profundidade local: 3)
✅ Chave '46' inserida com sucesso no bucket 1110.
Tentando inserir chave '50' no bucket 0010 (Profundidade local: 4)
✅ Chave '50' inserida com sucesso no bucket 0010.
Tentando inserir chave '47' no bucket 1111 (Profundidade local: 4)
✅ Chave '47' inserida com sucesso no bucket 1111.
Tentando inserir chave '49' no bucket 0001 (Profundidade local: 3)
⚠️ Bucket no índice 0001 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '49' no bucket 0001 (Profundidade local: 4)
✅ Chave '49' inserida com sucesso no bucket 0001.
Tentando inserir chave '24' no bucket 1000 (Profundidade local: 3)
⚠️ Bucket no índice 1000 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '24' no bucket 1000 (Profundidade local: 4)
✅ Chave '24' inserida com sucesso no bucket 1000.
Tentando inserir chave '5' no bucket 0101 (Profundidade local: 3)
⚠️ Bucket no índice 0101 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '5' no bucket 0101 (Profundidade local: 4)
✅ Chave '5' inserida com sucesso no bucket 0101.
Tentando inserir chave '37' no bucket 0101 (Profundidade local: 4)
✅ Chave '37' inserida com sucesso no bucket 0101.
Tentando inserir chave '30' no bucket 1110 (Profundidade local: 3)
⚠️ Bucket no índice 1110 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 4
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '30' no bucket 1110 (Profundidade local: 4)
✅ Chave '30' inserida com sucesso no bucket 1110.
--- [40/50] Inserindo chave 32 ---
Tentando inserir chave '32' no bucket 0000 (Profundidade local: 4)
✅ Chave '32' inserida com sucesso no bucket 0000.
Tentando inserir chave '8' no bucket 1000 (Profundidade local: 4)
✅ Chave '8' inserida com sucesso no bucket 1000.
Tentando inserir chave '45' no bucket 1101 (Profundidade local: 4)
✅ Chave '45' inserida com sucesso no bucket 1101.
Tentando inserir chave '14' no bucket 1110 (Profundidade local: 4)
✅ Chave '14' inserida com sucesso no bucket 1110.
Tentando inserir chave '15' no bucket 1111 (Profundidade local: 4)
✅ Chave '15' inserida com sucesso no bucket 1111.
Tentando inserir chave '42' no bucket 1010 (Profundidade local: 4)
✅ Chave '42' inserida com sucesso no bucket 1010.
Tentando inserir chave '25' no bucket 1001 (Profundidade local: 4)
✅ Chave '25' inserida com sucesso no bucket 1001.
Tentando inserir chave '2' no bucket 0010 (Profundidade local: 4)
⚠️ Bucket no índice 0010 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 5
🔁 Diretório cheio — duplicando o diretório...
✅ Nova profundidade global: 5
✅ Tamanho do diretório: 32
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '2' no bucket 00010 (Profundidade local: 5)
✅ Chave '2' inserida com sucesso no bucket 00010.
Tentando inserir chave '22' no bucket 10110 (Profundidade local: 4)
✅ Chave '22' inserida com sucesso no bucket 10110.
Tentando inserir chave '9' no bucket 01001 (Profundidade local: 4)
✅ Chave '9' inserida com sucesso no bucket 01001.
--- [50/50] Inserindo chave 17 ---
Tentando inserir chave '17' no bucket 10001 (Profundidade local: 4)
⚠️ Bucket no índice 10001 está cheio. Iniciando divisão...
🔹 Nova profundidade local do bucket: 5
✅ Bucket dividido! Reorganizados 3 itens entre dois buckets.
Tentando inserir chave '17' no bucket 10001 (Profundidade local: 5)
✅ Chave '17' inserida com sucesso no bucket 10001.

(Inserção de 50 elementos concluída)

📘 Estado após todas as inserções:

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 5
Tamanho do diretório: 32
Índices [00000, 10000]: Depth 4, Items: {48: 48, 16: 16, 32: 32}
Índices [00001]: Depth 5, Items: {1: 1, 33: 33}
Índices [00010]: Depth 5, Items: {34: 34, 2: 2}
Índices [00011, 10011]: Depth 4, Items: {35: 35, 3: 3, 19: 19}
Índices [00100, 10100]: Depth 4, Items: {4: 4, 36: 36, 20: 20}
Índices [00101, 10101]: Depth 4, Items: {21: 21, 5: 5, 37: 37}
Índices [00110, 10110]: Depth 4, Items: {38: 38, 6: 6, 22: 22}
Índices [00111, 10111]: Depth 4, Items: {23: 23, 39: 39, 7: 7}
Índices [01000, 11000]: Depth 4, Items: {40: 40, 24: 24, 8: 8}
Índices [01001, 11001]: Depth 4, Items: {41: 41, 25: 25, 9: 9}
Índices [01010, 11010]: Depth 4, Items: {26: 26, 10: 10, 42: 42}
Índices [01011, 11011]: Depth 4, Items: {27: 27, 43: 43, 11: 11}
Índices [01100, 11100]: Depth 4, Items: {12: 12, 44: 44, 28: 28}
Índices [01101, 11101]: Depth 4, Items: {13: 13, 29: 29, 45: 45}
Índices [01110, 11110]: Depth 4, Items: {46: 46, 30: 30, 14: 14}
Índices [01111, 11111]: Depth 4, Items: {31: 31, 47: 47, 15: 15}
Índices [10001]: Depth 5, Items: {49: 49, 17: 17}
Índices [10010]: Depth 5, Items: {18: 18, 50: 50}
───────────────────────────────

🔻 Removendo 10 chaves aleatórias...

--- Removendo chave 46 ---
Tentando remover chave '46' do bucket 01110...
🗑️ Chave '46' removida com sucesso do bucket 01110.
--- Removendo chave 24 ---
Tentando remover chave '24' do bucket 11000...
🗑️ Chave '24' removida com sucesso do bucket 11000.
--- Removendo chave 22 ---
Tentando remover chave '22' do bucket 10110...
🗑️ Chave '22' removida com sucesso do bucket 10110.
--- Removendo chave 15 ---
Tentando remover chave '15' do bucket 01111...
🗑️ Chave '15' removida com sucesso do bucket 01111.
--- Removendo chave 28 ---
Tentando remover chave '28' do bucket 11100...
🗑️ Chave '28' removida com sucesso do bucket 11100.
--- Removendo chave 23 ---
Tentando remover chave '23' do bucket 10111...
🗑️ Chave '23' removida com sucesso do bucket 10111.
--- Removendo chave 29 ---
Tentando remover chave '29' do bucket 11101...
🗑️ Chave '29' removida com sucesso do bucket 11101.
--- Removendo chave 12 ---
Tentando remover chave '12' do bucket 01100...
🗑️ Chave '12' removida com sucesso do bucket 01100.
--- Removendo chave 26 ---
Tentando remover chave '26' do bucket 11010...
🗑️ Chave '26' removida com sucesso do bucket 11010.
--- Removendo chave 21 ---
Tentando remover chave '21' do bucket 10101...
🗑️ Chave '21' removida com sucesso do bucket 10101.

📘 Estado após remoções:

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 5
Tamanho do diretório: 32
Índices [00000, 10000]: Depth 4, Items: {48: 48, 16: 16, 32: 32}
Índices [00001]: Depth 5, Items: {1: 1, 33: 33}
Índices [00010]: Depth 5, Items: {34: 34, 2: 2}
Índices [00011, 10011]: Depth 4, Items: {35: 35, 3: 3, 19: 19}
Índices [00100, 10100]: Depth 4, Items: {4: 4, 36: 36, 20: 20}
Índices [00101, 10101]: Depth 4, Items: {5: 5, 37: 37}
Índices [00110, 10110]: Depth 4, Items: {38: 38, 6: 6}
Índices [00111, 10111]: Depth 4, Items: {39: 39, 7: 7}
Índices [01000, 11000]: Depth 4, Items: {40: 40, 8: 8}
Índices [01001, 11001]: Depth 4, Items: {41: 41, 25: 25, 9: 9}
Índices [01010, 11010]: Depth 4, Items: {10: 10, 42: 42}
Índices [01011, 11011]: Depth 4, Items: {27: 27, 43: 43, 11: 11}
Índices [01100, 11100]: Depth 4, Items: {44: 44}
Índices [01101, 11101]: Depth 4, Items: {13: 13, 45: 45}
Índices [01110, 11110]: Depth 4, Items: {30: 30, 14: 14}
Índices [01111, 11111]: Depth 4, Items: {31: 31, 47: 47}
Índices [10001]: Depth 5, Items: {49: 49, 17: 17}
Índices [10010]: Depth 5, Items: {18: 18, 50: 50}
───────────────────────────────

🔍 Buscando algumas chaves aleatórias...
🔍 Chave '17' encontrada no bucket 10001: 17
🔍 Chave '13' encontrada no bucket 01101: 13
❌ Chave '22' não encontrada (bucket 10110).
🔍 Chave '38' encontrada no bucket 00110: 38
🔍 Chave '25' encontrada no bucket 11001: 25
❌ Chave '100' não encontrada (bucket 00100).
❌ Chave '101' não encontrada (bucket 00101).
❌ Chave '102' não encontrada (bucket 00110).

✅ Teste finalizado! Estrutura e comportamento verificados.
´´´
