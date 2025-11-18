# Seu Primeiro Documento

**Guia prático para criar e compilar seu primeiro projeto com ConTeXt Academic Press**

Este tutorial irá guiá-lo através da criação de um documento acadêmico simples, do início à compilação. Em aproximadamente 15 minutos, você terá um PDF elegante e profissional.

## ⚡ Pré-requisitos

Antes de começar, certifique-se de ter:

- ✅ ConTeXt portátil instalado com `python setup-context.py`
- ✅ Python 3.8+ instalado
- ✅ Framework cap-base baixado

## 📝 Passo 1: Criar o Projeto

### Setup Inicial (primeira vez apenas)

Se ainda não fez o setup do ConTeXt portátil:

```bash
# Navegue até o diretório cap-base
cd C:\MeuTrabalho\cap-base

# Instale ConTeXt portátil (5-15 minutos)
python setup-context.py
```

### Criar projeto básico

```bash
# Certifique-se de estar dentro de cap-base/
cd C:\MeuTrabalho\cap-base

# Crie seu primeiro projeto
python cap.py new meu-primeiro-livro

# O projeto será criado FORA de cap-base, no diretório pai!
```

Isso criará a seguinte estrutura:

```
C:\MeuTrabalho/
├── cap-base/                       ← Framework
│   ├── core/
│   ├── build/
│   └── cap.py
│
└── meu-primeiro-livro/             ← Seu projeto (FORA do cap-base)
    ├── content/
    │   ├── chapters/               # Seus capítulos
    │   ├── frontmatter/            # Material inicial
    │   └── backmatter/             # Material final
    ├── assets/
    │   ├── images/                 # Suas imagens
    │   └── logos/                  # Logos
    ├── config/
    │   └── book.yaml               # Configurações
    ├── output/                     # PDFs gerados
    ├── main.tex                    # Arquivo principal
    ├── build.py                    # Helper de compilação
    └── README.md                   # Instruções do projeto
```

### Entrar no diretório do projeto

```bash
# Navegar para o projeto (um nível acima e então entrar)
cd ../meu-primeiro-livro
```

## ⚙️ Passo 2: Configurar Metadados

Abra o arquivo `config/book.yaml` em seu editor de texto favorito e edite as informações básicas:

```yaml
# Informações do livro
title: "Introdução à Matemática"
subtitle: "Fundamentos e Aplicações"
author: "Seu Nome Completo"
date: "\\currentdate"  # Data automática

# Informações da instituição (opcional)
institution:
  name: "Universidade XYZ"
  logo: ""  # Deixe vazio por enquanto
  colors:
    primary: "#2196F3"    # Azul
    secondary: "#FF9800"  # Laranja

# Configurações de design
design:
  template: "base"
  type: "textbook"
  style: "modern-minimal"

  fonts:
    main: "Libertinus Serif"
    sans: "Inter"
    mono: "JetBrains Mono"
    math: "Libertinus Math"

  layout:
    type: "classic"
    paper: "A4"
    margins: "generous"

# Idioma
language: "pt"
```

💡 **Dica**: Por enquanto, mantenha as configurações padrão. Você pode personalizar depois!

## 📖 Passo 3: Editar o Conteúdo Principal

Abra `main.tex` e veja a estrutura básica:

```tex
% meu-primeiro-livro
% Documento criado com ConTeXt Academic Press

% Carregar framework CAP (path relativo para cap-base)
\environment ../cap-base/core/cap-core

\startdocument

% ========================================
% MATÉRIA PRELIMINAR (Capa, Sumário)
% ========================================

\startfrontmatter

% Capa
\startstandardmakeup
  \vfill
  \midaligned{\definedfont[SansBold at 42pt]\color[CAPPrimary]{Introdução à Matemática}}
  \vskip 1cm
  \midaligned{\definedfont[Sans at 18pt]\color[cap:text:secondary]{Fundamentos e Aplicações}}
  \vskip 2cm
  \midaligned{\definedfont[SansBold at 24pt]{Seu Nome Completo}}
  \vfill
  \midaligned{\definedfont[Sans at 14pt]{Universidade XYZ}}
  \vskip 5mm
  \midaligned{\definedfont[Sans at 14pt]{\currentdate}}
\stopstandardmakeup

% Sumário
\page
\title{Sumário}
\placecontent

\stopfrontmatter

% ========================================
% CORPO DO DOCUMENTO
% ========================================

\startbodymatter

% Incluir capítulos
\component content/chapters/01-introduction

\stopbodymatter

% ========================================
% MATÉRIA FINAL
% ========================================

\startbackmatter

% Aqui você pode adicionar:
% - Bibliografia
% - Índice remissivo
% - Apêndices

\stopbackmatter

\stopdocument
```

