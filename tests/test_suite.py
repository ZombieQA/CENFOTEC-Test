from src.form_functionality import Form

class TestForm:
    def test_001_name_has_more_than_30_chars_message(self):
        """Test case for name with more than 30 characters."""
        form = Form()
        actual_message = form.enter_name("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print("Actual Message:", actual_message)
        assert actual_message == 'name has more than 30 chars'

    def test_002_name_invalid_length_message(self):
        """Test case for name with invalid length."""
        form = Form()
        actual_message = form.enter_name("ab")
        assert actual_message == 'Invalid value'

    def test_003_valid_name(self):
        """Test case for valid name."""
        form = Form()
        actual_message = form.enter_name("John Doe")
        assert actual_message == 'Your name is John Doe'

    def test_004_invalid_age_message(self):
        """Test case for invalid age."""
        form = Form()
        actual_message = form.enter_age("12")
        assert actual_message == 'Invalid value for field age'
        
from src.login_module import Login

class TestLogin:
    def test_001_validate_user_with_valid_email(self):
        login = Login()
        login.enter_user("example@mail.com")
        assert login.validate_user() == 'Valid email format'

    def test_002_validate_user_with_empty_email(self):
        login = Login()
        login.enter_user("")
        assert login.validate_user() == 'Email is mandatory'

    def test_003_validate_user_with_invalid_email(self):
        login = Login()
        login.enter_user("user@invalid")
        assert login.validate_user() == 'Invalid email'

    def test_004_validate_user_with_wrong_email(self):
        login = Login()
        login.enter_user("user@example.com")
        assert login.validate_user() == 'Valid email format'

    def test_005_validate_password_with_valid_password(self):
        login = Login()
        login.enter_password("pass1234")
        assert login.validate_password() == 'Valid password'

    def test_006_validate_password_with_empty_password(self):
        login = Login()
        login.enter_password("")
        assert login.validate_password() == 'password is mandatory'

    def test_007_validate_password_with_invalid_password(self):
        login = Login()
        login.enter_password("1234")
        assert login.validate_password() == 'Invalid password'

    def test_008_login_with_valid_credentials(self):
        login = Login()
        login.enter_user("example@mail.com")
        login.enter_password("pass1234")
        assert login.login() == 'Login success!'

    def test_009_login_with_invalid_email(self):
        login = Login()
        login.enter_user("user@invalid")
        login.enter_password("pass1234")
        assert login.login() == 'Invalid credentials'

    def test_010_login_with_invalid_password(self):
        login = Login()
        login.enter_user("example@mail.com")
        login.enter_password("wrongpassword")
        assert login.login() == 'Invalid credentials'

    def test_011_login_with_both_invalid(self):
        login = Login()
        login.enter_user("user@invalid")
        login.enter_password("wrongpassword")
        assert login.login() == 'Invalid credentials'