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

1. **Клонируйте репозиторий и запустите проект:**

```bash
git clone https://github.com/yourname/test-alteg.git
cd test-alteg
docker-compose up --build
```

```shell
git clone https://github.com/yourname/test-alteg.git
cd test-alteg
docker compose up --build
```



   
## sql запросы
-- запрос по дням  
with cte as (select sale_date, quantity*price as sum 
from my_database.sales s)  
select sale_date, sum(sum)  
from cte  
group by sale_date  
order by sale_date asc  
;  


--запрос топ 5 по количеству  
select product_name, sum(quantity) as sum_q  
from my_database.sales s  
group by product_name   
order by sum_q desc   
limit 5;  


--запрос топ 5 по сумме  
with cte as (select product_name, quantity*price as sum_s  
from my_database.sales s)  
select product_name, sum(sum_s) as sum_s  
from cte  
group by product_name   
order by sum_s desc   
limit 5;  
