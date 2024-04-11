import bitarray
import hashlib
import random
import string
import sys
import time


class bf:
    def __init__(self, size):
        self.size = size
        self.bitarray = bitarray.bitarray(size)
        self.list = [0]*size
        self.bitarray.setall(False)
        self.hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha3_224, hashlib.sha3_512, hashlib.sha512, hashlib.sha3_384]
        # , hashlib.sha1, hashlib.sha224, hashlib.sha256 hashlib.sha3_224, hashlib.sha3_512, hashlib.sha512
        # self.hash_functions = [hashlib.sha1,hashlib.md5]

    def add_data(self, data):
        for hash_func in self.hash_functions:
            # print(hash_func)
            index = int(hash_func(data).hexdigest(), 16) % self.size
            self.bitarray[index] = 1
            self.list[index] = 1
      
       

    def is_data_exist(self, data):
        result = bitarray.bitarray([True])
        for hash_func in self.hash_functions:
            index = int(hash_func(data).hexdigest(), 16) % self.size
            result &= self.bitarray[index:index+1]

        if result[0]:
            return True
        else:
            return False
if __name__ == "__main__":
    bf_size = 10000
    bf_contain_data_size = 1000
    test_case_amount = 1000
    random.seed(time.time())

    b = bf(bf_size)
    s = set()
    d = {}

    list =[]
    for i in range(bf_contain_data_size):
            data = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
            data = str.encode(data)
            list.append(data)
    print(list)

    for i in list:
        b.add_data(i)
        s.add(i)
        d[i] = 1

    false_positive_amount = 0

    for i in range(test_case_amount):
        data = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
        data = str.encode(data)
        if b.is_data_exist(data) ^ (data in s):
            false_positive_amount += 1

    fail_rate = round((false_positive_amount / test_case_amount) * 100, 2)
    print("{:20} {}\n".format("success case amount:", test_case_amount - false_positive_amount))
    print("{:20} {}\n".format("fail case amount:", false_positive_amount))
    print("{:20} {}%\n".format("fail rate:", fail_rate))
    print("{:20} {} bytes\n".format("bf bitarray size:", sys.getsizeof(b.bitarray.tobytes())))
    print("{:20} {} bytes\n".format("bf list size:", sys.getsizeof(b.list)))
    print("{:20} {} bytes\n".format("set size:", sys.getsizeof(s)))
    print("{:20} {} bytes\n".format("dict size:", sys.getsizeof(d)))
