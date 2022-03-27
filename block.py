


import hashlib


class Block:
  def __init__(self,data,hash,prev_hash):
    self.data = data
    self.hash = hash
    self.prev_hash = prev_hash


  def generate_hash(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

