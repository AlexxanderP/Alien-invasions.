This will be edited and modified as the project progresses.

Pygame module used for most of the drawing functions


File break down:
    Alien_invasion.py
        Run time file.
        Stores main Conditional loop, as well as object, and draw screen method calls.
    alien.py
        Stores the alien object, used to initialize the individual alien settings within the fleet.
    bullet.py
        Stores bullet object and information needed for drawing and terminating the fired bullets when on and once off screen.
    button.py
        Stores the button class and associated default settings to start the game after user "starts".
    game_functions.py
        stores all function definitions with calls to linked parameters in other files, used by run-time. 
    gamestats.py
        Stores each instances game stats, inititalized at the start of each game.
    scoreboard.py
        Stores the scoreboard class and linked methods for rendering the score to image, aswell as set its rect attribute.
    settings.py
        stores the settings class called throughout the application.
        This is how I will increase game difficulty as the player progresses.
    ship.py
        Stores the ship object and information needed to initialize and draw the ship, while being responsive.
    
    