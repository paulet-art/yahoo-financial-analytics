class ResponseValidator:

    @staticmethod
    def validate(data: dict):

        if not data:
            return False, "Empty response received from API."
        
        if "Error Message" in data:
            return False, data['Error Message']
        
        if "Note" in data:
            return False, "Rate limit exceeded. Please wait and try again later."
        
        if "Time Series (Daily)" not in data:
            return False, "Unexpected response format."
        
        return True, "Response is valid."
