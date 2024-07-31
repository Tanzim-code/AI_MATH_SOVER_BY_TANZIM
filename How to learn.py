#print('pizza')
#print('it is very delicious')
#name = 'Tanzim '
#print('my name is ' + name)
#print(name)
#print(type(name))
#first_name = 'Tanzim'
#second_name = ' ul'
#third_name = ' Anwar'
#full_name = first_name + second_name + third_name
#print("my full name is "+full_name)
#age = 21
#age = age + 1
#print(age)
#print(type(age))
#print("This is Elon Musk")
#print(age)
#age = age + 3
#print(age)
#print('HOw to learn')
#value = 'No value'
#print(value)
#print("bro's age is "+str(age))
#My_age = "13"
#print("My age is " + str(My_age))
#Height = 160.5
#print("My height is " + str(Height) + " cm")
#print(type(Height))
#human = True
#print(human)
#print(type(human))
#print("Are you a human: " + str(human))
#attractive = True
#print(full_name)
#print(attractive)
#print(age)
#Name, Age, Attractive = "Tashfeer", 34, True
#print(Name)
#print(Age)
#print(Attractive)
#Tanzim = Tashfeer = Anwar = Diesel = 24
#print(Tanzim)
#print(Tashfeer)
#name = "Anwar"
#print(len(name))
#print(name.find('r'))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count('a'))
#print(name.replace("a","o"))
#print(name*9)
#x = 1
#y = 2.5
#z= '3'
#print(x, y, z)
#print(str( x))
#print('My roll number is '+(str(x)))
#print(x +(int(y)))
#print(y + (float(x)))
#z = (int(z))
#print(z*3)
#name = input("what is your name? :")
#print("hello " + ((name)))
#age = int(input("how old are you? :"))
#age = age + 4
#print(age)
#print("I am " + (str(age))+ ' years old')
#height = float(input("how tall are you?:"))
#print("My height is " + str(height) +"cm")
#print("how to learn Python")
#import math
#pi = 3.14
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi , 5))
#print(pow(pi , -19))
#print(math.sqrt(pi))
#X =1
#Y =2
#Z =3
#print(max(X,Y,Z))
#print(min(X,Y,Z))

#name = "Tanzim Anwar"
#first_name =name[0]
#print(first_name)
##print("Python is better than HTML")
#last_name = name[0:7]
#print(last_name)
#name_name =name[0:12:3]
#print(name_name)
#reversed_name =name[::-1]
#print(reversed_name)
#website="http://youtube.com"
#sliced_name = slice(7,-4)
#print(website[sliced_name])
#website_2="http://google.com"
#print(website_2[sliced_name])
#print(sliced_name)
#variable='How to be Eric Ten Hag'
#coach_name = slice(10,22)
#rint(variable[coach_name])
#age= int(input("how old are you:"))

#if age<=-1:
    #print("you will come to earth in a few years")
#elif age ==500:
    #print("Mission passed!!!!!")
#elif age==400:
    #print("Mission passed!!!!")
#elif age==300:
    #print("Mission passed!!!")
#elif age==200:
    #print("Mission passed!!")
#elif age==100:
    #print("Mission passed!")
#elif age>=500:
    #print("you are not a human")
#elif age<=17:
    #print("you are not an adult")
#elif age>=18:
    #print("you are an adult")

#Temperature= int(input("What is the temperature today :"))
#if Temperature>= 0 and Temperature <= 20:
   #print("the temperature is cold today")
   #print("you should wear warm cloths")
#if  (Temperature>=21 and Temperature <= 30):
       
    #print("it is a nice day")
    #print("you can go outside to play")
#elif (Temperature<0 or Temperature>30):
    #print("it is a bad day")
    #print("you should not go out")

#while  1==1:
   #print('tanzim')

#something = ""
#while len(something) ==0:
  #something=input("What is your name")
#print("how are you "+something)

#for i in range(20+1):
    #print(i)
#for i in range(50,100+1,5):
    #print(i)

#for i in "tanzim":
   # print(i)

#import time

#for seconds in range(10,0,-1):
 #   print(seconds)
  #  time.sleep(1)
#print("Happy new year!!!!!")

#x=5
#y=6
#bhdzgey=x+y
#print(bhdzgey)

#print("i was"+str(x+y)+"years old")

































#if request.remote_addr == "":
   # abort(403)  # Flask example

#import subprocess

