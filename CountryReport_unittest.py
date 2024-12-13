import unittest
from Country_report import city_country_reporter

class cityCountryTestCase(unittest.TestCase):
    def test_CityCountryReport(self):
        report=city_country_reporter('Abuja',"Nigeria")
        self.assertEqual(report,"Abuja,Nigeria")
    
    def test_CityCoutryPopuationReport(self):
        report=city_country_reporter('Lagos',"Nigeria",20000000)
        self.assertEqual(report,"Lagos,Nigeria - population:20000000")

if __name__=='__main__':
    unittest.main()