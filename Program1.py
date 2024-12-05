from datetime import datetime

def datetime_info(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    formatted_date = date.strftime('%d-%m-%Y')
    
    day_of_week = date.strftime('%A')
    
    next_year = datetime(date.year + 1, 1, 1)
    days_until_next_year = (next_year - date).days
    
    return {
        "Дата в формате ДД-ММ-ГГГГ": formatted_date,
        "День недели": day_of_week,
        "Кол-во дней до следующего года": days_until_next_year
    }

try:
    date_str = datetime_info(input("Введите дату в формате \"YYYY-MM-DD\": "))
    print(date_str)
except ValueError:
    print("Неккоректный формат даты")