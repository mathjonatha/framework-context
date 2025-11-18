# ConTeXt Academic Press

**Framework profissional para publicações acadêmicas elegantes**

Um sistema completo baseado em ConTeXt para criar livros didáticos, apostilas e materiais acadêmicos com design moderno e minimalista, fugindo da estética "seca" tradicional do LaTeX.

## 🎯 Características

- **Design Moderno**: Templates elegantes e minimalistas
- **Tipografia Profissional**: Fontes Google otimizadas (Libertinus, Inter, JetBrains Mono)
- **Sistema de Cores**: Paletas configuráveis para diferentes identidades visuais
- **Componentes Reutilizáveis**: Teoremas, exemplos, exercícios com estilos consistentes
- **Matemática de Alta Qualidade**: Suporte completo para equações, fórmulas e notações
- **Build Automatizado**: CLI Python para compilação e exportação
- **Multi-formato**: Exportação para PDF, HTML, EPUB e mais
- **Impressão Profissional**: Suporte para offset (CMYK, PDF/X)

## 📋 Pré-requisitos

- Python 3.8+
- ~300MB de espaço em disco (para ConTeXt portátil)
- (Opcional) Pandoc para exportação
- (Opcional) Calibre para conversão EPUB

### 🚀 ConTeXt Portátil (Recomendado!)

O framework inclui **ConTeXt portátil** - não precisa instalar no sistema!

```bash
# Setup automático do ConTeXt
python setup-context.py
```

✅ **Vantagens**:
- Não interfere com o sistema
- Totalmente portátil
- Sem configuração de PATH
- Funciona automaticamente

📖 **[Guia de Setup Portátil](docs/setup-portatil.md)**

### Instalação Tradicional do ConTeXt (Alternativa)

Se preferir instalar ConTeXt globalmente no sistema:

📖 **Guias de Instalação Detalhados**:
- [🇧🇷 Windows 64-bit (Português)](docs/pt-BR/installation/windows.md)
- [🇺🇸 Windows 64-bit (English)](docs/en/installation/windows.md)

**Instalação Rápida**:

**Linux/macOS:**
```bash
rsync -av rsync://contextgarden.net/minimals/setup/first-setup.sh .
sh ./first-setup.sh
```

