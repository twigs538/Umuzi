import os
import json
import re


class Visitor:
    def __init__(
        self, full_name, age, date_of_visit, time_of_visit, comments, assistant_name
    ):
        self.full_name = Visitor.validate_str(full_name, "Full name")
        self.age = Visitor.validate_int(age, "Age")
        self.date_of_visit = Visitor.validate_date(date_of_visit, "Date of visit")
        self.time_of_visit = Visitor.validate_time(time_of_visit, "Time of visit")
        self.comments = Visitor.validate_str(comments, "Comments")
        self.assistant_name = Visitor.validate_str(assistant_name, "Assistant name")

    @staticmethod
    def validate_str(value, field_name):
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string.")
        return value

    @staticmethod
    def validate_int(value, field_name):
        if not isinstance(value, int):
            raise ValueError(f"{field_name} must be an integer.")
        return value

    @staticmethod
    def validate_date(value, field_name):
        components = value.split("-")
        components = [str(int(comp)) for comp in components]
        value_without_zeros = "-".join(components)

        date_pattern = r"^\d{4}-\d{1,2}-\d{1,2}$"
        if not re.match(date_pattern, value_without_zeros):
            raise ValueError(f"{field_name} must be in the format 'YYYY-MM-DD'.")
        return value_without_zeros


    @staticmethod
    def validate_time(value, field_name):
        time_pattern = r"^\d{2}:\d{2}$"
        if not re.match(time_pattern, value):
            raise ValueError(f"{field_name} must be in the format 'HH:MM'.")
        return value

    def save(self):
        if not os.path.exists("src/json_files"):
            os.makedirs("src/json_files")

        filename = self.get_filename(self.full_name)
        data = {
            "full_name": self.full_name,
            "age": self.age,
            "date_of_visit": self.date_of_visit,
            "time_of_visit": self.time_of_visit,
            "comments": self.comments,
            "assistant_name": self.assistant_name,
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    @classmethod
    def load(cls, full_name):
        filename = cls.get_filename(full_name)
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.validate_data(data)
                return cls(**data)
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")

    @staticmethod
    def validate_data(data):
        required_fields = [
            "full_name",
            "age",
            "date_of_visit",
            "time_of_visit",
            "comments",
            "assistant_name",
        ]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Field '{field}' is missing in the loaded data.")

    @staticmethod
    def get_filename(full_name):
        return os.path.join(
            "src/json_files", f"visitor_{full_name.lower().replace(' ', '_')}.json"
        )


if __name__ == "__main__":
    alice = Visitor("Alice Cooper", 30, "2023-4-23", "14:30", "Nice visit!", "John")
    alice.save()

    loaded_alice = Visitor.load("Alice Cooper")
    print(loaded_alice.full_name)
    print(loaded_alice.age)
