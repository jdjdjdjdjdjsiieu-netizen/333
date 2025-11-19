#!/usr/bin/env python3
"""
Автоматическая проверка и обновление зависимостей
Alfa Campaign Manager v2.0
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path
from typing import List, Tuple, Dict

# Цвета для консоли
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header():
    """Вывод заголовка"""
    print(f"""
{Colors.BLUE}╔════════════════════════════════════════════════════════════╗
║   ALFA CAMPAIGN MANAGER - Проверка зависимостей            ║
║   Автоматическая проверка и обновление библиотек           ║
╚════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

def check_python_version() -> bool:
    """Проверка версии Python"""
    print(f"{Colors.BOLD}[1/5] Проверка версии Python...{Colors.RESET}")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"{Colors.GREEN}✓ Python {version.major}.{version.minor}.{version.micro} - OK{Colors.RESET}")
        return True
    else:
        print(f"{Colors.RED}✗ Python {version.major}.{version.minor}.{version.micro} - требуется Python 3.8+{Colors.RESET}")
        return False

def upgrade_pip() -> bool:
    """Обновление pip до последней версии"""
    print(f"\n{Colors.BOLD}[2/5] Обновление pip...{Colors.RESET}")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{Colors.GREEN}✓ pip обновлен до последней версии{Colors.RESET}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.YELLOW}⚠ Не удалось обновить pip: {e}{Colors.RESET}")
        return False

