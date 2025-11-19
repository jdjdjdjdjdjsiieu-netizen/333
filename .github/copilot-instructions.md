<!-- .github/copilot-instructions.md - инструкции для AI coding agents -->
# Краткие инструкции для Copilot / AI-агентов

Ниже — концентрированная справка, чтобы агент мог быстро начать работу с этим репозиторием.

- **Главная идея проекта:** это исправленная версия "Alfa Campaign Manager" — Python/FastAPI бэкенд + React/TSX фронтенд с интеграциями в Telegram (Telethon) и внешние LLM-сервисы. Ключевые файлы: `main.py`, `launcher.py`, `check_and_update_dependencies.py`, `requirements.txt`, `build_exe.py`, `start.sh`, `START.bat`, фронтенд: `AdminPanel.tsx`, `CampaignManager.tsx`.

- **Быстрые проверки перед изменениями:**
  - Убедиться, что Python >= 3.8 установлен: `python --version`.
  - Запустить автоматическую проверку зависимостей: `python check_and_update_dependencies.py`.
  - Для ручной установки зависимостей: `pip install -r requirements.txt`.

- **Проектные конвенции, важные для агента:**
  - `check_and_update_dependencies.py` — центральный скрипт установки/диагностики зависимостей; любые изменения в установке пакетов должны поддерживать его поведение и флаги (см. специальную обработку `psycopg2-binary`).
  - `launcher.py`, `start.sh`, `START.bat` — вызывают проверку зависимостей и используют fallback, если проверочный скрипт отсутствует; при изменении логики проверки обновляй эти файлы согласованно.
  - В `requirements.txt` предпочтительно указывать `psycopg2-binary>=2.9.9` и при установке использовать флаги `--only-binary=:all:` и `--no-cache-dir` чтобы избежать сборки из исходников.

- **Поведенческие правила для AGENT-PR:**
  - Перед открытием PR запусти `python check_and_update_dependencies.py` и `python -m pip install --upgrade pip` локально (или в CI) и зафиксируй изменения в `requirements.txt`, если меняешь зависимости.
  - Если меняешь установку/обработку пакета (особенно `psycopg2-binary`), добавь тестовый запуск установки в CI шаг или в инструкцию запуска.

- **Интеграции и секреты:**
  - Telegram: credentials (API_ID, API_HASH, PHONE) запрашиваются в Setup Wizard (см. `setup_wizard.py`).
  - LLM API keys (Google Gemini, Groq, Hugging Face) хранятся в конфиге (`config.py`) — не коммитить реальные ключи в репо.
  - БД: `database.py` + `models.py` (SQLAlchemy) — ожидается PostgreSQL/psycopg2.

- **Типичные команды и примеры:**
  - Запуск локально (универсально): `python launcher.py`.
  - Быстрый старт (Linux/macOS): `./start.sh` (файлу `start.sh` нужен `chmod +x`).
  - Установка проблемного пакета вручную: ``pip install psycopg2-binary --only-binary=:all: --no-cache-dir``.
  - Запуск приложения: `uvicorn main:app --reload` (если нужно быстро проверить API).

- **Что искать в коде при задачах:**
  - При проблемах с зависимостями — `check_and_update_dependencies.py` и места вызова в `launcher.py`.
  - При изменениях API — `main.py` (FastAPI роуты) и фронтенд-TSX файлы (`AdminPanel.tsx`, `CampaignManager.tsx`) для соответствия контрактам.
  - При изменениях в сборке `.exe` — `build_exe.py` (проблемы с тройными кавычками уже исправлены в текущей ветке).

- **Ограничения, которые агент должен уважать:**
  - Не изменяй способ хранения/чтения секретов без явного указания; используемые файлы конфигурации — `config.py`.
  - Любые изменения, влияющие на установку зависимостей, должны сохранять обратную совместимость (fallback в `launcher.py` / `start.sh` / `START.bat`).

- **Если нужно:** я могу добавить CI-команды, пример env-файла, PR-checklist или тесты для установки зависимостей — скажите, что важнее.
