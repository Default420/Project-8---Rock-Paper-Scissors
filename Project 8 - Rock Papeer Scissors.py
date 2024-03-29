# -*- coding: utf-8 -*-
"""Copy of AT_CapstoneProject2_RockPaperScissors_QuestionCopy_v0.3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T52oxMn8xOglWZa9416BlmTDyIi8Nj6B

# Capstone Project 2: The Rock-Paper-Scissors Game

---

### Overview

In this project, you have to create a ROCK-PAPER-SCISSORS game in which a player plays either 'Rock', 'Paper' or 'Scissors' and a computer tries to beat the player based on the player's previous moves. This game is generally played between two people. The rules of this game are:

1. Rock beats scissors.

2. Scissors beat paper.

3. Paper beats rock.


<img src="https://s3-whjr-v2-prod-bucket.whjr.online/b5ceb1fc-1760-4cd4-ae6c-ea600e577899.svg"/>

*Image Credits: https://commons.wikimedia.org/wiki/*


Click on the link provided below to know how the game is played between two players in real life.

[How to Play Rock-Paper-Scissors](https://www.wikihow.com/Video/Play-Rock,-Paper,-Scissors)

For every move, either a human player gets 1 point or the computer gets 1 point. The game runs till either a human player or the computer reaches a score of 10 points.

**Player Input Format**

A player should play his/her move by entering the numbers 0, 1 and 2 where-

- 0 denotes ROCK.

- 1 denotes PAPER.

- 2 denotes SCISSORS.

---

#### Getting Started

Follow the steps described below to solve the project:

1. Click on the link provided below to open the Colab file for this project.
   
   https://colab.research.google.com/drive/1U3sgqsbyo6AvjD5zdPwHdqC_X_nRvMHr

2. Create the duplicate copy of the Colab file. Here are the steps to create the duplicate copy:

    - Click on the **File** menu. A new drop-down list will appear.

      <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/0_file_menu.png' width=500>

    - Click on the **Save a copy in Drive** option. A duplicate copy will get created. It will open up in the new tab on your web browser.

      <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/1_create_colab_duplicate_copy.png' width=500>

     - After creating the duplicate copy of the notebook, please rename it in the **YYYY-MM-DD_StudentName_CapstoneProject2** format.

3. Now, write your code in the prescribed code cells.

---

### The Algorithm

In the algorithm, the computer should keep a count of player moves (i.e., the counts for 0, 1 and 2) in three separate variables - `count_rock`, `count_paper` and `count_scissors`. The algorithm should decide the computer's move based on the following possibilities:

- If  `count_rock` $\\>$ `count_paper` and `count_rock` $\\>$ `count_scissors`, then the computer's move should be ROCK.


- If  `count_paper` $\\>$ `count_rock` and `count_paper` $\\>$ `count_scissors`, then the computer's move should be PAPER.

- If  `count_scissors` $\\>$ `count_rock` and `count_scissors` $\\>$ `count_paper`, then the computer's move should be SCISSORS.

- In all other cases, the computer should play ROCK, PAPER and SCISSORS randomly.

---

### Game Requirements and Flowchart

To make this game, you have to create five variables, one list and three functions.

**Flowchart:**

<img src="https://s3-whjr-v2-prod-bucket.whjr.online/ec033af4-e842-4ddc-b0f0-f9599bcec7b3.jpg"/>

---

#### Import the `random` Module and Create the Count Variables

- As a first step to create this game, import the `random` module.

- Create the `count_rock`, `count_paper` and `count_scissors` variables and set their initial values equal to `0`.
"""

# Import the random module in the next line.
import random

# Create count_rock, count_paper and count_scissors variables and set their initial values equal to 0.
count_rock = 0
count_paper = 0
count_scissors = 0

"""---

#### Create The `update_counts()` Function

Now create a function and name it `update_counts()`. It should take `user_input` variable as input and update the count variables based on the following logic.

- If the player plays ROCK (or `user_input == 0`), then increase the value of `count_rock` variable.

- Else if the player plays PAPER (or `user_input == 1`), then increase the value of `count_paper` variable.

- Else if the player plays SCISSORS (or `user_input == 2`), then increase the value of `count_scissors` variable.

The `update_counts()` function should not return anything. In other words, it should not contain the `return` statement. It should only perform the actions prescribed above. Make sure that you add the `global` keyword before the `count_rock`, `count_paper` and `count_scissors` variables before incrementing their values. Without it you will face an error while running the game.
"""

