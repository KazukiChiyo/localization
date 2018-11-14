# Author: Zeran Zhu
# 11/10/2018

# change me
__bt_dev__ = "/dev/cu.HawkEyeBT-RNI-SPP"


def send_to_bt(f, s):
    try:
        f.write(s.encode())
        f.flush()
        print("->")
        print(s)
    except:
        print("[error] Error sending data to BT")


def read_from_bt(f):
    try:
        ret = f.readline().decode()
    except:
        print("[error] Error reading data from BT")
        ret = ""
    print("<-")
    print(ret)
    return ret




if __name__ == '__main__':
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
    send_to_bt(f, "RSS0123401234\n")
    while read_from_bt(f):
        pass