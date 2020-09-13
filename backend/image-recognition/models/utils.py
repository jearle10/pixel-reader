

def class_text_to_int(row_label):
    if row_label == '2s':
        return 33
    elif row_label == '2c':
        return 34
    elif row_label == '2d':
        return 35
    elif row_label == '2h':
        return 36
    elif row_label == '3s':
        return 37
    elif row_label == '3c':
        return 38
    elif row_label == '3d':
        return 39
    elif row_label == '3h':
        return 40
    elif row_label == '4s':
        return 41
    elif row_label == '4c':
        return 42
    elif row_label == '4d':
        return 43
    elif row_label == '4h':
        return 44
    elif row_label == '5s':
        return 45
    elif row_label == '5c':
        return 46
    elif row_label == '5d':
        return 47
    elif row_label == '5h':
        return 48
    elif row_label == '6s':
        return 49
    elif row_label == '6c':
        return 50
    elif row_label == '6d':
        return 51
    elif row_label == '6h':
        return 52
    elif row_label == '7s':
        return 1
    elif row_label == '8s':
        return 2
    elif row_label == '9s':
        return 3
    elif row_label == 'Qs':
        return 4
    elif row_label == 'Ks':
        return 5
    elif row_label == '10s':
        return 6
    elif row_label == 'As':
        return 7
    elif row_label == 'Js':
        return 8
    elif row_label == '7h':
        return 9
    elif row_label == '8h':
        return 10
    elif row_label == '9h':
        return 11
    elif row_label == 'Qh':
        return 12
    elif row_label == 'Kh':
        return 13
    elif row_label == '10h':
        return 14
    elif row_label == 'Ah':
        return 15
    elif row_label == 'Jh':
        return 16
    elif row_label == '7d':
        return 17
    elif row_label == '8d':
        return 18
    elif row_label == '9d':
        return 19
    elif row_label == 'Qd':
        return 20
    elif row_label == 'Kd':
        return 21
    elif row_label == '10d':
        return 22
    elif row_label == 'Ad':
        return 23
    elif row_label == 'Jd':
        return 24
    elif row_label == '7c':
        return 25
    elif row_label == '8c':
        return 26
    elif row_label == '9c':
        return 27
    elif row_label == 'Qc':
        return 28
    elif row_label == 'Kc':
        return 29
    elif row_label == '10c':
        return 30
    elif row_label == 'Ac':
        return 31
    elif row_label == 'Jc':
        return 32
    else:
        return 0


def class_int_to_text(pred):
    card_type_dict = {
        3: '9s',
        28: 'Qc',
        36: '2h',
        49: '6s',
        20: 'Qd',
        45: '5s',
        31: 'Ac',
        21: 'Kd',
        44: '4h',
        2: '8s',
        18: '8d',
        9: '7h',
        33: '2s',
        27: '9c',
        30: '10c',
        19: '9d',
        7: 'As',
        39: '3d',
        6: '10s',
        4: 'Qs',
        17: '7d',
        8: 'Js',
        48: '5h',
        15: 'Ah',
        14: '10h',
        35: '2d',
        5: 'Ks',
        11: '9h',
        23: 'Ad',
        50: '6c',
        40: '3h',
        1: '7s',
        46: '5c',
        24: 'Jd',
        32: 'Jc',
        41: '4s',
        52: '6h',
        10: '8h',
        26: '8c',
        42: '4c',
        16: 'Jh',
        22: '10d',
        25: '7c',
        51: '6d',
        38: '3c',
        29: 'Kc',
        34: '2c',
        43: '4d',
        12: 'Qh',
        13: 'Kh',
        47: '5d',
        37: '3s'
    }
    return card_type_dict[pred]