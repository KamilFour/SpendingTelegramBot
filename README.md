# SpendingTelegramBot

This is a simple expense tracker Telegram bot that allows users to record their expenses in different categories. The bot is built using Python and utilizes the SQLite database for storing the expense records.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3
- SQLite

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/expense-tracker.git
```

2. Navigate to the project directory:

```
cd expense-tracker
```

3. Install the required dependencies:

```
pip install python-telegram-bot sqlite3
```

## Usage

1. Create a new Telegram bot and obtain the API token.

2. Replace `'Your Token'` in the code with your actual API token.

3. Run the following command to start the expense tracker bot:

```
python expense_tracker.py
```

4. Open Telegram and search for your bot. Start a conversation with the bot and send the `/start` command.

5. The bot will present a list of expense categories as inline buttons. Select a category by tapping on the corresponding button.

6. Enter the amount spent in the category as a text message.

7. The bot will store the expense record in the `expenses.db` database and display a confirmation message.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was inspired by the need for a simple expense tracking solution using Telegram.
