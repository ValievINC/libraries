import requests
import json

# Готовим ссылки
characters = 'https://rickandmortyapi.com/api/character/'
locations = 'https://rickandmortyapi.com/api/location/'
episodes = 'https://rickandmortyapi.com/api/episode/'


# Получаем json-представление ссылок
def get_json(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


# Получаем список из имён всех персонажей
# Проходимся по страницам и вытягиваем имена
def get_list(types):
    pages = get_json(types)['info']['pages']
    list = []
    for page in range(pages):
        for data in get_json(types + f'?page={page + 1}')['results']:
            list.append(data['name'])
    return list


# Получаем индекс персонажа из get_list и собираем data с посвященной ему странички
def get_character_info(name):
    index = get_list(characters).index(name)
    data = get_json(characters + str(index+1))
    print(data['species'])
    print(data['gender'])
    print(data['status'])


# Same, но с локациями
def get_location_info(name):
    index = get_list(locations).index(name)
    data = get_json(locations + str(index + 1))
    print(data['type'])
    print(data['dimension'])
    print(get_persona_name(data['residents']))


# Same, но с эпизодами
def get_episode_info(name):
    index = get_list(episodes).index(name)
    data = get_json(episodes + str(index+1))
    print(data['air_date'])
    print(data['episode'])
    print(get_persona_name(data['characters']))


# Здесь парсим линки на выяснение имён, иначе в принте будут ссылки
def get_persona_name(links):
    list = []
    for link in links:
        data = get_json(link)
        name = data['name']
        list.append(name)
    return list


# Непосредственно команды
def make_command(str, first, second):
    if str == 'characters list':
        print(get_list(characters))
    elif str == 'locations list':
        print(get_list(locations))
    elif str == 'episodes list':
        print(get_list(episodes))
    elif first == 'character':
        get_character_info(second)
    elif first == 'location':
        get_location_info(second)
    elif first == 'episode':
        get_episode_info(second)


inp = input()
first_word = inp.split(' ')[0]
second_word = inp.replace(first_word + ' ', '')
make_command(inp, first_word, second_word)
