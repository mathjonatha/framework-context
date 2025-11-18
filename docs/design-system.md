# Sistema de Design - ConTeXt Academic Press

O ConTeXt Academic Press utiliza um sistema de design modular baseado em **design tokens**, permitindo personalização consistente em todos os elementos.

## Filosofia de Design

### Princípios

1. **Elegância Minimalista**: Menos é mais - foco no conteúdo
2. **Hierarquia Visual Clara**: Facilita navegação e compreensão
3. **Consistência**: Elementos similares têm aparência similar
4. **Legibilidade**: Tipografia e espaçamento otimizados para leitura
5. **Profissionalismo**: Adequado para publicações acadêmicas formais

### Inspirações

- Tufte's Visual Explanations (uso de espaço em branco)
- Material Design (sistema de cores e elevação)
- Swiss Typography (grid e clareza)
- Livros da Princeton University Press (elegância acadêmica)

## Design Tokens

Design tokens são as variáveis fundamentais que definem a aparência visual.

### Cores

#### Paleta Primary (Azul)

Cores principais para elementos de destaque:

```
cap:primary:50   #E3F2FD  (mais claro)
cap:primary:100  #BBDEFB
cap:primary:200  #90CAF9
cap:primary:300  #64B5F6
cap:primary:400  #42A5F5
cap:primary:500  #2196F3  ← Primary padrão
cap:primary:600  #1E88E5
cap:primary:700  #1976D2
cap:primary:800  #1565C0
cap:primary:900  #0D47A1  (mais escuro)
```

**Uso:**
- Títulos de capítulos e seções
- Links e referências
- Elementos interativos
- Bordas de teoremas

#### Paleta Accent (Laranja)

Cores de destaque para elementos secundários:

```
cap:accent:50   #FFF3E0
cap:accent:100  #FFE0B2
...
cap:accent:500  #FF9800  ← Accent padrão
...
cap:accent:900  #E65100
```

**Uso:**
- Elementos de destaque (warnings, important boxes)
- Decorações
- Gráficos e diagramas

#### Paleta Neutral (Cinzas)

```
cap:neutral:50   #FAFAFA  (quase branco)
cap:neutral:100  #F5F5F5
...
cap:neutral:900  #212121  (quase preto)
```

**Uso:**
- Texto principal: `cap:neutral:900`
- Texto secundário: `cap:neutral:700`
- Fundos: `cap:neutral:50`

#### Cores Semânticas

```
Success:  #4CAF50 (verde) - Exemplos, soluções
Warning:  #FFC107 (amarelo) - Avisos
Error:    #F44336 (vermelho) - Erros, cuidados
Info:     #03A9F4 (azul claro) - Informações
```

#### Personalizando Cores

Em `config/book.yaml`:

```yaml
institution:
  colors:
    primary: "#003366"    # Sobrescreve primary
    secondary: "#FF6600"  # Sobrescreve accent
```

Ou direto em ConTeXt:

```tex
\definecolor[CAPPrimary][h=003366]
\definecolor[CAPAccent][h=FF6600]
```

### Tipografia

#### Escalas Tipográficas

Baseado em **Perfect Fifth** (ratio 1.5):

```
Base:     11pt
Small:    ~9.2pt   (0.833×)
Large:    ~16.5pt  (1.5×)
XLarge:   ~24.75pt (2.25×)
XXLarge:  ~37.1pt  (3.375×)
XXXLarge: ~55.7pt  (5.063×)
```

#### Hierarquia

```
Título de Capítulo:  XXXLarge (55.7pt) Sans Bold
Número de Capítulo:  72pt Sans Bold (decorativo)
Seção:               XLarge (37.1pt) Sans Bold
Subseção:            Large (24.75pt) Sans Bold
Subsubseção:         Base (16.5pt) Sans Bold
Corpo de texto:      Base (11pt) Serif
Legendas/Notas:      Small (9.2pt) Serif
```

#### Fontes

**Configuração padrão:**

```yaml
fonts:
  main: "Libertinus Serif"  # Texto
  sans: "Inter"             # Títulos
  mono: "JetBrains Mono"    # Código
  math: "Libertinus Math"   # Matemática
```

**Alternativas:**

Serif: EB Garamond, Crimson Pro, Source Serif Pro
Sans: Work Sans, Manrope, Rubik
Mono: Fira Code, IBM Plex Mono, Source Code Pro

#### Leading (Altura de Linha)

Baseado na **proporção áurea** (1.618):

```
Tight:    1.25× (para títulos)
Normal:   1.618× (texto corrido)
Relaxed:  1.75× (para listas)
Loose:    2× (para ênfase)
```

#### OpenType Features

