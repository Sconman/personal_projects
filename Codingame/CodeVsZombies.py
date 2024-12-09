import math
# very very scuffed algorithim
# in my head i want this program to do a sort of minimax algorithim  
# where it goes through the future scenarios given a move and decides which one gives the most points
# but alas i have no idea how to do that right now and i have finals soon so im just happy I got the 40k achievement  
class CodeVsZombies:
    def __init__(self):
        pass

    def distance(self, x1, y1, x2, y2):
        """Calculate Euclidean distance."""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def humans_under_threat(self, zombies, humans):
        """Identify the most threatened human."""
        threat_levels = {human: float("inf") for human in humans}

        for zombie in zombies:
            zombie_x, zombie_y, _, _ = zombie
            for human in humans:
                human_x, human_y = human
                dist = self.distance(zombie_x, zombie_y, human_x, human_y)
                threat_levels[human] = min(threat_levels[human], dist)

        # Sort humans by threat level (lowest distance first)
        return sorted(threat_levels.items(), key=lambda x: x[1])

    def cluster_kill_score(self, ash_x, ash_y, zombies, human_count):
        """
        Calculate how many zombies Ash can kill in one move.
        Return the number of zombies and their combined score.
        """
        kills = []
        for zombie in zombies:
            zombie_x, zombie_y, _, _ = zombie
            if self.distance(ash_x, ash_y, zombie_x, zombie_y) <= 2000:
                kills.append(zombie)

        # Calculate score for multiple kills
        kills_count = len(kills)
        if kills_count == 0:
            return 0, 0  # No zombies can be killed
        fib = [1, 2]
        while len(fib) < kills_count + 2:
            fib.append(fib[-1] + fib[-2])  # Extend Fibonacci series

        # Compute score
        score = sum(fib[i] * (human_count ** 2) * 10 for i in range(kills_count))
        return kills_count, score

    def play_turn(self, ash_x, ash_y, humans, zombies):
        """
        Determine the best move for Ash.
        """
        # Step 1: Find the most threatened human
        most_threatened = self.humans_under_threat(zombies, humans)
        target_human = most_threatened[0][0]  # Human with the lowest threat distance

        # Step 2: Find the zombie targeting this human
        target_zombie = None
        min_zombie_distance = float("inf")
        for zombie in zombies:
            zombie_x, zombie_y, _, _ = zombie
            dist_to_human = self.distance(zombie_x, zombie_y, target_human[0], target_human[1])
            if dist_to_human < min_zombie_distance:
                min_zombie_distance = dist_to_human
                target_zombie = zombie

        # Step 3: Check for cluster killing potential
        human_count = len(humans)
        cluster_kills, cluster_score = self.cluster_kill_score(ash_x, ash_y, zombies, human_count)
        if cluster_kills > 1:
            # Move to the center of zombie cluster if it provides a better score
            center_x = sum(z[0] for z in zombies) // len(zombies)
            center_y = sum(z[1] for z in zombies) // len(zombies)
            return center_x, center_y

        # Step 4: Target the zombie threatening the most endangered human
        if target_zombie:
            return target_zombie[0], target_zombie[1]

        # Fallback: Move towards the closest human (lol ik its bad)
        closest_human = min(humans, key=lambda h: self.distance(ash_x, ash_y, h[0], h[1]))
        return closest_human[0], closest_human[1]


# Game loop
game = CodeVsZombies()

while True:
    ash_x, ash_y = [int(i) for i in input().split()]
    human_count = int(input())
    humans = []
    for _ in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append((human_x, human_y))
    zombie_count = int(input())
    zombies = []
    for _ in range(zombie_count):
        zombie_id, zombie_x, zombie_y, next_zombie_x, next_zombie_y = [int(j) for j in input().split()]
        zombies.append((zombie_x, zombie_y, next_zombie_x, next_zombie_y))

    # Compute the "best" move for Ash
    target_x, target_y = game.play_turn(ash_x, ash_y, humans, zombies)
    print(f"{target_x} {target_y}")
