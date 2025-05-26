# Тестовое задание Alteg.io

## Описание проекта

В рамках тестового задания необходимо:

- Развернуть базу данных **MySQL** и создать в ней таблицы с данными о продажах.
- Развернуть базу данных **ClickHouse**.
- Перенести данные из MySQL в ClickHouse батчами.
- Подключиться к ClickHouse через **Power BI** и построить дашборд по продажам.

Все компоненты проекта разворачиваются с использованием **Docker**.

---

## Стек технологий

- MySQL
- ClickHouse
- Python (скрипты переноса данных)
- Docker / Docker Compose
- Power BI (для визуализации)

---

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/yourname/test-alteg.git
   cd alteg
   docker compose up --build
   
