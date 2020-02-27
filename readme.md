# Rock Paper Scissors
_By Christopher Cybusz_

This is a Rock Paper Scissors programming challenge that I took on in Python. The program is command-line and run from the application's root directory by typing: `python play.py`. The Program has a few dependencies, but they are non-critical to the core logic and control-flow of the game, and are instead used to provide a better UX. Have fun!
## My Solutions for the Requirements
The rules of Rock Paper Scissors are centered around two Players, and this challenge required three profiles (or "player types") to be implemented into the game. Already, Interfaces would be the way to go to centralize the core functions between all player types, and streamline the development and implementation of new player types down the line:
1. Every Player Type Provides and Contains a name
2. Every Player Type Plays the game
3. Every Player keeps track of their score.
Note: The implementation of a "name" was not a requirement, but I found it made the experience much funner given the text-based format of the game. Since this is a game, fun should be one of the core metrics to decide implementations by.
### Human Player
The Human Type player Provides their name from user-input as well as their choice of which option to play during the game's matches. These two methods and their corresponding variables are core to the Player interface, and throw errors if they are not implemented.
### "Random" CPU
The First opponent created was the "Random CPU" who provides a name from a random list of 26 names, and select their choice pseudo-randomly from the list of choices. This is done using the python `random` library.
### "Tactical" CPU
The "Tactical" CPU was created when the game's source code was completed in order to self-demonstrate how easy it is to implement new types of players. Since it is a CPU, the name was again provided randomly from a list of 26 names, but the play logic was different. Instead, it overtook the parent's `__init__()` function to initialize a variable that kept track of its last move (as subsequent moves are chosen to beat the previous choice). 
Since the variable that tracked the last played option was unique to the "Tactical" CPU, this proved that new Player types are easily implemented and highly customizable, as long as they adhere to the core interface.
## Coding Practice
The Source codes contains highly detailed comments and plenty of `TODO:` observations. The Code logic should definitely be reviewed for best-practice and optimizations, as it is my first time coding Python utilizing this level of OOP (my previous experience mostly included data processing and Webpage scraping).
## Extensions
All extensions highlighted in the Rock Paper Scissors spec sheet have already been implemented, and both comments and this readme file explain how they were accomplished and how they could be modified in the future.