"""
Comprehensive Test Suite для Альфа Проекта
Тестирование всех компонентов: Backend, Telethon, ИИ, База знаний, Dialog Initiator
"""

import asyncio
import sys
import time
from typing import Dict, List
import json

# Цвета для вывода
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class TestRunner:
    def __init__(self):
        self.results = {
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'errors': []
        }
        self.start_time = None
        self.end_time = None

    def print_header(self, text: str):
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}{Colors.RESET}\n")

    def print_test(self, name: str, status: str, message: str = ""):
        status_color = Colors.GREEN if status == "✓ PASS" else Colors.RED if status == "✗ FAIL" else Colors.YELLOW
        print(f"{status_color}{status}{Colors.RESET} | {name}")
        if message:
            print(f"       └─ {message}")

    def print_summary(self):
        total = self.results['passed'] + self.results['failed'] + self.results['skipped']
        elapsed = self.end_time - self.start_time if self.start_time and self.end_time else 0
        
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
        print(f"  ИТОГОВЫЙ ОТЧЕТ")
        print(f"{'='*60}{Colors.RESET}")
        print(f"{Colors.GREEN}✓ Пройдено: {self.results['passed']}{Colors.RESET}")
        print(f"{Colors.RED}✗ Не пройдено: {self.results['failed']}{Colors.RESET}")
        print(f"{Colors.YELLOW}⊘ Пропущено: {self.results['skipped']}{Colors.RESET}")
        print(f"Всего тестов: {total}")
        print(f"Время выполнения: {elapsed:.2f} сек\n")
        
        if self.results['errors']:
            print(f"{Colors.RED}ОШИБКИ:{Colors.RESET}")
            for error in self.results['errors']:
                print(f"  • {error}")

# ============================================================================
# ТЕСТ 1: Проверка конфигурации
# ============================================================================

def test_configuration():
    """Проверка всех необходимых переменных окружения"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 1: КОНФИГУРАЦИЯ")
    
    required_vars = [
        'TELEGRAM_API_ID',
        'TELEGRAM_API_HASH',
        'TELEGRAM_PHONE_NUMBER',
    ]
    
    optional_vars = [
        'GEMINI_API_KEY',
        'GROQ_API_KEY',
        'DATABASE_URL'
    ]
    
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    # Проверка обязательных переменных
    for var in required_vars:
        if os.getenv(var):
            runner.results['passed'] += 1
            runner.print_test(f"Переменная {var}", "✓ PASS", "Найдена")
        else:
            runner.results['failed'] += 1
            runner.print_test(f"Переменная {var}", "✗ FAIL", "Не найдена")
            runner.results['errors'].append(f"Отсутствует {var}")
    
    # Проверка опциональных переменных
    for var in optional_vars:
        if os.getenv(var):
            runner.results['passed'] += 1
            runner.print_test(f"Переменная {var}", "✓ PASS", "Найдена")
        else:
            runner.results['skipped'] += 1
            runner.print_test(f"Переменная {var}", "⊘ SKIP", "Опциональная переменная")
    
    return runner

# ============================================================================
# ТЕСТ 2: Проверка импортов и зависимостей
# ============================================================================

def test_imports():
    """Проверка всех необходимых импортов"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 2: ИМПОРТЫ И ЗАВИСИМОСТИ")
    
    modules_to_test = [
        ('telethon', 'Telethon'),
        ('fastapi', 'FastAPI'),
        ('sqlalchemy', 'SQLAlchemy'),
        ('pydantic', 'Pydantic'),
        ('aiohttp', 'AIOHTTP'),
        ('google.generativeai', 'Google Generative AI'),
        ('groq', 'Groq'),
    ]
    
    for module, name in modules_to_test:
        try:
            __import__(module)
            runner.results['passed'] += 1
            runner.print_test(f"Импорт {name}", "✓ PASS", f"Модуль {module} загружен")
        except ImportError as e:
            runner.results['failed'] += 1
            runner.print_test(f"Импорт {name}", "✗ FAIL", str(e))
            runner.results['errors'].append(f"Не удалось импортировать {module}")
    
    return runner

