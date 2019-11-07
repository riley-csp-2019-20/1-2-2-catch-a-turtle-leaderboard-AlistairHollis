#-----import statements-----
import turtle as trtl
import random
import time
import leaderboard as lb
#-----leaderboard  variables-----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("State the name you were initially given at birth: ")

#-----game configuration-----
font_setup = ("impact", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
if (player_name == str("boomer")):
  size = 0.1
else:
  size = 3

figure = "circle"
score = 0
speed = 0
wn = trtl.Screen()

#-----:)-----



#-----initialize turtle-----

target = trtl.Turtle()
target.shape(figure)
counter =  trtl.Turtle()
scoreman = trtl.Turtle()
scoreman.hideturtle()
scoreman.penup()
target.pu()
target.speed(speed)
scoreman.goto(-360,350)
target.shapesize(size)

#-----game functions-----
counter.penup()
counter.hideturtle()
counter.goto(330,350)
def target_clicked(x,y):
  score_change()
  target_move()
def countdown():
  global timer
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    manage_leaderboard()
    game_over()
    
  else:
    counter.write("Timer: " + str(timer), align="center", font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def score_change():
    global score
    score += 1
    scoreman.clear()
    scoreman.write("Score: " + str(score), align="center", font=font_setup)
def game_over():
    target.ht()
    target.pu()
    counter.clear()
    target.goto(9001,9001)
    counter.goto(80,80)
    font_setup = ("impact", 70, "normal")
    counter.write("Time's Up", font=font_setup)
    while True:
      wn.bgcolor("red")
      time.sleep(0.2)
      wn.bgcolor("orange")
      time.sleep(0.2)
      wn.bgcolor("yellow")
      time.sleep(0.2)
      wn.bgcolor("green")
      time.sleep(0.2)
      wn.bgcolor("blue")
      time.sleep(0.2)
      wn.bgcolor("indigo")
      time.sleep(0.2)
      wn.bgcolor("purple")
      time.sleep(0.2)

def target_move():

  randx = random.randint(-400,400)
  randy = random.randint(-300,300)

  target.goto(randx, randy)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global target

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, target, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, target, score)

#---------events---------
target.onclick(target_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()