# ConTeXt - Diretório de Distribuições e Instalação

Este diretório contém as distribuições do ConTeXt e a instalação portátil ativa.

## 📁 Estrutura

```
context/
├── distributions/              # Distribuições (ZIPs) versionadas
│   ├── win64/                 # Windows 64-bit
│   │   ├── latest.zip        # Última versão
│   │   └── [outras versões]  # Versões específicas (futuro)
│   │
│   ├── linux64/               # Linux 64-bit (futuro)
│   │   └── latest.zip
│   │
│   └── osx64/                 # macOS 64-bit (futuro)
│       └── latest.zip
│
├── standalone/                 # Instalação ativa (NÃO versionado)
│   ├── tex/                   # ConTeXt instalado
│   │   ├── texmf-*/bin/      # Binários
│   │   ├── texmf-cache/      # Cache
│   │   ├── texmf-context/    # Macros ConTeXt
│   │   └── setuptex.bat      # Script de setup
│   └── first-setup.bat
│
├── active-version.txt          # Versão instalada (gerado)
│
└── README.md                   # Este arquivo
```

## 🎯 Propósito

### `distributions/`
**Versionado no Git** ✅

Contém os arquivos ZIP de instalação do ConTeXt para diferentes plataformas.
Estes arquivos são pequenos (1-2 MB) e servem como bootstrap para a instalação completa.

**Benefícios de versionar**:
- ✅ Setup rápido sem precisar baixar
- ✅ Mesma versão para todos os desenvolvedores
- ✅ Funciona offline
- ✅ Múltiplas versões disponíveis

### `standalone/`
**NÃO versionado** ❌

Contém a instalação completa do ConTeXt (~300MB).
É gerado automaticamente ao executar `python setup-context.py`.

**Por que não versionar**:
- ❌ Muito grande (~300MB)
- ❌ Gerado automaticamente
- ❌ Específico da máquina
- ❌ Pode ser recriado facilmente

## 🚀 Uso

### Instalação Inicial

```bash
# Na raiz do framework
python setup-context.py
```

Isso irá:
1. Detectar sua plataforma (win64, linux64, osx64)
2. Procurar `distributions/{plataforma}/latest.zip`
3. Extrair para `standalone/`
4. Executar instalação completa
5. Registrar versão em `active-version.txt`

### Listar Distribuições Disponíveis

```bash
python setup-context.py --list
```

Saída:
```
📦 Distribuições disponíveis:

  win64:
    - latest.zip (1.8 MB)

  linux64:
    (vazio)

  osx64:
    (vazio)
```

### Especificar Plataforma

```bash
# Forçar uso de plataforma específica
python setup-context.py --platform win64
```

### Reinstalar

```bash
# Limpar e reinstalar
python setup-context.py --force
```

### Limpar Instalação

```bash
# Apenas remover standalone/
python setup-context.py --clean
```

## 📦 Adicionar Nova Distribuição

### Windows 64-bit

```bash
# 1. Baixar
wget http://minimals.contextgarden.net/setup/context-setup-win64.zip

# 2. Mover para distributions/
mv context-setup-win64.zip context/distributions/win64/latest.zip

# 3. (Opcional) Versionar específica
cp context/distributions/win64/latest.zip \
   context/distributions/win64/2024.04.01.zip

# 4. Commit
git add context/distributions/win64/
git commit -m "Update ConTeXt win64 distribution"
```

### Linux 64-bit

```bash
# 1. Baixar
wget http://minimals.contextgarden.net/setup/context-setup-linux-64.zip

# 2. Mover
mv context-setup-linux-64.zip context/distributions/linux64/latest.zip

# 3. Commit
git add context/distributions/linux64/
git commit -m "Add ConTeXt linux64 distribution"
```

### macOS 64-bit

```bash
# 1. Baixar
wget http://minimals.contextgarden.net/setup/context-setup-osx-64.zip

# 2. Mover
mv context-setup-osx-64.zip context/distributions/osx64/latest.zip

# 3. Commit
git add context/distributions/osx64/
git commit -m "Add ConTeXt osx64 distribution"
```