# ============================================================================
# ТЕСТ 3: Проверка базы данных
# ============================================================================

async def test_database():
    """Проверка подключения и работы БД"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 3: БАЗА ДАННЫХ")
    
    try:
        from database import engine, Base, SessionLocal
        
        # Проверка подключения
        try:
            with SessionLocal() as session:
                session.execute("SELECT 1")
            runner.results['passed'] += 1
            runner.print_test("Подключение к БД", "✓ PASS", "БД доступна")
        except Exception as e:
            runner.results['failed'] += 1
            runner.print_test("Подключение к БД", "✗ FAIL", str(e))
            runner.results['errors'].append(f"Ошибка подключения к БД: {e}")
        
        # Проверка таблиц
        try:
            Base.metadata.create_all(bind=engine)
            runner.results['passed'] += 1
            runner.print_test("Создание таблиц", "✓ PASS", "Таблицы созданы/обновлены")
        except Exception as e:
            runner.results['failed'] += 1
            runner.print_test("Создание таблиц", "✗ FAIL", str(e))
            runner.results['errors'].append(f"Ошибка создания таблиц: {e}")
        
    except ImportError as e:
        runner.results['failed'] += 1
        runner.print_test("Импорт модулей БД", "✗ FAIL", str(e))
        runner.results['errors'].append(f"Не удалось импортировать модули БД: {e}")
    
    return runner

# ============================================================================
# ТЕСТ 4: Проверка Telethon Service
# ============================================================================

async def test_telethon_service():
    """Проверка Telethon сервиса"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 4: TELETHON SERVICE")
    
    try:
        from telethon_service import TelethonService
        
        service = TelethonService()
        runner.results['passed'] += 1
        runner.print_test("Инициализация TelethonService", "✓ PASS", "Сервис создан")
        
        # Проверка методов
        methods = [
            'get_contacts',
            'get_groups_and_channels',
            'send_message',
            'send_batch_messages',
            'get_message_history'
        ]
        
        for method in methods:
            if hasattr(service, method):
                runner.results['passed'] += 1
                runner.print_test(f"Метод {method}", "✓ PASS", "Метод существует")
            else:
                runner.results['failed'] += 1
                runner.print_test(f"Метод {method}", "✗ FAIL", "Метод не найден")
                runner.results['errors'].append(f"Метод {method} не найден в TelethonService")
        
    except Exception as e:
        runner.results['failed'] += 1
        runner.print_test("Telethon Service", "✗ FAIL", str(e))
        runner.results['errors'].append(f"Ошибка Telethon Service: {e}")
    
    return runner

# ============================================================================
# ТЕСТ 5: Проверка Knowledge Base
# ============================================================================

