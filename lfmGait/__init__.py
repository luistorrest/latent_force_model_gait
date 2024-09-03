from data.C3DReading import * 
from visualization.TimeSeriesPlotter import *

if __name__ == '__main__':

    file_path = '/home/luistorrest/Documents/UdeA/Thesis/Repo/test_code/07_01.c3d'
    handler = C3DFileHandler(file_path)
    point_data, labels = handler.read_c3d_file()

    output_csv = '/home/luistorrest/Documents/UdeA/Thesis/Repo/test_code/07_01_converted.csv'
    converter = C3DToCSVConverter(point_data, labels, output_csv)
    converter.convert_to_csv()

    plotter = TimeSeriesPlotter(output_csv, frame_rate=120)
    plotter.plot_point_time_series(point_name=labels[10])
