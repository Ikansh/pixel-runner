import pygame
from sys import exit
from random import randint, choice


# Initiating pygame engine for main & unit tests
pygame.init()
WIDTH = 800
HEIGHT = 400
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
pygame.display.set_icon(player_stand)
clock = pygame.time.Clock()
start_time = 0
score = 0

# GLOBAL Background
sky_surf = pygame.image.load('graphics/sky.png').convert()
gnd_surf = pygame.image.load('graphics/ground.png').convert()
gnd_rect = gnd_surf.get_rect(top=HEIGHT * 0.75, left=0)


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.frames: list[pygame.Surface] = [
            pygame.image.load('graphics/player/player_walk_1.png').convert_alpha(),
            pygame.image.load('graphics/player/player_walk_2.png').convert_alpha(),
        ]
        self.i: int = 0
        self.image: pygame.Surface = self.frames[self.i]
        self.rect: pygame.Rect = self.image.get_rect(bottom=gnd_rect.top, left=100)

        self.jump_surf: pygame.Surface = pygame.image.load(
            'graphics/player/jump.png').convert_alpha()
        self.gravity: int = 0

        try:
            self.jump_sound: pygame.mixer.Sound = pygame.mixer.Sound('audio/jump.mp3')
            self.jump_sound.set_volume(0.2)
        except:
            pass
        return

    def animate(self) -> None:
        if self.rect.bottom < gnd_rect.top:
            self.image = self.jump_surf
        else:
            self.i += 0.15
            if (self.i >= len(self.frames)):
                self.i = 0
            self.image = self.frames[int(self.i)]
        return

    def jump(self) -> None:
        # Jumping the character when space key is pressed and player is on ground
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and (self.rect.bottom >= gnd_rect.top):
            try:
                self.jump_sound.play()
            except:
                pass
            self.gravity = -20
        self.gravity += 1
        self.rect.y += self.gravity
        if (self.rect.bottom >= gnd_rect.top):
            self.rect.bottom = gnd_rect.top
        return

    def update(self):
        self.animate()
        self.jump()


# PARENT ENEMY SPRITE CLASS with all methods
class Enemy(pygame.sprite.Sprite):
    def __init__(self, *frames) -> None:
        super().__init__()
        self.frames: list[pygame.Surface] = list(frames)
        self.i: int = 0
        try:
            self.image: pygame.Surface = self.frames[self.i]
        except IndexError:
            raise AttributeError("Add image surfaces as frames for the Enemy.")
        self.rect: pygame.Rect = self.image.get_rect(
            bottom=gnd_rect.top, right=randint(WIDTH, WIDTH + 100))
        self.initial_speed: float = 1.0
        self.speed = self.initial_speed

    def move(self) -> None:
        self.rect.x -= 5 * self.speed
        if self.rect.right <= 0:
            self.kill()
        return

    def animate(self) -> None:
        self.i += 0.05 * self.speed
        if (self.i >= len(self.frames)):
            self.i = 0
        self.image = self.frames[int(self.i)]
        return

    def update(self) -> None:
        self.move()
        self.animate()
        self.speed = self.initial_speed + 0.1 * int(score / 10)
        return

# Snail Sprite


class Snail(Enemy):
    def __init__(self) -> None:
        super().__init__(
            pygame.image.load('graphics/snail/snail1.png').convert_alpha(),
            pygame.image.load('graphics/snail/snail2.png').convert_alpha(),
        )
        self.initial_speed = randint(10, 13) / 10
        return

# Fly Sprite


class Fly(Enemy):
    def __init__(self) -> None:
        super().__init__(
            pygame.image.load('graphics/fly/fly1.png').convert_alpha(),
            pygame.image.load('graphics/fly/fly2.png').convert_alpha(),
        )
        self.rect.bottom = gnd_rect.top - 100
        self.initial_speed = randint(15, 17) / 10
        return


def main():
    # Game Title in Window
    pygame.display.set_caption("Pixel Runner")

    # Player Sprite
    player = get_player_sprite()

    # Enemy Sprites & Spawn Timer
    enemies = pygame.sprite.Group()
    spawn_event = pygame.USEREVENT + 1
    global score

    # Game Over and Start Screen Image
    global player_stand
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Game Title
    title_font = pygame.font.Font('font/pixeltype.ttf', 100)
    title_txt = title_font.render("PIXEL RUNNER", False, (111, 196, 169))
    title_rect = title_txt.get_rect(centerx=WIDTH // 2, top=player_stand_rect.bottom + 10)

    # Score Font
    score_font = pygame.font.Font('font/pixeltype.ttf', 50)

    # Instruction to Start
    instruct_txt = score_font.render("Press ENTER to play.", False, 'Black')
    instruct_rect = instruct_txt.get_rect(centerx=WIDTH // 2, top=title_rect.bottom)

    # Background Music
    try:
        bg_music = pygame.mixer.Sound('audio/music.wav')
        bg_music.set_volume(0.1)
        bg_music.play(loops=-1)
    except:
        pass

    # Game Loop
    global start_time
    game_active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Spawning Enemies
            if event.type == spawn_event:
                enemies.add(choice((Snail(),
                                    Snail(),
                                    Fly(),
                                    )))

        if game_active:
            # GAMEPLAY
            screen.blit(sky_surf, (0, 0))
            screen.blit(gnd_surf, gnd_rect)

            player.draw(screen)
            player.update()
            enemies.draw(screen)
            enemies.update()

            # Calculate score only when game is active
            score = get_score(start_time)
            if score == 0:
                INTERVAL = 1500
                pygame.time.set_timer(spawn_event, INTERVAL)
            if score == 80:
                INTERVAL = 700
                pygame.time.set_timer(spawn_event, INTERVAL)

            # Check for collisions
            if collision(player, enemies):
                game_active = False
                enemies.empty()
        else:
            # GAME OVER
            screen.fill((94, 129, 162))
            screen.blit(title_txt, title_rect)
            screen.blit(player_stand, player_stand_rect)
            screen.blit(instruct_txt, instruct_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                start_time = pygame.time.get_ticks() // 1000
                player.sprite.rect.bottom = gnd_rect.top
                player.sprite.gravity = 0
                enemies.empty()
                game_active = True

        txt_surf = score_font.render(f"Score: {score}", False, 'Black')
        txt_rect = txt_surf.get_rect(centerx=WIDTH // 2, top=50)
        screen.blit(txt_surf, txt_rect)

        pygame.display.update()
        clock.tick(FPS)
    return


def get_score(start_time=0):
    if (start_time < 0):
        raise ValueError("Start time must be greater than or equal 0.")
    try:
        return pygame.time.get_ticks() // 1000 - start_time
    except TypeError:
        raise ValueError("Start time must be an integer.")


def get_player_sprite():
    play_grp = pygame.sprite.GroupSingle()
    play_grp.add(Player())
    return play_grp


def collision(spritegrpsingle: pygame.sprite.GroupSingle, spritegrp: pygame.sprite.Group):
    return bool(pygame.sprite.spritecollide(spritegrpsingle.sprite, spritegrp, False))


if __name__ == "__main__":
    main()