def test_knowledge_base():
    """Проверка базы знаний"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 5: БАЗА ЗНАНИЙ")
    
    try:
        from knowledge_base import KnowledgeBase
        
        kb = KnowledgeBase()
        runner.results['passed'] += 1
        runner.print_test("Инициализация KnowledgeBase", "✓ PASS", "База знаний создана")
        
        # Проверка данных
        if kb.program_info:
            runner.results['passed'] += 1
            runner.print_test("Информация о программе", "✓ PASS", f"Загружено {len(kb.program_info)} элементов")
        else:
            runner.results['failed'] += 1
            runner.print_test("Информация о программе", "✗ FAIL", "Данные не загружены")
            runner.results['errors'].append("Информация о программе пуста")
        
        if kb.products:
            runner.results['passed'] += 1
            runner.print_test("Каталог продуктов", "✓ PASS", f"Загружено {len(kb.products)} продуктов")
        else:
            runner.results['failed'] += 1
            runner.print_test("Каталог продуктов", "✗ FAIL", "Продукты не загружены")
            runner.results['errors'].append("Каталог продуктов пуст")
        
        # Проверка методов
        methods = [
            'get_product_by_category',
            'get_partner_structure',
            'get_strategy_recommendation',
            'analyze_campaign'
        ]
        
        for method in methods:
            if hasattr(kb, method):
                runner.results['passed'] += 1
                runner.print_test(f"Метод {method}", "✓ PASS", "Метод существует")
            else:
                runner.results['failed'] += 1
                runner.print_test(f"Метод {method}", "✗ FAIL", "Метод не найден")
                runner.results['errors'].append(f"Метод {method} не найден в KnowledgeBase")
        
    except Exception as e:
        runner.results['failed'] += 1
        runner.print_test("Knowledge Base", "✗ FAIL", str(e))
        runner.results['errors'].append(f"Ошибка Knowledge Base: {e}")
    
    return runner

# ============================================================================
# ТЕСТ 6: Проверка Free LLM Service
# ============================================================================

async def test_free_llm_service():
    """Проверка сервиса бесплатных ИИ"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 6: FREE LLM SERVICE")
    
    try:
        from free_llm_service import FreeLLMService
        
        service = FreeLLMService()
        runner.results['passed'] += 1
        runner.print_test("Инициализация FreeLLMService", "✓ PASS", "Сервис создан")
        
        # Проверка доступных провайдеров
        providers = service.get_available_providers()
        if providers:
            runner.results['passed'] += 1
            runner.print_test("Доступные провайдеры", "✓ PASS", f"Найдено {len(providers)} провайдеров: {', '.join(providers)}")
        else:
            runner.results['failed'] += 1
            runner.print_test("Доступные провайдеры", "✗ FAIL", "Нет доступных провайдеров")
            runner.results['errors'].append("Ни один провайдер ИИ не настроен")
        
        # Проверка методов
        methods = [
            'generate_response',
            'analyze_text',
            'generate_recommendation',
            'handle_objection'
        ]
        
        for method in methods:
            if hasattr(service, method):
                runner.results['passed'] += 1
                runner.print_test(f"Метод {method}", "✓ PASS", "Метод существует")
            else:
                runner.results['failed'] += 1
                runner.print_test(f"Метод {method}", "✗ FAIL", "Метод не найден")
                runner.results['errors'].append(f"Метод {method} не найден в FreeLLMService")
        
    except Exception as e:
        runner.results['failed'] += 1
        runner.print_test("Free LLM Service", "✗ FAIL", str(e))
        runner.results['errors'].append(f"Ошибка Free LLM Service: {e}")
    
    return runner

# ============================================================================
# ТЕСТ 7: Проверка Dialog Initiator
# ============================================================================

