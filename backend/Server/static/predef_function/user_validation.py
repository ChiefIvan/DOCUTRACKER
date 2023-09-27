from re import compile


class EntryValidator:
    def __init__(self, entries: dict):
        self.entries = entries

    def validate(self) -> bool | dict:
        length_error: str = "Your Firstname must be greater than 3 Characters"
        error_responses: dict = {
            "name": "Username Entry is Empty!",
            "email": "Email Entry is Empty!",
            "password": "Password Entry is Empty!",
        }

        for key, value in self.entries.items():
            if value != None:
                if len(value) == 0:
                    return {"error": error_responses.get(key, "Password Confirmation is Empty!")}

        if self.entries["name"] != None:
            if len(self.entries["name"]) < 4:
                return {"error": length_error}

        return True


class EmailValidator:
    def __init__(self, entries: dict):
        self.entries = entries

    def validate(self) -> bool | dict:
        email_format_error: str = "Your Email Format is Invalid."
        pattern = compile(
            r'^[a-zA-Z0-9._%+-]{5,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        if not pattern.match(self.entries["email"]):
            return {"error": email_format_error}

        return True


class PasswordValidator:
    def __init__(self, entries: dict):
        self.entries = entries

    def validate(self) -> bool | dict:
        length_error: str = "Your Password must be greater than 7 Characters!"
        combination_error: str = "Your Password have atleast 1 Uppercase, 1 Lowercase and a Number"
        password_error: str = "Your Password and Confirmation Password must be the same!"
        pattern = compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$")

        for key, value in self.entries.items():
            if value != None:
                if key == "password":
                    if len(value) < 8:
                        return {"error": length_error}

                    if not pattern.match(value):
                        return {"error": combination_error}

        if self.entries["confirm_password"] != None and self.entries["password"] != None:
            if self.entries["password"] != self.entries["confirm_password"]:
                return {"error": password_error}

        return True


class UserValidation:
    def __init__(self, entries: dict):
        self.validators = [
            EntryValidator(entries),
            EmailValidator(entries),
            PasswordValidator(entries)
        ]

    def validate_user(self) -> bool | dict:
        for validator in self.validators:
            response = validator.validate()
            if isinstance(response, dict):
                return response

        return True
