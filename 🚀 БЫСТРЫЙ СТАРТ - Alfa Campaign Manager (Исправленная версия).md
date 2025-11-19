# 🚀 БЫСТРЫЙ СТАРТ - Alfa Campaign Manager (Исправленная версия)

## ✅ ЧТО ИСПРАВЛЕНО

1. **Ошибка установки psycopg2-binary** - исправлена
2. **Синтаксическая ошибка в build_exe.py** - исправлена
3. **Добавлена автоматическая проверка зависимостей** - новая функция
4. **Добавлено автообновление библиотек** - новая функция

---

## 📋 ТРЕБОВАНИЯ

- **Python 3.8+** (рекомендуется 3.11)
- **pip** (менеджер пакетов Python)
- **Интернет-соединение** (для установки зависимостей)

---

## 🎯 ЗАПУСК ПРОЕКТА

### Windows:

1. Распакуйте архив
2. Дважды кликните на **START.bat**
3. Дождитесь автоматической установки зависимостей
4. Браузер откроется автоматически

### Linux/macOS:

```bash
# Распакуйте архив
unzip alfa-campaign-manager-FIXED.zip
cd alfa_fixed

# Сделайте скрипт исполняемым
chmod +x start.sh

# Запустите
./start.sh
```

### Универсальный запуск (через Python):

```bash
python launcher.py
```

---

## 🔧 РУЧНАЯ ПРОВЕРКА ЗАВИСИМОСТЕЙ

Если хотите проверить зависимости перед запуском:

```bash
python check_and_update_dependencies.py
```

Этот скрипт:
- ✅ Проверит версию Python
- ✅ Обновит pip
- ✅ Проверит все зависимости
- ✅ Установит отсутствующие пакеты
- ✅ Выведет детальный отчет

---

## 📦 УСТАНОВКА ЗАВИСИМОСТЕЙ ВРУЧНУЮ

Если автоматическая установка не работает:

```bash
# Обновите pip
python -m pip install --upgrade pip

# Установите зависимости
pip install -r requirements.txt

# Если проблемы с psycopg2-binary:
pip install psycopg2-binary --only-binary=:all: --no-cache-dir
```

---

## 🌐 ДОСТУП К ПРИЛОЖЕНИЮ

После запуска приложение будет доступно по адресу:

- **Главная страница:** http://localhost:8000
- **Настройка:** http://localhost:8000/setup
- **Админ-панель:** http://localhost:8000/admin

---

## ⚙️ НАСТРОЙКА

При первом запуске:

1. Откроется Setup Wizard
2. Введите Telegram API credentials (API_ID, API_HASH, PHONE)
3. Настройте API ключи для ИИ (опционально):
   - Google Gemini (бесплатно)
   - Groq (бесплатно)
   - Hugging Face (бесплатно)

### Где получить API ключи:

- **Telegram API:** https://my.telegram.org/apps
- **Google Gemini:** https://makersuite.google.com/app/apikey
- **Groq:** https://console.groq.com/keys
- **Hugging Face:** https://huggingface.co/settings/tokens

---

## 📁 СТРУКТУРА ПРОЕКТА

```
alfa_fixed/
├── START.bat                          # Запуск для Windows
├── start.sh                           # Запуск для Linux/macOS
├── launcher.py                        # Универсальный лаунчер
├── check_and_update_dependencies.py   # Автопроверка зависимостей (НОВОЕ)
├── requirements.txt                   # Список зависимостей (ИСПРАВЛЕНО)
├── build_exe.py                       # Сборка .exe (ИСПРАВЛЕНО)
├── main.py                            # Главное приложение
├── config.py                          # Конфигурация
├── database.py                        # База данных
├── models.py                          # Модели БД
├── telethon_service.py                # Telegram API
├── free_llm_service.py                # ИИ сервисы
├── knowledge_base.py                  # База знаний
├── dialog_initiator.py                # Инициация диалогов
├── setup_wizard.py                    # Мастер настройки
├── CHANGELOG_FIXES.md                 # Отчет об исправлениях
└── README_QUICK_START.md              # Эта инструкция
```

---

## 🐛 РЕШЕНИЕ ПРОБЛЕМ

### Ошибка: "Python не найден"
```bash
# Установите Python 3.11+
# Windows: https://www.python.org/downloads/
# Linux: sudo apt install python3.11
# macOS: brew install python@3.11
```

### Ошибка: "pip не найден"
```bash
python -m ensurepip --upgrade
```

### Ошибка: "Не удалось установить зависимости"
```bash
# Попробуйте с правами администратора
# Windows: запустите START.bat от имени администратора
# Linux/macOS: используйте sudo или виртуальное окружение
```

### Ошибка: "psycopg2-binary не устанавливается"
```bash
# Используйте специальный флаг
pip install psycopg2-binary --only-binary=:all: --no-cache-dir
```

---

## 📝 ДОПОЛНИТЕЛЬНАЯ ДОКУМЕНТАЦИЯ

- **Полная документация:** `📚 Полная Документация Проекта Альфа.md`
- **Руководство по развертыванию:** `DEPLOYMENT_GUIDE.md`
- **Инструкция по созданию .exe:** `BUILD_EXE_INSTRUCTIONS.md`
- **Отчет об исправлениях:** `CHANGELOG_FIXES.md`

---

## 💡 ПОЛЕЗНЫЕ КОМАНДЫ

```bash
# Проверка версии Python
python --version

# Проверка установленных пакетов
pip list

# Обновление всех пакетов
pip install --upgrade -r requirements.txt

# Запуск тестов
python test_suite.py

# Создание .exe файла (Windows)
python build_exe.py
```

---

## 🎉 ГОТОВО!

Теперь вы можете запустить проект без ошибок. Все исправления применены, система проверки зависимостей работает автоматически.

**Приятной работы с Alfa Campaign Manager!**

---

## 📞 ПОДДЕРЖКА

Если возникли вопросы или проблемы:

1. Проверьте `CHANGELOG_FIXES.md` - там описаны все исправления
2. Запустите `python check_and_update_dependencies.py` для диагностики
3. Изучите логи ошибок в консоли
4. Обратитесь к разработчику с подробным описанием проблемы

---

**Версия:** 2.0 (Fixed)  
**Дата исправлений:** 19 ноября 2025
