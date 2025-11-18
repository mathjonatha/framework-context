# Instalação do ConTeXt no Windows 64-bit

**Guia de instalação do ConTeXt Standalone (MkIV) para Windows 64-bit**

> **NOTA IMPORTANTE**: Este guia é para instalar o ConTeXt MkIV (versão standalone clássica). Para a versão mais recente, considere instalar o [ConTeXt LMTX](https://wiki.contextgarden.net/Installation).

## Visão Geral

O ConTeXt Standalone é uma distribuição completa e atualizada do ConTeXt que pode ser instalada e atualizada eficientemente. Ele pode coexistir em paralelo com outras instalações TeX existentes, como MiKTeX, TeXLive, etc.

### Vantagens do ConTeXt Standalone

- **Atualizações contínuas**: Diferente do TeXLive (atualizado anualmente), o Standalone é atualizado continuamente
- **Não-interferente**: Não altera seu PATH nem variáveis de sistema globalmente
- **Portátil**: Pode ser movido entre diretórios ou computadores
- **Múltiplas instâncias**: Permite ter várias versões instaladas simultaneamente
- **Auto-contido**: Não interfere com outras distribuições TeX instaladas

### O que está incluído

- ConTeXt MkIV (engine LuaTeX)
- Fontes livres (aproximadamente 200MB)
- Binários rsync para Windows
- Scripts de atualização automática

### O que NÃO está incluído

- LaTeX e seus pacotes
- ConTeXt MkII (versão antiga)

## Requisitos

### Sistema

- Windows 7 ou superior
- Arquitetura 64-bit
- Aproximadamente 300MB de espaço em disco
- Conexão com a internet (para download inicial e atualizações)

### Programas Opcionais

Os seguintes programas não são necessários para executar o ConTeXt, mas adicionam funcionalidades extras:

- **curl**: Para incluir conteúdo remoto
- **ghostscript**: Para converter imagens PostScript para PDF
- **graphicsmagick** (convert): Para converter imagens GIF e TIFF
- **inkscape**: Para converter SVG e SVG comprimido
- **mupdf** (mudraw): Para converter PDF para PNG (usado para capas ePub)
- **pstoedit**: Para converter PostScript para contornos MetaPost
- **zint**: Para fornecer códigos de barras
- **zip** ou **7zip**: Para geração de EPUB

## Instalação

### Passo 1: Escolher o Diretório de Instalação

Escolha um diretório onde deseja instalar o ConTeXt. **Recomendações importantes**:

✅ **Recomendado**:
- `C:\context`
- `C:\Programs\context`
- `C:\tools\context`

❌ **Evite**:
- Caminhos com espaços: `C:\Program Files\context`
- Caminhos muito longos
- Caminhos com letras maiúsculas: `C:\CONTEXT` ou `C:\Temp`

> **Por quê?** O rsync às vezes tem problemas com caminhos que contêm letras maiúsculas ou espaços. Além disso, devido às convenções de nomes de arquivo 8.3 do Windows, nomes de diretório muito longos podem causar problemas.

### Passo 2: Baixar os Arquivos de Instalação

1. Baixe o arquivo de instalação para Windows 64-bit:
   - [context-setup-win64.zip](http://minimals.contextgarden.net/setup/context-setup-win64.zip)

2. Extraia o conteúdo para o diretório escolhido (ex: `C:\context`)

### Passo 3: Executar a Instalação

1. Abra o **Prompt de Comando** (`cmd.exe`)
   - Pressione `Win + R`
   - Digite `cmd` e pressione Enter

2. Navegue até o diretório de instalação:
   ```cmd
   cd C:\context
   ```

3. Execute o script de instalação:
   ```cmd
   first-setup.bat
   ```

   **Esta etapa demora bastante tempo** (pode levar 10-30 minutos dependendo da sua conexão), então aproveite para um café! ☕

### Opções de Instalação

#### Instalar versão estável (ao invés da beta)

Por padrão, o suite instala a versão beta do ConTeXt. Para instalar a versão estável:

```cmd
first-setup.bat --context=latest
```

#### Instalar todos os módulos de terceiros

Por padrão, o suite não instala módulos. Para instalar todos os módulos disponíveis:

```cmd
first-setup.bat --modules=all
```

#### Instalação completa com módulos

Para uma instalação completa com todos os módulos:

```cmd
first-setup.bat --context=latest --modules=all
```

## Configuração de Proxy (se necessário)

Se você está atrás de um servidor proxy, precisa informar os detalhes ao rsync.

### Método 1: Variável temporária

No Prompt de Comando, antes de executar `first-setup.bat`:

```cmd
set RSYNC_PROXY=usuario:senha@proxyhost:porta
```

Substitua:
- `usuario`: seu nome de usuário do proxy
- `senha`: sua senha do proxy
- `proxyhost`: endereço do servidor proxy
- `porta`: porta do proxy (geralmente 8080 ou 3128)

### Método 2: Variável permanente

Para definir permanentemente a variável de ambiente:

1. Clique com botão direito em "Meu Computador" ou "Este Computador"
2. Selecione "Propriedades"
3. Clique em "Configurações avançadas do sistema"
4. Clique em "Variáveis de Ambiente"
5. Adicione nova variável do sistema:
   - Nome: `RSYNC_PROXY`
   - Valor: `usuario:senha@proxyhost:porta`

### Problemas com Firewall

Se a porta 873 estiver bloqueada pelo firewall, mas a porta 22 (SSH) estiver aberta:

```cmd
set RSYNC_CONNECT_PROG=ssh tunnelhost nc %H 873
```

Onde `tunnelhost` é uma máquina fora do firewall na qual você tem acesso SSH.

## Uso do ConTeXt

O ConTeXt Standalone não interfere com o sistema porque não adiciona nada ao seu `PATH` nem define variáveis de sistema. Isso significa que você precisa fazer uma inicialização antes de usar.

### Uso Básico no Prompt de Comando

Antes de executar o ConTeXt, você precisa executar o `setuptex.bat`:

```cmd
C:\context\tex\setuptex.bat
```

Depois disso, você pode usar o ConTeXt normalmente:

```cmd
context --version
context meu-documento.tex
```

### Criar Atalho Permanente

Para evitar ter que digitar o caminho do `setuptex.bat` sempre, você pode criar um atalho:

1. Clique com botão direito no Desktop
2. Selecione "Novo" → "Atalho"
3. No campo de localização, digite:
   ```
   C:\WINDOWS\System32\cmd.exe /k C:\context\tex\setuptex.bat
   ```
   (Ajuste `C:\context` para seu diretório de instalação)
4. Dê um nome ao atalho, por exemplo: "ConTeXt Shell"

Agora, ao clicar neste atalho, você abrirá um Prompt de Comando com o ConTeXt já configurado!

### Verificar Instalação

Para verificar se está tudo funcionando:

```cmd
C:\context\tex\setuptex.bat
context --version
```

Você deve ver informações sobre a versão do ConTeXt instalada.

## Usando ConTeXt com Cygwin

Se você usa Cygwin, pode executar o ConTeXt dentro dele:

1. Execute `setuptex.bat` no Prompt de Comando do Windows
2. No mesmo prompt, entre no Cygwin executando `cygwin.bat` (no diretório de instalação do Cygwin)
3. No prompt do Cygwin, execute: `context.cmd teste.tex`

> **Nota**: É necessário usar a extensão `.cmd` no Cygwin.

## Atualizando o ConTeXt

Para atualizar sua instalação do ConTeXt:

1. Abra o Prompt de Comando
2. Navegue até o diretório de instalação:
   ```cmd
   cd C:\context
   ```
3. Execute novamente o script de instalação:
   ```cmd
   first-setup.bat
   ```

### Atualizar mantendo módulos instalados

Para atualizar e manter os módulos já instalados:

```cmd
first-setup.bat --keep
```

### Atualizar e instalar módulos específicos

```cmd
first-setup.bat --modules=t-letter,t-mathsets
```

## Desinstalação

O ConTeXt Standalone não modifica nada fora de sua pasta de instalação. Para desinstalar:

1. Simplesmente **delete o diretório de instalação** (ex: `C:\context`)
2. Se criou atalhos, delete-os também

Pronto! Nenhuma limpeza adicional é necessária.

## Instalando Módulos de Terceiros

O ConTeXt suite vem apenas com o módulo t-bib do Taco. Para instalar módulos adicionais:

### Instalar módulo específico

Para instalar o módulo t-letter do Wolfgang:

```cmd
first-setup.bat --modules=t-letter
```

### Instalar múltiplos módulos

Para instalar mais de um módulo, separe-os por vírgulas:

```cmd
first-setup.bat --modules=t-letter,t-mathsets
```

### Instalar todos os módulos

Para instalar todos os módulos extras de uma vez:

```cmd
first-setup.bat --modules=all
```

## Reverter para Versão Antiga

Se por algum motivo você quiser reverter para uma versão mais antiga:

```cmd
first-setup.bat --context=data
```

Onde `data` é a data de uma das versões estáveis do ConTeXt. A lista completa de versões antigas disponíveis está em: http://minimals.contextgarden.net/setup/

## Movendo a Instalação

A árvore de instalação do ConTeXt é **portátil** e pode ser movida entre diretórios ou máquinas.

Para mover a instalação:

1. Copie o diretório completo para o novo local
2. No novo local, limpe o cache:
   ```cmd
   mtxrun --generate
   ```

Isso regenera o cache (`./tex/texmf-cache/luatex-cache`).

## Refazendo os Formatos

Normalmente, o script de atualização cria os formatos automaticamente. Se por algum motivo você precisar recriá-los:

### Para formato MKIV (LuaTeX)

```cmd
mtxrun --generate
context --make
```

## Solução de Problemas

### Problema: rsync tem problemas com caminhos

**Sintomas**: Erros durante a instalação relacionados a caminhos.

**Solução**:
- Reinstale em um caminho totalmente em minúsculas, sem espaços
- Exemplo: `C:\context` ao invés de `C:\Context` ou `C:\Program Files\context`

### Problema: Erros com nomes de diretório de 8 caracteres

**Sintomas**: Avisos de arquivos ausentes contendo nomes de diretório de 8 caracteres criados pelo Windows (ex: `C:\CONTEX~1\tex`).

**Solução**:
- Use um nome de diretório curto (8 caracteres ou menos)
- Exemplo: `C:\ctx` ou `C:\context`

### Problema: rsync timeout atrás de firewall

**Sintomas**: Timeout durante download.

**Solução**:
- Abra a porta 873 para conexões TCP de saída no firewall
- Ou use o método de tunelamento SSH (veja seção de Proxy acima)

### Problema: Engine mismatch após atualização

**Sintomas**: Mensagem de erro tipo:
```
engine mismatch (luv: This is LuaTeX, Version beta-<version>...)
```

**Solução**:
1. Vá para `C:\context\tex\texmf-win64\bin`
2. Certifique-se de que `luatex.exe` e `texlua.exe` têm a mesma data
3. Delete o arquivo `luatex.dll`
4. Execute `context --make` novamente

### Problema: ConTeXt não encontrado após instalação

**Sintomas**: Comando `context` não é reconhecido.

**Solução**:
- Execute `setuptex.bat` antes de usar o ConTeXt
- Ou use o atalho criado na seção "Criar Atalho Permanente"

## Integrando com Editores

Para usar o ConTeXt com seu editor favorito:

### Método 1: Via Terminal

1. Abra o Prompt de Comando
2. Execute `setuptex.bat`
3. Inicie o editor a partir do mesmo prompt

### Método 2: Configurar PATH do Editor

Adicione `C:\context\tex\texmf-win64\bin` ao PATH que o editor busca. Os detalhes variam dependendo do editor.

Veja [Editores de Texto](../text-editors.md) para instruções específicas de integração com vários editores.

## Usando com ConTeXt Academic Press

Após instalar o ConTeXt Standalone, você pode usá-lo com o framework ConTeXt Academic Press:

1. Certifique-se de que o ConTeXt está instalado e funcionando
2. Navegue até o diretório do seu projeto CAP
3. Execute `setuptex.bat` do ConTeXt
4. Use o CLI do CAP normalmente:
   ```cmd
   python cap.py build
   ```

## Recursos Adicionais

- [ConTeXt Wiki](https://wiki.contextgarden.net)
- [ConTeXt Garden](http://www.contextgarden.net)
- [Lista de discussão](https://mailman.ntg.nl/mailman/listinfo/ntg-context)
- [Navegador de código fonte](http://source.contextgarden.net)

## Próximos Passos

Após instalar o ConTeXt com sucesso:

1. Leia o [Guia de Início Rápido](../getting-started.md)
2. Explore o [Sistema de Design](../design-system.md)
3. Crie seu primeiro projeto com ConTeXt Academic Press
4. Consulte a [Referência de Componentes](../components-reference.md)

---

**Documentação atualizada**: 2025-01-18
**Baseada em**: ConTeXt Standalone Wiki
