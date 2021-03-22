import json

# Application ru-com operators

okko = 'ru.more.play'
ivi = 'ru.ivi.client'
kinopoisk = 'ru.kinopoisk'
tnt_premier = 'gpm.tnt_premier'
start = 'ru.start.androidmobile'
netflix = 'com.netflix.mediaclient'
megogo = 'com.megogo.application'
wink = 'ru.rt.video.app.mobile'
amediateka = 'com.amdteka'


def scarp_and_write(buffer_name, application):
    result = reviews_all(
        application,
        sleep_milliseconds=0,  # defaults to 0
        lang='ru',  # defaults to 'en'
        country='ru',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        filter_score_with=1  # defaults to None(means all score)
    )
    with open(buffer_name, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4, default=str)


def clear_buffer(buffer_name):
    open(buffer_name, 'w').close()


clear_buffer('buffer.json')
scarp_and_write('buffer.json', okko)
