from random import randint

class CAB():
  def __init__(self):
    self.number = [0,0,0,0]
    for i in range(4):
        self.number[i] = randint(0, 9)
    self.state = 'playing'
    self.count = 0

  def guess(self, guess_number):
    self.count += 1
    match_count = 0
    for i in range(4):
      if self.number[i] == guess_number[i]:
          match_count += 1
    return ['cow'] * match_count


