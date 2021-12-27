import unittest
import NetworkSpeed as ns

class DeviceTestCase(unittest.TestCase):
    """Tests for 'NetworkSpeed.py'."""
    
    def test_device_one_stations(self):
        """Do stations like '[[0, 0, 9], [20, 20, 6]]' work 
        for device at '[0, 0]'?"""
        device = [0, 0]
        stations = [[0, 0, 9], [20, 20, 6]]
        result = ns.best_network(device, stations)
        self.assertEqual(
            result, 
            'Best network station for device at (0, 0) is (0, 0) with speed 81.0'
            )
    
    def test_device_two_stations(self):
        """Do stations like '[[0, 0, 9], [20, 20, 6]]' work 
        for device at '[100, 100]'"""
        device = [100, 100]
        stations = [[0, 0, 9], [20, 20, 6]]
        result = ns.best_network(device, stations)
        self.assertEqual(
            result, 
            'No network station within reach for device at (100, 100)'
            )
        
    def test_station_speed(self):
        """Does station like '[0, 0, 9]' work for device at '[0, 0]'"""
        station = [0, 0, 9]
        device_x = 0
        device_y = 0
        station_obj = ns.Station(station, device_x, device_y)
        result = station_obj.station_speed()
        self.assertEqual(result, 81.0)
        
if __name__ == '__main__':
    unittest.main()
