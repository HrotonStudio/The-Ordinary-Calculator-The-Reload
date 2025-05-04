import hashlib

def md5_lock(str:str):
    md = hashlib.md5(str.encode())
    md5_str = md.hexdigest()
    return md5_str