## 🔄 Gerenciamento de Versões

### Estrutura de Versionamento

```
distributions/win64/
├── latest.zip              # Sempre a versão mais recente
├── 2024.04.01.zip         # Versão estável LTS
├── 2023.05.15.zip         # Versão antiga
└── beta-2024.11.18.zip    # Versão beta
```

### Como Adicionar Versão Específica

```bash
# 1. Copiar latest.zip para versão específica
cp context/distributions/win64/latest.zip \
   context/distributions/win64/$(date +%Y.%m.%d).zip

# 2. Commit
git add context/distributions/win64/
git commit -m "Archive ConTeXt version $(date +%Y.%m.%d)"
```

### Usar Versão Específica

```bash
# Futuro: permitir escolher versão
# python setup-context.py --version 2024.04.01

# Por enquanto: renomear manualmente
mv context/distributions/win64/latest.zip \
   context/distributions/win64/latest.zip.old

cp context/distributions/win64/2024.04.01.zip \
   context/distributions/win64/latest.zip

python setup-context.py --force
```

## 📊 Tamanhos Típicos

| Arquivo/Dir | Tamanho | Versionado? |
|-------------|---------|-------------|
| latest.zip (win64) | ~1-2 MB | ✅ Sim |
| latest.zip (linux64) | ~1-2 MB | ✅ Sim |
| latest.zip (osx64) | ~1-2 MB | ✅ Sim |
| standalone/ | ~300 MB | ❌ Não |

## 🔍 Verificar Instalação Ativa

```bash
# Ver informações da versão instalada
cat context/active-version.txt
```

Saída:
```
version=latest
platform=win64
installed_date=2025-01-18 14:30:00
zip_file=latest.zip
```

## ⚙️ Workflow Recomendado

### Para Desenvolvedores

```bash
# 1. Clonar repositório
git clone <repo>
cd ConTeXt

# 2. Instalar ConTeXt (uma vez)
python setup-context.py

# 3. Usar normalmente
python cap.py build
```

### Para Adicionar Plataforma

```bash
# 1. Baixar distribuição
wget <url-da-distribuição>

# 2. Mover para diretório correto
mv <arquivo> context/distributions/<plataforma>/latest.zip

# 3. Testar instalação
python setup-context.py --platform <plataforma> --force

# 4. Commit
git add context/distributions/<plataforma>/
git commit -m "Add <plataforma> distribution"
```

## 🐛 Troubleshooting

### Distribuição não encontrada

**Erro:**
```
❌ Erro: Distribuição não encontrada!
   Procurado: context/distributions/win64/latest.zip
```

**Solução:**
1. Baixar ZIP manualmente
2. Salvar em `context/distributions/win64/latest.zip`
3. Executar `python setup-context.py` novamente

### Instalação corrompida

**Sintomas:** Erros ao compilar documentos

**Solução:**
```bash
# Limpar e reinstalar
python setup-context.py --clean
python setup-context.py
```

### Múltiplas plataformas

**Situação:** Trabalhar em Windows e Linux

**Solução:**
Mantenha distribuições para ambas plataformas:
```
distributions/
├── win64/latest.zip      ✅
└── linux64/latest.zip    ✅
```

O script detecta automaticamente a plataforma correta.

## 📝 Notas

1. **Git LFS**: Se os ZIPs ficarem muito grandes, considere usar Git LFS
2. **CDN**: Para projetos públicos, pode hospedar ZIPs em CDN e baixar sob demanda
3. **Versionamento**: Mantenha ao menos uma versão estável versionada
4. **Limpeza**: `standalone/` é automaticamente ignorado pelo Git

## 🔗 Links Úteis

- [ConTeXt Standalone Download](http://minimals.contextgarden.net/current/setup/)
- [ConTeXt Wiki](https://wiki.contextgarden.net)
- [Framework Documentation](../README.md)
- [Setup Guide](../SETUP-PORTABLE.md)

---

**Última atualização**: 2025-01-18
