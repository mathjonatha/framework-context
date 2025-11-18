# Makefile para projeto ConTeXt Academic Press
# Facilita comandos comuns de build

# Variáveis
MAIN = main.tex
PDF = main.pdf
PYTHON = python3
CAP = $(PYTHON) ../cap.py

# Comandos principais
.PHONY: all build draft final print digital watch clean validate help

# Build padrão
all: build

# Build normal
build:
	@echo "Compilando documento..."
	context $(MAIN)

# Build rascunho (mais rápido)
draft:
	@echo "Compilando em modo rascunho..."
	context --mode=draft $(MAIN)

# Build final (otimizado)
final:
	@echo "Compilando versão final..."
	context --mode=final --purgeall $(MAIN)

# Build para impressão
print:
	@echo "Gerando PDF para impressão offset..."
	context --mode=print --purgeall $(MAIN)

# Build para digital
digital:
	@echo "Gerando PDF para leitura digital..."
	context --mode=digital --purgeall $(MAIN)

# Observar mudanças e recompilar
watch:
	@echo "Modo watch: observando mudanças..."
	@while true; do \
		inotifywait -qre close_write .; \
		make build; \
	done

# Validar projeto
validate:
	@echo "Validando projeto..."
	$(CAP) validate

# Limpar arquivos temporários
clean:
	@echo "Limpando arquivos temporários..."
	@rm -f *.tuc *.log *.tmp *.bak
	@rm -rf output/*

# Limpar tudo (incluindo PDF)
distclean: clean
	@echo "Removendo PDF gerado..."
	@rm -f $(PDF)

# Exportar para HTML
export-html: final
	@echo "Exportando para HTML..."
	$(CAP) export --format html

# Exportar para EPUB
export-epub: final
	@echo "Exportando para EPUB..."
	$(CAP) export --format epub

# Ajuda
help:
	@echo "ConTeXt Academic Press - Comandos Makefile"
	@echo ""
	@echo "Uso: make [comando]"
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  build       - Compilar documento (padrão)"
	@echo "  draft       - Compilar em modo rascunho (rápido)"
	@echo "  final       - Compilar versão final (otimizada)"
	@echo "  print       - Gerar PDF para impressão offset"
	@echo "  digital     - Gerar PDF para leitura digital"
	@echo "  watch       - Observar mudanças e recompilar"
	@echo "  validate    - Validar estrutura do projeto"
	@echo "  clean       - Limpar arquivos temporários"
	@echo "  distclean   - Limpar tudo (incluindo PDF)"
	@echo "  export-html - Exportar para HTML"
	@echo "  export-epub - Exportar para EPUB"
	@echo "  help        - Mostrar esta ajuda"
