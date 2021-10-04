import re
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


def str_to_JSON(STR):
    STR_Full = '{"records": [' + STR[2:]
    JSON = STR_Full[:-2]


    return JSON


# Lists
file_location = 'C:/Users/Alex/Desktop/Python/pythonProject/report.xlsx'

TIME_MAP = 'Дата начала звонка'
CALL_ID_MAP = 'Имя файла'  # не забыть снести расширение
EXTENSION_MAP = 'Имя оператора'
CALLER_MAP = 'Номер клиента'

format_unit = {
    "call_id": "CALL_ID_MAP_NO",
    "time_start": "TIME_MAP",

    "files": [
        {
            "channel_number": 0,
            "filename": "CALL_ID_MAP_YES",
            "lang_id": 1,
            "role_id": 1
        },
        {
            "channel_number": 1,
            "filename": "CALL_ID_MAP_YES",
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
# j = re.sub(r'CALL_ID_MAP', i, str(format_unit), 0, re.MULTILINE)

# print(remove_ext(get_list(file_location, CALL_ID_MAP)))


def create_JSON(format_unit,
                TIME_MAP_LIST,
                CALL_ID_MAP_LIST_YES,
                CALL_ID_MAP_LIST_NO,
                EXTENSION_MAP_LIST,
                CALLER_MAP_LIST):
    JSON = []
    k = 0
    while k < len(TIME_MAP_LIST):
        unit_it_1 = re.sub(r'TIME_MAP', str(TIME_MAP_LIST[k]), str(format_unit), 0, re.MULTILINE)
        unit_it_2 = re.sub(r'CALL_ID_MAP_YES', str(CALL_ID_MAP_LIST_YES[k]), unit_it_1, 0, re.MULTILINE)
        unit_it_3 = re.sub(r'CALL_ID_MAP_NO', str(CALL_ID_MAP_LIST_NO[k]), unit_it_2, 0, re.MULTILINE)
        unit_it_4 = re.sub(r'EXTENSION_MAP', str(EXTENSION_MAP_LIST[k]), unit_it_3, 0, re.MULTILINE)
        unit_it_5 = re.sub(r'CALLER_MAP', str(CALLER_MAP_LIST[k]), unit_it_4, 0, re.MULTILINE)

        JSON.append(unit_it_5)
        k += 1

    with open('C:/Users/Alex/Desktop/Python/pythonProject/Dump.txt', 'w') as txt:
        txt.write(str(JSON))

    return str(JSON)


p = create_JSON(format_unit,
                get_list(file_location, TIME_MAP),
                get_list(file_location, CALL_ID_MAP),
                remove_ext(get_list(file_location, CALL_ID_MAP)),
                get_list(file_location, EXTENSION_MAP),
                get_list(file_location, CALLER_MAP))

# print(p)
print(str_to_JSON(p))
