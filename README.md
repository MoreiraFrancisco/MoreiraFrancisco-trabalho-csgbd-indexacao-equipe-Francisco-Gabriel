
# Trabalho Prático 1 - Estruturas de indexação: Hash Extensível e Árvore B+
## Equipe: Francisco Moreira e Gabriel Ileis

# Hash Extensível
## A implementação inclui:
- Divisão automática de buckets (split) quando cheios
- Duplicação de diretório quando necessário
- Fusão de buckets vazios (merge)
- Contração de diretório para otimizar espaço
- Validação de invariantes da estrutura

## Arquivos
- ExtensibleHash — Implementação das classes principais:
  - ExtensibleHash: operações insert, search, remove e lógica de divisão/união de buckets.
  - Bucket: estrutura auxiliar para armazenar pares chave-valor e controlar a profundidade local.
- testEH — Bloco principal executa cenários automatizados de inserção, busca, splits, remoção e atualização, mostrando o estado da estrutura após cada etapa.
- outputTestEH - Saída dos testes em testEH

```
( ===== TESTE 1: Criação de um hash extensível vazio =====)

📘 ESTADO ATUAL DO HASH EXTENSÍVEL 📘
Profundidade global: 1
Tamanho do diretório: 2
Índices [0]: Depth 1, Items: {}
Índices [1]: Depth 1, Items: {}
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
```
