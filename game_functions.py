import pygame
import sys
from time import process_time

from bullet import Bullet
from game_over import GameOver

def check_events(settings, stats, ship, screen, bullets, play_button, hud):
    '''Checks for keyboard and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ship, stats, bullets, hud)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, stats, bullets, play_button, mouse_x, mouse_y, hud)

def check_play_button(settings, stats, bullets, play_button, mouse_x, mouse_y, hud):
    '''Starts new game when player clicks play'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats, bullets, hud)
        settings.initialise_dynamic_settings()

def start_game(stats, bullets, hud):
    '''Starts game'''
    stats.reset_stats()
    bullets.empty()
    hud.prep_hits()
    hud.prep_misses()
    stats.game_active = True

def check_keydown_events(event, screen, ship, stats, bullets, hud):
    '''Checks for key presses'''
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_p:
        if stats.game_active == False:
            start_game(stats, bullets, hud)

def check_keyup_events(event, ship):
    '''Checks for key releases'''
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_bullets(settings, bullets):
    for bullet in bullets.sprites():
        bullet.update_position()
        bullet.draw_bullet()

    for bullet in bullets.copy():
        if bullet.rect.left >= settings.screen_width:
            bullets.remove(bullet)

def update_target(settings, target):
    if target.check_edges():
        settings.target_direction *= -1

    target.update_target()

def check_bullet_target_collisions(settings, stats, target, bullets, bullets_target, hud):
    '''Respond to bullet-target collisiosn'''
    if pygame.sprite.spritecollideany(target, bullets):
        for bullet in bullets.copy():
            if bullet.rect.right >= target.rect.left:
                bullets_target.append(bullet)
                bullets.remove(bullet)
                hud.prep_hits()
                hud.prep_misses()
                if len(bullets_target) == 30:
                    bullets_target.clear()
                    stats.reset_stats()

def check_bullet_screen_edge_collision(stats, screen, target, bullets, hud):
    screen_rect = screen.get_rect()          
    if not pygame.sprite.spritecollideany(target, bullets):
        for bullet in bullets.copy():
            if bullet.rect.right >= screen_rect.right:
                bullets.remove(bullet)
                stats.bullets_left -= 1
                hud.prep_misses()
                #m_line.draw_miss_line()
                return True
            else:
                return False

def game_over(screen, stats):
    go = GameOver(screen)
    if stats.bullets_left == 0:
        stats.game_active = False
        go.blitme()
        stats.reset_stats()

def update_screen(settings, screen, stats, ship, bullets, target, play_button, hud, m_line):
    '''Update screen elements'''
    screen.fill(settings.bg_colour)
    update_bullets(settings, bullets)
    update_target(settings, target)
    ship.blitme()
    if check_bullet_screen_edge_collision == True:
        m_line.draw_miss_line()
        process_time(2)
    target.draw_target()
    hud.show_info()
    game_over(screen, stats)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()