# Your First Document

**Practical guide to creating and compiling your first project with ConTeXt Academic Press**

This tutorial will guide you through creating a simple academic document, from start to compilation. In approximately 15 minutes, you'll have an elegant and professional PDF.

## ⚡ Prerequisites

Before starting, make sure you have:

- ✅ ConTeXt installed and working ([Installation Guide](installation/windows.md))
- ✅ Python 3.8+ installed
- ✅ ConTeXt Academic Press framework downloaded

## 📝 Step 1: Create the Project

Open the terminal (on Windows, use the "ConTeXt Shell" shortcut or run `setuptex.bat` first).

### Create basic project

```bash
# Navigate to the framework directory
cd C:\context-academic-press

# Create your first project
python cap.py new my-first-book --template base --type textbook
```

This will create the following structure:

```
my-first-book/
├── content/
│   ├── chapters/
│   │   └── 01-introduction.tex    # Example chapter
│   ├── frontmatter/                # Front matter
│   └── backmatter/                 # Back matter
├── assets/
│   ├── images/                     # Your images
│   └── logos/                      # Logos
├── config/
│   └── book.yaml                   # Configuration
├── main.tex                        # Main file
└── Makefile                        # Build automation
```

### Enter the project directory

```bash
cd my-first-book
```

## ⚙️ Step 2: Configure Metadata

Open the `config/book.yaml` file in your favorite text editor and edit the basic information:

```yaml
# Book information
title: "Introduction to Mathematics"
subtitle: "Fundamentals and Applications"
author: "Your Full Name"
date: "\\currentdate"  # Automatic date

# Institution information (optional)
institution:
  name: "XYZ University"
  logo: ""  # Leave empty for now
  colors:
    primary: "#2196F3"    # Blue
    secondary: "#FF9800"  # Orange

# Design settings
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

# Language
language: "en"
```

💡 **Tip**: For now, keep the default settings. You can customize later!

## 📖 Step 3: Edit the Main Content

Open `main.tex` and see the basic structure:

```tex
% my-first-book
% Document created with ConTeXt Academic Press

\environment ../core/cap-core

\startdocument

% ========================================
% FRONT MATTER (Cover, Table of Contents)
% ========================================

\startfrontmatter

% Cover page
\startstandardmakeup
  \vfill
  \midaligned{\definedfont[SansBold at 42pt]\color[CAPPrimary]{Introduction to Mathematics}}
  \vskip 1cm
  \midaligned{\definedfont[Sans at 18pt]\color[cap:text:secondary]{Fundamentals and Applications}}
  \vskip 2cm
  \midaligned{\definedfont[SansBold at 24pt]{Your Full Name}}
  \vfill
  \midaligned{\definedfont[Sans at 14pt]{XYZ University}}
  \vskip 5mm
  \midaligned{\definedfont[Sans at 14pt]{\currentdate}}
\stopstandardmakeup

% Table of contents
\page
\title{Contents}
\placecontent

\stopfrontmatter

% ========================================
% DOCUMENT BODY
% ========================================

\startbodymatter

% Include chapters
\component content/chapters/01-introduction

\stopbodymatter

% ========================================
% BACK MATTER
% ========================================

\startbackmatter

% Here you can add:
% - Bibliography
% - Index
% - Appendices

\stopbackmatter

\stopdocument
```

### Customize the Cover

Edit the cover lines with your information:

```tex
\midaligned{\definedfont[SansBold at 42pt]\color[CAPPrimary]{Introduction to Mathematics}}
```
→ Change "Introduction to Mathematics" to your book title

```tex
\midaligned{\definedfont[SansBold at 24pt]{Your Full Name}}
```
→ Change "Your Full Name" to your name

## ✍️ Step 4: Create Your First Chapter

Create a new file `content/chapters/01-introduction.tex`:

```tex
% Chapter 1 - Introduction

\startchapter[title={Introduction},reference=chap:intro]

\startsection[title={Welcome}]

This is my first document created with \color[CAPPrimary]{\bf ConTeXt Academic Press}.
In this book, we will explore fundamental mathematical concepts in a clear and elegant way.

\stopsection

\startsection[title={Objectives}]

The main objectives of this material are:

\startitemize[packed]
  \item Present mathematical concepts in an accessible way
  \item Provide practical examples and exercises
  \item Develop logical reasoning
  \item Prepare for advanced studies
\stopitemize

\stopsection

\startsection[title={Book Structure}]

This book is organized as follows:

\startitemize[n]
  \item \bold{Chapter 1}: Introduction (you are here!)
  \item \bold{Chapter 2}: Sets and Numbers
  \item \bold{Chapter 3}: Functions
  \item \bold{Chapter 4}: Limits and Continuity
\stopitemize

\stopsection

\stopchapter
```

