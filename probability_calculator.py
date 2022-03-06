import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball in balls:
            for i in range(balls[ball]):
                self.contents.append(ball)
    
    def draw(self,draw_num):
        removed_balls = []
        max_balls = len(self.contents)
        
        if draw_num < max_balls:
            for i in range(draw_num):
                chosen_ball_num = random.randrange(max_balls)
                removed_balls.append(self.contents[chosen_ball_num])
                self.contents.pop(chosen_ball_num)
                max_balls -= 1
            return (removed_balls)

        else:
            removed_balls = self.contents
            return removed_balls
            
        

def experiment (hat, expected_balls, num_balls_drawn, num_experiments):   
    counter = 0 
    for i in range(num_experiments):
        internal_counter = 0
        expt_drawn_balls = {}
        contents_copied = hat.contents.copy()

        # start drawing
        removed_balls = hat.draw(num_balls_drawn)

        # reverts the contents to before the draw
        hat.contents = contents_copied
        
        # make a dictionary to track qty of each distinct ball drawn out
        for ball in removed_balls:
            expt_drawn_balls[ball] = expt_drawn_balls.get(ball,0) +1
    
        # see if expected_balls are drawn out
        for key in expected_balls:
            val = expected_balls[key]
            if key in expt_drawn_balls:
                if expt_drawn_balls[key] >= val:
                    internal_counter += 1
    
        # confirms the expected balls are drawn out, then counts +1 to num of positive expts
        if internal_counter == len(expected_balls):
            counter += 1

    return (counter/num_experiments)

        
# test1
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print (probability)

# test2
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, 
                    expected_balls={"blue":2,"green":1}, 
                    num_balls_drawn=4, 
                    num_experiments=1000)
print (probability)

# test3
hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, 
                expected_balls={"yellow":2,"blue":3,"test":1}, 
                num_balls_drawn=20, 
                num_experiments=100)
print (probability)