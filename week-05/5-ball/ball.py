import vector

class Ball():
    def __init__(self, pos, velocity, radius):
        self.pos = pos
        self.velocity = velocity
        self.size = vector.multiply((radius, radius), 2)

    def get_bbox(self):
        start = vector.add(self.pos, vector.multiply(self.size, -0.5))
        end = vector.add(self.pos, vector.multiply(self.size, 0.5))
        return start + end

    def move(self):
        self.pos = vector.add(self.pos, self.velocity)
