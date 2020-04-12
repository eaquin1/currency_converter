from flask import Flask, session, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from conversion import Currency_Codes
from decimal import Decimal

currency_codes = Currency_Codes()
currency_rates = CurrencyRates()
currency_symbols = CurrencyCodes()

app = Flask(__name__)
app.config['SECRET_KEY'] = "shhhh"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def render_home():
    """Render the homepage"""
    return render_template("form.html", currencies=currency_codes.codes)

@app.route('/currencycodes', methods=["POST"])
def check_currency_codes():
    """Validate form info"""
    from_currency = request.form["from_currency"].upper()
    to_currency = request.form["to_currency"].upper()
    amount = request.form["amount"]
    
    session['from_currency'] = from_currency
    session['to_currency'] = to_currency
    session['amount'] = amount
    
    from_currency_valid = currency_codes.check_code(from_currency)
    to_currency_valid = currency_codes.check_code(to_currency)
    
    if from_currency_valid == False or to_currency_valid == False:
        flash('Please enter a valid currency code', 'danger')
        return redirect('/')
    
    if not amount.isdigit():
        flash('Please enter a valid number in the amount form', 'danger')
        return redirect('/')

    return redirect('/result')

@app.route('/result')
def render_result():
    """Show converted amount"""
    from_currency = session['from_currency']
    to_currency = session['to_currency']
    amount = session['amount']

    converted_amount = currency_rates.convert(from_currency, to_currency, Decimal(amount)).quantize(Decimal("1.00"))
    symbol = currency_symbols.get_symbol(to_currency)
    
    return render_template("result.html", converted_amount=converted_amount, symbol=symbol, to_currency=to_currency)