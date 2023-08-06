import hashlib
from hashlib import *

hash = sha224()
string = 'Hello'

hash.update(b"string")
print(hash.hexdigest())

# Condensed Way to get the same result.
hash = sha224(b"string").hexdigest()
print(hash)

# -----------------------------------------------------------------------------
sha_list1 = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']

for s in sha_list1:
    # print(s)
    hsh = f'{s}(b"{string}").hexdigest()'
    print(hsh)

a = sha1()
b = sha224()
c = sha256()
d = sha384()
e = sha512()

sha_list = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']

a.update(b"Hello world")
b.update(b"Hello world")
c.update(b"Hello world")
d.update(b"Hello world")
e.update(b"Hello world")

hash_list = [a.hexdigest(), b.hexdigest(), c.hexdigest(), d.hexdigest(), e.hexdigest()]

for i, j in zip(sha_list, hash_list):
    print('')
    print(f'\tHash of {i.upper()} is \n\t{j}.')
    print('')


#

import hashlib
from hashlib import blake2b
h = blake2b()
h.update(b'Hello world')

print(f'Digest: {h.digest()}\nHEX-Encoded String: {h.hexdigest()},\nlength of Hex is: {len(h.hexdigest())}')

print(f'Hex Encoded String:{blake2b(b"Hello world").hexdigest()}\nand the lenght is {len(blake2b(b"Hello world").hexdigest())}.')

# Hex Encoded String:6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183
# and the lenght is 128.

input_str = input('Enter Text: ')

rev_str = input_str[-1::-1]
hex_str = blake2b(b"input_str").hexdigest()  
rev_hex_str = blake2b(b"rev_str").hexdigest()  

print(hex_str)
print(rev_hex_str)

hash_object = blake2b(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# Output: 4386a08a265111c9896f56456e2cb61a64239115c4784cf438e36cc851221972da3fb0115f73cd02486254001f878ab1fd126aac69844ef1c1ca152379d0a9bd

hash_object1 = sha512(b'Hello')
print(hash_object1)
hex_dig1 = hash_object1.hexdigest()
print(hex_dig1)

str1 = 'hello'
str_salt = 'wrld'
str_pepper = 'q'

main_str = f'{str1}{str_salt}{str_pepper}'

hash_object = blake2b(b'main_str')
hex_dig = hash_object.hexdigest()
print(hex_dig)
print(len(hex_dig))