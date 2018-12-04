# Author: Zeran Zhu
# 11/10/2018

import ast, time

# change me
__bt_dev__ = "/dev/cu.HawkEyeBT-RNI-SPP"


def send_to_bt(f, s):
    try:
        f.write(s.encode())
        f.flush()
    except:
        print("[error] Error sending data to BT")


def read_from_bt(f):
    try:
        ret = f.readline().decode()
    except:
        print("[error] Error reading data from BT")
        ret = ""
    return ret


def pair_bt():
    """Connect to BlueTooth and return file descriptor."""
    f = None
    while True:
        try:
            print("[info] Opening Bluetooth device...")
            f = open(__bt_dev__, "rb+")
            print("[info] Success!")
            break
        except IOError as e:
            print("[error] ", e, "Retrying.")
            continue
        except:
            print("[error] Unexpected Error.\nRetrying.")
    return f


def rssi_query_one(f, id):
    """Query one array of RSSI reading given its id."""
    query_str = "RSS" + str(id) + "\n"
    send_to_bt(f, query_str)
    while True:
        ret = read_from_bt(f)
        if ret:
            return ast.literal_eval(ret)[0]

def rssi_query_all(f):
    """Query an array of RSSI readings."""
    send_to_bt(f, "RSS01234\n")
    while True:
        ret = read_from_bt(f)
        if ret:
            return ast.literal_eval(ret)
