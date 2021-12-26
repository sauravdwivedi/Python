import unittest
import NetworkSpeed as ns

class DeviceTestCase(unittest.TestCase):
    """Tests for 'NetworkSpeed.py'."""
    
    def test_device_stations(self):
        """Do lists like '[0, 0], [[0, 0, 9], [20, 20, 6]]' work?"""
        device = [0, 0]
        stations = [[0, 0, 9], [20, 20, 6]]
        result = ns.best_network(device, stations)
        self.assertEqual(result, 'Best network station for device at (0, 0) is (0, 0) with speed 81.0')
        
if __name__ == '__main__':
    unittest.main()
