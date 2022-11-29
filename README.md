# Бот для создания постов с комиксами на стене группы
Программа получает комиксы с https://xkcd.com/ и постит их на стену группы VK.

## Установка и настройка
Для установки клонируйте репозиторий командой:
```bash
git clone git@github.com:Flash-kir/vacancies.git
```
Установите необходимые библиотеки:
```bash
pip install -r requirements.txt
```
Для создания файла `.env` выполните команду:
```bash
cp example.env .env
```

На [странице](https://vk.com/groups?tab=admin) cоздайте группу VK по [инструкции](https://vk.com/@tectgryppa-poshagovaya-instrukciya-po-sozdaniu-gruppy-v-vk).

Создайте (приложение)[https://vk.com/editapp?act=create], тип укажите `standalone`. Запишите в `VK_CLIENT_ID` идентификационный номер приложения.

Для определения `VK_GROUP_ID` воспользуйтесь сервисом по (ссылке)[https://regvk.com/id/].

Для получения токена `VK_CLIENT_TOKEN` следуйте [инструкции](https://vk.com/dev/implicit_flow_user).