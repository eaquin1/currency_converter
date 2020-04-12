from app import app
from conversion import Currency_Codes
from flask import session
from unittest import TestCase


# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
currency_codes = Currency_Codes()
#currency_rates = CurrencyRates()

class FlaskTests(TestCase):
    def setUp(self):
        """Before each test"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        """Test if home page renders"""
        with self.client:
            resp = self.client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)
    
    def test_check_currency(self):
        """Test if currency code is valid"""
        with self.client:
            with self.client.session_transaction() as sess:
                sess['from_currency'] = "CAD"
            
            self.assertTrue(currency_codes.check_code(sess['from_currency']))

    def test_render_result(self):
        """Test if currency is properly converted"""
        with self.client:
            with self.client.session_transaction() as sess:
                sess['from_currency'] = "USD"
                sess['to_currency'] = "USD"
                sess['amount'] = 1

            resp = self.client.get('/result')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p>The result is US$1.00 USD</p>', html)