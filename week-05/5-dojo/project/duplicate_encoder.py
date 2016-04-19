# "".join(list(map(lambda c: '(' if str.lower().count(c) == 1 else ')', str.lower())))

class DuplicateEncoder:
  def __init__(self, text):
    self.text = text.lower()

  def encode_char(self, c):
    return '(' if self.text.count(c) == 1 else ')'

  def encode(self):
    out = ""
    for c in self.text:
      out += self.encode_char(c)

    return out
