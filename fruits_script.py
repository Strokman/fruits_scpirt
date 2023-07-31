from csv import DictReader
import pandas as pd

path = ''
def filter_csv(path):
    # Use a breakpoint in the code line below to debug your script.
    group_1 = dict()
    group_1['id'] = list()
    group_1['13C'] = list()
    group_1['Unc_13C'] = list()
    group_1['15N'] = list()
    group_1['Unc_15N'] = list()
    group_2 = dict()
    group_2['id'] = list()
    group_2['13C'] = list()
    group_2['Unc_13C'] = list()
    group_2['15N'] = list()
    group_2['Unc_15N'] = list()
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = DictReader(f, delimiter=';')
        for i in reader:
            i: dict
            if -21 <= float(i.get('13C').replace(',', '.')) <= -18:
                group_1['id'].append(int(i.get('id')))
                group_1['13C'].append(float(i.get('13C').replace(',', '.')))
                group_1['15N'].append(float(i.get('15N').replace(',', '.')))
                group_1['Unc_13C'].append(0.2)
                group_1['Unc_15N'].append(0.2)
            elif -15 <= float(i.get('13C').replace(',', '.')) <= -13:
                group_2['id'].append(int(i.get('id')))
                group_2['13C'].append(float(i.get('13C').replace(',', '.')))
                group_2['15N'].append(float(i.get('15N').replace(',', '.')))
                group_2['Unc_13C'].append(0.2)
                group_2['Unc_15N'].append(0.2)

    return [group_1, group_2]


def to_excel(*args):
    for k in args:
        for i in range(len(k)):
            df = pd.DataFrame(k[i], [pd.Index(range(1, len(k[i].get('id')) + 1))])
            df.to_excel(f'/Users/antonstrokov/Desktop/group{i}.xlsx', sheet_name='kek')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(filter_csv())
    to_excel(filter_csv())