import hashlib
h = hashlib.new('md5', b'ca').hexdigest()
print(f'initial hash is {h}')