



from typing import Dict, List

def sort_by_date(input_list: List[Dict], sorting: bool = True) -> List[Dict]:
    """
    возвращает список словарей, отсортированный по дате
    :param input_list: список словарей
    :param sorting: необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    :return: list отсортированный по дате список словарей
    """
    return sorted(input_list, key=lambda current_dict: current_dict["date"], reverse=sorting)


# lists = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# # print(filter_by_state(lists, 'CANCELED'))
# print(sort_by_date(lists, False))
