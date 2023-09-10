
# Battleships Game - (In development)

As someone who loves learning programming, I decided to create my own version of the classic game, Battleship, using Python Essentials for the Course at Code Institute.
Have you ever played it? It's a really fun game that requires strategy and a bit of guessing. It's meant for two players, and the game board has grids where each player places their own fleet of ships. The goal is to sink your opponent's fleet before they sink yours!

It's a popular game played all over the world, and you can learn more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) if you're interested.

[View the live project here](https://battleships-jogo-5dc3cf77bd06.herokuapp.com/)

![Battleship Mockup Images](readme_images/mockup-battleships.jpg)

## How To Play

- In this version, the player enters their name and a qustion about the grid size is made.
- The player have to choose the Grid Size between 5 to 9.
- Based on the size of the grid selected by the player, the ships will be shown. The number of ships will always be twice the size of the grid. For example, if the player selects a grid size of 5, there will be 10 ships displayed on both the player's and computer's boards. If the grid size is 6, then 12 ships will be shown on both boards and so on.
- The Player can view the location of their own ships denoted by **S**, but they won't be able to see where the computer's ships are placed.
- After all the ships are placed, each player takes turns trying to guess where the other player's ships are located on the board.
- Guesses are marked on the board with an **O** and Hits are marked with a **X**.
- The first to destroy 5 ships wins the game.

[Back to top ⇧](#)

## UX

### User Demographic

- **The target audience of this game is:**

    - New user
    - Current user

- **Demographic:**

    - All ages
    - All puzzle playing levels

- **Psychographic:**

    - Lifestyles:
        - Interest in games
        - Interest in battles
    - Personality/Attitudes:
        - Focused
        - Creative

### New User Goals

1. New Users are looking for clear instructions on how to play the game.
2. They want to see a visual representation of whether the shot hit or missed a ship.
3. They want to see a scoreboard that shows who is winning.
4. New Users want the ability to replay the game.

### Current User

1. Current users want the ability to replay the game.
2. Current users want to be able to choose a grid size that raises the game's difficulty level.
3. They want a visual representation of whether the shot hit or missed a ship.
4. They want the ability to replay the game.

### Scope

The scope of the project involves defining requirements based on user goals. The required features have been categorized based on the goals of new and current users:

- Content Requirements:
    - The user will be looking for:
        - Clear and concise instructions.
        - A consistent theme, and game play.
- Functionality Requirements:
    - The user will be able to:
        - Enter co-ordinates using numbers and letters.
        - Replay the game.
        - End the program at the end of the game.

### Structure

The project will be deployed to a Heroku terminal. There will be no styling.

### Skeleton

A flowchart was created to clearly illustrate the logical sequence that the functions will follow.

<details>
<summary>Flowchart</summary>
    
![Flowchart](readme_images/Flowchart.jpeg)

</details>

[Back to top ⇧](#)

## Features

### Existing Features

#### The Welcome Message to Battleships Game

- When a new game starts the welcome message is displayed.
- It also includes the user's goal and the number of HITs needed to win the game.
- The player is then prompted for name input. Input is repeated until a valid name is entered.

![Welcome message](readme_images/welcome.jpg)

#### The Game Rules

- When a new game starts the welcome message is displayed.

![Game Rules](readme_images/rules_grid.jpg)

### Future Features

- Allow Player to position ships themselves
- Have ships larger than 1x1

## Data Model

- llllll

## Testing

- llll

### Bugs

#### Solved Bugs

- lllll
#### Remaining Bugs

- jjjjjjj

#### Validator Testing

- lllll

## Deployment

lllllll

## Credits

llllll