### Personalizar a Capa

Edite as linhas da capa com suas informações:

```tex
\midaligned{\definedfont[SansBold at 42pt]\color[CAPPrimary]{Introdução à Matemática}}
```
→ Mude "Introdução à Matemática" para o título do seu livro

```tex
\midaligned{\definedfont[SansBold at 24pt]{Seu Nome Completo}}
```
→ Mude "Seu Nome Completo" para seu nome

## ✍️ Passo 4: Criar Seu Primeiro Capítulo

Crie um novo arquivo `content/chapters/01-introducao.tex`:

```tex
% Capítulo 1 - Introdução

\startchapter[title={Introdução},reference=cap:intro]

\startsection[title={Bem-vindo}]

Este é meu primeiro documento criado com o \color[CAPPrimary]{\bf ConTeXt Academic Press}.
Neste livro, vamos explorar conceitos fundamentais da matemática de forma clara e elegante.

\stopsection

\startsection[title={Objetivos}]

Os principais objetivos deste material são:

\startitemize[packed]
  \item Apresentar conceitos matemáticos de forma acessível
  \item Fornecer exemplos práticos e exercícios
  \item Desenvolver o raciocínio lógico
  \item Preparar para estudos avançados
\stopitemize

\stopsection

\startsection[title={Estrutura do Livro}]

Este livro está organizado da seguinte forma:

\startitemize[n]
  \item \bold{Capítulo 1}: Introdução (você está aqui!)
  \item \bold{Capítulo 2}: Conjuntos e Números
  \item \bold{Capítulo 3}: Funções
  \item \bold{Capítulo 4}: Limites e Continuidade
\stopitemize

\stopsection

\stopchapter
```

### Incluir o Capítulo no Main

Edite `main.tex` e substitua:

```tex
\component content/chapters/01-introduction
```

Por:

```tex
\component content/chapters/01-introducao
```

## 🎨 Passo 5: Adicionar Conteúdo Matemático

Vamos criar um segundo capítulo com conteúdo matemático. Crie `content/chapters/02-conjuntos.tex`:

```tex
% Capítulo 2 - Conjuntos

\startchapter[title={Conjuntos e Números},reference=cap:conjuntos]

\startsection[title={Noção de Conjunto}]

Um \index{conjunto}conjunto é uma coleção de objetos, chamados \index{elementos}elementos.

\startdefinition[title={Conjunto}]
Um conjunto é uma coleção bem definida de objetos distintos, chamados elementos.
Denotamos que um elemento \math{x} pertence a um conjunto \math{A} por:

\startformula
  x \in A
\stopformula
\stopdefinition

\startsubsection[title={Exemplos}]

Veja alguns exemplos de conjuntos:

\startexample[title={Conjuntos Numéricos}]
Os principais conjuntos numéricos são:

\startitemize
  \item \math{\naturals = \{0, 1, 2, 3, \ldots\}} — Números Naturais
  \item \math{\integers = \{\ldots, -2, -1, 0, 1, 2, \ldots\}} — Números Inteiros
  \item \math{\rationals} — Números Racionais
  \item \math{\reals} — Números Reais
  \item \math{\complexes} — Números Complexos
\stopitemize
\stopexample

\stopsubsection

\stopsection

\startsection[title={Operações com Conjuntos}]

\startsubsection[title={União}]

\startdefinition[title={União de Conjuntos}]
A união de dois conjuntos \math{A} e \math{B}, denotada por \math{A \cup B}, é o conjunto
formado por todos os elementos que pertencem a \math{A} ou a \math{B}:

\startformula
  A \cup B = \{x \mid x \in A \text{ ou } x \in B\}
\stopformula
\stopdefinition

\stopsubsection

\startsubsection[title={Interseção}]

\startdefinition[title={Interseção de Conjuntos}]
A interseção de dois conjuntos \math{A} e \math{B}, denotada por \math{A \cap B}, é o conjunto
formado por todos os elementos que pertencem simultaneamente a \math{A} e a \math{B}:

\startformula
  A \cap B = \{x \mid x \in A \text{ e } x \in B\}
\stopformula
\stopdefinition

\stopsubsection

\stopsection

\startsection[title={Exercícios}]

\startexercise
Sejam \math{A = \{1, 2, 3, 4\}} e \math{B = \{3, 4, 5, 6\}}. Determine:

\startitemize[n]
  \item \math{A \cup B}
  \item \math{A \cap B}
  \item \math{A - B}
\stopitemize
\stopexercise

\startCAPNote
Lembre-se: A união contém elementos de ambos os conjuntos, enquanto a interseção
contém apenas elementos comuns.
\stopCAPNote

\stopsection

\stopchapter
```

