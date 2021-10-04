mport re
import pandas as pd


def get_list(path, header):  # header - STR название колонки

    i = pd.read_excel(path, sheet_name=0)
    agents_df = (i[header])
    agents_list = agents_df.values.tolist()  # list of agents
    # unique_agents = list(dict.fromkeys(agents_list))
    # print(unique_agents)  # unique agents list
    return agents_list


def remove_ext(list):  # remove .ogg .wav etc
    new_list = []
    for i in list:
        i = i[:-4]
        new_list.append(i)

    return new_list


# Lists
file_location = 'C:/Users/Alex/Desktop/Python/pythonProject/report.xlsx'

TIME_MAP = 'Дата начала звонка'
CALL_ID_MAP = 'Имя файла'  # не забыть снести расширение
EXTENSION_MAP = 'Имя оператора'
CALLER_MAP = 'Номер клиента'

format_unit = {
    "call_id": "CALL_ID_MAP",
    "time_start": "TIME_MAP",

    "files": [
        {
            "channel_number": 0,
            "filename": "CALL_ID_MAP*",
            "lang_id": 1,
            "role_id": 1
        },
        {
            "channel_number": 1,
            "filename": "CALL_ID_MAP*",
            "lang_id": 1,
            "role_id": 2
        },
    ],

    "role_data": [
        {
            "role_id": 1,
            "extension": "EXTENSION_MAP"
        },
        {
            "role_id": 2,
            "phone": "CALLER_MAP"
        }
    ]
}

# print(format_unit)
i = 'kek'
j = re.sub(r'CALL_ID_MAP', i, str(format_unit), 0, re.MULTILINE)

print(remove_ext(get_list(file_location, CALL_ID_MAP)))
