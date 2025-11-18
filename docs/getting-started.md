# Guia de Início - ConTeXt Academic Press

Bem-vindo ao ConTeXt Academic Press! Este guia irá ajudá-lo a criar seu primeiro livro acadêmico com design elegante e profissional.

## Instalação

### 1. Instalar ConTeXt

**ConTeXt Standalone (Recomendado)**

O ConTeXt standalone é a forma mais confiável de ter a versão mais recente.

**Linux/macOS:**
```bash
# Baixar script de instalação
rsync -av rsync://contextgarden.net/minimals/setup/first-setup.sh .

# Executar instalação
sh ./first-setup.sh

# Adicionar ao PATH
export PATH=$HOME/context/tex/texmf-linux-64/bin:$PATH
```

**Windows:**
1. Baixe o instalador: https://wiki.contextgarden.net/ConTeXt_Standalone
2. Extraia para C:\context
3. Execute first-setup.bat
4. Adicione C:\context\tex\texmf-win64\bin ao PATH

### 2. Instalar Python

ConTeXt Academic Press requer Python 3.8 ou superior.

**Verificar instalação:**
```bash
python --version  # ou python3 --version
```

**Instalar dependências Python:**
```bash
pip install pyyaml  # Para processar arquivos de configuração
```

**Dependências opcionais:**
```bash
pip install watchdog  # Para modo watch (recompilação automática)
```

### 3. Instalar Fontes

As fontes Google utilizadas pelo framework:

- **Libertinus Serif**: https://github.com/alerque/libertinus
- **Inter**: https://rsms.me/inter/
- **JetBrains Mono**: https://www.jetbrains.com/lp/mono/

**Instalação automática (em desenvolvimento):**
```bash
python cap.py fonts install
```

## Seu Primeiro Projeto

### Passo 1: Criar Projeto

```bash
python cap.py new meu-primeiro-livro --template base --type textbook
cd meu-primeiro-livro
```

Isso cria a estrutura:
```
meu-primeiro-livro/
├── content/
│   ├── chapters/
│   │   └── 01-introduction.tex
│   ├── frontmatter/
│   └── backmatter/
├── assets/
│   ├── images/
│   └── logos/
├── config/
│   └── book.yaml
├── main.tex
└── Makefile
```

### Passo 2: Configurar Metadados

Edite `config/book.yaml`:

```yaml
title: "Introdução ao Cálculo"
author: "João Silva"
institution:
  name: "Universidade Federal XYZ"
  colors:
    primary: "#003366"  # Azul da instituição
    secondary: "#FF6600"

design:
  style: "modern-minimal"
  fonts:
    main: "Libertinus Serif"
    sans: "Inter"
```

### Passo 3: Escrever Conteúdo

Edite ou crie capítulos em `content/chapters/`:

**content/chapters/01-introduction.tex:**
```tex
\startchapter[title={Introdução ao Cálculo},reference=chap:intro]

\startsection[title={O que é Cálculo?}]

O cálculo é um ramo da matemática que estuda mudanças contínuas.
Foi desenvolvido independentemente por Isaac Newton e Gottfried Leibniz
no século XVII.

\stopsection

\startsection[title={Conceitos Fundamentais}]

\startsubsection[title={Limites}]

O conceito de limite é fundamental para entender o cálculo.

\startdefinition[title={Limite de uma Função}]
Dizemos que o limite de \math{f(x)} quando \math{x} tende a \math{a}
é \math{L}, e escrevemos:

\startformula
  \lim_{x \to a} f(x) = L
\stopformula

se os valores de \math{f(x)} se aproximam arbitrariamente de \math{L}
quando \math{x} se aproxima de \math{a}.
\stopdefinition

\stopsubsection

\stopsection

\stopchapter
```

### Passo 4: Compilar

**Compilação rápida (modo rascunho):**
```bash
python cap.py build --draft
# ou usando Make:
make draft
```

**Compilação final:**
```bash
python cap.py build --final
# ou:
make final
```

