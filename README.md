🍅 Pomodoro Timer

A simple command-line Pomodoro Timer built with Python.

The project is designed to practice Python fundamentals, functions, testing with pytest, and GitHub Actions.

📌 Features

* ⏱️ Work timer
* ☕ Break timer
* 🔁 Start another Pomodoro session
* 🛑 Stop the timer
* 🧪 Automated tests with pytest
* ⚙️ Automated testing with GitHub Actions

🛠️ Technologies

* Python
* Pytest
* GitHub Actions

📁 Project Structure

Pomodoro-Timer/
├── src/
│   └── pomodoro.py
├── tests/
│   └── test_pomodoro.py
├── .github/
│   └── workflows/
│       └── test.yml
├── requirements.txt
├── README.md
└── .gitignore

▶️ Run the Timer

Clone the repository and run:

python src/pomodoro.py

The default timer uses:

* 25 minutes of work
* 5 minutes of break

🧪 Run Tests

Install the dependencies:

pip install -r requirements.txt

Then run:

pytest

⚙️ GitHub Actions

Every push to the main branch and every pull request triggers the automated test workflow.

The workflow:

1. Sets up Python 3.12
2. Installs the project dependencies
3. Runs the test suite with pytest

🎯 Learning Goals

This project demonstrates:

* Python functions
* Loops and conditions
* User input
* Time handling
* Basic automated testing
* Test assertions
* GitHub Actions / CI

👨‍💻 Author

Yassir.B

Built as part of my Python development learning journey.
