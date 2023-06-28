import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

# Conversation states
CATEGORY, AMOUNT = range(2)


def start(update, context):
    categories = [[InlineKeyboardButton("🍔 Food", callback_data='Food'),
                   InlineKeyboardButton("🚗 Transport", callback_data='Transport')],
                  [InlineKeyboardButton("💡 Utilities", callback_data='Utilities'),
                   InlineKeyboardButton("🛍 Household goods", callback_data='Household goods')],
                  [InlineKeyboardButton("👕 Clothing", callback_data='Clothing'),
                   InlineKeyboardButton("👶 Children", callback_data='Children')],
                  [InlineKeyboardButton("💄 Health and beauty", callback_data='Health and beauty'),
                   InlineKeyboardButton("🎉 Recreation", callback_data='Recreation')],
                  [InlineKeyboardButton("💸 Taxes", callback_data='Taxes'),
                   InlineKeyboardButton("📦 Other", callback_data='Other')],
                  [InlineKeyboardButton("💰 View expenses", callback_data='view')]]
    reply_markup = InlineKeyboardMarkup(categories)
    update.message.reply_text('Please select the category of your expense:', reply_markup=reply_markup)

    return CATEGORY

def category(update, context):
    query = update.callback_query
    context.user_data['category'] = query.data
    query.answer()
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please enter the amount spent:')

    return AMOUNT

def amount(update, context):
    amount = update.message.text
    category = context.user_data['category']

    # Write the spending record to the database
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()
    conn.close()

    context.bot.send_message(chat_id=update.effective_chat.id, text='Spending record added!')

    return ConversationHandler.END

def main():
    # Set up the Updater and add the handlers
    updater = Updater("Your Token", use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CATEGORY: [CallbackQueryHandler(category)],
            AMOUNT: [MessageHandler(Filters.text, amount)]
        },
        fallbacks=[],
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()