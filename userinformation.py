class UserInfo:
    def __init__(self, first_name, last_name, email, age=None):
        """
        Initialize a new user with basic information.

        :param first_name: A string representing the user's first name.
        :param last_name: A string representing the user's last name.
        :param email: A string representing the user's email address.
        :param age: An optional integer representing the user's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def full_name(self):
        """
        Return the full name of the user.
        """
        return f"{self.first_name} {self.last_name}"

    def update_email(self, new_email):
        """
        Update the email address of the user.

        :param new_email: The new email address to set.
        """
        self.email = new_email

    def __str__(self):
        """
        Return a string representation of the user information.
        """
        return f"User: {self.full_name()}, Email: {self.email}, Age: {self.age}"


