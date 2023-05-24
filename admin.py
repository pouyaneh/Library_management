class Admin:
    def __init__(self, id, name, password, education, expertise):
        if len(str(id)) != 10 or str(id)[9] != '1':
            raise ValueError("Invalid ID")
        self.id = id
        self.name = name
        self.password = password
        self.education = education
        self.expertise = expertise

    def print_info(self):
        print("Admin ID:", self.id)
        print("Name:", self.name)
        print("Education:", self.education)
        print("Expertise:", self.expertise)

# Example usage:
#admin1 = Admin(1000000001, "John Doe", "password", "PhD in Computer Science", "Data Analysis")
#admin1.print_info()