### Include the Chapter in Main

Edit `main.tex` and replace:

```tex
\component content/chapters/01-introduction
```

With:

```tex
\component content/chapters/01-introduction
```

## 🎨 Step 5: Add Mathematical Content

Let's create a second chapter with mathematical content. Create `content/chapters/02-sets.tex`:

```tex
% Chapter 2 - Sets

\startchapter[title={Sets and Numbers},reference=chap:sets]

\startsection[title={Set Concept}]

A \index{set}set is a collection of objects, called \index{elements}elements.

\startdefinition[title={Set}]
A set is a well-defined collection of distinct objects, called elements.
We denote that an element \math{x} belongs to a set \math{A} by:

\startformula
  x \in A
\stopformula
\stopdefinition

\startsubsection[title={Examples}]

See some examples of sets:

\startexample[title={Number Sets}]
The main number sets are:

\startitemize
  \item \math{\naturals = \{0, 1, 2, 3, \ldots\}} — Natural Numbers
  \item \math{\integers = \{\ldots, -2, -1, 0, 1, 2, \ldots\}} — Integers
  \item \math{\rationals} — Rational Numbers
  \item \math{\reals} — Real Numbers
  \item \math{\complexes} — Complex Numbers
\stopitemize
\stopexample

\stopsubsection

\stopsection

\startsection[title={Set Operations}]

\startsubsection[title={Union}]

\startdefinition[title={Set Union}]
The union of two sets \math{A} and \math{B}, denoted by \math{A \cup B}, is the set
formed by all elements that belong to \math{A} or \math{B}:

\startformula
  A \cup B = \{x \mid x \in A \text{ or } x \in B\}
\stopformula
\stopdefinition

\stopsubsection

\startsubsection[title={Intersection}]

\startdefinition[title={Set Intersection}]
The intersection of two sets \math{A} and \math{B}, denoted by \math{A \cap B}, is the set
formed by all elements that belong simultaneously to \math{A} and \math{B}:

\startformula
  A \cap B = \{x \mid x \in A \text{ and } x \in B\}
\stopformula
\stopdefinition

\stopsubsection

\stopsection

\startsection[title={Exercises}]

\startexercise
Let \math{A = \{1, 2, 3, 4\}} and \math{B = \{3, 4, 5, 6\}}. Determine:

\startitemize[n]
  \item \math{A \cup B}
  \item \math{A \cap B}
  \item \math{A - B}
\stopitemize
\stopexercise

\startCAPNote
Remember: The union contains elements from both sets, while the intersection
contains only common elements.
\stopCAPNote

\stopsection

\stopchapter
```

### Include the Second Chapter

In `main.tex`, add after the first chapter:

```tex
\startbodymatter

\component content/chapters/01-introduction
\component content/chapters/02-sets

\stopbodymatter
```

## 🔨 Step 6: Compile the Document

Now let's compile! There are several ways:

### Method 1: Using CAP CLI (Recommended)

```bash
# Quick compilation (draft mode)
python ../cap.py build --draft

# Final compilation (optimized)
python ../cap.py build --final
```

### Method 2: Using Make (if available)

```bash
# Default compilation
make build

# Draft mode (faster)
make draft

# Final version
make final
```

### Method 3: Direct ConTeXt

```bash
# Compile with ConTeXt
context main.tex
```

### During Compilation

You'll see messages in the terminal indicating progress:

```
Compiling document...
resolvers       | formats | executing runner 'run luatex format': ...
pages           > flushing realpage 1, userpage 1
...
mkiv lua stats  > used platform: mswin, type: windows, binary subtree: texmf-win64
mkiv lua stats  > used engine: luatex version: 1.15
...
```

⏱️ **First compilation**: May take 30-60 seconds (generates cache)
⏱️ **Subsequent compilations**: 5-10 seconds

## 📄 Step 7: View the Result

