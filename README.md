# Бот для создания постов с комиксами на стене группы
Программа получает комиксы с [сайта](https://xkcd.com/) и постит их на стену группы VK.

## Установка и настройка
### Клонирование реппозитория
Для установки клонируйте репозиторий командой:
```bash
git clone git@github.com:Flash-kir/vacancies.git
```

### Установка пакетов
Установите необходимые библиотеки:
```bash
pip install -r requirements.txt
```

### Переменные окружения
Для создания файла с переменными окружения `.env` выполните команду:
```bash
cp example.env .env
```
В созданном файле хранятся переменные окружения:
```bash
VK_CLIENT_ID='514...'
VK_GROUP_ID='2171....'
VK_CLIENT_TOKEN='vk1.a.EMQlcDqdD0....'
```

#### Получение переменных
На [странице](https://vk.com/groups?tab=admin) cоздайте группу VK по [инструкции](https://vk.com/@tectgryppa-poshagovaya-instrukciya-po-sozdaniu-gruppy-v-vk).
- VK_CLIENT_ID

Создайте [приложение](https://vk.com/editapp?act=create), тип укажите `standalone`. Запишите в `VK_CLIENT_ID` идентификационный номер приложения.
- VK_GROUP_ID

Для определения `VK_GROUP_ID` воспользуйтесь сервисом по [ссылке](https://regvk.com/id/).
- VK_CLIENT_TOKEN

Для получения токена `VK_CLIENT_TOKEN` следуйте [инструкции](https://vk.com/dev/implicit_flow_user).

## Запуск приложения
Выполните команду:
```bash
python get_comics.py
```
