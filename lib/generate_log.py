from datetime import datetime


def generate_log(data):
    # 1. Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    # 2. Create filename (STRICT format required)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # 3. Write file (must match input exactly, including empty list)
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # 4. Print confirmation (must include filename)
    print(f"Log written to {filename}")

    # 5. Return filename (often required for tests)
    return filename


if __name__ == "__main__":
    sample_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]
    generate_log(sample_data)