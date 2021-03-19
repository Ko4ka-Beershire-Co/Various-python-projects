from google_play_scraper import Sort, reviews_all
import json


def scarp_and_write(buffer_name):
    result = reviews_all(
        'com.nianticlabs.pokemongo',
        sleep_milliseconds=0,  
        lang='en',  # Язык %LL%
        country='us',  # Страна %СС%
        sort=Sort.MOST_RELEVANT,  # Сортировка из Google Play
        filter_score_with=1  # Выводить только с %I% оценкой
    )
    with open(buffer_name, 'w', encoding='utf-8') as f:

        json.dump(result, f, ensure_ascii=False, indent=4, default=str)  # JSON сериалайзабилити мне теперь сниться будет


def clear_buffer(buffer_name):  # Если он есть
    open(buffer_name, 'w').close()


clear_buffer('buffer.json')
scarp_and_write('buffer.json')
