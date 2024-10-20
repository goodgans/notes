# Промежуточная контрольная работа по блоку специализация
## Урок 1. Приложение заметки (Python)

### Задание
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.Например:
```
python notes.py add --title "новая заметка" –msg "тело новой заметки"
```
Или так:
```
Введите команду: add
Введите заголовок заметки: новая заметка
Введите тело заметки: тело новой заметки
Заметка успешно сохранена
Введите команду:
```
При чтении списка заметок реализовать фильтрацию по дате.


# Решение

Реализовано в двух вариантах работы 
* с помощью kонсоли 
* с помощью аргументов


### Программа для заметок для GEEKBRAINS

Это простая программа для ведения заметок. Программа позволяет пользователям легко добавлять, редактировать, удалять, читать, фильтровать и выходить из заметок через интерфейс командной строки.

### Использование
Для запуска и работы с помощью консоли:
1. `git clone`
2. `cd memo_py`
3. (Run main.py and work in terminal)
```commandline
python main.py               
Command line arguments not recognized.
Enter command (add, edit, delete, read, filter, exit):

```

Для запуска с помощью аргументов:
1. `git clone`
2. `cd memo_py`
3. (запускать с помощью агрументов.
   В случае отсутствия аргументов запускается вариант работы через диалог консоли.
   
Для запуска программы выполните функцию main(). Программа принимает следующие аргументы командной строки:

- `--command`: Укажите действие для выполнения (add, edit, delete, read, filter, exit).
- `--title`: Укажите заголовок заметки.
- `--msg`: Введите содержимое заметки.
- `--note_id`: Укажите идентификатор заметки для редактирования или удаления (положительное число).

### Описание параментов агрументов 
Ключевое слово `--command` обязательно.
В зависимости от установленной версии python начало команды может отличаться:
`python main.py --command read` или `python3.11.exe main.py --command read`

### Доступные аргументы
- **add**: Добавить новую заметку с указанным заголовком и сообщением.
```commandline
python main.py --command add --title TITLETEXT --msg MSGTEXT
```
- **edit**: Редактировать существующую заметку, указав идентификатор заметки, новый заголовок и новое сообщение.
```commandline
python main.py --command edit --note_id IDNUMBER --title NEWTITLE --msg NEWMESSAGE
```
```commandline
python main.py --command edit
Enter note id to edit: 5
Enter new title: new_title
Enter new message: new_msg

```
```commandline
python main.py --command edit --note_id IDNUMBERNEW 
```
- **delete**: Удалить заметку, указав идентификатор заметки.
```commandline
python main.py --command delete 
Enter note id to delete: 8
Note deleted successfully.
```
- **read**: Показать все заметки.
```commandline
python main.py --command read  
```
```commandline
python main.py --command read
```
- **filter**: Отфильтровать заметки по конкретной дате (в формате ГГГГ-ММ-ДД).
```commandline
python main.py --command filter
Enter date to filter notes (YYYY-MM-DD):2024-03-27 
```
- **exit** или quit: Выйти из программы.
```commandline
main.py --command exit
```

Работа производиться с файлом note.json
Разделитель: ','

Формат данных:

```json
[   
   {
        "id": 1,
        "title": "Title1",
        "message": "Message1",
        "timestamp": "2024-03-23T08:30:53.585406"
    }
]
```
