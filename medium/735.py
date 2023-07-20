from typing import List, Optional


# Clean code solution, obviuously it is pretty slow with heap allocated
# functions and unnecesarry object properties, but at least it is clear)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rights = []
        res = []

        signed_asteroids = [[abs(x), 1 if x > 0 else -1] for x in asteroids]
        self.current_left_asteroid: Optional[int] = None

        def update_current_left(value):
            self.current_left_asteroid = value

        def handle_collision(right, left):
            if right > left:
                rights.append(right)
                update_current_left(None)
            elif right < left:
                update_current_left(left)
            else:
                update_current_left(None)

        def handle_left_asteroid(left_asteroid):
            if len(rights) == 0:
                res.append(-asteroid)
                update_current_left(None)
                return
            prev_right_asteroid = rights.pop()
            handle_collision(prev_right_asteroid, left_asteroid)

        i = 0
        while i < len(signed_asteroids) or self.current_left_asteroid is not None:
            if self.current_left_asteroid is None:
                asteroid, direction = signed_asteroids[i]
                i += 1
                if direction == 1:
                    rights.append(asteroid)
                else:
                    handle_left_asteroid(asteroid)
            else:
                handle_left_asteroid(self.current_left_asteroid)

        if self.current_left_asteroid:
            return res + rights + [self.current_left_asteroid]
        return res + rights
