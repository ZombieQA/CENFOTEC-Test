from src.form_functionality import Form

class TestExamples:
    def test_001_name_has_more_than_30_chars_message(self):
        """Test case for name with more than 30 characters."""
        form = Form()
        actual_message = form.enter_name("aaaaaaaaaaaaaaaaaaaaaaaaa")
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
