# test_monitorurn.py
"""
Tests for MonitorUrn module.
"""

import unittest
from monitorurn import MonitorUrn

class TestMonitorUrn(unittest.TestCase):
    """Test cases for MonitorUrn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MonitorUrn()
        self.assertIsInstance(instance, MonitorUrn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MonitorUrn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