**Windows:**
Baixe [context-setup-win64.zip](http://minimals.contextgarden.net/setup/context-setup-win64.zip), extraia e execute `first-setup.bat`

## 🚀 Início Rápido

### 1. Instalar ConTeXt (primeira vez)

```bash
# Navegue até o diretório do framework
cd cap-base

# Instale ConTeXt portátil (aguarde 5-15 minutos)
python setup-context.py
```

### 2. Criar seu primeiro projeto

```bash
# Crie um novo projeto
python cap.py new meu-livro

# Navegue para o projeto criado
cd ../meu-livro
```

💡 **Nota**: O projeto é criado automaticamente fora do framework para manter tudo organizado!

### 3. Configurar seu livro

Edite `config/book.yaml` com informações do seu livro:

```yaml
title: "Cálculo Diferencial"
author: "Seu Nome"
institution:
  name: "Universidade XYZ"
  colors:
    primary: "#003366"
```

### 4. Escrever conteúdo

Adicione capítulos em `content/chapters/`:

```tex
\startchapter[title={Limites}]

\startsection[title={Definição}]

Texto do seu capítulo...

\stopsection

\stopchapter
```

### 5. Compilar e visualizar

```bash
# Compilar (simples!)
python build.py

# Modos disponíveis:
python build.py --draft      # Rápido (para desenvolvimento)
python build.py --final      # Otimizado (versão final)

# Abrir o PDF gerado
start output\main.pdf        # Windows
xdg-open output/main.pdf     # Linux
open output/main.pdf         # macOS
```

## 📁 Estrutura de um Projeto

Quando você cria um projeto, esta é a estrutura gerada:

```
meu-livro/
├── main.tex                    # Arquivo principal
├── content/                    # Seu conteúdo
│   ├── chapters/               #   Capítulos
│   ├── frontmatter/            #   Material inicial
│   └── backmatter/             #   Material final
├── assets/                     # Recursos
│   ├── images/                 #   Suas imagens
│   └── logos/                  #   Logos
├── config/
│   └── book.yaml               # Configuração do livro
├── output/                     # PDFs gerados aqui
├── build.py                    # Script de compilação
└── README.md                   # Instruções
```

## 🎨 Sistema de Design

### Cores

Paletas configuráveis baseadas em Material Design:

- **Primary**: Azul (#2196F3)
- **Accent**: Laranja (#FF9800)
- **Neutros**: Escala de cinzas
- **Semânticos**: Success, Warning, Error, Info

### Tipografia

Escala harmônica baseada em Perfect Fifth (1.5):

- **Serif**: Libertinus Serif (texto)
- **Sans**: Inter (títulos)
- **Mono**: JetBrains Mono (código)
- **Math**: Libertinus Math (matemática)

### Espaçamento

Sistema modular baseado em 8pt para consistência visual.

## 📚 Componentes

### Ambientes Matemáticos

```tex
\starttheorem[title={Teorema de Pitágoras}]
  Em um triângulo retângulo...
  \startformula
    c^2 = a^2 + b^2
  \stopformula
\stoptheorem

\startdefinition[title={Continuidade}]
  Uma função é contínua...
\stopdefinition
```

### Exemplos e Exercícios

```tex
\startexample[title={Limite}]
  Calcule: ...

  \startsolution
    Solução aqui...
  \stopsolution
\stopexample

\startexercise
  Liste de exercícios...
\stopexercise
```

### Boxes Especiais

```tex
\startCAPNote
  Nota informativa importante.
\stopCAPNote

\startCAPWarning
  Aviso sobre conceito complexo.
\stopCAPWarning
```

## 🔧 Comandos Principais

### Criar Projetos

```bash
# Do diretório cap-base/
python cap.py new meu-livro              # Projeto básico
python cap.py new apostila --type handbook   # Apostila
```

### Compilar Documentos

```bash
# Do diretório do projeto/
python build.py              # Compilação padrão
python build.py --draft      # Modo rápido (desenvolvimento)
python build.py --final      # Modo final (publicação)
```

### Gerenciar ConTeXt

```bash
# Do diretório cap-base/
python setup-context.py           # Instalar
python setup-context.py --list    # Listar versões
python setup-context.py --clean   # Limpar instalação
```

## 📖 Documentação

### 🚀 Comece Aqui

- **[Seu Primeiro Documento](docs/pt-BR/primeiro-documento.md)** - Tutorial completo (15 min)
- **[Your First Document](docs/en/first-document.md)** - Complete tutorial (15 min)

### Documentação Multi-idioma

Escolha seu idioma / Choose your language:

- 🇧🇷 **[Documentação em Português](docs/pt-BR/README.md)**
  - [Instalação Windows](docs/pt-BR/installation/windows.md)
  - **[🚀 Seu Primeiro Documento](docs/pt-BR/primeiro-documento.md)** ⏱️ 15 min
  - [Guia de Início](docs/pt-BR/getting-started.md)
  - [Sistema de Design](docs/pt-BR/design-system.md)

- 🇺🇸 **[Documentation in English](docs/en/README.md)**
  - [Windows Installation](docs/en/installation/windows.md)
  - **[🚀 Your First Document](docs/en/first-document.md)** ⏱️ 15 min
  - [Getting Started Guide](docs/en/getting-started.md)
  - [Design System](docs/en/design-system.md)

### Documentação Original (Português)

- [Guia de Início](docs/getting-started.md)
- [Sistema de Design](docs/design-system.md)
- [Referência de Componentes](docs/components-reference.md)
- [Guia de Templates](docs/templates-guide.md)

## 🎓 Exemplos

Projetos exemplo em `examples/`:

- `minimal/` - Projeto mínimo
- `math-textbook/` - Livro de matemática
- `programming-book/` - Livro de programação
- `chemistry-manual/` - Manual de química

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- ConTeXt e TeX community
- Google Fonts
- Material Design color system
- Todos os contribuidores

## 📧 Contato

Para dúvidas, sugestões ou feedback:

- Issues: [GitHub Issues]
- Discussões: [GitHub Discussions]

---

**ConTeXt Academic Press** - Transformando publicações acadêmicas com design elegante
