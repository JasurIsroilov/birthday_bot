import os
from dotenv import load_dotenv


text = 'Сегодня замечательный праздник - день рождения нашего любимого сотрудника ' \
       '{}\n\n' \
       'С днем рожденья, коллега! Желаю всегда гореть огнем стремления, ' \
       'уверенности и энтузиазма. Желаю вам еще больше новых идей и перспектив, ' \
       'интересных начинаний и успешных завершений. ' \
       'Пусть хватает сил и здоровья на все задумки, пусть хватает денег и энергии на все желания и мечты!'


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')
TG_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


SHEET_ID = os.getenv('SHEET_ID')
SHEET_URL = f'https://docs.google.com/spreadsheet/ccc?key={SHEET_ID}&output=csv'
