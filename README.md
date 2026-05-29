Purchase Tracker CLI

Консольное приложение для учёта и анализа покупок.

Возможности

* Добавление покупок
* Просмотр покупок
* Удаление покупок
* Анализ расходов
* Статистика по категориям

Установка

git clone https://github.com/USERNAME/purchase-tracker.git
cd purchase-tracker
pip install -r requirements.txt

Запуск

python main.py

Структура проекта

* core/commands.py — логика покупок
* core/storage.py — работа с JSON
* core/analytics.py — аналитика
* tests/ — тестирование

Git Flow

Проект разрабатывался в отдельных ветках:

* feature/interface
* feature/storage
* feature/analytics
* feature/tests
Приложение помогает анализировать расходы пользователей