# Функции бота
Пользовательские команды (!):
- бросить монетку

Админские команды ($$):
- удалить сообщения на канале (пока работает только на канале tst-bot)
- загрузить Cog файл
- выгрузить Cog файл
- перезагрузиь Cog файл

## Пользовательские команды
Все пользовательские команды выполняются с перфиксом !

## Пользовательские команды
Все пользовательские команды выполняются с перфиксом !

### Бросить монетку
Позволяет бросать жребий.
При простом использовании просто скажет орел или решка.
Команда принимает аргументы в качестве никнеймов пользователей сервера в формате дискорда \@nickname разделенных пробелами.
Вот несколько примеров использования:
1. Просто скажет орел или решка в формате emoji.
    - !coin
2. Назовет кто победил, автор сообщения или тот чей ник указан в качестве параметра.
    - !coin \@nickname1
3. Назовет кто победил, автор сообщения или четыре человека которые указаные в качестве параметров.
    - !coin \@nickname1 \@nickname2 \@nickname3 \@nickname4
> \@nickname** это никнейм человека на канале с которым вы бросаете жребий.

## Админские команды
Все админские команды выполняются с префиксом $$

### Удалить сообщения на канале
> (пока работает только на канале tst-bot)

Для удаления сообщений на канале используйте команду:

* $$clear <number_of_messages>
> <number_of_messages> это количество сообщений которые вы хотите удалить.

### Загрузить Cog файл
* $$load <CogName>
> <CogName> это название модуля который мы хотим загрузить. Название модуля это название Cog файла без расширения .py

### Выгрузить Cog файл
* $$unload <CogName>
> <CogName> это название модуля который мы хотим выгрузить. Название модуля это название Cog файла без расширения .py

### Перезагрузиь Cog файл
* $$reload <CogName>
> <CogName> это название модуля который мы хотим перезагрузить. Название модуля это название Cog файла без расширения .py

# Дополнительное описание

## Работа с Cog файлами
Для реализации бота был выбран модульный подход. Данный подход позволяет гибко управлять функциями, а так же систематизирует файлы разработки. Текущая структура проекта такова:
- commands - папка с комадами
    - CoinToss.py - файл команды "бросить монетку"
- templates - папка с шаблонами
    - cog_template.py - шаблон Cog файла для того что быстро создать новую команду, а также вспомнить что по чем.
- main.py - основной файл бота
- README.md - файл с данным текстом
- secrets.py - файл с секретным токеном

В дальнейшем для каждой новой команды планируется создавать новый Cog файл в папке commands на основе шаблона в папке templates.
При запуске бота, все Cog файлы подгружаются автоматически. Но если будет необходимость выгрузить, перезагрузить или загрузить новый Cog файл в программу, можно воспользоваться командами:
- загрузить Cog файл
- выгрузить Cog файл
- перезагрузиь Cog файл

```md
# TODO
Необходимо проработать возможность автоматизации или хотябы оптимизации различных процессов:
- Регистрация игроков в лиге
- Заполнение статистики матчей
- Вывод объявлений
- и тд.
```