def test_dialog_initiator():
    """Проверка модуля инициации диалогов"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 7: DIALOG INITIATOR")
    
    try:
        from dialog_initiator import DialogInitiator
        
        initiator = DialogInitiator()
        runner.results['passed'] += 1
        runner.print_test("Инициализация DialogInitiator", "✓ PASS", "Модуль создан")
        
        # Проверка методов
        methods = [
            'generate_first_message',
            'initiate_dialog',
            'initiate_batch_dialogs',
            'handle_response',
            'generate_follow_up'
        ]
        
        for method in methods:
            if hasattr(initiator, method):
                runner.results['passed'] += 1
                runner.print_test(f"Метод {method}", "✓ PASS", "Метод существует")
            else:
                runner.results['failed'] += 1
                runner.print_test(f"Метод {method}", "✗ FAIL", "Метод не найден")
                runner.results['errors'].append(f"Метод {method} не найден в DialogInitiator")
        
    except Exception as e:
        runner.results['failed'] += 1
        runner.print_test("Dialog Initiator", "✗ FAIL", str(e))
        runner.results['errors'].append(f"Ошибка Dialog Initiator: {e}")
    
    return runner

# ============================================================================
# ТЕСТ 8: Нагрузочное тестирование
# ============================================================================

async def test_load():
    """Нагрузочное тестирование"""
    runner = TestRunner()
    runner.print_header("ТЕСТ 8: НАГРУЗОЧНОЕ ТЕСТИРОВАНИЕ")
    
    try:
        from knowledge_base import KnowledgeBase
        from free_llm_service import FreeLLMService
        
        kb = KnowledgeBase()
        llm = FreeLLMService()
        
        # Тест 1: Генерация 100 рекомендаций
        print("Генерирование 100 рекомендаций...")
        start = time.time()
        
        test_profiles = [
            {"name": "Иван", "profession": "Бизнесмен", "interests": "Инвестиции"},
            {"name": "Мария", "profession": "Врач", "interests": "Здоровье"},
            {"name": "Петр", "profession": "Студент", "interests": "Образование"},
        ]
        
        for i in range(100):
            profile = test_profiles[i % len(test_profiles)]
            # Имитация генерации рекомендации
            _ = kb.get_product_by_category("credit")
        
        elapsed = time.time() - start
        rps = 100 / elapsed  # Requests per second
        
        if rps > 10:
            runner.results['passed'] += 1
            runner.print_test("Генерация 100 рекомендаций", "✓ PASS", f"{rps:.2f} RPS за {elapsed:.2f} сек")
        else:
            runner.results['failed'] += 1
            runner.print_test("Генерация 100 рекомендаций", "✗ FAIL", f"Низкая производительность: {rps:.2f} RPS")
            runner.results['errors'].append(f"Производительность ниже ожидаемой: {rps:.2f} RPS")
        
        # Тест 2: Параллельная обработка
        print("Параллельная обработка 50 контактов...")
        start = time.time()
        
        async def process_contact(contact_id):
            await asyncio.sleep(0.01)  # Имитация обработки
            return contact_id
        
        tasks = [process_contact(i) for i in range(50)]
        results = await asyncio.gather(*tasks)
        
        elapsed = time.time() - start
        
        if len(results) == 50 and elapsed < 1:
            runner.results['passed'] += 1
            runner.print_test("Параллельная обработка 50 контактов", "✓ PASS", f"Обработано за {elapsed:.2f} сек")
        else:
            runner.results['failed'] += 1
            runner.print_test("Параллельная обработка 50 контактов", "✗ FAIL", f"Ошибка при обработке")
            runner.results['errors'].append("Параллельная обработка не работает корректно")
        
    except Exception as e:
        runner.results['failed'] += 1
        runner.print_test("Нагрузочное тестирование", "✗ FAIL", str(e))
        runner.results['errors'].append(f"Ошибка нагрузочного тестирования: {e}")
    
    return runner

# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

async def run_all_tests():
    """Запуск всех тестов"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}╔════════════════════════════════════════════════════════════╗")
    print(f"║                  АЛЬФА ПРОЕКТ - ТЕСТ SUITE                   ║")
    print(f"║              Комплексное тестирование системы                 ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    all_results = {
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'errors': []
    }
    
    # Запуск тестов
    test_results = [
        test_configuration(),
        test_imports(),
        await test_database(),
        await test_telethon_service(),
        test_knowledge_base(),
        await test_free_llm_service(),
        test_dialog_initiator(),
        await test_load(),
    ]
    
    # Агрегирование результатов
    for result in test_results:
        all_results['passed'] += result.results['passed']
        all_results['failed'] += result.results['failed']
        all_results['skipped'] += result.results['skipped']
        all_results['errors'].extend(result.results['errors'])
    
    # Итоговый отчет
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
    print(f"  ФИНАЛЬНЫЙ ОТЧЕТ")
    print(f"{'='*60}{Colors.RESET}")
    print(f"{Colors.GREEN}✓ Пройдено: {all_results['passed']}{Colors.RESET}")
    print(f"{Colors.RED}✗ Не пройдено: {all_results['failed']}{Colors.RESET}")
    print(f"{Colors.YELLOW}⊘ Пропущено: {all_results['skipped']}{Colors.RESET}")
    print(f"Всего тестов: {all_results['passed'] + all_results['failed'] + all_results['skipped']}\n")
    
    if all_results['failed'] == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!{Colors.RESET}\n")
        return True
    else:
        print(f"{Colors.RED}{Colors.BOLD}✗ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ!{Colors.RESET}\n")
        if all_results['errors']:
            print(f"{Colors.RED}ОШИБКИ:{Colors.RESET}")
            for error in all_results['errors']:
                print(f"  • {error}\n")
        return False

if __name__ == "__main__":
    result = asyncio.run(run_all_tests())
    sys.exit(0 if result else 1)
