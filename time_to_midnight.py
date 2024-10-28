def time_to_midnight(time_str):
    """Calculates the time until midnight from a given time string.

    Args:
        time_str: A string representing the time in 24-hour format,
                  e.g., "1:0:1", "13:34:59", or "7:48:8".

    Returns:
        A string representing the time until midnight in the same format
        as the input, e.g., "22:59:59", "10:25:01", or "16:12:0".
    """
    hours, minutes, seconds = map(int, time_str.split(':'))

    # Calculate the time remaining until midnight
    remaining_seconds = (23 - hours) * 3600 + (59 - minutes) * 60 + (60 - seconds)

    # Convert total seconds back to hours, minutes, and seconds
    hours_remaining, remainder = divmod(remaining_seconds, 3600)
    minutes_remaining, seconds_remaining = divmod(remainder, 60)

    # Adjust each component's format based on the length of the input parts
    input_parts = time_str.split(':')
    hours_str = str(hours_remaining).zfill(len(input_parts[0]))
    minutes_str = str(minutes_remaining).zfill(len(input_parts[1]))
    seconds_str = str(seconds_remaining).zfill(len(input_parts[2]))

    return f"{hours_str}:{minutes_str}:{seconds_str}"

# Test cases
print(time_to_midnight("1:0:1"))    # Expected Output: 22:59:59
print(time_to_midnight("13:34:59"))  # Expected Output: 10:25:01
print(time_to_midnight("7:48:8"))    # Expected Output: 16:12:52
print(time_to_midnight("13:5:1"))    # Expected Output: 10:54:59
