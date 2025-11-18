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

- ConTeXt (instalação standalone recomendada)
- Python 3.8+
- (Opcional) Pandoc para exportação
- (Opcional) Calibre para conversão EPUB

### Instalação do ConTeXt

📖 **Guias de Instalação Detalhados**:
- [🇧🇷 Windows 64-bit (Português)](docs/pt-BR/installation/windows.md)
- [🇺🇸 Windows 64-bit (English)](docs/en/installation/windows.md)

**Instalação Rápida**:

**Linux/macOS:**
```bash
# Download ConTeXt standalone
rsync -av rsync://contextgarden.net/minimals/setup/first-setup.sh .
sh ./first-setup.sh
```

**Windows:**
Baixe [context-setup-win64.zip](http://minimals.contextgarden.net/setup/context-setup-win64.zip), extraia e execute `first-setup.bat`

## 🚀 Início Rápido

### 1. Criar novo projeto

```bash
python cap.py new meu-livro --template math-textbook
cd meu-livro
```

### 2. Editar configurações

Edite `config/book.yaml` com informações do seu livro:

```yaml
title: "Cálculo Diferencial"
author: "Seu Nome"
institution:
  name: "Universidade XYZ"
  colors:
    primary: "#003366"
```

### 3. Escrever conteúdo

Adicione capítulos em `content/chapters/`:

```tex
\startchapter[title={Limites}]

\startsection[title={Definição}]

Texto do seu capítulo...

\stopsection

\stopchapter
```

### 4. Compilar

```bash
# Compilação rápida (rascunho)
python cap.py build --draft

# Compilação final
python cap.py build --final

# Para impressão offset
python cap.py build --print

# Para leitura digital
python cap.py build --digital
```

## 📁 Estrutura do Framework

```
context-academic-press/
├── core/                    # Núcleo do framework
│   ├── design-tokens/      # Cores, tipografia, espaçamento
│   ├── components/         # Componentes base
│   ├── layouts/           # Layouts de página
│   └── cap-core.mkiv      # Módulo principal
├── modules/               # Módulos especializados
│   ├── stem/             # Ciências Exatas
│   ├── chemistry/        # Química
│   ├── programming/      # Programação
│   └── humanities/       # Humanidades
├── templates/            # Templates completos
├── build/               # Sistema de build Python
├── examples/           # Projetos exemplo
├── docs/              # Documentação
└── cap.py            # CLI principal
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

## 🔧 Comandos CLI

```bash
# Criar novo projeto
cap new <nome> [--template <template>] [--type <tipo>]

# Compilar
cap build [--draft|--final|--print|--digital] [--watch]

# Validar projeto
cap validate

# Exportar
cap export --format [html|epub|docx|xml]

# Limpar arquivos temporários
cap clean
```

## 📖 Documentação

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