O PDF será gerado como `main.pdf`.

### Passo 5: Visualizar Resultado

Abra `main.pdf` com seu visualizador favorito.

## Estrutura de um Documento

### Arquivo Principal (main.tex)

```tex
\environment ../core/cap-core

\startdocument

% Matéria preliminar (capa, sumário)
\startfrontmatter
  % Capa
  \startstandardmakeup
    % Conteúdo da capa
  \stopstandardmakeup

  % Sumário
  \placecontent
\stopfrontmatter

% Corpo do documento
\startbodymatter
  \component content/chapters/01-introduction
  \component content/chapters/02-limits
  % ... mais capítulos
\stopbodymatter

% Material final (bibliografia, índice)
\startbackmatter
  % Bibliografia, índice, etc
\stopbackmatter

\stopdocument
```

### Estrutura de um Capítulo

```tex
\startchapter[title={Título do Capítulo},reference=chap:ref]

\startsection[title={Primeira Seção}]

Conteúdo da seção...

\startsubsection[title={Subseção}]
Conteúdo da subseção...
\stopsubsection

\stopsection

\stopchapter
```

## Elementos Comuns

### Matemática

**Inline:**
```tex
A equação \math{E = mc^2} é famosa.
```

**Display:**
```tex
\startformula
  \int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
\stopformula
```

### Teoremas e Definições

```tex
\starttheorem[title={Nome do Teorema}]
  Enunciado do teorema...
\stoptheorem

\startdefinition[title={Nome da Definição}]
  Texto da definição...
\stopdefinition
```

### Listas

**Lista com marcadores:**
```tex
\startitemize
  \item Primeiro item
  \item Segundo item
  \item Terceiro item
\stopitemize
```

**Lista numerada:**
```tex
\startitemize[n]
  \item Primeiro passo
  \item Segundo passo
  \item Terceiro passo
\stopitemize
```

### Figuras

```tex
\startplacefigure[
  title={Legenda da figura},
  reference=fig:exemplo
]
  \externalfigure[nome-arquivo.pdf][width=0.8\textwidth]
\stopplacefigure
```

Coloque as imagens em `assets/images/`.

### Referências Cruzadas

**Definir label:**
```tex
\startchapter[title={...},reference=chap:intro]
\startformula\label[eq:pitagoras]
  c^2 = a^2 + b^2
\stopformula
```

**Referenciar:**
```tex
Como vimos no capítulo~\in[chap:intro]...
De acordo com a equação~\in[eq:pitagoras]...
```

## Próximos Passos

- Explore [Sistema de Design](design-system.md) para personalizar cores e fontes
- Consulte [Referência de Componentes](components-reference.md) para todos os elementos disponíveis
- Veja [Guia de Templates](templates-guide.md) para templates especializados
- Confira projetos em `examples/` para inspiração

## Dicas

1. **Use modo draft durante desenvolvimento** - Compila mais rápido
2. **Valide regularmente** - `cap validate` detecta problemas cedo
3. **Organize capítulos em arquivos separados** - Facilita manutenção
4. **Use referências ao invés de números fixos** - ConTeXt atualiza automaticamente
5. **Commit frequentemente se usar Git** - Facilita rastrear mudanças

## Solução de Problemas

### ConTeXt não encontrado

Certifique-se de que ConTeXt está no PATH:
```bash
which context  # Linux/macOS
where context  # Windows
```

### Fontes não encontradas

Verifique se as fontes estão instaladas no sistema ou use:
```bash
mtxrun --script fonts --reload
```

### Erros de compilação

1. Verifique o arquivo de log: `main.log`
2. Tente limpar arquivos temporários: `make clean`
3. Compile novamente: `make build`

## Ajuda

Se precisar de ajuda:
- Consulte a documentação completa em `docs/`
- Veja issues no GitHub
- Consulte a wiki do ConTeXt: https://wiki.contextgarden.net

Bom trabalho criando materiais acadêmicos elegantes! 🎓
