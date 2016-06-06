class Task(object):
  def __init__(self, checked = False, text = ''):
    self.checked = checked
    self.text = text
  
  def set_from_db_line(self, line):
    splitted_line = line.split(';')
    self.checked = splitted_line[0] == 'True'
    self.text = splitted_line[1]

  def get_to_db_line(self):
    return str(self.checked) + ';' + self.text

  def to_string(self):
    check = '[ ]'
    if self.checked:
      check = '[X]'
    return check + self.text
