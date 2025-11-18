#!/usr/bin/env python3
"""
ConTeXt Academic Press - Portable ConTeXt Setup
Instala e configura o ConTeXt standalone dentro do projeto
"""

import os
import sys
import zipfile
import subprocess
from pathlib import Path
import shutil


class ContextSetup:
    """Gerencia instalação portátil do ConTeXt"""

    def __init__(self):
        self.framework_dir = Path(__file__).parent

        # Novos caminhos organizados
        self.context_dir = self.framework_dir / "context"
        self.distributions_dir = self.context_dir / "distributions"
        self.standalone_dir = self.context_dir / "standalone"

        # Detectar plataforma
        self.platform = self.detect_platform()

        # Caminho do ZIP baseado na plataforma
        self.context_zip = self.distributions_dir / self.platform / "latest.zip"

        # Diretório tex dentro de standalone
        self.tex_dir = self.standalone_dir / "tex"

    def detect_platform(self):
        """
        Detecta a plataforma do sistema

        Returns:
            str: 'win64', 'linux64' ou 'osx64'
        """
        import platform

        system = platform.system().lower()
        machine = platform.machine().lower()

        if system == 'windows':
            return 'win64'
        elif system == 'linux':
            return 'linux64'
        elif system == 'darwin':  # macOS
            return 'osx64'
        else:
            return 'win64'  # Default

    def list_available_platforms(self):
        """Lista plataformas disponíveis"""
        print("\n📦 Distribuições disponíveis:\n")

        if not self.distributions_dir.exists():
            print("❌ Diretório de distribuições não encontrado!")
            return

        for platform_dir in self.distributions_dir.iterdir():
            if platform_dir.is_dir():
                platform_name = platform_dir.name
                zips = list(platform_dir.glob("*.zip"))

                if zips:
                    print(f"  {platform_name}:")
                    for zip_file in zips:
                        size_mb = zip_file.stat().st_size / (1024 * 1024)
                        print(f"    - {zip_file.name} ({size_mb:.1f} MB)")
                else:
                    print(f"  {platform_name}: (vazio)")
        print()

    def check_zip_exists(self):
        """Verifica se o arquivo ZIP do ConTeXt existe"""
        if not self.context_zip.exists():
            print(f"❌ Erro: Distribuição não encontrada!")
            print(f"\n   Procurado: {self.context_zip}")
            print(f"   Plataforma detectada: {self.platform}")
            print(f"\nSoluções:")
            print(f"1. Baixe o ConTeXt standalone para {self.platform}:")

            if self.platform == 'win64':
                print(f"   http://minimals.contextgarden.net/setup/context-setup-win64.zip")
            elif self.platform == 'linux64':
                print(f"   http://minimals.contextgarden.net/setup/context-setup-linux-64.zip")
            elif self.platform == 'osx64':
                print(f"   http://minimals.contextgarden.net/setup/context-setup-osx-64.zip")

            print(f"\n2. Salve como: {self.context_zip}")
            print(f"\n3. Ou use --platform para especificar outra plataforma")

            # Mostrar o que está disponível
            self.list_available_platforms()

            return False

        size_mb = self.context_zip.stat().st_size / (1024 * 1024)
        print(f"✓ Distribuição encontrada: {self.platform}/latest.zip ({size_mb:.1f} MB)")
        return True

    def extract_context(self):
        """Extrai o arquivo ZIP do ConTeXt"""
        print(f"\n📦 Extraindo ConTeXt para {self.standalone_dir}...")

        try:
            # Criar diretório se não existir
            self.standalone_dir.mkdir(parents=True, exist_ok=True)

            # Extrair ZIP
            with zipfile.ZipFile(self.context_zip, 'r') as zip_ref:
                # Listar arquivos
                file_list = zip_ref.namelist()
                total_files = len(file_list)

                print(f"   Extraindo {total_files} arquivos...")

                # Extrair com progresso
                for i, file in enumerate(file_list, 1):
                    zip_ref.extract(file, self.standalone_dir)

                    # Mostrar progresso a cada 10%
                    if i % (total_files // 10 or 1) == 0:
                        progress = (i / total_files) * 100
                        print(f"   {progress:.0f}% completo...")

            print(f"✓ Extração concluída!")
            return True

        except Exception as e:
            print(f"❌ Erro ao extrair: {e}")
            return False

    def run_first_setup(self):
        """Executa o script de instalação do ConTeXt"""
        # Procurar script de instalação na plataforma correta
        # ConTeXt pode usar install.bat ou first-setup.bat
        if self.platform == 'win64':
            # Tentar install.bat primeiro, depois first-setup.bat
            install_script = self.standalone_dir / "install.bat"
            if not install_script.exists():
                install_script = self.standalone_dir / "first-setup.bat"
        else:
            # Linux/macOS
            install_script = self.standalone_dir / "install.sh"
            if not install_script.exists():
                install_script = self.standalone_dir / "first-setup.sh"

        if not install_script.exists():
            print(f"❌ Erro: Script de instalação não encontrado!")
            print(f"   Procurado: install.bat ou first-setup.bat")
            print(f"   Diretório: {self.standalone_dir}")
            print(f"\n   Arquivos encontrados:")
            for f in self.standalone_dir.iterdir():
                print(f"   - {f.name}")
            return False

        print(f"✓ Encontrado: {install_script.name}")

        print(f"\n🔧 Executando instalação do ConTeXt...")
        print(f"   Isso pode levar vários minutos. Por favor, aguarde...")
        print(f"   (Baixando binários, fontes e macros...)\n")

        try:
            # Executar script de instalação no diretório correto
            if self.platform == 'win64':
                result = subprocess.run(
                    [str(install_script)],
                    cwd=str(self.standalone_dir),
                    capture_output=True,
                    text=True,
                    shell=True
                )
            else:
                # Linux/macOS
                result = subprocess.run(
                    ['sh', str(install_script)],
                    cwd=str(self.standalone_dir),
                    capture_output=True,
                    text=True
                )

            if result.returncode == 0:
                print(f"\n✓ ConTeXt instalado com sucesso!")
                return True
            else:
                print(f"\n❌ Erro na instalação:")
                print(result.stdout)
                print(result.stderr)
                return False

        except Exception as e:
            print(f"❌ Erro ao executar instalação: {e}")
            return False

    def verify_installation(self):
        """Verifica se a instalação foi bem-sucedida"""
        print(f"\n🔍 Verificando instalação...")

        # Verificar se diretório tex existe
        if not self.tex_dir.exists():
            print(f"❌ Diretório tex não encontrado!")
            return False

        # Procurar binário do context baseado na plataforma
        context_exe = None

        if self.platform == 'win64':
            bin_patterns = [
                self.tex_dir / "texmf-win64" / "bin" / "context.exe",
                self.tex_dir / "texmf-mswin" / "bin" / "context.exe",
            ]
        elif self.platform == 'linux64':
            bin_patterns = [
                self.tex_dir / "texmf-linux-64" / "bin" / "context",
                self.tex_dir / "texmf-linux" / "bin" / "context",
            ]
        else:  # osx64
            bin_patterns = [
                self.tex_dir / "texmf-osx-64" / "bin" / "context",
                self.tex_dir / "texmf-osx" / "bin" / "context",
            ]

        for bin_path in bin_patterns:
            if bin_path.exists():
                context_exe = bin_path
                break

        if not context_exe:
            print(f"❌ Executável do ConTeXt não encontrado!")
            print(f"   Procurado em:")
            for p in bin_patterns:
                print(f"   - {p}")
            return False

        print(f"✓ Binário do ConTeXt encontrado: {context_exe.name}")

        # Verificar setuptex
        if self.platform == 'win64':
            setuptex = self.tex_dir / "setuptex.bat"
        else:
            setuptex = self.tex_dir / "setuptex"

        if setuptex.exists():
            print(f"✓ Script setuptex encontrado")
        else:
            print(f"⚠ setuptex não encontrado (opcional)")

        return True

    def create_environment_file(self):
        """Cria arquivo de ambiente para uso fácil"""
        if self.platform == 'win64':
            env_file = self.framework_dir / "setup-cap-env.bat"
            setuptex_path = self.tex_dir / "setuptex.bat"

            content = f"""@echo off
REM ConTeXt Academic Press - Environment Setup
REM Configura ambiente para usar ConTeXt portátil

echo ========================================
echo ConTeXt Academic Press
echo ========================================
echo.

REM Configurar ConTeXt
call "{setuptex_path}"

echo.
echo ✓ Ambiente configurado!
echo   Plataforma: {self.platform}
echo.
echo Comandos disponíveis:
echo   context --version       Verificar versão do ConTeXt
echo   python cap.py --help    Ajuda do CAP CLI
echo   python cap.py new       Criar novo projeto
echo   python cap.py build     Compilar projeto
echo.
"""
        else:
            # Linux/macOS
            env_file = self.framework_dir / "setup-cap-env.sh"
            setuptex_path = self.tex_dir / "setuptex"

            content = f"""#!/bin/bash
# ConTeXt Academic Press - Environment Setup
# Configura ambiente para usar ConTeXt portátil

echo "========================================"
echo "ConTeXt Academic Press"
echo "========================================"
echo

# Configurar ConTeXt
source "{setuptex_path}"

echo
echo "✓ Ambiente configurado!"
echo "  Plataforma: {self.platform}"
echo
echo "Comandos disponíveis:"
echo "  context --version       Verificar versão do ConTeXt"
echo "  python cap.py --help    Ajuda do CAP CLI"
echo "  python cap.py new       Criar novo projeto"
echo "  python cap.py build     Compilar projeto"
echo
"""

        print(f"\n📝 Criando script de ambiente...")

        try:
            with open(env_file, 'w', encoding='utf-8') as f:
                f.write(content)

            # Dar permissão de execução no Linux/macOS
            if self.platform != 'win64':
                os.chmod(env_file, 0o755)

            print(f"✓ Script criado: {env_file.name}")
            print(f"\n   Execute este script antes de usar o framework:")

            if self.platform == 'win64':
                print(f"   > {env_file.name}")
            else:
                print(f"   $ source {env_file.name}")

            return True

        except Exception as e:
            print(f"❌ Erro ao criar script: {e}")
            return False

    def create_version_file(self):
        """Cria arquivo indicando versão instalada"""
        version_file = self.context_dir / "active-version.txt"

        from datetime import datetime

        content = f"""version=latest
platform={self.platform}
installed_date={datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
zip_file={self.context_zip.name}
"""

        try:
            with open(version_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Versão registrada: {version_file.name}")
            return True
        except Exception as e:
            print(f"⚠ Erro ao criar arquivo de versão: {e}")
            return True  # Não crítico

    def is_already_installed(self):
        """Verifica se ConTeXt já está instalado"""
        if not self.standalone_dir.exists():
            return False

        if not self.tex_dir.exists():
            return False

        # Verificar se há binários
        bin_dirs = list(self.tex_dir.glob("texmf-*/bin"))
        if not bin_dirs:
            return False

        return True

    def clean_installation(self):
        """Remove instalação existente"""
        if self.standalone_dir.exists():
            print(f"🗑️  Removendo instalação anterior...")
            try:
                shutil.rmtree(self.standalone_dir)
                print(f"✓ Removido: {self.standalone_dir}")
                return True
            except Exception as e:
                print(f"❌ Erro ao remover: {e}")
                return False
        return True

    def run(self, force=False, platform=None):
        """Executa instalação completa"""
        print("=" * 60)
        print("ConTeXt Academic Press - Setup do ConTeXt Portátil")
        print("=" * 60)
        print()

        # Permitir override de plataforma
        if platform:
            self.platform = platform
            self.context_zip = self.distributions_dir / self.platform / "latest.zip"
            print(f"ℹ Plataforma especificada: {self.platform}")

        # Verificar se já está instalado
        if self.is_already_installed() and not force:
            print("✓ ConTeXt já está instalado!")
            print()
            response = input("Deseja reinstalar? (s/N): ").strip().lower()

            if response not in ['s', 'sim', 'y', 'yes']:
                print("\nInstalação cancelada.")
                env_script = "setup-cap-env.bat" if self.platform == 'win64' else "setup-cap-env.sh"
                print(f"\nPara usar o ConTeXt, execute:")
                print(f"  {self.framework_dir / env_script}")
                return True

            # Limpar instalação anterior
            if not self.clean_installation():
                return False

        # 1. Verificar ZIP
        if not self.check_zip_exists():
            return False

        # 2. Extrair ConTeXt
        if not self.extract_context():
            return False

        # 3. Executar instalação
        if not self.run_first_setup():
            return False

        # 4. Verificar instalação
        if not self.verify_installation():
            return False

        # 5. Criar script de ambiente
        if not self.create_environment_file():
            return False

        # 6. Registrar versão
        self.create_version_file()

        print()
        print("=" * 60)
        print("✅ INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        print()
        print("📌 PRÓXIMOS PASSOS:")
        print()
        print("1. Execute o script de ambiente:")

        if self.platform == 'win64':
            print(f"   > setup-cap-env.bat")
        else:
            print(f"   $ source setup-cap-env.sh")

        print()
        print("2. Verifique a instalação:")
        print(f"   > context --version")
        print()
        print("3. Crie seu primeiro projeto:")
        print(f"   > python cap.py new meu-projeto")
        print()

        return True


def main():
    """Função principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Instala ConTeXt portátil no ConTeXt Academic Press"
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Forçar reinstalação mesmo se já existir'
    )
    parser.add_argument(
        '--clean',
        action='store_true',
        help='Apenas limpar instalação existente'
    )
    parser.add_argument(
        '--platform',
        choices=['win64', 'linux64', 'osx64'],
        help='Especificar plataforma (detecta automaticamente se omitido)'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='Listar distribuições disponíveis'
    )

    args = parser.parse_args()

    setup = ContextSetup()

    if args.list:
        setup.list_available_platforms()
        return 0

    if args.clean:
        print("Limpando instalação do ConTeXt...")
        if setup.clean_installation():
            print("✓ Limpeza concluída!")
            return 0
        else:
            return 1

    # Executar instalação
    success = setup.run(force=args.force, platform=args.platform)

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
