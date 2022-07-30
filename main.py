import turtle
import pandas

data = pandas.read_csv("states.csv")
data_states = data.state.to_list()
screen = turtle.Screen()

screen.title("India states game")
image = "india-political-map.gif"
screen.setup(width=1.0, height=1.0)
screen.addshape(image)
turtle.shape(image)

missing_states = data_states
guessed_states = []
total_states = 0
is_game_on = True
while len(guessed_states) < 36:
    answer = screen.textinput(title=f"{total_states}/36 States and UTs", prompt="Which is another state?")
    answer = answer.title()
    if answer == "Exit":
        break
    if answer in data_states:
        guessed_states.append(answer)
        total_states += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_cor = data[data.state == answer]
        t.goto(int(state_cor.x), int(state_cor.y))
        t.write(answer)
        missing_states.remove(answer)

print(missing_states)

# new_data = pandas.DataFrame(missing_states)
# header = ["States you missed"]
# new_data.to_csv("Missed_states.csv", header=header)
