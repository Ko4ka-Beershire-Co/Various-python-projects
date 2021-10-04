import pandas as pd


def get_list(path):
    i = pd.read_excel(path, sheet_name=0)
    agents_df = (i['Имя оператора'])
    agents_list = agents_df.values.tolist()  # list of agents
    unique_agents = list(dict.fromkeys(agents_list))
    # print(unique_agents)  # unique agents list

    return unique_agents


def tie_extension(list):
    # create extension list
    k = 0
    extensions = []
    for i in list:
        extensions.append(k)
        k += 1
    return extensions

def create_agent_tuple(agents, IDs):
    final = list(zip(agents, IDs))
    print(final)

    return final

a = get_list('C:/Users/Alex/Desktop/Python/pythonProject/report.xlsx')

b = tie_extension(a)

create_agent_tuple(a, b)
