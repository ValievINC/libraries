import pandas as pd      # Импортируем pandas


def get_data(date):
    # Заменяем пробел на входе на "-"
    date = date.replace(' ', '-')
    # Создаем колонки для нашей DataField
    columns = ['Date', 'Year', 'Name', 'Caption', 'URL']
    # Читаем CSV файл и даем имя колонкам
    df = pd.read_csv(
        r'https://drive.google.com/uc?export=download&id=1DA14L63MuunBbVJPRr2h1cjz_QXbRxqA',
        header=None, names=columns)
    # Указываем, что теперь у нас индекс - Дата
    df = df.set_index(['Date'])
    # Подаем имени, году, описанию и ссылке данные ячеек
    name = df.loc[date]['Name']
    year = df.loc[date]['Year']
    caption = df.loc[date]['Caption']
    URL = df.loc[date]['URL']
    # Делаем из этого кортеж и выводим
    arr = (name, year, caption, URL)
    return arr


info = get_data(input())
for str in info:
    print(str)