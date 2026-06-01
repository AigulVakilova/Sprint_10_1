# Sprint_10_1 - Автотесты для проверки веб-приложения Яндекс Маршруты

## Описание проекта

Проект содержит UI-тесты для проверки основных пользовательских сценариев: отрисовки маршрута, выбора вида маршрута, подготовки к заказу такси и оформления заказа.

## Технологии

- Python 3.13
- Selenium 4.18.1
- pytest 7.4.4
- Allure 2.13.2
- Page Object Model (POM)

## Структура проекта
Sprint_10_1
├── locators/                          # Локаторы элементов
│   ├── main_page_locators.py
│   ├── order_taxi_page_locators.py
│   ├── route_page_locator.py
│   └── search_page_locators.py
├── pages/                             # Page Object Model
│   ├── base_page.py                   # Базовые методы
│   ├── main_page.py                   # Методы главной страницы
│   ├── order_taxi_page.py             # Методы формы заказа такси
│   ├── route_page.py                  # Методы блока выбора маршрута
│   └── search_page.py                 # Методы окна поиска и деталей заказа
├── tests/                             # Тесты
│   ├── test_route_block_rendering.py  # Тесты отрисовки блока маршрута
│   ├── test_route_rendering.py        # Тесты отрисовки маршрута на карте
│   ├── test_taxi_order_preparation.py # Тесты подготовки к заказу такси
│   └── test_taxi_tariff_order.py      # Тесты заказа тарифа и полный флоу
├── conftest.py                        # Фикстуры pytest
├── data.py                            # Тестовые данные
├── README.md
└── urls.py                            # URL-адреса приложения
```

## Тестовые сценарии

| Файл | Что проверяет |
|------|---------------|
| `test_route_rendering.py` | Отображение точек маршрута на карте |
| `test_route_block_rendering.py` | Отображение блока с выбором маршрута |
| `test_taxi_order_preparation.py` | Переключение табов, типы передвижения, кнопки действий |
| `test_taxi_tariff_order.py` | Тарифы, тултипы, поля формы, полный флоу заказа |

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest -v
```

## Генерация Allure-отчёта

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Известные баги

| Тест | Описание бага |
|------|---------------|
| `test_tariff_sleepy_tooltip_shows_correct_description` | Перепутаны описания тарифов Сонный и Разговорчивый |
| `test_full_taxi_order_flow` | Чекбокс Столик для ноутбука включён по умолчанию |