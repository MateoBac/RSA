import random
import time as t
def getrange(digents):
    n = 10
    for i in range(digents):
        n *= 10
    return n


class RSA:
    def __init__(self,sec=512):
        random.seed(t.time())
        st = t.time()
        prime1 = self.getprime(sec)
        prime2 = self.getprime(sec)

        while prime1 == prime2:
            prime2 = self.getprime(sec)
        self.N = prime1 * prime2
        self.p = (prime1 - 1) * (prime2 - 1)

        self.e = self.getprime(sec)
        print(f"Zeit Für Primezahlenberechnung {t.time()-st}")
        self.d = self.getiverse(self.e, self.p)[1]



    def get_privat_key(self):
        return self.d,self.N

    def get_public_key(self):
        return self.e , self.N

    def set_public_key(self,e,N):
        self.e = e
        self.N = N
    def set_privat_key(self,d,N):
        self.d = d
        self.N = N

    def encrypt(self,number):
        if number>= self.N:
            return False
        return pow(number,self.e,self.N)

    def decrypt(self,number):
        return pow(number,self.d,self.N)

    def encrypttext(self,text:str):
        encrypted = []
        for char in text:
            encrypted.append(self.encrypt(ord(char)))
        return encrypted
    def decrypttext(self,text:list):
        decrypted = ""
        for char in text:
            decrypted += chr(self.decrypt(char))
        return decrypted

    #
    #
    #
    def getiverse(self, a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            (faktor, rest) = divmod(a, b)
            (ggt, inn_mul_a, inmul_b) = self.getiverse(b, rest)
            (mul_a, mull_b) = (inmul_b, inn_mul_a - faktor * inmul_b)
            return (ggt, mul_a, mull_b)

    def is_prime(self,n, k=50):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        for i in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    def getprime(self,length):
        while True:
            candidate = random.getrandbits(length)
            if candidate % 2 == 0:
                candidate += 1
            if self.is_prime(candidate):
                return candidate

privat = RSA(512)#zahl in den klammern gibt die bitlänge der einzelnen primzahlen an die zu erstellung der schlüssel verwendet werden(NICHT ÜBER 1512)
public = RSA(10)
t1,t2 = privat.get_public_key()
public.set_public_key(t1,t2)

encrypted = public.encrypttext("Platzhalter Für zu verschlüsselnen text")

print(encrypted)
print(privat.decrypttext(encrypted))


