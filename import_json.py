from TA import xlsx_to_dict, dict_to_pd
import pandas as pd
import json

json_frame = {
      "call_id": "mikopbx-1655352126_2_351h3x",
      "time_start": "2022-08-10T08:58:45.000+03:00",
      "call_type_id": 1,
      "system_phone": "123",
      "enable_diarization": "false",
      "files": [
        {
          "channel_number": 0,
          "filename": "mikopbx-1655352126_2_351h3x.mp3",
          "lang_id": 1,
          "role_id": 1
        },
        {
          "channel_number": 1,
          "filename": "mikopbx-1655352126_2_351h3x.mp3",
          "lang_id": 1,
          "role_id": 2
        }
      ],
      "role_data": [
        {
          "role_id": 1,
          "extension": "1000"
        },
        {
          "role_id": 2,
          "phone": "7777"
        }
      ]
    }

meta = dict_to_pd(xlsx_to_dict('./targ.xlsx'))
print(meta)

final = []
for index, row in meta.iterrows():

    json_frame = {
        "call_id": str(row['ИмяФайла'])[:-4],
        "time_start": f"2022-06-16T09:00:00.000+03:00",
        "call_type_id": 1,
        "system_phone": row['ИмяОператора'],
        "enable_diarization": "false",
        "files": [
            {
                "channel_number": 0,
                "filename": row['ИмяФайла'],
                "lang_id": 1,
                "role_id": 1
            },
            {
                "channel_number": 1,
                "filename": row['ИмяФайла'],
                "lang_id": 1,
                "role_id": 2
            }
        ],
        "role_data": [
            {
                "role_id": 1,
                "extension": row['ИмяОператора']
            },
            {
                "role_id": 2,
                "phone": row['НомерКлиента']
            }
        ]
    },

    final.append(json_frame)

with open('./json_dump.txt', 'w', encoding='utf-8') as d:
    d.write(str(final))
