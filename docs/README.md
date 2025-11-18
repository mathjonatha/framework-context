# ConTeXt Academic Press - Documentation

**Multi-language documentation for ConTeXt Academic Press framework**

## 🌍 Choose Your Language / Escolha seu Idioma

### Available Languages / Idiomas Disponíveis

- **[🇧🇷 Português Brasileiro](pt-BR/README.md)** - Documentação completa em português
- **[🇺🇸 English](en/README.md)** - Complete documentation in English

### Coming Soon / Em Breve

- 🇪🇸 Español - Spanish documentation
- 🇫🇷 Français - French documentation
- 🇩🇪 Deutsch - German documentation

## 📖 Documentation Structure / Estrutura da Documentação

All language versions follow the same structure for easy navigation:

```
docs/
├── pt-BR/                      # Brazilian Portuguese
│   ├── README.md              # Language index
│   ├── installation/          # Installation guides
│   │   └── windows.md        # Windows installation
│   ├── getting-started.md    # Getting started guide
│   ├── design-system.md      # Design system guide
│   └── components-reference.md
│
├── en/                        # English
│   ├── README.md              # Language index
│   ├── installation/          # Installation guides
│   │   └── windows.md        # Windows installation
│   ├── getting-started.md    # Getting started guide
│   ├── design-system.md      # Design system guide
│   └── components-reference.md
│
└── [future languages]/        # Other languages
    └── ...
```

## 🚀 Quick Start / Início Rápido

### Portuguese / Português

1. [Instalar ConTeXt no Windows](pt-BR/installation/windows.md)
2. [Guia de Início](pt-BR/getting-started.md)
3. [Sistema de Design](pt-BR/design-system.md)

### English

1. [Install ConTeXt on Windows](en/installation/windows.md)
2. [Getting Started Guide](en/getting-started.md)
3. [Design System](en/design-system.md)

## 📚 Documentation Coverage / Cobertura da Documentação

| Document | 🇧🇷 PT-BR | 🇺🇸 EN | 🇪🇸 ES | 🇫🇷 FR | 🇩🇪 DE |
|----------|--------|-----|-----|-----|-----|
| Windows Installation | ✅ | ✅ | 🔜 | 🔜 | 🔜 |
| Getting Started | ✅ | ✅ | 🔜 | 🔜 | 🔜 |
| Design System | ✅ | ✅ | 🔜 | 🔜 | 🔜 |
| Components Reference | 🔜 | 🔜 | 🔜 | 🔜 | 🔜 |

Legend: ✅ Available | 🔜 Coming soon | ❌ Not planned

## 💡 Contributing Translations / Contribuindo com Traduções

We welcome translations to new languages! To contribute:

### How to Add a New Language / Como Adicionar um Novo Idioma

1. **Create language directory** / Criar diretório do idioma:
   ```bash
   mkdir -p docs/[language-code]/installation
   ```

   Use ISO 639-1 codes:
   - `pt-BR` - Brazilian Portuguese
   - `en` - English
   - `es` - Spanish
   - `fr` - French
   - `de` - German
   - etc.

2. **Copy structure from English** / Copiar estrutura do inglês:
   ```bash
   cp -r docs/en/* docs/[language-code]/
   ```

3. **Translate all files** / Traduzir todos os arquivos:
   - Keep the same filename structure
   - Translate content maintaining formatting
   - Update internal links to point to your language version

4. **Update this README** / Atualizar este README:
   - Add language to "Available Languages" section
   - Update documentation coverage table
   - Add quick start links

5. **Submit a Pull Request** / Enviar Pull Request

### Translation Guidelines / Diretrizes de Tradução

- ✅ Keep code examples unchanged
- ✅ Translate comments in code if helpful
- ✅ Maintain markdown formatting
- ✅ Keep file and directory names in English (for consistency)
- ✅ Update cross-references to point to same language
- ✅ Use native language conventions (e.g., date formats)

## 🔧 Maintaining Translations / Mantendo Traduções

When updating documentation:

1. Update English version first (source of truth)
2. Mark other languages as needing update in coverage table
3. Update translations following the English changes
4. Keep version numbers in sync

## 📞 Contact / Contato

- **GitHub Issues**: For documentation bugs and improvements
- **Discussions**: For questions and suggestions
- **Email**: [documentation@context-academic-press.org]

## 📄 License / Licença

This documentation is licensed under Creative Commons CC-BY-SA 4.0

---

**Framework Version**: 1.0.0
**Documentation Version**: 1.0.0
**Last Updated**: 2025-01-18
