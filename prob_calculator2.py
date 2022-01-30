from ast import arg
import random

class Hat:
   
    def __init__(self, *args):
        self.contents = []
        for arg in args:
            x = str(arg).split('=')
            colors = x[0].rstrip()
            number = int(x[1])
            for color in range(number):
                self.contents.append(str(colors))

    def draw(self, numbers):
        balls_drawn = []
        if numbers > len(self.contents):
            return self.contents
        else:
            for num in range(numbers):
                random_num = random.choice(self.contents)
                balls_drawn.append(self.contents.pop(self.contents.index(random_num)))
            return balls_drawn

def experiment(hat,expected_balls, num_balls_drawn, num_experiments):
    m = 0
    count = 0
    colorsright = 0

    for experiment in range (0,int(num_experiments)):
        balls_drawn = []
        if num_balls_drawn > len(hat.contents):
            return hat.contents
        else:
            for num in range(int(num_balls_drawn)):
                random_num = random.choice(hat.contents)
                balls_drawn.append(random_num)
        
        for b,n in expected_balls.items():
            if (balls_drawn.count(b) == n) == True:
                colorsright = colorsright + 1
            if colorsright == len(expected_balls):
                m = m + 1
            count = count + 1
            
        count = 0
        colorsright = 0
    
    prob = m / num_experiments
    return prob

myhat = Hat('black=6', 'red=4', 'green=3')
hat = experiment(myhat, {'red': 1, 'black':2},3,5000)
print (hat)