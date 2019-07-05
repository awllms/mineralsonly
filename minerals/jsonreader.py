import json

with open('../assets/minerals.json') as mineralfile:
    MINERAL_LIST_DATA = json.load(mineralfile)
    # Testing json data
    # for mineral in MINERAL_LIST_DATA:
    #     for key, value in mineral.items():
    #         print('{}: {}'.format(key, value))
