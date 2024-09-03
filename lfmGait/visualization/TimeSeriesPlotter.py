import pandas as pd
import matplotlib.pyplot as plt

class TimeSeriesPlotter:
    def __init__(self, csv_file, frame_rate):
        self.csv_file = csv_file
        self.frame_rate = frame_rate

    def plot_point_time_series(self, point_name):
        # Read the CSV file
        df = pd.read_csv(self.csv_file)
        
        # Create time array
        time = df['Frame'] / self.frame_rate
        
        # Extract X, Y, Z coordinates for the specified point
        x = df[f'{point_name}_X']
        y = df[f'{point_name}_Y']
        z = df[f'{point_name}_Z']

        # Create the plot
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
        fig.suptitle(f'Time Series for Point: {point_name}')

        # Plot X coordinate
        ax1.plot(time, x)
        ax1.set_ylabel('X Position')
        ax1.grid(True)

        # Plot Y coordinate
        ax2.plot(time, y)
        ax2.set_ylabel('Y Position')
        ax2.grid(True)

        # Plot Z coordinate
        ax3.plot(time, z)
        ax3.set_ylabel('Z Position')
        ax3.set_xlabel('Time (seconds)')
        ax3.grid(True)

        plt.tight_layout()
        plt.show()
