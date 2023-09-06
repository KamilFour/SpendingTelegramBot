# Expense Tracker Telegram Bot

This is a simple Telegram bot that allows users to track their expenses by category and view a pie chart of their spending. Users can input their expenses by selecting a category and entering the amount they spent. The bot also provides an option to view all expenses and presents the total spending in a pie chart.

## Features

- **Expense Tracking**: Users can select a category for their expenses and enter the amount they spent. The expenses are then saved to a SQLite database.

- **Category Selection**: Users can choose from various predefined expense categories using inline keyboard buttons.

- **View All Expenses**: Users can view all their expenses and see a breakdown of spending by category in a pie chart.

## Getting Started

Follow these steps to set up and run the Expense Tracker Telegram Bot:

1. Clone the repository to your local machine:

   ```shell
   git clone <repository_url>
   ```

2. Create a virtual environment and install the required dependencies:

   ```shell
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a Telegram Bot and obtain your API token. You can do this by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

4. Update the `main()` function in the code with your Telegram Bot API token:

   ```python
   updater = Updater("YOUR_TOKEN", use_context=True)
   ```

5. Create an SQLite database file named `expenses.db` in the same directory as the code:

   ```shell
   touch expenses.db
   ```

6. Run the bot:

   ```shell
   python bot.py
   ```

7. Start a conversation with your bot on Telegram by searching for its username and typing `/start`.

## Usage

1. Start the conversation with the bot by sending `/start`.

2. Select a category for your expense using the provided inline keyboard buttons.

3. Enter the amount you spent when prompted.

4. Repeat the process to log additional expenses.

5. To view all expenses and see a pie chart breakdown, select the "Все расходы" (All Expenses) option.

## Database

The bot uses an SQLite database (`expenses.db`) to store expense records. The database schema consists of a single table named `expenses` with the following columns:

- `id` (auto-incremented integer)
- `category` (text) - The expense category.
- `amount` (real) - The amount spent.

## Dependencies

- `sqlite3`: For working with the SQLite database.
- `matplotlib`: For generating pie charts.
- `python-telegram-bot`: A Python wrapper for the Telegram Bot API.

## Contributing

Contributions to this project are welcome. If you would like to contribute, please fork the repository, create a new branch, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
