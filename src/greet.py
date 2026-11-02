"""Greeting helpers used to test the agent."""


def greet(name: str) -> str:
    """Return a greeting for name.

    This sentance deliberately contains a speling mistake.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
