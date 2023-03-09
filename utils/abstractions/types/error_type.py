

class Error(dict):
    KEY_CHOICES = ['message', 'code']
    VALUE_CODE_CHOICES = []
    
    def __init__(self, message: str, code: int = 500):
        print(type(message), 'msg')
        print(type(code), 'code')
        if (not isinstance(message, str)) or (not isinstance(code, int)):
            raise TypeError
            
        self['message'] = message
        self['code'] = code

    def __setitem__(self, key: str, value = None):
        key, value = self.__item_validation(key, value)
        super().__setitem__(key.lower(), value)
    
    @classmethod
    def __item_validation(cls, key, value):
        key = cls.__key_validation(key)
        if key == 'code':
            cls.__value_validation(value, int)
        else:
            cls.__value_validation(value, str)
        return key, value
    
    @classmethod        
    def __key_validation(cls, key):
        key = key.lower()
        if key not in cls.KEY_CHOICES:
            return ValueError
        return key
    
    @classmethod
    def __value_validation(cls, value, target_type):
        if not isinstance(value, target_type):
            raise TypeError(f'Validation error - {value} should be {target_type}!')
            