# ConTeXt Portátil - Guia de Instalação

**Sistema de ConTeXt auto-contido dentro do framework**

Este guia explica como configurar o ConTeXt de forma portátil dentro do ConTeXt Academic Press, **sem necessidade de instalação global no Windows**.

## 🎯 Vantagens do ConTeXt Portátil

✅ **Não interfere com o sistema**: ConTeXt fica apenas no projeto
✅ **Portátil**: Copie o framework e leve para qualquer lugar
✅ **Isolado**: Não depende de instalação externa
✅ **Versionável**: Controle a versão exata do ConTeXt por projeto
✅ **Sem configuração de PATH**: Funciona automaticamente
✅ **Múltiplas versões**: Tenha diferentes versões em projetos diferentes

## 📋 Pré-requisitos

- Windows 64-bit
- Python 3.8+
- Arquivo `context-win64.zip` (já incluído no framework)
- ~300MB de espaço em disco

## 🚀 Instalação Rápida

### Passo 1: Executar Setup

Abra o terminal no diretório do framework e execute:

```bash
python setup-context.py
```

O script irá:
1. ✓ Verificar se `context-win64.zip` existe
2. ✓ Extrair para `context-standalone/`
3. ✓ Executar instalação do ConTeXt (baixa binários e fontes)
4. ✓ Criar script de ambiente `setup-cap-env.bat`

⏱️ **Tempo estimado**: 5-15 minutos (dependendo da conexão)

### Passo 2: Verificar Instalação

Execute:

```bash
setup-cap-env.bat
context --version
```

Você deve ver informações sobre a versão do ConTeXt instalada.

## 📁 Estrutura Criada

Após a instalação:

```
ConTeXt/
├── context-win64.zip           # Arquivo original (mantido)
├── context-standalone/         # ConTeXt instalado aqui
│   ├── tex/
│   │   ├── texmf-win64/       # Binários Windows 64-bit
│   │   │   └── bin/
│   │   │       ├── context.exe
│   │   │       ├── luatex.exe
│   │   │       └── ...
│   │   ├── texmf-cache/       # Cache
│   │   ├── texmf-context/     # Macros ConTeXt
│   │   ├── texmf-fonts/       # Fontes
│   │   └── setuptex.bat       # Script de setup
│   └── first-setup.bat
├── setup-cap-env.bat           # Script de ambiente (criado)
├── setup-context.py            # Script de instalação
└── ...
```

> **Nota**: O diretório `context-standalone/` está no `.gitignore` e não será versionado.

## 🔧 Uso Diário

### Opção 1: Automático (Recomendado)

O framework **detecta automaticamente** o ConTeXt portátil. Basta usar:

```bash
python cap.py build
```

### Opção 2: Com Script de Ambiente

Se quiser usar comandos ConTeXt diretamente:

```bash
# 1. Configurar ambiente
setup-cap-env.bat

# 2. Usar ConTeXt
context main.tex

# 3. Ou usar CAP CLI
python cap.py build
```

### Opção 3: Em Projetos

Ao criar um projeto, o ConTeXt portátil será usado automaticamente:

```bash
python cap.py new meu-livro
cd meu-livro
python ../cap.py build
```

## 🔄 Atualizando o ConTeXt

Para atualizar o ConTeXt portátil:

```bash
# Navegar até context-standalone
cd context-standalone

# Executar atualização
first-setup.bat
```

Ou reinstalar completamente:

```bash
# Remover instalação antiga
python setup-context.py --clean

# Instalar novamente
python setup-context.py
```

## 🗑️ Desinstalação

Para remover o ConTeXt portátil:

### Método 1: Script

```bash
python setup-context.py --clean
```

### Método 2: Manual

Simplesmente delete os diretórios:
```bash
rmdir /s context-standalone
del setup-cap-env.bat
```

## 🔍 Verificação de Funcionamento

### Teste 1: ConTeXt disponível

```bash
setup-cap-env.bat
context --version
```

Deve mostrar:
```
mtx-context     | ConTeXt Process Management ...
mtx-context     | current version: 2024.xx.xx ...
```

### Teste 2: Compilação funciona

Crie um arquivo `test.tex`:

```tex
\starttext
Hello, ConTeXt!
\stoptext
```

Compile:
```bash
context test.tex
```

Deve gerar `test.pdf`.

### Teste 3: CAP CLI funciona

```bash
python cap.py new projeto-teste
cd projeto-teste
python ../cap.py build
```

Deve gerar `main.pdf`.

## ⚙️ Opções Avançadas

### Forçar Reinstalação

```bash
python setup-context.py --force
```

### Apenas Limpar

```bash
python setup-context.py --clean
```

### Usar ConTeXt do Sistema

Se você tem ConTeXt instalado globalmente e quer usá-lo:

