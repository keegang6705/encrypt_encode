## encrypt,encoder
encryptและdecryptข้อความแบบง่ายๆ(ง่ายมาก)

---

## วิธีใช้

```py
import encrypt_encode as enc
print(enc.encode("hello"))
#aGVsbG8=
print(enc.decode("aGVsbG8="))
#hello
print(enc.encrypt("hello"))
#('ncdLAcZ=', 'rAGVhPt3lExQBay6RDK1S5wvCLbXHcpUjW2gms4TFizMNo0Zq7k8Jdfnu9OeIY')
#encrypt(text,key)ถ้าไม่ใส่keyจะสุ่มkeyให้เอง
print(enc.encrypt("hello","rAGVhPt3lExQBay6RDK1S5wvCLbXHcpUjW2gms4TFizMNo0Zq7k8Jdfnu9OeIY"))
#ncdLAcZ=
#encrypt(text,key)ถ้าใส่keyจะreturnแค่ข้อความ
print(enc.decrypt("ncdLAcZ=", "rAGVhPt3lExQBay6RDK1S5wvCLbXHcpUjW2gms4TFizMNo0Zq7k8Jdfnu9OeIY"))
#keyหาได้จาก keygen() หรือ encrypt() ก็ได้
```
