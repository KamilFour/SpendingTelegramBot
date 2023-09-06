import sqlite3
import matplotlib.pyplot as plt
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

# Conversation states
CATEGORY, AMOUNT = range(2)


def start(update, context):
    categories = [[InlineKeyboardButton("🍔 Рестораны", callback_data='Рестораны'),
                   InlineKeyboardButton("🚗 Транспорт", callback_data='Транспорт')],
                  [InlineKeyboardButton("💡💧🏠 КУ", callback_data='Коммунальные услуги'),
                   InlineKeyboardButton("🛍 Продукты", callback_data='Продукты')],
                  [InlineKeyboardButton("👕 Одежда", callback_data='Одежда'),
                   InlineKeyboardButton("👶 Ребёнку", callback_data='Ребёнку')],
                  [InlineKeyboardButton("💄 Красота и здоровье", callback_data='Красота и здоровье'),
                   InlineKeyboardButton("🎉 Развлечения", callback_data='Развлечения')],
                  [InlineKeyboardButton("💸 Налоги и Долги", callback_data='Налоги и Долги'),
                   InlineKeyboardButton("📦 Другое", callback_data='Другое')],
                  [InlineKeyboardButton("Все расходы", callback_data='Все расходы')]]
    reply_markup = InlineKeyboardMarkup(categories)
    update.message.reply_text('Пожалуйста выберите категорию расходов:', reply_markup=reply_markup)

    return CATEGORY


def amount(update, context):
    amount = update.message.text
    category = context.user_data['category']

    # Write the spending record to the database
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()
    conn.close()

    context.bot.send_message(chat_id=update.effective_chat.id, text='Расход добавлен!')

    return ConversationHandler.END


def button(update, context):
    query = update.callback_query

    if query.data == 'Все расходы':
        view_expenses(update, context)
        return ConversationHandler.END
    else:
        context.user_data['category'] = query.data
        query.answer()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Введите сумму траты:')
        return AMOUNT


def view_expenses(update, context):
    # Retrieve the spending data from the database
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = c.fetchall()
    total_spending = sum([row[1] for row in data])  # Calculate the total spending
    conn.close()

    # Generate the pie chart
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    ax.set_title(f'Всего расходов: {total_spending:.2f}')  # Add the total spending as the title of the pie chart
    plt.savefig('pie.png')

    # Send the pie chart as a photo
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('pie.png', 'rb'))

    return ConversationHandler.END


def main():
    # Set up the Updater and add the handlers
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CATEGORY: [CallbackQueryHandler(button)],
            AMOUNT: [MessageHandler(Filters.text, amount)]
        },
        fallbacks=[],
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