```
Texto:    Old-style numbers, ligatures, kerning
Títulos:  Lining numbers, ligatures, kerning
Código:   Sem ligatures, kerning
```

### Espaçamento

#### Sistema Modular (8pt)

Todos os espaçamentos são múltiplos de 8pt:

```
Escala:
0:  0pt
1:  4pt    (0.5 unit)
2:  8pt    (1 unit - base)
3:  12pt   (1.5 units)
4:  16pt   (2 units)
5:  24pt   (3 units)
6:  32pt   (4 units)
7:  40pt   (5 units)
8:  48pt   (6 units)
9:  64pt   (8 units)
10: 80pt   (10 units)
11: 96pt   (12 units)
12: 128pt  (16 units)
```

#### Espaçamento Vertical

```
Entre parágrafos:         16pt
Antes de seção:           48pt
Depois de seção:          24pt
Antes de capítulo:        128pt
Depois de capítulo:       40pt
Antes/depois de boxes:    24pt
Antes/depois de fórmulas: 16pt
```

#### Indentação

```
Nenhuma:  0pt
Pequena:  1em
Normal:   1.5em (padrão)
Grande:   2em
```

### Grid System

#### Layouts Disponíveis

**Classic (Padrão):**
```
Backspace (lombo):    25mm
Largura do texto:     145mm
Margem superior:      20mm
Altura do texto:      220mm
Cabeçalho:           10mm
Rodapé:              10mm
```

**Modern:**
```
Backspace:     20mm
Largura:       160mm
Margem superior: 18mm
Altura:        235mm
```

**Compact:**
```
Backspace:     18mm
Largura:       174mm
Margem superior: 15mm
Altura:        247mm
```

#### Paper Sizes

- A4: 210×297mm (padrão internacional)
- Letter: 216×279mm (EUA)
- B5: 176×250mm (comum para livros)
- Crown Quarto: 189×246mm (livros britânicos)

#### Baseline Grid

Grid vertical ativado por padrão para alinhamento perfeito de linhas entre páginas adjacentes.

## Componentes

### Estilos de Títulos

#### Capítulos

**Large Number (Padrão):**
```
┌─────────────────────────────────┐
│  01                             │
│  Introdução                     │
│                                 │
│  Texto do capítulo...           │
└─────────────────────────────────┘
```

**Simple:**
```
Capítulo 1
Introdução
─────────────
```

**Decorative:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━
    C A P Í T U L O   I
       Introdução
━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Estilos de Boxes

#### Teoremas

**Leftbar:**
```
┃ Teorema 1.1 (Pitágoras)
┃
┃ Em um triângulo retângulo...
┃     c² = a² + b²
```

**Boxed:**
```
┌─────────────────────────────┐
│ Teorema 1.1 (Pitágoras)     │
│                             │
│ Em um triângulo retângulo...│
│     c² = a² + b²            │
└─────────────────────────────┘
```

**Minimal:**
```
Teorema 1.1 (Pitágoras)

Em um triângulo retângulo...
    c² = a² + b²
```

#### Exemplos

**Shaded (Padrão):**
```
┌──────────────────────────────┐
│░ Exemplo 1.1                 │
│░                             │
│░ Calcule...                  │
│░                             │
│░ Solução:                    │
│░ ...                         │
└──────────────────────────────┘
```

## Modos de Impressão

### Digital

```yaml
colorspace: RGB
hyperlinks: true
bookmarks: true
resolution: 150dpi
```

### Print (Offset)

```yaml
colorspace: CMYK
pdf_standard: PDF/X-1a
resolution: 300dpi
bleed: 3mm
```

## Personalização Avançada

### Criar Tema Customizado

1. Copie `core/design-tokens/colors.mkiv`
2. Modifique as cores
3. Carregue no seu projeto:

```tex
\environment meu-tema-colors.mkiv
```

### Criar Componente Customizado

```tex
% Definir box personalizado
\definetextbackground[meubox][
  background=color,
  backgroundcolor=cap:primary:50,
  frame=on,
  framecolor=CAPPrimary,
  corner=round,
  offset=\measured{cap:space:3}
]

% Usar
\startmeubox
  Conteúdo do box...
\stopmeubox
```

## Melhores Práticas

1. **Use apenas cores do sistema** - Garante consistência
2. **Respeite o espaçamento modular** - Mantém ritmo visual
3. **Não misture muitas fontes** - Máximo 3 famílias
4. **Teste em impressão** - PDF digital pode parecer diferente
5. **Use grid baseline** - Para livros impressos

## Recursos

- [ConTeXt Garden](https://wiki.contextgarden.net)
- [Material Design Colors](https://material.io/design/color)
- [Practical Typography](https://practicaltypography.com)
- [The Elements of Typographic Style](http://webtypography.net)
