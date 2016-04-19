names = [{ 'id': 1, 'name': 'John'},
         { 'id': 2, 'name': 'Molly'},
         { 'id': 3, 'name': 'Jane'}]

# use TDD, test the functions!
# return the array of names
# return the array of names which begins with J

class MyMagic:
  def __init__(self, list_of_users):
    self.database = list_of_users

  def names_as_list(self):
    return list(map(lambda u: u['name'], self.database))

  def names_start_with_j(self):
    return list(filter(lambda name: name.startswith('J'), self.names_as_list()))
