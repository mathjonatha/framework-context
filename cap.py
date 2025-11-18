#!/usr/bin/env python3
"""
ConTeXt Academic Press - CLI Tool
Ferramenta de linha de comando para gerenciar projetos acadêmicos
"""

import sys
import argparse
from pathlib import Path

# Adiciona o diretório build ao path
sys.path.insert(0, str(Path(__file__).parent / 'build'))

from cli.new_project import create_new_project
from cli.compile import compile_document
from cli.validate import validate_project
from cli.export import export_document

__version__ = "1.0.0"


def main():
    parser = argparse.ArgumentParser(
        description="ConTeXt Academic Press - Sistema de editoração acadêmica",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  cap new meu-livro --template math-textbook
  cap build
  cap build --final --print
  cap validate
  cap export --format epub
        """
    )

    parser.add_argument(
        '--version',
        action='version',
        version=f'ConTeXt Academic Press {__version__}'
    )

    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')

    # Comando: new
    new_parser = subparsers.add_parser(
        'new',
        help='Criar novo projeto'
    )
    new_parser.add_argument(
        'name',
        help='Nome do projeto'
    )
    new_parser.add_argument(
        '--template',
        default='base',
        help='Template a ser usado (default: base)'
    )
    new_parser.add_argument(
        '--type',
        choices=['textbook', 'handbook', 'monograph'],
        default='textbook',
        help='Tipo de documento (default: textbook)'
    )

    # Comando: build
    build_parser = subparsers.add_parser(
        'build',
        help='Compilar documento'
    )
    build_parser.add_argument(
        '--draft',
        action='store_true',
        help='Compilar em modo rascunho (mais rápido)'
    )
    build_parser.add_argument(
        '--final',
        action='store_true',
        help='Compilar versão final (otimizada)'
    )
    build_parser.add_argument(
        '--print',
        action='store_true',
        help='Gerar para impressão offset (CMYK, PDF/X)'
    )
    build_parser.add_argument(
        '--digital',
        action='store_true',
        help='Gerar para leitura digital (RGB, hyperlinks)'
    )
    build_parser.add_argument(
        '--watch',
        action='store_true',
        help='Observar mudanças e recompilar automaticamente'
    )

    # Comando: validate
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validar estrutura do projeto'
    )

    # Comando: export
    export_parser = subparsers.add_parser(
        'export',
        help='Exportar para outros formatos'
    )
    export_parser.add_argument(
        '--format',
        choices=['html', 'epub', 'docx', 'xml'],
        required=True,
        help='Formato de exportação'
    )
    export_parser.add_argument(
        '--output',
        help='Arquivo de saída (opcional)'
    )

    # Comando: clean
    clean_parser = subparsers.add_parser(
        'clean',
        help='Limpar arquivos temporários de compilação'
    )

    # Parse argumentos
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    try:
        # Executar comando apropriado
        if args.command == 'new':
            create_new_project(args.name, args.template, args.type)
        elif args.command == 'build':
            compile_document(
                draft=args.draft,
                final=args.final,
                print_mode=args.print,
                digital=args.digital,
                watch=args.watch
            )
        elif args.command == 'validate':
            validate_project()
        elif args.command == 'export':
            export_document(args.format, args.output)
        elif args.command == 'clean':
            print("Limpando arquivos temporários...")
            # TODO: Implementar limpeza

        return 0

    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
