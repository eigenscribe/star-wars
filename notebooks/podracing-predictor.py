import random

track_length = 100 # Total length of track
obstacles = [random.randint(10, 90) for _ in range(5)] # Random obstacle positions [length]
speed_boosts = [random.randint(10, 90) for _ in range(3)] # Random speed boost positions [length/time]


print("Obstacles: ", obstacles)
print("Speed Boosts: ", speed_boosts)

def force_prediction(outcome):
    if outcome == "success":
        print("Anakin senses victory through the Force!")
        return "aggressive" # Take risks
    else:
        print("Anakin senses a disturbance in the Force...")
        return "cautious" # Play it safe
    
def podrace(strategy):
    position = 0
    time = 0
    
    print(f"Starting podrace with {strategy} strategy...")
    while position < track_length:
        # Simulate movement
        move = random.randint(5, 15) if strategy == "aggressive" else random.randint(3, 10)
        position += move
        time += 1
        
        # Check for obstacles
        if position in obstacles:
            print(f"Potential collision with an obstacle at position {position}! Slowing down...")
            position -= 5 if strategy == "aggressive" else 2
            
        # Check for clear path for speed boost
        if position in speed_boosts:
            print(f"Clear path for speed boost at position {position}! Speeding up...")
            position += 10
            
        # Print current status
        print(f"Current position: {position}, Time: {time}")
        
    # Determine outcome
    outcome = "success" if time < 15 else "fail" 
    print(f"Podrace finished! Outcome: {outcome}")
    return outcome

outcome = podrace("neutral")
strategy = force_prediction(outcome)
final_outcome = podrace(strategy)

import statistics
from scipy import stats

def podrace_time(strategy, obstacles, speed_boosts):
    position = 0
    time = 0
    track_length = 100
    while position < track_length:
        move = random.randint(5, 15) if strategy == "aggressive" else random.randint(3, 10)
        position += move
        time += 1
        
        if position in obstacles:
            if strategy == "cautious":
                position -= 5
            else:
                position -= 2
            
        if position in speed_boosts:
            if strategy == "aggressive":
                position += 10
            else:
                position += 5
    return time

def simulate_races(rounds=1000):
    times_no_strategy = []
    times_retro_strategy = []
    
    for _ in range(rounds):
        # Generate random obstacles and speed boosts for each race
        osbstacles = [random.randint(10, 90) for _ in range(5)]
        speed_boosts = [random.randint(10, 90) for _ in range(3)]
        
        # No strategy run: neutral, simulate time directly 
        neutral_time = podrace_time("neutral", obstacles, speed_boosts)
        times_no_strategy.append(neutral_time)
        
        # Determine outcome to pick strategy for retrocausal approach
        outcome = "success" if neutral_time < 15 else "fail"
        strategy = force_prediction(outcome) # aggressive or cautious 
        
        # Run race with retrocausal strategy
        retro_time = podrace_time(strategy, obstacles, speed_boosts)
        times_retro_strategy.append(retro_time)
        
    # Calculate mean and std devs 
    mean_no_strategy = statistics.mean(times_no_strategy)
    mean_retro_strategy = statistics.mean(times_retro_strategy)
    std_no_strategy = statistics.stdev(times_no_strategy)
    std_retro_strategy = statistics.stdev(times_retro_strategy)
    
    # Run independent t-test
    t_stat, p_value = stats.ttest_ind(times_no_strategy, times_retro_strategy)
    
    print(f"\nAfter {rounds} simulated races:")
    print(f"No Strategy - Mean Time: {mean_no_strategy:.2f}, Std Dev: {std_no_strategy:.2f}")
    print(f"Retro Strategy - Mean Time: {mean_retro_strategy:.2f}, Std Dev: {std_retro_strategy:.2f}")
    print(f"T-test: t = {t_stat:.3f}, p = {p_value:.3f}")
    
    if p_value < 0.05:
        print("Significant difference between strategies!")
    else:
        print("No significant difference detected.")

# Run the simulation
simulate_races(1000)