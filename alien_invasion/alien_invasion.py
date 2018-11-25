import pygame
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Display the Start Button
    start_button = Button(ai_settings, screen, "Start!")
    
    #Create an instance to store game stats and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship, bullets, and aliens stored in groups
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Make a new fleet of Aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, start_button, ship, aliens, bullets)


        if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, start_button)        
run_game()
