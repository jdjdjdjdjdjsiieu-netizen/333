# 🔑 РУКОВОДСТВО: Как получить Telegram API_ID и API_HASH

**API_ID** и **API_HASH** — это уникальные ключи, необходимые для работы с Telegram API (Telethon). Они используются для авторизации вашего бота/приложения.

---

## 1. Перейдите на официальный сайт Telegram

Откройте в браузере:
[https://my.telegram.org](https://my.telegram.org)

---

## 2. Авторизуйтесь

1. **Введите свой номер телефона** (тот, который вы используете в Telegram).
2. Нажмите **"Next"**.
3. **Введите код подтверждения**, который придет вам в Telegram (в чат с "Telegram").
4. Нажмите **"Sign In"**.

---

## 3. Создайте новое приложение

После авторизации вы попадете на страницу **"API Development Tools"**.

1. Нажмите на ссылку **"Create new application"** (или **"App configuration"**).

2. Заполните поля:

| Поле | Значение |
| :--- | :--- |
| **App title** | `Alfa Campaign Manager` (или любое другое название) |
| **Short name** | `AlfaBot` (или любое другое короткое имя) |
| **URL** | `https://alfa-campaign.com` (можно любой URL) |
| **Platform** | Выберите `Desktop` |
| **Description** | `Telegram bot for Alfa Partner Campaign` |

3. Нажмите **"Create application"**.

---

## 4. Получите ключи

После создания приложения вы увидите страницу с данными вашего приложения.

Вам нужны два поля:

1. **App api_id:** (Это ваш **API_ID**)
2. **App api_hash:** (Это ваш **API_HASH**)

---

## 5. Введите ключи в Setup Wizard

Скопируйте эти два значения и вставьте их в соответствующие поля в **Setup Wizard** вашего проекта:

- **Web UI:** [http://localhost:8000/setup](http://localhost:8000/setup)
- **CLI:** `python setup_wizard.py`

---

## ⚠️ ВАЖНО

- **API_HASH** — это секретный ключ. Никому его не сообщайте.
- **API_ID** и **API_HASH** используются для авторизации вашего номера телефона в Telethon.
- **Это не то же самое, что токен Telegram-бота!** Токен бота вы получаете от @BotFather.

---

**Теперь вы можете получить API_HASH и завершить настройку!**
