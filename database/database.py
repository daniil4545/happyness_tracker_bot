import sqlite3
from datetime import datetime


conn = sqlite3.connect('happiness.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS happiness_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
    ''')
    conn.commit()

# Функция для сохранения статистики
def save_message(user_id, message_text):
    cursor.execute('INSERT INTO happiness_log (user_id, message) VALUES (?,?)', (user_id, message_text))
    conn.commit()

# Функция для получения общего количества записей
def get_total_count(user_id):
    cursor.execute('SELECT COUNT(*) FROM happiness_log WHERE user_id = ?', (user_id,))
    return cursor.fetchone()[0]

# Функция для получения количества записей за сегодня
def get_today_count(user_id):
    cursor.execute('SELECT COUNT(*) FROM happiness_log WHERE user_id = ? AND DATE(timestamp) = DATE(\'now\')', (user_id,))
    return cursor.fetchone()[0]

# Функция для получения количества записей за неделю
def get_weekly_count(user_id):
    cursor.execute('SELECT COUNT(*) FROM happiness_log WHERE user_id = ? AND timestamp >= DATE(\'now\', \'-7 days\')', (user_id,))
    return cursor.fetchone()[0]

# Функция для получения самого счастливого дня в неделе
def get_happiest_day_in_week(user_id):
    cursor.execute('''
        SELECT DATE(timestamp) AS date, COUNT(*) AS count
        FROM happiness_log
        WHERE user_id = ? AND timestamp >= DATE('now', '-7 days')
        GROUP BY DATE(timestamp)
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ''', (user_id,))
    result = cursor.fetchone()
    if result:
        date, count = result
        weekday = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
        return date, weekday, count
    return None

# Функция для получения самого счастливого дня в месяце
def get_happiest_day_in_month(user_id):
    cursor.execute('''
        SELECT DATE(timestamp) AS date, COUNT(*) AS count
        FROM happiness_log
        WHERE user_id = ? AND timestamp >= DATE('now', 'start of month')
        GROUP BY DATE(timestamp)
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ''', (user_id,))
    result = cursor.fetchone()
    if result:
        date, count = result
        weekday = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
        return date, weekday, count
    return None

# Функция для получения самого счастливого времени суток
def get_happiest_time_of_day(user_id):
    cursor.execute('''
        SELECT strftime('%H', timestamp) AS hour, COUNT(*) AS count
        FROM happiness_log
        WHERE user_id = ?
        GROUP BY strftime('%H', timestamp)
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ''', (user_id,))
    result = cursor.fetchone()
    if result:
        hour, count = result
        return hour, count
    return None

# Функция для получения среднего количества записей в день за неделю
def get_average_daily_count_week(user_id):
    cursor.execute('SELECT COUNT(*) FROM happiness_log WHERE user_id = ? AND timestamp >= DATE(\'now\', \'-7 days\')', (user_id,))
    total_count = cursor.fetchone()[0]
    return total_count / 7

# Функция для получения среднего количества записей в день за все время
def get_average_daily_count_all_time(user_id):
    cursor.execute('SELECT COUNT(*) FROM happiness_log WHERE user_id = ?', (user_id,))
    total_count = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(DISTINCT DATE(timestamp)) FROM happiness_log WHERE user_id = ?', (user_id,))
    total_days = cursor.fetchone()[0]
    return total_count / total_days if total_days > 0 else 0
