#decode base64 code using brute force algorithm
import base64
encoded_string='BR3tCNDUzXzYxWDdZXzRSfQ=='
base64Map='QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890+/='
for i in range(64):
     for j in range(64):
             r='R'+base64Map[i]+base64Map[j]+encoded_string
             decoded=base64.b64decode(r)
             if b'FLAG' in decoded:
                    print(decoded)
                    