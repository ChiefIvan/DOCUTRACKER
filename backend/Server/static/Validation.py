import re

class Validation :
    def __init__(self, entries: dict) :
        self.entries = entries        
    
    def empty_validation(self) -> bool | dict :
        invalid_length_error: str = "Your firstname must be greater than 3 characters"
        
        EMPTY_ERROR_MESSAGES: dict= {
            "name" : "Username entry is empty!",
            "email" : "Email entry is empty!",
            "password" : "Password entry is empty!",
        }
        
        for key, value in self.entries.items() :
            if value != None:
                if len(value) == 0 :
                    return {"error": EMPTY_ERROR_MESSAGES.get(key, "Password confirmation is empty!")}
        
        if self.entries["name"] != None:
            if len(self.entries["name"]) < 4 :
                return {"error": invalid_length_error}
            
        return True
    
    def password_validation(self) -> bool | dict:
        length_error: str = "Your password must be greater than 7 characters!"
        combination_error: str = "Your password have atleast 1 Uppercase, 1 Lowercase and a number"
        unequal_password_error: str = "Your password and confirmation password must be the same!"
        pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$")
        
        for key, value in self.entries.items() :
            if value != None:
                if key == "password" :
                    if len(value) < 8 :
                        return {"error": length_error}
                
                    if not pattern.match(value) :
                        return {"error": combination_error}
        
        if self.entries["confirm_password"] != None and self.entries["password"] != None:
            if self.entries["password"] != self.entries["confirm_password"] :
                return {"error": unequal_password_error}
                
        return True


class Validated(Validation) :
    def __init__(self, entries: dict) :
        super().__init__(entries)
        
        self.VALID = (
            self.empty_validation,
            self.password_validation
        )
        
    def valid(self) -> bool | dict :
        for validity in self.VALID :
            if isinstance(response:=validity(), dict) :
                return response
            
        return True
    