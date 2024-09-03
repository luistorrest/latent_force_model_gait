import csv
import c3d
import numpy as np

class C3DFileHandler:
    """
    A class to handle the reading and processing of C3D files.

    Attributes:
    -----------
    file_path : str
        The path to the C3D file to be read.
    point_data : np.ndarray
        A numpy array containing the point data from the C3D file.
    labels : list
        A list of labels for the points in the C3D file.
    frame_rate : float
        The frame rate of the C3D file.
    """

    def __init__(self, file_path):
        """
        Initializes the C3DFileHandler with the given file path.

        Parameters:
        -----------
        file_path : str
            The path to the C3D file.
        """
        self.file_path = file_path
        self.point_data = None
        self.labels = None
        self.frame_rate = None

    def read_c3d_file(self):
        """
        Reads the C3D file and extracts point data, labels, and frame rate.

        Returns:
        --------
        tuple:
            A tuple containing the point data (np.ndarray) and labels (list).
        """
        with open(self.file_path, 'rb') as handle:
            reader = c3d.Reader(handle)

            # Get header information
            self.frame_rate = reader.point_rate
            self.labels = reader.point_labels
            frames = [points for _, points, _ in reader.read_frames()]

            # Convert to numpy array for easier handling
            self.point_data = np.array(frames)

            # Display summary information
            self._display_summary(reader)

        return self.point_data, self.labels

    def _display_summary(self, reader):
        """
        Displays a summary of the C3D file, including point count, frame count, 
        frame rate, and sample point data.

        Parameters:
        -----------
        reader : c3d.Reader
            The C3D reader object used to extract the data.
        """
        print(f"Header information:")
        print(f"Point count: {reader.point_used}")
        print(f"Frame count: {reader.last_frame - reader.first_frame + 1}")
        print(f"Frame rate: {self.frame_rate}")
        print(f"First frame: {reader.first_frame}")
        print(f"Last frame: {reader.last_frame}")
        print(f"\nPoint labels: {self.labels}")
        print(f"\nPoint data shape: {self.point_data.shape}")
        print("Point data includes: X, Y, Z coordinates")

        # Example: Print the first 5 frames of data for the first marker
        print(f"\nFirst 5 frames of data for marker '{self.labels[0]}':")
        for frame in range(5):
            x, y, z = self.point_data[frame, 0, :3]
            print(f"Frame {frame}: X={x:.2f}, Y={y:.2f}, Z={z:.2f}")


class C3DToCSVConverter:
    """
    A class to convert C3D file data to a CSV format.

    Attributes:
    -----------
    point_data : np.ndarray
        A numpy array containing the point data from the C3D file.
    labels : list
        A list of labels for the points in the C3D file.
    output_file : str
        The path to the output CSV file.
    """

    def __init__(self, point_data, labels, output_file):
        """
        Initializes the C3DToCSVConverter with the point data, labels, and output file path.

        Parameters:
        -----------
        point_data : np.ndarray
            The point data extracted from the C3D file.
        labels : list
            The labels corresponding to the points in the C3D file.
        output_file : str
            The path to the output CSV file.
        """
        self.point_data = point_data
        self.labels = labels
        self.output_file = output_file

    def convert_to_csv(self):
        """
        Converts the C3D point data to a CSV format and writes it to the specified output file.
        """
        num_frames, num_points, _ = self.point_data.shape
        
        with open(self.output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            header = ['Frame']
            for label in self.labels:
                header.extend([f'{label}_X', f'{label}_Y', f'{label}_Z'])
            writer.writerow(header)
            
            # Write data
            for frame in range(num_frames):
                row = [frame]
                for point in range(num_points):
                    row.extend(self.point_data[frame, point, :3])
                writer.writerow(row)
        
        print(f"CSV file has been created: {self.output_file}")
