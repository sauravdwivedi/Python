"""Write a program to find most suitable (with highest non-zero speed)
network station for a device a point (x, y). A network station is located 
at (p, q) and had a reach r. For a device at (x, y), the network station's 
speed is given as:
    speed = (reach - device's distance from network station)**2
    if distance > reach, speed = 0
    
Input: 
devices at (x, y): (0, 0), (100, 100), ...
stations at (p, q) with reach r: (0, 0, 9), (20, 20, 6), ..."""

import math

class Station:
    """Class to model stations for a device"""
    def __init__(self, station, device_x, device_y):
        """Initialize attributes to describe a station."""
        self.station = station
        self.device_x = device_x
        self.device_y = device_y
        
    def station_speed(self):
        #(p, q) coordinates for a station and its reach
        station_p = self.station[0]
        station_q = self.station[1]
        reach = self.station[2]
        distance = math.sqrt(((self.device_x - station_p) ** 2) 
            + ((self.device_y - station_q) ** 2))
        if distance > reach:
            speed = 0
        else:
            speed = (reach - distance) ** 2
        return round(speed, 2)
        
        
def best_network(device, stations):
    """Method to return best network with given speed or find none"""
    #(x, y) coordinates for a device 
    device_x = device[0]
    device_y = device[1]
    speeds = [
        Station(station, device_x, device_y).station_speed() 
        for station in stations
        ] 
    result = f""
    for station in stations:
        station_obj = Station(station, device_x, device_y)
        if max(speeds) == 0:
            result = f"No network station within reach for device at " \
                + f"({station_obj.device_x}, {station_obj.device_y})"
        elif station_obj.station_speed() == max(speeds):
            result = f"Best network station for device at " \
                + f"({station_obj.device_x}, {station_obj.device_y}) " \
                + f"is ({station_obj.station[0]}, {station_obj.station[1]})" \
                + f" with speed {station_obj.station_speed()}"
    return result

if __name__ == '__main__':
    input_file_stations = 'NetworkSpeed_input_stations.txt'
    input_file_devices = 'NetworkSpeed_input_devices.txt'
    output_file = 'NetworkSpeed_output.txt'
    try:
        with open(input_file_stations) as f:
            lines_stations = f.readlines()
        with open(input_file_devices) as f:
            lines_devices = f.readlines()
    except OSError as error:
        print("File {:s} failed".format(error.filename))         
    else:
        stations = [
            list(map(int, line_string.rstrip().split())) 
            for line_string in lines_stations
            ]   
        devices = [
            list(map(int, line_string.rstrip().split())) 
            for line_string in lines_devices
            ]
        for device in devices:
            with open(output_file, 'a') as f:
                f.write(best_network(device, stations) + '\n')
            print(best_network(device, stations))
        print(f"Output saved in file {output_file}!")
