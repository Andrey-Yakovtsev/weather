Этот проект - это шаблон обвязок для любого Питон-проекта с больими планами на будущее.
Шаблон вдохновлен книгой "Надежный Python" и реализует мое представление о необходимых пререквизитах для написания качественного, легко поддерживаемого и надежного кода.

В составе:
1. Mypy - для типизации
2. Pylint - для проверки CodeStyle
3. Black - для принудительного форматирования под соблюдение CodeStyle
4. Pytest - как указатель на необходимость покрытия кода тестами
5. Logging - как указатель на необходимость логгирования действий в коде
6. Профайлинг и бенчмарк - как контрольные точки для проверки работы  под нагрузкой
7. Bandit - поиск известных уязвимостей
8. Autoflake - удаление неиспользуемых импортов
8. Все это завернуто в пре-коммит хук для автоматизации предложенного контроля.

Исполняемый код взят из репозитория Алексея Голобурдина (проект "Диджитализируй").

Программа показывает погоду по текущим GPS координатам.

Координаты берутся из IP локатора (допилить...)
Получение погоды по координатам происходит в сервисе OpenWeather.

Для запуска проекта выполнить следующие действия:
1. Установить зависимости
`poetry init`
2. Установить pre-commit
3. установить Хук: pre-commit install




[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
