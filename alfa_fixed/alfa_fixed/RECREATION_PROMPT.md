# 🤖 PROMPT ДЛЯ ВОССОЗДАНИЯ ПРОЕКТА: Alfa Campaign Manager v2.0

## 🎯 Цель

Воссоздать полнофункциональный, коммерчески готовый Telegram-бот **"Alfa Campaign Manager v2.0"** для программы "Свой в Альфе", включая:
1.  **Backend** на Python/FastAPI с интеграцией Telethon.
2.  **Frontend** на React/TypeScript для админ-панели.
3.  **Setup Wizard** (CLI и Web UI) для автоматической настройки API ключей и переменных окружения.
4.  **Автоматизацию запуска** (START.bat, start.sh, launcher.py) и возможность создания **.exe** файла.
5.  **Полную документацию** для продажи и развертывания.

---

## 💡 Контекст и Требования

### 1. Основная функциональность

- **Назначение:** Автоматизация работы партнера программы "Свой в Альфе" (Альфа-Банк).
- **Ключевые функции:**
    - **Автоматическая инициация диалогов** с новыми контактами.
    - **ИИ-рекомендации** продуктов (дебетовые карты, кредиты, счета) на основе контекста клиента.
    - **Парсинг** контактов из Telegram групп и каналов.
    - **Управление кампаниями** рассылок через веб-интерфейс.
    - **Аналитика** в реальном времени.
- **База знаний:** Встроенная информация о программе "Свой в Альфе" (баллы, условия, партнерские ссылки).

### 2. Технический стек

- **Backend:** Python 3.11+, FastAPI, Telethon, SQLAlchemy.
- **Frontend:** React, TypeScript, Axios.
- **База данных:** SQLite (по умолчанию), с возможностью подключения PostgreSQL/MySQL.
- **ИИ:** Интеграция с **Gemini API** и **Groq API** (бесплатные альтернативы OpenAI).

### 3. Коммерческая готовность (Ключевые особенности)

- **Setup Wizard (CLI и Web UI):**
    - Должен автоматически запускаться при отсутствии `.env` файла.
    - Должен принимать и валидировать: `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `TELEGRAM_PHONE_NUMBER`, `TELEGRAM_BOT_TOKEN`, `GEMINI_API_KEY`, `GROQ_API_KEY`.
    - Должен сохранять данные в `.env` файл.
    - Должен содержать встроенные инструкции по получению всех ключей.
- **Автоматизация запуска:**
    - Создать **START.bat** (Windows) и **start.sh** (Linux/macOS) для запуска двойным кликом.
    - Создать **launcher.py** для кроссплатформенного запуска.
    - Скрипты должны проверять Python, устанавливать зависимости, запускать Setup Wizard и открывать браузер на `http://localhost:8000/setup`.
- **Создание .exe:**
    - Создать **build_exe.py** для автоматической сборки исполняемого файла с помощью PyInstaller.
    - Создать **BUILD_EXE_INSTRUCTIONS.md** с инструкциями по сборке.

### 4. Документация

Создать следующие документы для коммерческого пакета:
- **README.md** (Главная документация, быстрый старт, FAQ).
- **DEPLOYMENT_GUIDE.md** (Развертывание на VPS, Docker, Colab).
- **API_HASH_GUIDE.md** (Инструкция по получению Telegram API_ID/HASH).
- **QUICKSTART.md** (5-минутный старт).
- **AUTOMATION_REPORT.md** (Отчет об автоматизации).
- **FINAL_DELIVERY_REPORT.md** (Финальный отчет о проекте).

---

## 🛠️ Структура проекта (Минимальный набор файлов)

Воссоздать следующие ключевые файлы:

### Backend (Python)
- `main.py` (FastAPI, Uvicorn, роутинг)
- `telethon_service.py` (Telethon клиент)
- `knowledge_base.py` (База знаний и RAG)
- `free_llm_service.py` (Интеграция Gemini/Groq)
- `dialog_initiator.py` (Логика инициации диалогов)
- `models.py` (SQLAlchemy модели, с `extra_data` вместо `metadata`)
- `database.py` (Подключение к БД, с использованием `os.getenv` для `DATABASE_URL`)
- `config.py` (Переменные окружения, константы)
- `sender.py` (Отправка сообщений)
- `api_keys_guide.py` (Руководство по API ключам)
- `setup_wizard.py` (CLI Setup Wizard)
- `setup_api.py` (API для Web Setup UI)
- `requirements.txt` (Зависимости: fastapi, uvicorn, telethon, sqlalchemy, pydantic, python-dotenv, google-genai, groq)

### Frontend (React/TypeScript)
- `SetupUI.tsx` (Веб-интерфейс для настройки)
- `AdminPanel.tsx` (Основная админ-панель)
- `CampaignManager.tsx` (Управление кампаниями)

### Автоматизация
- `START.bat` (Windows launcher)
- `start.sh` (Linux/macOS launcher)
- `launcher.py` (Универсальный Python launcher)
- `build_exe.py` (Сборщик .exe)

### Документация
- `README.md`
- `DEPLOYMENT_GUIDE.md`
- `API_HASH_GUIDE.md`
- `QUICKSTART.md`
- `AUTOMATION_REPORT.md`
- `FINAL_DELIVERY_REPORT.md`

---

## 📝 Инструкция для ИИ

1.  **Воссоздай** все перечисленные файлы, основываясь на их описании и функциональности, как если бы ты создавал их с нуля.
2.  **Особое внимание** удели `setup_wizard.py`, `setup_api.py`, `SetupUI.tsx`, `launcher.py`, `START.bat`, `start.sh` для обеспечения полной автоматизации и коммерческой готовности.
3.  **Убедись**, что `models.py` использует `extra_data` вместо `metadata` для совместимости.
4.  **Убедись**, что `database.py` использует `os.getenv` для `DATABASE_URL`.
5.  **Собери** все файлы в архив `alfa-campaign-manager-v2.0-COMMERCIAL.zip`.
6.  **Предоставь** финальный архив и все созданные документы.

---

## 🚀 Финальный результат

Предоставить архив `alfa-campaign-manager-v2.0-COMMERCIAL.zip` и краткое сообщение о завершении.