# Create the update_counts() function.
def update_counts(user_input):
    global count_rock, count_paper, count_scissors
    if user_input == 0:
        count_rock += 1
    elif user_input == 1:
        count_paper += 1
    elif user_input == 2:
        count_scissors += 1

"""---

#### Create The `predict()` Function

Next, you need to create a function called `predict()` which should return -

- ROCK (or `0`), if the value of the `count_rock` variable is greater than the values of the `count_paper` and `count_scissors` variables.

- PAPER (or `1`), if the value of the `count_paper` variable is greater than the values of the `count_rock` and `count_scissors` variables.

- SCISSORS (or `2`), if the value of the `count_scissors` variable is greater than the values of the `count_rock` and `count_paper` variables.

- `0, 1` or `2` randomly if the values of all the three variables i.e. `count_rock, count_paper` and `count_scissors` are equal.

Use the `and` keyword to check two conditions simultaneously. For example, the code below should return `True` because  5 is less than 8 and 5 is less than 10.
"""

5 < 8 and 5 < 10

"""The code below should return `False` because 5 is less than 13."""

5 > 13 and 5 < 10

"""The statement, `condition1 and condition2` is `True` if and only if both the conditions are `True`. If at least one of them is `False`, then the whole statement becomes `False`.


Now, create the `predict()` function.
"""

# Create the predict() function.
import random

def predict():
    if count_rock > count_paper and count_rock > count_scissors:
        return 0
    elif count_paper > count_rock and count_paper > count_scissors:
        return 1
    elif count_scissors > count_rock and count_scissors > count_paper:
        return 2
    else:
        return random.randint(0, 2)

"""---

#### Scores
Now, create two variables `player_score` and `comp_score` to keep a track of the points secured by a player and a computer, respectively. Set their initial values equal to 0.
"""

# Create the player_score and comp_score variables.
player_score = 0
comp_score = 0

"""---

#### The `update_scores()` Function

Create a function and name it `update_scores()`. It should take the `user_input` variable as input and update the scores of the computer and a player. For every player input, there are 3 possible responses from the computer.

**In total, there are 9 possible situations:**

1. Player plays ROCK, computer plays ROCK, resulting in a tie.

2. Player plays ROCK, computer plays PAPER, the computer wins.

3. Player plays ROCK, computer plays SCISSORS, the player wins.

4. Player plays PAPER, computer plays PAPER, resulting in a tie.

5. Player plays PAPER, computer plays ROCK, the player wins.

6. Player plays PAPER, computer plays SCISSORS, the computer wins.

7. Player plays SCISSORS, computer plays SCISSORS, resulting in a tie.

8. Player plays SCISSORS, computer plays ROCK, the computer wins.

9. Player plays SCISSORS, computer plays PAPER, the player wins.

This function needs to cover all the 9 possible situations to update the scores. To correctly create this function, do the following tasks:

1. Write the `global` keyword before the `player_score` and `comp_score` variables.

2. Create a variable called `pred` and store the value returned by the `predict()` function.

3. Write an `if` statement to cover the first 3 possible situations. The code for this part has been provided to you already as a reference to enable you to write the remaining statements.

4. Write an `elif` statement to cover the next 3 possible situations.

5. Write the `else` statement to cover the remaining 3 possible situations.

6. For every possible situation you must print the following:

  - `You played X, computer played Y.`

  - `Computer Score:`
  
  - `Your Score:`
  
  Here, `X` is either `ROCK, PAPER` or `SCISSORS` and `Y` is also either `ROCK, PAPER` or `SCISSORS`.

**Note:** The `\n` is called the **newline** character. It adds an empty newline at the beginning if placed it is before a string or at the end if it is place after a string. Refer to the code shown below.
"""

# Placing \n before a string.
print("\nPlacing the newline character before the string.")

"""As you can see, an empty new line is added before the string."""

# Placing \n after a string.
print("Placing the newline character before the string.\n")

"""As you can see, an empty new line is added after the string.

Now, create the `update_scores()` function.
"""

