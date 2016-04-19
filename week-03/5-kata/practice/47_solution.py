# create a Class called FileLines
# lines = FileLines('alma.txt')
# lines.get_last() <- returns the last line of the file
# lines.get_first() <- returns the fitst line of the file
# lines.get_nth(2) <- returns the nth line given in the argument

class FileLines:
    def __init__(self, file_name):
        fobj = open(file_name)
        self.lines = fobj.readlines()
        fobj.close()

    def get_first(self):
        return self.get_nth(0)

    def get_last(self):
        return self.get_nth(-1)

    def get_nth(self, n):
        return self.lines[n]

lines = FileLines('alma.txt')
print(lines.get_first())
print(lines.get_last())
print(lines.get_nth(1))
