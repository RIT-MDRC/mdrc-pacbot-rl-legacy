from typing import Literal, Mapping, Optional

import numpy as np

class GhostAgent:
    def clear_start_path(self) -> None: ...
    @property
    def pos(self) -> Mapping[Literal["current", "next"], tuple[int, int]]: ...

class PacBot:
    def update(self, position: tuple[int, int]) -> None: ...
    @property
    def direction(self) -> int: ...
    @property
    def pos(self) -> tuple[int, int]: ...

class GameState:
    def __init__(self) -> None: ...
    def is_frightened(self) -> bool: ...
    def next_step(self) -> None: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def restart(self) -> None: ...
    def print_ghost_pos(self) -> None: ...
    def frightened_counter(self) -> int: ...
    def state(self) -> int: ...
    @property
    def pacbot(self) -> PacBot: ...
    @property
    def red(self) -> GhostAgent: ...
    @property
    def pink(self) -> GhostAgent: ...
    @property
    def orange(self) -> GhostAgent: ...
    @property
    def blue(self) -> GhostAgent: ...
    @property
    def pellets(self) -> int: ...
    @property
    def power_pellets(self) -> int: ...
    @property
    def cherry(self) -> bool: ...
    @property
    def score(self) -> int: ...
    @property
    def play(self) -> bool: ...
    @property
    def lives(self) -> int: ...

def create_obs_semantic(game_state: GameState) -> np.ndarray: ...
def get_heuristic_value(
    game_state: GameState, pos: tuple[int, int]
) -> Optional[float]: ...
def get_action_heuristic_values(game_state: GameState) -> list[Optional[float]]: ...