1. Remova ou renomeie `context-standalone/`
2. O framework usará automaticamente o ConTeXt do PATH

```bash
# Renomear para desabilitar temporariamente
ren context-standalone context-standalone.disabled
```

## 🐛 Solução de Problemas

### Problema: "context-win64.zip não encontrado"

**Solução**:
1. Baixe o ConTeXt standalone:
   - URL: http://minimals.contextgarden.net/setup/context-setup-win64.zip
2. Salve como `context-win64.zip` na raiz do framework

### Problema: Extração falha

**Solução**:
```bash
# Verificar se zip está corrompido
python -c "import zipfile; zipfile.ZipFile('context-win64.zip').testzip()"

# Se corrompido, baixar novamente
```

### Problema: first-setup.bat falha

**Solução**:
1. Verifique conexão com internet (baixa binários)
2. Desabilite antivírus temporariamente
3. Execute como administrador se necessário

### Problema: "ConTeXt não encontrado" ao compilar

**Solução 1**: Use o script de ambiente
```bash
setup-cap-env.bat
python cap.py build
```

**Solução 2**: Verifique instalação
```bash
python setup-context.py --force
```

### Problema: Binários não funcionam

**Sintomas**: Erro ao executar context.exe

**Solução**:
1. Verifique se é Windows 64-bit:
   ```bash
   systeminfo | find "System Type"
   ```
   Deve mostrar "x64-based PC"

2. Instale Visual C++ Redistributables se necessário

### Problema: Cache corrompido

**Solução**:
```bash
# Limpar cache
rmdir /s context-standalone\tex\texmf-cache
mkdir context-standalone\tex\texmf-cache

# Regenerar
setup-cap-env.bat
context --make
```

## 📊 Comparação: Portátil vs Global

| Aspecto | ConTeXt Portátil | ConTeXt Global |
|---------|------------------|----------------|
| Instalação | Automática via script | Manual no sistema |
| Localização | Dentro do projeto | C:\context ou similar |
| PATH | Não modifica | Precisa configurar |
| Portabilidade | ✅ Total | ❌ Presa ao sistema |
| Múltiplas versões | ✅ Fácil | ❌ Difícil |
| Espaço em disco | ~300MB por projeto | ~300MB total |
| Velocidade | Igual | Igual |
| Atualizações | Por projeto | Global |

## 🎯 Quando Usar Cada Abordagem

### Use ConTeXt Portátil se:
- ✅ Quer portabilidade total
- ✅ Trabalha em múltiplos projetos
- ✅ Precisa de versões diferentes
- ✅ Compartilha projetos com outros
- ✅ Não quer modificar o sistema

### Use ConTeXt Global se:
- ✅ Usa apenas um projeto
- ✅ Prefere instalação tradicional
- ✅ Já tem ConTeXt instalado
- ✅ Quer economizar espaço em disco

## 📝 Notas Importantes

1. **Git**: O `context-standalone/` está no `.gitignore`. Para compartilhar:
   - Inclua `context-win64.zip` (ou link para download)
   - Outros executam `python setup-context.py`

2. **Espaço**: Cada instalação usa ~300MB. Se trabalha em muitos projetos, considere:
   - Usar instalação global
   - Ou compartilhar uma instalação portátil entre projetos via symlink

3. **Performance**: Não há diferença de performance entre portátil e global.

4. **Atualizações**: Para atualizar todos os projetos:
   ```bash
   # Atualizar o zip base
   # Depois em cada projeto:
   cd projeto1
   python setup-context.py --force

   cd projeto2
   python setup-context.py --force
   ```

## 🚀 Workflow Recomendado

### Para novo projeto:

```bash
# 1. Setup inicial (primeira vez)
python setup-context.py

# 2. Criar projeto
python cap.py new meu-livro
cd meu-livro

# 3. Trabalhar
# Editar arquivos .tex...

# 4. Compilar (automático!)
python ../cap.py build
```

### Para projeto existente:

```bash
# 1. Clonar/baixar framework
git clone ...
cd ConTeXt

# 2. Instalar ConTeXt
python setup-context.py

# 3. Usar normalmente
python cap.py build
```

## 💡 Dicas Profissionais

1. **Primeiro projeto**: Execute setup uma vez, use em todos os projetos
2. **Backup**: Mantenha `context-win64.zip` em local seguro
3. **Compartilhamento**: Compartilhe o framework completo (exceto context-standalone)
4. **CI/CD**: Em pipelines, execute `setup-context.py` automaticamente
5. **Docker**: Considere criar imagem Docker com framework + ConTeXt

---

**Precisa de ajuda?** Consulte a [documentação completa](README.md) ou abra uma [issue](https://github.com/context-academic-press/issues).
