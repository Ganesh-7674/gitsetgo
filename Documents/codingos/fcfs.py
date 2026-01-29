import matplotlib.pyplot as plt
import random

# Input number of processes
n = int(input("Enter number of processes: "))

# Generate random arrival and burst times
processes = []
for i in range(n):
    arrival = random.randint(0, 5)   # Arrival time 0-5
    burst = random.randint(1, 9)     # Burst time 1-9
    processes.append({'pid': i+1, 'arrival': arrival, 'burst': burst})

# Sort processes by arrival time (FCFS)
processes.sort(key=lambda x: x['arrival'])

# Calculate start, completion, waiting, turnaround times
current_time = 0
for p in processes:
    if current_time < p['arrival']:
        current_time = p['arrival']
    p['start'] = current_time
    p['completion'] = current_time + p['burst']
    p['turnaround'] = p['completion'] - p['arrival']
    p['waiting'] = p['turnaround'] - p['burst']
    current_time = p['completion']

# Display process table
print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
for p in processes:
    print(f"P{p['pid']}\t{p['arrival']}\t{p['burst']}\t{p['waiting']}\t{p['turnaround']}")

# Plot Gantt chart
fig, ax = plt.subplots(figsize=(12, 4))
bar_height = 6
y_position = 10

for p in processes:
    ax.broken_barh([(p['start'], p['burst'])], (y_position, bar_height),
                   facecolors=('tab:blue'), edgecolor='black', linewidth=1.5)
    # Process ID in the middle of the bar
    ax.text(p['start'] + p['burst']/2, y_position + bar_height/2, f"P{p['pid']}",
            ha='center', va='center', color='white', fontweight='bold', fontsize=12)
    # Start time
    ax.text(p['start'], y_position - 1, str(p['start']), ha='center', va='top', fontsize=10)

# Add completion time for last process
ax.text(processes[-1]['completion'], y_position - 1, str(processes[-1]['completion']),
        ha='center', va='top', fontsize=10)

# Labels and formatting
ax.set_ylim(0, 25)
ax.set_xlim(0, max(p['completion'] for p in processes) + 2)
ax.set_xlabel('Time', fontsize=12)
ax.set_yticks([])
ax.set_title('Gantt Chart (FCFS Scheduling)', fontsize=14, fontweight='bold')
ax.grid(True, axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()