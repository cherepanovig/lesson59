# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
#cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

# Заполняем базу 10-ю записями
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"user{i}",
#     f"example{i}@gmail.com", f"{i}0", "1000"))

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500
#cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 != 0")

# Удаляем записи с id 1, 4, 7 и 10
#cursor.execute("DELETE FROM Users WHERE id IN (1, 4, 7, 10)")

# выборка всех записей при помощи fetchall(), где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    username, email, age, balance = user  # Распаковываем кортеж
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")
    #print(user)


connection.commit() # сохраняем состояние
connection.close() # закрываем соединение
