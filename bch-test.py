from bitcoin import *

def btctosatoshi(v):
    return int(float(v)*100000000.0)

addr = '1Dfg9vmCNh7yjTAyFq9W6DjdZSBVNr5eqE'

data = make_request(
    'https://bitcoincash.blockexplorer.com/api/addr/%s' %
    addr)
try:
    jsonobj = json.loads(data.decode("utf-8"))
except:
    raise Exception("Failed to decode data: "+data)

txes = jsonobj["transactions"]

for tx in txes:
    data = make_request(
        'https://bitcoincash.blockexplorer.com/api/tx/%s' % tx)
    try:
        jsonobj = json.loads(data.decode("utf-8"))
    except:
        raise Exception("Failed to decode data: "+data)
    vout = jsonobj["vout"]
    vin = jsonobj["vin"]
    print("INPUTS = ")
    print(vin)
    print("------------------------")
    print("OUTPUTS = ")
    print(vout)
