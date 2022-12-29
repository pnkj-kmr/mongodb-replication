import os
import json
import time


# {"t":{"$date":"2022-12-06T06:07:03.204+05:30"},"s":"I",  "c":"CONNPOOL", "id":22576,   "ctx":"ReplNetwork","msg":"Connecting","attr":{"hostAndPort":"nr-ma-mongodb2.stllab.in:27017"}}
# {"t":{"$date":"2022-12-06T06:07:03.436+05:30"},"s":"I",  "c":"NETWORK",  "id":22944,   "ctx":"conn572696","msg":"Connection ended","attr":{"remote":"192.168.7.1:37644","connectionId":572696,"connectionCount":257}}


def find_c_vs_s(filename):
    ret = {}
    temp = {}
    x, y = 0, 0
    try:
        with open(os.getcwd() + os.sep + filename) as f:
            c = 0
            while True:
                line = f.readline()
                # couting line counts
                x = ret.setdefault("total_lines_in_file", 0)
                ret['total_lines_in_file'] = x + 1
                
                if len(line) > 1:
                    temp = json.loads(line)
                    # count component vs severity - count
                    y = ret.setdefault(temp['c'], {}).setdefault(temp['s'], 0)
                    ret[temp['c']][temp['s']] = y + 1
                    if not line:
                        break
                    ## Added for testing till  - 10
                    c = c +1 
                    if c == 10000000:
                        break   # testing
    except Exception as exc:
        print(f"Exception===", exc)
    return ret


if __name__ == "__main__":
    log_file = "mongod.log"
    st = time.time()
    print(f"Function call initiated...")
    data = find_c_vs_s(log_file)
    print(f"Completed T: {(time.time()-st)}")
    print(json.dumps(data, indent=4))
    