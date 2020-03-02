from subprocess import check_call


def format() -> None:
    check_call(
        ["black", "--check", "--diff", "src/", "tests/"],
    )


def reformat() -> None:
    check_call(["black", "src/", "tests/"])


def lint() -> None:
    check_call(["flake8", "src/", "tests/"])
    check_call(["mypy", "sanic_test/", "tests/"])


def start() -> None:
    check_call(["python", "sanic_test/main.py"])


def test() -> None:
    check_call(["pytest", "tests/"])
