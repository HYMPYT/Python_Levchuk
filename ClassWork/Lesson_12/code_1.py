import sys

def get_ip_or_none():
    try:
        ip = sys.argv[1]
        octats = ip.split('.')
        if len(octats) != 4:
            return None
        for octat in octats:
            if not octat.isdigit():
                return None
        return ip
    except BaseException as e:
        print(e)
        return None

IP = get_ip_or_none()

try:
    QUANTITY = int(sys.argv[2])
except ValueError as e:
    QUANTITY = 0
    print("Invalid value")

def atack():
    print('IP:', IP)
    print('QUANTITY:', QUANTITY)
    print('Finish')

atack()