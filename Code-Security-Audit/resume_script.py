

def greet_user(name):
    """Greet the user by name."""
    return f"Hello, {name}! Welcome to the resume website."


def calculate_experience(start_year, current_year):
    """Calculate years of experience."""
    if current_year >= start_year:
        return current_year - start_year
    else:
        raise ValueError("Current year cannot be earlier than start year.")


# Example usage
if __name__ == "__main__":
    name = "Jaskomal"
    print(greet_user(name))

    try:
        experience = calculate_experience(2023, 2025)
        print(f"Years of experience: {experience}")
    except ValueError as ve:
        print(f"Error: {ve}")
