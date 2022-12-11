# **Turtle Run**

This Program is a project for Computer Programming 1 Course. It is inspired by 
Temple run and Subway surfers.

### Overview and Features

This Game is a parkour game.  that can be played using only 1 player.
Turtle will run in the road with 5 lanes and you must dodge obstacles that will block you 
throughout your run.
![](../../Pictures/Screenshots/Screenshot_20221211_092641.png)
![](../../Pictures/Screenshots/Screenshot_20221211_111837.png)


### How to use and play?

1. Sign Up or Log in with username and password.
2. Press Y/N to ready to play the game.
3. The game starts.
   * press "Left", "Right" or "A", "D" to Move.
4. When your life = 0 this game will end. 
5. The Current Top 5 Leaderboard will be showed up.

### Program's Requirement

There are 4 Python Modules & Libraries required in this program.

* [turtle](https://docs.python.org/3/library/turtle.html): Used for Gameplay 
* [json](https://docs.python.org/3/library/json.html?highlight=json#module-json): Used for Storing User's Data
* [time](https://docs.python.org/3.11/library/time.html): Used for Story Display 
* [random](https://docs.python.org/3/library/random.html): Used for Gameplay

### Program Design
There are **4** classes in this Program.
* **Player**: This class is used for register or login and controlling player to play this game.
* **Point**: This class is used for create an object that can collect points from this object.
* **Obstacles**: This class is used for create objects that reduce your health.
* **Map**: This class is main class used for create the map to support the work of class Point and Obstacles

![](../../../Pictures/Screenshots/Screenshot_20221211_115317.png)

### Code Structure
* [turtle_run.py](turtle_run.py): Run the Program.
* [players.json](players.json): Contains Users' Data (Name, Password and High Score).

https://github.com/TSpoomM/Turtle-run/tree/main/Turtle%20run
