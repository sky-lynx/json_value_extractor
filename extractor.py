# importing modules
import json

class getter:
    
    # setting values to object
    def __init__(self, json_string, json_key):
        self.string_ = json_string
        self.key = json_key
        self.value_ = ''
    
    # extracts the value
    def value(self):
        try:
            self.value_ = self.string_.get(self.key)
            if self.value_ is not None:
                return self.value_
            else:
                return None
        except:
            return None

json_acceptable_string = '{}' # put in your json string here
formatted_string = json.loads(json_acceptable_string)
get_key = getter(formatted_string, 'some_key') # replace 'some_key' with your key
                                        
print(get_key.value())
