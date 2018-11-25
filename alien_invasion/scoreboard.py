import pygame.font


class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        """Initializes score keeper"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font settings for scoring
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare initial score board
        self.prep_score()

    def prep_score(self):
        """Render score into an image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #Display score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #Draw score to screen
        self.screen.blit(self.score_image, self.score_rect)