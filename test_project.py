import pytest
from project import *


def test_get_score() -> None:
    assert type(get_score()) == int
    assert get_score(0) == pygame.time.get_ticks() // 1000
    with pytest.raises(ValueError):
        assert get_score(-15)
        assert get_score('15')


def test_get_player_sprite() -> None:
    assert len(get_player_sprite()) == 1
    assert type(get_player_sprite()) == pygame.sprite.GroupSingle
    assert type(get_player_sprite().sprite) == Player


def test_collision() -> None:
    sprite1 = pygame.sprite.GroupSingle()
    sprite1.add(Player())
    sprite2 = pygame.sprite.Group()
    sprite2.add(Snail())
    sprite2.sprites()[0].rect.x = sprite1.sprites()[0].rect.left
    sprite2.add(Fly())
    sprite2.sprites()[1].rect.x = sprite1.sprites()[0].rect.right + 10
    assert collision(sprite1, sprite2) == True