### Incluir o Segundo Capítulo

Em `main.tex`, adicione após o primeiro capítulo:

```tex
\startbodymatter

\component content/chapters/01-introducao
\component content/chapters/02-conjuntos

\stopbodymatter
```

## 🔨 Passo 6: Compilar o Documento

Agora vamos compilar! Com a nova estrutura cap-base, é muito simples:

### Método 1: Usando o Helper do Projeto (Recomendado)

```bash
# Certifique-se de estar no diretório do projeto
cd C:\MeuTrabalho\meu-primeiro-livro

# Compilação padrão
python build.py

# Compilação rápida (modo draft - mais rápido)
python build.py --draft

# Compilação final (otimizada)
python build.py --final
```

💡 **Vantagem**: O `build.py` automaticamente encontra o cap-base e chama o compilador!

### Método 2: Chamando cap.py Diretamente

```bash
# Do diretório do projeto
python ../cap-base/cap.py build --draft
python ../cap-base/cap.py build --final
```

### Método 3: ConTeXt Direto (Avançado)

```bash
# Apenas se ConTeXt estiver no PATH
context main.tex
```

### Durante a Compilação

Você verá mensagens no terminal indicando o progresso:

```
→ Executando: python C:\MeuTrabalho\cap-base\cap.py build

✓ Usando ConTeXt portátil: C:\MeuTrabalho\cap-base\context\standalone
✓ Binários do ConTeXt: ...\texmf-win64\bin

Compilando: main.tex
Modo: default

resolvers       | formats | executing runner 'run luatex format': ...
pages           > flushing realpage 1, userpage 1
...
mkiv lua stats  > used platform: mswin, type: windows, binary subtree: texmf-win64
mkiv lua stats  > used engine: luatex version: 1.15
...

✓ Compilação concluída em 8.42s
PDF gerado: output/main.pdf
```

⏱️ **Primeira compilação**: Pode levar 30-60 segundos (gera cache)
⏱️ **Compilações seguintes**: 5-10 segundos

## 📄 Passo 7: Visualizar o Resultado

Após a compilação bem-sucedida, você encontrará o arquivo PDF em `output/main.pdf`.

### Abrir o PDF

**Windows:**
```bash
start output\main.pdf
```

**Linux:**
```bash
xdg-open output/main.pdf
```

**macOS:**
```bash
open output/main.pdf
```

Ou simplesmente navegue até a pasta `output/` e clique duas vezes no arquivo `main.pdf`.

## 🎉 Resultado Esperado

Você deve ver um PDF com:

✅ **Capa elegante** com:
- Título do livro em destaque
- Subtítulo
- Nome do autor
- Instituição e data

✅ **Sumário automático** com:
- Capítulo 1: Introdução
- Capítulo 2: Conjuntos e Números

✅ **Capítulos formatados** com:
- Títulos em fonte sans-serif azul
- Seções bem estruturadas
- Listas formatadas
- Caixas de definição com fundo colorido
- Exemplos destacados
- Fórmulas matemáticas elegantes
- Notas informativas

## 🔧 Próximos Passos

### 1. Adicionar Mais Conteúdo

