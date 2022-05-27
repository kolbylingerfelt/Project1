# Escape Room Simulator - P1

## Project Description
This Project involved creating a command line application that can perform the basic CRUD operations, is able to connect to mongoDB, and must be able to parse data from a CSV or JSON file. We were given creative freedom regarding the type of application we could make, so I chose to create a game that requires the user to inspect various locations in order to find a code and escape the room.

## Technologies Used

 1. Python 3
	 -- File I/O
	 -- Collections
	 -- Random
 2. Visual Studio Code
 3. MongoDB
 4. PyMongo
 5. git SCM (+ Github)

## Features

 - Connects to MongoDB using PyMongo
 - Uploads game data from a JSON file into the MongoDB server
 - Allows for all CRUD operations
 - Most importantly, an enjoyable game
 
 To Do list:
 - Fully update all print statements to delay printing to the terminal
 - Manage visualizations of text and wrapping
 - Allow for multiple escape rooms that the user will be able to choose from upon launching the application

## Getting Started

 - Launch your chosen CLI
 - In the CLI type the following:
	 -- git clone [kolbylingerfelt/Project1: Python project 1 - a text based adventure game. (github.com)](https://github.com/kolbylingerfelt/Project1)
 - Upon successfully cloning the repository, type the command: git pull (This will allow for you to pull the files inside the repository onto your system).
 - Navigate to your Windows Powershell. Once inside, navigate to where you have placed the repository (File path included below for reference).  
 - You then want to launch the application with the command 'py actualmenu_demo.py'
 ![filepath](https://ucarecdn.com/63df900e-1305-4dbb-b0d0-d213b5b12fc5/)
 
 - If successful, you will be presented with an introduction, and thus starts gameplay.
 ![intro](https://ucarecdn.com/c5eb4b98-260b-4262-b8a4-ebe16e606162/)
 ## Usage
 
 - The user is presented with options that correlate to locations that need to be searched. Once all locations have been investigated to the liking of the user, they can head to our Floor Puzzle where they are presented with a "lock" that requires the 3 digits found whilst searching our locations.
 ![puzzle](https://ucarecdn.com/3e165d2e-9728-4da2-8b2c-d79471ff2cd7/)
 - Once they finish the game, successful or not, the user is brought back to the main menu. 
 ![enter image description here](https://ucarecdn.com/0219f813-5906-4b5c-98b6-913364ed2244/)
 They can save their win or loss to the Scoreboard (connected to mongoDB) if they want, or they can access any of the other features like view scoreboard, start a new escape room, update alias (for scoreboard), edit the scoreboard (delete saved records), upload data from JSON files, or quit the application.