After successful compilation, you'll find the `main.pdf` file in the project directory.

### Open the PDF

**Windows:**
```bash
start main.pdf
```

**Linux:**
```bash
xdg-open main.pdf
```

**macOS:**
```bash
open main.pdf
```

Or simply double-click the `main.pdf` file in the file explorer.

## 🎉 Expected Result

You should see a PDF with:

✅ **Elegant cover** with:
- Book title prominently displayed
- Subtitle
- Author name
- Institution and date

✅ **Automatic table of contents** with:
- Chapter 1: Introduction
- Chapter 2: Sets and Numbers

✅ **Formatted chapters** with:
- Titles in blue sans-serif font
- Well-structured sections
- Formatted lists
- Definition boxes with colored background
- Highlighted examples
- Elegant mathematical formulas
- Informative notes

## 🔧 Next Steps

### 1. Add More Content

Create more chapters following the same pattern:

```bash
content/chapters/03-functions.tex
content/chapters/04-limits.tex
```

### 2. Add Figures

Place images in `assets/images/` and use:

```tex
\startplacefigure[
  title={Figure caption},
  reference=fig:example
]
  \externalfigure[filename.pdf][width=0.7\textwidth]
\stopplacefigure
```

### 3. Add Bibliography

Create `content/bibliography.bib`:

```bibtex
@book{example2025,
  author = "Author, Name",
  title = "Book Title",
  publisher = "Publisher",
  year = 2025
}
```

And cite in text:

```tex
As shown by \cite[example2025]...
```

### 4. Customize Design

Edit `config/book.yaml` to change:
- Colors (primary, secondary)
- Fonts
- Layout (margins, spacing)
- Component styles

### 5. Explore Components

Try using:

```tex
% Theorems
\starttheorem[title={Theorem Name}]
  Statement...
\stoptheorem

% Proofs
\startproof
  Demonstration...
\stopproof

% Warnings
\startCAPWarning
  Be careful with...
\stopCAPWarning

% Numbered equations
\startformula
  E = mc^2
\stopformula
```

## 📚 Useful Resources

### Documentation

- [Design System](design-system.md) - Visual customization
- [Components Reference](components-reference.md) - All commands
- [Templates Guide](templates-guide.md) - Advanced templates

### Examples

See complete examples in:
```
examples/
├── minimal/          # Minimal example
├── math-textbook/    # Complete math book
└── programming-book/ # Programming book
```

### Useful Commands

```bash
# Validate project
python cap.py validate

# Compile and watch for changes
python cap.py build --watch

# Clean temporary files
make clean

# Export to EPUB
python cap.py export --format epub
```

## ⚠️ Common Problems

### Error: "ConTeXt not found"

**Solution**: Run `setuptex.bat` before compiling:
```bash
C:\context\tex\setuptex.bat
```

### Compilation error

**Solution**: Check that:
1. Every `\start...` has a corresponding `\stop...`
2. `.tex` files are saved in UTF-8
3. File paths are correct

### PDF doesn't update

**Solution**:
1. Close the PDF before recompiling
2. Clear cache: `make clean` or delete `.tuc`, `.log` files

### Fonts don't appear correctly

**Solution**:
1. Make sure fonts are installed
2. Run: `mtxrun --script fonts --reload`

## 💡 Professional Tips

1. **Use draft mode during development**
   ```bash
   python cap.py build --draft
   ```
   It's much faster!

2. **Organize chapters by number**
   ```
   01-introduction.tex
   02-sets.tex
   03-functions.tex
   ```

3. **Use references instead of fixed numbers**
   ```tex
   As we saw in chapter~\in[chap:intro]...
   Equation~\in[eq:pythagoras] shows that...
   ```

4. **Comment your code**
   ```tex
   % TODO: Add more examples here
   % FIXME: Review this proof
   ```

5. **Make frequent commits (if using Git)**
   ```bash
   git add .
   git commit -m "Add chapter 2 about sets"
   ```

## 🎓 Congratulations!

You've created your first academic document with ConTeXt Academic Press!

Now you can:
- ✅ Create projects
- ✅ Edit content
- ✅ Compile documents
- ✅ Use mathematical components
- ✅ Generate professional PDFs

Keep exploring and creating elegant academic materials! 📚✨

---

**Need help?** Check the [complete documentation](README.md) or the [practical examples](../../examples/).