#def unblock_ip(ip_address):
  #try:
    ## Get the list of current iptables rules
    #result = subprocess.run(['sudo', 'iptables', '-L', '-n', '--line-numbers'], stdout=subprocess.PIPE)
    #rules = result.stdout.decode('utf-8').split('\n')

    ## Search for the rule with the specified IP address
    #for rule in rules:
      #if ip_address in rule:
        ## Extract the line number of the rule
        #line_number = rule.split()[0]

        ## Delete the rule
        #subprocess.run(['sudo', 'iptables', '-D', 'INPUT', line_number])
        #print(f"IP address {ip_address} has been unblocked.")
        #return

    #print(f"IP address {ip_address} not found in the iptables rules.")
  #except Exception as e:
   # print(f"An error occurred: {e}")

# Example usage
#unblock_ip('')











#pip install pygame
#import tkinter as tk
#import random
## Set up the window
#root = tk.Tk()
#root.title("Snake Game")

## Set up the canvas
#canvas = tk.Canvas(root, width=400, height=400, bg="black")
#canvas.pack()

## Initial snake and food position
#snake = [(20, 20), (30, 20), (40, 20)]
#snake_direction = "Right"
#food_position = (100, 100)
#food = canvas.create_rectangle(*food_position, *food_position, outline="red", fill="red")

## Draw the snake
#snake_squares = []
#for x, y in snake:
    #square = canvas.create_rectangle(x, y, x+10, y+10, fill="white")
    #snake_squares.append(square)

#def move_snake():
    #global snake, snake_direction, food_position

    ## Calculate the new position of the snake's head
    #head_x, head_y = snake[-1]
    #if snake_direction == "Left":
        #new_head = (head_x - 10, head_y)
    #elif snake_direction == "Right":
        #new_head = (head_x + 10, head_y)
    #elif snake_direction == "Up":
        #new_head = (head_x, head_y - 10)
    #elif snake_direction == "Down":
        #new_head = (head_x, head_y + 10)

    ## Check for collisions
    #if new_head[0] < 0 or new_head[0] >= 400 or new_head[1] < 0 or new_head[1] >= 400 or new_head in snake:
        #print("Game over!")
        #root.quit()
        #return

    ## Check if snake has eaten the food
    #if new_head == food_position:
        #food_position = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)
        #canvas.coords(food, food_position[0], food_position[1], food_position[0]+10, food_position[1]+10)
    #else:
        ## Remove the last segment of the snake
        #del snake[0]
        #canvas.delete(snake_squares[0])
        #del snake_squares[0]

    ## Add the new head to the snake
    #snake.append(new_head)
    #square = canvas.create_rectangle(new_head[0], new_head[1], new_head[0]+10, new_head[1]+10, fill="white")
    #snake_squares.append(square)

    ## Call this function again after 100ms
    #root.after(100, move_snake)

#def change_direction(new_direction):
    #global snake_direction
    #if new_direction == "Left" and snake_direction != "Right":
        #snake_direction = new_direction
    #elif new_direction == "Right" and snake_direction != "Left":
        #snake_direction = new_direction
    #elif new_direction == "Up" and snake_direction != "Down":
        #snake_direction = new_direction
    #elif new_direction == "Down" and snake_direction != "Up":
        #snake_direction = new_direction

## Bind the arrow keys to change the direction of the snake
#root.bind("<Left>", lambda event: change_direction("Left"))
#root.bind("<Right>", lambda event: change_direction("Right"))
#root.bind("<Up>", lambda event: change_direction("Up"))
#root.bind("<Down>", lambda event: change_direction("Down"))

## Start the game
#move_snake()
#root.mainloop()






#import subprocess

#def block_ip(ip_address):
   # try:
       # subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", f"name=BlockIP_{ip_address}", f"dir=in", f"action=block", f"remoteip={ip_address}"], check=True)
       # print(f"Successfully blocked IP address: {ip_address}")
   # except subprocess.CalledProcessError as e:
       # print(f"Failed to block IP address: {ip_address}\n{e}")

#block_ip("")

# app.py
from flask import Flask, request, jsonify
import sympy as sp

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Math Solver AI!"

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    problem = data.get('problem')

    if not problem:
        return jsonify({"error": "No problem provided"}), 400

    try:
        solution = sp.sympify(problem).evalf()
        return jsonify({"solution": str(solution)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    problem = data.get('problem')
    operation = data.get('operation', 'solve')

    if not problem:
        return jsonify({"error": "No problem provided"}), 400

    try:
        expr = sp.sympify(problem)
        if operation == 'solve':
            solution = sp.solve(expr)
        elif operation == 'simplify':
            solution = sp.simplify(expr)
        elif operation == 'differentiate':
            variable = data.get('variable', 'x')
            solution = sp.diff(expr, sp.Symbol(variable))
        elif operation == 'integrate':
            variable = data.get('variable', 'x')
            solution = sp.integrate(expr, sp.Symbol(variable))
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"solution": str(solution)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400