# Create the update_scores() function.
def update_scores(user_input):
  global player_score, comp_score
  # Rock wins over scissors, scissors win over paper and paper wins over rock.
  pred = predict()

  # Code for Situation 1, 2 and 3.
  if user_input == 0:
    if pred == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

  # Code for Situation 4, 5 and 6.
  elif user_input == 1:
    if pred == 1:
      print("\nYou played PAPER, computer played PAPER.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 0:
      print("\nYou played PAPER, computer played ROCK.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played PAPER, computer played SCISSORS.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

  else:
    # (Write the code for else statement to cover situation 7,8 and 9.)

"""---

#### Gameplay

Now, it is time to run the game.

1. Create a list: `['0', '1', '2']` and store it in the variable called `valid_entries`, i.e, `valid_entries = ['0', '1', '2']`.

2. Create an infinite `while` loop. Inside the loop, create a variable called `user_input` to store the input taken by the player.

3. Use the `input()` function to take input from a player. Inside the `input()` function, write the `Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ` statement to show it as a message to a player.

4. Write another `while` loop to check whether the input provided by a player exists in the `valid_entries` list or not.

5. If the input provided by a player does not exist in the `valid_entries` list, then print `Invalid Input!` message. In the next line, rewrite the `user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")` statement.

6. Now, outside the inner `while` loop, convert the `user_input` value to an integer value using the `int()` function.

7. Call the `update_scores()` function with the `user_input` as an input to update the scores of the computer and the player.

8. Call the `update_counts()` function with the `user_input` as an input to update the counts of the inputs provided by the player.

9. Write an `if` statement to check if the score is 10 for any of the player. If the `comp_score == 10`, then print the `Computer Won!` message and break the loop. Else if the `player_score == 10`, then print the `You won!` message and break the loop.

After writing code for the gameplay, the game should run smoothly till either the computer or the human player has reached a score of 10 points.
"""

# 1. Create a list: ['0', '1', '2'] and store it in the variable called valid_entries, i.e, valid_entries = ['0', '1', '2']
valid_entries = ['0', '1', '2']

# 2. Create an infinite while loop. Inside the loop, create a variable called user_input to store the input taken by the player.
while True:
  # 3. Use the input() function to take input from a player.
  # Inside the input() function, write the Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: statement to show it as a message to a player.
  user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
  # 4. Write another while loop to check whether the input provided by a player exists in the valid_entries list or not.
  while user_input not in valid_entries:
    # 5. If the input provided by a player does not exist in the valid_entries list, then print Invalid Input! message.
    # In the next line, rewrite the user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ") statement.
    print("\nInvalid Input!")
    user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")

  # 6. Now, outside the inner while loop, convert the user_input value to an integer value using the int() function.
  user_input = int(user_input)
  # 7. Call the update_scores() function with the user_input as an input to update the scores of the computer and the player.
  update_scores(user_input)
  # 8. Call the update_counts() function with the user_input as an input to update the counts of the inputs provided by the player.
  update_counts(user_input)

  # (write the code for Step 9)
  # 9. Write an if statement to check if the score is 10 for any of the player.
  # If the comp_score == 10, then print the Computer Won! message and break the loop.
  # Else if the player_score == 10, then print the You won! message and break the loop.
  if comp_score == 10:
    print("Computer Won!")
    break
  elif player_score == 10:
    print("You won!")
    break

"""---

### How To Submit The Project

Follow the steps described below to submit the project.

1. After finishing the project, click on the **Share** button on the top right corner of the notebook. A new dialog box will appear.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/2_share_button.png' width=500>

2. In the dialog box, click on the **Copy link** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/3_copy_link.png' width=500>


3. The link of the duplicate copy (named as **YYYY-MM-DD_StudentName_CapstoneProject2**) of the notebook will get copied

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/4_copy_link_confirmation.png' width=500>

4. Go to your dashboard and click on the **My Projects** option.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/5_student_dashboard.png' width=800>

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/6_my_projects.png' width=800>

5. Click on the **View Project** button for the project you want to submit.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/7_view_project.png' width=800>

6. Click on the **Submit Project Here** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/8_submit_project.png' width=800>

7. Paste the link to the project file named as **YYYY-MM-DD_StudentName_CapstoneProject2** in the URL box and then click on the **Submit** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/9_enter_project_url.png' width=800>
"""