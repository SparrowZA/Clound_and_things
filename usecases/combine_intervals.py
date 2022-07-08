interval_list = [
    (1, 5),
    (2,6),
    (22, 30),
    (9,16),
    (15,22),
    (31, 45)
]

def extract_first(tuple_item: tuple):
    return tuple_item[0]

def extract_second(tuple_item: tuple):
    return tuple_item[1]

def order_list(_list) -> list:
    _list.sort(key=extract_first)
    return _list

def intervals_overlap(_item_1, _item_2) -> bool:
    if extract_first(_item_1) > extract_second(_item_2):
        return True
    else:
        return False

def combine_intervals(_item, _item_2):
    max_value = max(extract_second(_item), extract_second(_item_2 ))
    return (extract_first(_item), max_value) 
    

def combine_overlapping_intervals(_list: list) -> list:
    tmp_list = []
    for interval in _list:
        # Assign temp list to temp list unless empty
        # then assign it to a list of intervals.
        tmp_list = tmp_list or [interval]

        if intervals_overlap(interval, tmp_list[-1]):
            tmp_list.append(interval)
        else:
            previous = tmp_list[-1]
            tmp_list[-1] = combine_intervals(previous, interval)
    return tmp_list

def combine_intervals_usecase(_interval_list: list):
    _interval_list = [
            (1, 5), 
            (2, 6), 
            (9, 16), 
            (15, 22), 
            (22, 30), 
            (31, 45)
        ]
    # Part 1: List ordering.
    order_interval_list = order_list(_interval_list)
    print(order_interval_list)

    # Part 2: Creating an overlap list.
    return combine_overlapping_intervals(order_interval_list)