Crie mais capítulos seguindo o mesmo padrão:

```bash
content/chapters/03-funcoes.tex
content/chapters/04-limites.tex
```

### 2. Adicionar Figuras

Coloque imagens em `assets/images/` e use:

```tex
\startplacefigure[
  title={Legenda da figura},
  reference=fig:exemplo
]
  \externalfigure[nome-arquivo.pdf][width=0.7\textwidth]
\stopplacefigure
```

### 3. Adicionar Bibliografia

Crie `content/bibliography.bib`:

```bibtex
@book{exemplo2025,
  author = "Autor, Nome",
  title = "Título do Livro",
  publisher = "Editora",
  year = 2025
}
```

E cite no texto:

```tex
Como mostrado por \cite[exemplo2025]...
```

### 4. Personalizar Design

Edite `config/book.yaml` para mudar:
- Cores (primary, secondary)
- Fontes
- Layout (margens, espaçamento)
- Estilos de componentes

### 5. Explorar Componentes

Experimente usar:

```tex
% Teoremas
\starttheorem[title={Nome do Teorema}]
  Enunciado...
\stoptheorem

% Provas
\startproof
  Demonstração...
\stopproof

% Avisos
\startCAPWarning
  Cuidado com...
\stopCAPWarning

% Equações numeradas
\startformula
  E = mc^2
\stopformula
```

## 📚 Recursos Úteis

### Documentação

- [Sistema de Design](design-system.md) - Personalização visual
- [Referência de Componentes](components-reference.md) - Todos os comandos
- [Guia de Templates](templates-guide.md) - Templates avançados

### Exemplos

Veja exemplos completos em:
```
examples/
├── minimal/          # Exemplo mínimo
├── math-textbook/    # Livro de matemática completo
└── programming-book/ # Livro de programação
```

### Comandos Úteis

```bash
# Do diretório do projeto:

# Validar projeto
python build.py validate

# Limpar arquivos temporários
python build.py clean

# Ou usando cap.py diretamente:
python ../cap-base/cap.py validate
python ../cap-base/cap.py build --watch
python ../cap-base/cap.py export --format epub
```

## ⚠️ Problemas Comuns

### Erro: "ConTeXt not found"

**Solução**: Instale o ConTeXt portátil:
```bash
cd C:\MeuTrabalho\cap-base
python setup-context.py
```

### Erro na compilação

**Solução**: Verifique:
1. Todos os `\start...` têm um `\stop...` correspondente
2. Arquivos `.tex` estão salvos em UTF-8
3. Caminhos de arquivos estão corretos

### PDF não atualiza

**Solução**:
1. Feche o PDF antes de recompilar
2. Limpe o cache: `python build.py clean` ou delete arquivos `.tuc`, `.log`

### Fontes não aparecem corretamente

**Solução**:
1. Certifique-se de que as fontes estão instaladas
2. Execute: `mtxrun --script fonts --reload`

## 💡 Dicas Profissionais

1. **Use modo draft durante desenvolvimento**
   ```bash
   python build.py --draft
   ```
   É muito mais rápido!

2. **Organize capítulos por número**
   ```
   01-introducao.tex
   02-conjuntos.tex
   03-funcoes.tex
   ```

3. **Use referências ao invés de números fixos**
   ```tex
   Como vimos no capítulo~\in[cap:intro]...
   A equação~\in[eq:pitagoras] mostra que...
   ```

4. **Comente seu código**
   ```tex
   % TODO: Adicionar mais exemplos aqui
   % FIXME: Revisar esta demonstração
   ```

5. **Faça commits frequentes (se usar Git)**
   ```bash
   git add .
   git commit -m "Adiciona capítulo 2 sobre conjuntos"
   ```

## 🎓 Parabéns!

Você criou seu primeiro documento acadêmico com ConTeXt Academic Press!

Agora você pode:
- ✅ Criar projetos
- ✅ Editar conteúdo
- ✅ Compilar documentos
- ✅ Usar componentes matemáticos
- ✅ Gerar PDFs profissionais

Continue explorando e criando materiais acadêmicos elegantes! 📚✨

---

**Precisa de ajuda?** Consulte a [documentação completa](README.md) ou o [README principal](../../README.md)
