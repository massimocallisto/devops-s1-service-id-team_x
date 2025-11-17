import unittest
from status_report import get_status, add_firma_digitale, add_autenticazione

class TestStatusReport(unittest.TestCase):
    def test_add_firma_digitale(self):
        service = add_firma_digitale()
        self.assertEqual(service["service"], "firma digitale")
        self.assertEqual(service["author"], "mario rossi")
        self.assertEqual(len(service), 2)

    def test_add_autenticazione(self):
        service = add_autenticazione()
        self.assertEqual(service["service"], "autenticazione")
        self.assertEqual(service["author"], "luigi verdi")
        self.assertEqual(len(service), 2)

    def test_get_status(self):
        result = get_status()
        
        # Test the base structure
        self.assertEqual(result["version"], "1.0.0")
        self.assertEqual(result["build_date"], "2024-01-01T00:00:00Z")
        self.assertEqual(result["status"], "regular")
        
        # Test services array
        services = result["services"]
        self.assertEqual(len(services), 2)
        
        # Test first service (firma digitale)
        self.assertEqual(services[0]["service"], "firma digitale")
        self.assertEqual(services[0]["author"], "mario rossi")
        
        # Test second service (autenticazione)
        self.assertEqual(services[1]["service"], "autenticazione")
        self.assertEqual(services[1]["author"], "luigi verdi")

    def test_status_structure(self):
        result = get_status()
        expected_keys = {"version", "build_date", "status", "services"}
        self.assertEqual(set(result.keys()), expected_keys)
        
        # Test that services is a list
        self.assertIsInstance(result["services"], list)
        
        # Test that all required fields are strings (except services)
        self.assertIsInstance(result["version"], str)
        self.assertIsInstance(result["build_date"], str)
        self.assertIsInstance(result["status"], str)

if __name__ == '__main__':
    unittest.main()
