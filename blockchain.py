

class Blockchain:
  def __init__(self):
    hashlast = generate_hash('gen_last')
    hashstart = generate_hash('gen_hash')

    genesis = Block('gen_data',hashstart,hashlast)
    self.chain = [genesis]

  def add_block(self, data):
    prev_hash = self.chain[-1].hash
    hash = generate_hash(data + prev_hash)
    block = Block(data, hash, prev_hash)
    self.chain.append(block) 


blk = Blockchain()
blk.add_block('1')
blk.add_block('2')
blk.add_block('3')

for block in blk.chain:
  print(block.__dict__)

