import copy
import random
# Consider using the modules imported above.

class Hat:
    # initialize object with variable # of keyword arguments dictionary
    # **kwargs makes these arguments a dictionary
    def __init__(self, **color_freq):
        self.contents = list()
        # extend the contents list for all the keys * value times in dict color_freq
        [self.contents.extend([ color ] * color_freq[color]) for color in color_freq.keys()]

    # to remove #num number of balls to draw from the hat at random
    # balls should not go back, so without replacement, cannot use choices()
    def draw(self, num_balls_to_draw: int):
        # avoid negative integer, use available balls if # to draw is too much
        num_balls_to_draw = min(max(0, num_balls_to_draw), len(self.contents))
        # use sample to create a a new list without replacement, but fails test module
        # return random.sample(self.contents, num_balls_to_draw)

        # use random.randrange to pick an element to drop in contents list
        draw_contents = list()
        for i in range(num_balls_to_draw):
            draw_index = random.randrange(0, len(self.contents))
            draw_contents.append(self.contents[draw_index])
            self.contents.pop(draw_index)
        return draw_contents

# hat: hat object
# expected_balls: group of balls to draw from the hat object, a dictionary
# num_balls_drawn: # of balls to draw out of the hat in each experiment
# num_experiments: # of experiments to run, more experiments -> more accurate
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    i = 0
    success_times = 0
    while i < num_experiments:
        # #deepcopy hat object 
        temp_hat = copy.deepcopy(hat)
        # attempt a draw, returns a list as result
        draw_result_list = temp_hat.draw(num_balls_drawn)
        # turn the list of ball colors into dictionary
        draw_result_dict = dict([(color, draw_result_list.count(color)) for color in set(draw_result_list)])
        # draw_result_dict = {color : draw_result_list.count(color) for color in set(draw_result_list) }
        # compare 2 dictionaries, if experiment succeeds, add 1
        if all(draw_result_dict.get(k, 0) >= v for (k, v) in expected_balls.items()):
            success_times += 1
        i += 1
    # end of while loop

    # error handle:
    if num_balls_drawn < sum(expected_balls.values()):
        return 'num_balls_drawn is smaller than sum of expected_balls'
    elif num_experiments == 0:
        return 'num_experiments cannot be zero'
    else:    
        # return success rate
        return float(success_times / num_experiments)


# # test cases
# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print('hat1:', hat1.contents)
# print('hat2:', hat2.contents)
# print('hat3:', hat3.contents)
# print('hat1 draw:', hat1.draw(3))
# print('hat2 draw:', hat2.draw(11))
# print('hat3 draw:', hat3.draw(5))

# random.seed(95)
# hat = Hat(blue=4, red=2, green=6)
# probability = experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)

# random.seed(95)
# hat = Hat(blue=3,red=2,green=6)
# probability = experiment(
#     hat=hat, 
#     expected_balls={"blue":2,"green":1}, 
#     num_balls_drawn=4, 
#     num_experiments=1000)
# print("Probability:", probability)
# # expected = 0.272

# random.seed(95)
# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# probability = experiment(
#     hat=hat, 
#     expected_balls={"yellow":2,"blue":3,"test":1}, 
#     num_balls_drawn=20, 
#     num_experiments=100)
# print("Probability:", probability)
# # expected = 1.0