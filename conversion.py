class Currency_Codes():
    def __init__(self):
        self.codes = self.read_codes("codes.txt")
    
    def read_codes(self, filename):
        """Read file and return each currency code"""
        f = open(filename)
        codes = [c.strip() for c in f]
        f.close()
        return codes

    def check_code(self, code):
        """Check if currency code is a valid code"""
        code_exists = code.upper() in self.codes
        return code_exists

