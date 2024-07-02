import numpy as np

# Function to calculate utility
def calculate_utility(RSSI):
    return np.exp(RSSI)  # Example utility function, can be adjusted based on requirements

# Function to select optimal channel
def select_channel(RSSI, current_strategy, other_strategies):
    max_utility = -np.inf
    optimal_channel = None
    
    for channel in range(len(current_strategy)):
        new_strategy = current_strategy.copy()
        new_strategy[channel] = 1
        utility = calculate_utility(RSSI[channel])
        
        for other_strategy in other_strategies:
            if utility < calculate_utility(RSSI[channel]) * other_strategy[channel]:
                break
        else:
            if utility > max_utility:
                max_utility = utility
                optimal_channel = channel
    
    return optimal_channel

# Example input data
num_sensors = int(input("Enter Number of Sensors: "))
num_channels = int(input("Enter Number of Channels: "))
RSSI_data = np.random.rand(num_sensors, num_channels)  # Example RSSI data, replace with actual data

# Initialization
current_strategies = np.zeros((num_sensors, num_channels))
for sensor in range(num_sensors):
    current_strategies[sensor, np.random.randint(num_channels)] = 1

# Iterative channel selection
while True:
    for sensor in range(num_sensors):
        for channel in range(num_channels):
            current_strategy = current_strategies[sensor].copy()
            current_strategy[channel] = 1
            new_channel = select_channel(RSSI_data[sensor], current_strategy, np.delete(current_strategies, sensor, axis=0))
            if new_channel is not None:
                current_strategies[sensor] = np.zeros(num_channels)
                current_strategies[sensor, new_channel] = 1
    else:
        break

print("Optimal channel selection strategies:")
print(current_strategies)