def parse_requirements(requirements_file: str = "requirements.txt") -> List[Tuple[str, str]]:
    """Парсинг файла requirements.txt"""
    requirements = []
    req_path = Path(requirements_file)
    
    if not req_path.exists():
        print(f"{Colors.RED}✗ Файл {requirements_file} не найден!{Colors.RESET}")
        return requirements
    
    with open(req_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Пропускаем комментарии и пустые строки
            if not line or line.startswith('#'):
                continue
            
            # Парсим название пакета и версию
            if '==' in line:
                package, version = line.split('==')
                requirements.append((package.strip(), version.strip()))
            elif '>=' in line:
                package, version = line.split('>=')
                requirements.append((package.strip(), f">={version.strip()}"))
            else:
                # Если версия не указана, берем последнюю
                requirements.append((line.strip(), "latest"))
    
    return requirements

def check_package_installed(package_name: str) -> bool:
    """Проверка, установлен ли пакет"""
    # Специальная обработка для пакетов с дефисами
    module_name = package_name.replace('-', '_')
    
    # Специальные случаи
    special_cases = {
        'python_dotenv': 'dotenv',
        'google_generativeai': 'google.generativeai',
        'huggingface_hub': 'huggingface_hub',
    }
    
    if module_name in special_cases:
        module_name = special_cases[module_name]
    
    try:
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    except (ModuleNotFoundError, ValueError, ImportError):
        # Если модуль не найден, возвращаем False
        return False

def install_package(package: str, version: str, use_binary: bool = False) -> bool:
    """Установка пакета"""
    try:
        if version == "latest":
            install_cmd = [sys.executable, "-m", "pip", "install", package]
        elif version.startswith(">="):
            install_cmd = [sys.executable, "-m", "pip", "install", f"{package}{version}"]
        else:
            install_cmd = [sys.executable, "-m", "pip", "install", f"{package}=={version}"]
        
        # Специальная обработка для psycopg2-binary
        if package == "psycopg2-binary":
            install_cmd.extend(["--only-binary=:all:", "--no-cache-dir"])
        
        subprocess.check_call(
            install_cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_dependencies() -> Tuple[int, int, int]:
    """Проверка и установка зависимостей"""
    print(f"\n{Colors.BOLD}[3/5] Проверка зависимостей...{Colors.RESET}\n")
    
    requirements = parse_requirements()
    if not requirements:
        print(f"{Colors.RED}✗ Не удалось прочитать requirements.txt{Colors.RESET}")
        return 0, 0, 0
    
    installed = 0
    missing = 0
    failed = 0
    
    for package, version in requirements:
        status = f"Проверка {package}..."
        print(f"  {status:<50}", end='', flush=True)
        
        if check_package_installed(package):
            print(f"{Colors.GREEN}✓ Установлен{Colors.RESET}")
            installed += 1
        else:
            print(f"{Colors.YELLOW}⚠ Не установлен, устанавливаю...{Colors.RESET}")
            missing += 1
            
            if install_package(package, version):
                print(f"  {' ' * 50}{Colors.GREEN}✓ {package} успешно установлен{Colors.RESET}")
                installed += 1
                missing -= 1
            else:
                print(f"  {' ' * 50}{Colors.RED}✗ Не удалось установить {package}{Colors.RESET}")
                failed += 1
                missing -= 1
    
    return installed, missing, failed

def verify_critical_packages() -> bool:
    """Проверка критически важных пакетов"""
    print(f"\n{Colors.BOLD}[4/5] Проверка критических пакетов...{Colors.RESET}\n")
    
    critical_packages = {
        'telethon': 'Telethon',
        'fastapi': 'FastAPI',
        'uvicorn': 'Uvicorn',
        'sqlalchemy': 'SQLAlchemy',
        'psycopg2': 'psycopg2-binary',
    }
    
    all_ok = True
    for module, display_name in critical_packages.items():
        try:
            __import__(module)
            print(f"  {display_name:<30} {Colors.GREEN}✓ OK{Colors.RESET}")
        except ImportError:
            print(f"  {display_name:<30} {Colors.RED}✗ НЕ НАЙДЕН{Colors.RESET}")
            all_ok = False
    
    return all_ok

def create_summary_report(installed: int, missing: int, failed: int):
    """Создание итогового отчета"""
    print(f"\n{Colors.BOLD}[5/5] Итоговый отчет:{Colors.RESET}\n")
    
    total = installed + missing + failed
    
    print(f"  Всего пакетов:        {total}")
    print(f"  {Colors.GREEN}✓ Установлено:        {installed}{Colors.RESET}")
    
    if missing > 0:
        print(f"  {Colors.YELLOW}⚠ Не установлено:     {missing}{Colors.RESET}")
    
    if failed > 0:
        print(f"  {Colors.RED}✗ Ошибки установки:   {failed}{Colors.RESET}")
    
    print()
    
    if missing == 0 and failed == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗")
        print(f"║   ✓ ВСЕ ЗАВИСИМОСТИ УСТАНОВЛЕНЫ И ГОТОВЫ К РАБОТЕ!         ║")
        print(f"╚════════════════════════════════════════════════════════════╝{Colors.RESET}")
        return True
    elif failed > 0:
        print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗")
        print(f"║   ✗ ОБНАРУЖЕНЫ ОШИБКИ ПРИ УСТАНОВКЕ ЗАВИСИМОСТЕЙ          ║")
        print(f"╚════════════════════════════════════════════════════════════╝{Colors.RESET}")
        print(f"\n{Colors.YELLOW}Рекомендации:{Colors.RESET}")
        print(f"  1. Попробуйте установить вручную: pip install -r requirements.txt")
        print(f"  2. Для psycopg2-binary: pip install psycopg2-binary --only-binary=:all:")
        print(f"  3. Проверьте подключение к интернету")
        return False
    else:
        print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗")
        print(f"║   ⚠ НЕКОТОРЫЕ ЗАВИСИМОСТИ НЕ УСТАНОВЛЕНЫ                  ║")
        print(f"╚════════════════════════════════════════════════════════════╝{Colors.RESET}")
        return False

def main():
    """Главная функция"""
    print_header()
    
    # Проверка Python
    if not check_python_version():
        sys.exit(1)
    
    # Обновление pip
    upgrade_pip()
    
    # Проверка и установка зависимостей
    installed, missing, failed = check_and_install_dependencies()
    
    # Проверка критических пакетов
    critical_ok = verify_critical_packages()
    
    # Итоговый отчет
    success = create_summary_report(installed, missing, failed)
    
    if success and critical_ok:
        print(f"\n{Colors.GREEN}Можно запускать приложение!{Colors.RESET}\n")
        sys.exit(0)
    else:
        print(f"\n{Colors.RED}Требуется устранить ошибки перед запуском приложения.{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
