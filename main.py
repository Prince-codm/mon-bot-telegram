import random
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

# Ton Token de bot
TOKEN = "8586879316:AAH9KGBPQ4TiKZc5nr2tjOjlMZ-weh3XqOk"

# Base de données sur les écrivains
HISTOIRES_ECRIVAINS = {
    "Victor Hugo": "Saviez-vous que Victor Hugo écrivait parfois debout à un pupitre ? Il pensait que cela stimulait son énergie créatrice.",
    "Molière": "Jean-Baptiste Poquelin, dit Molière, n'est pas mort sur scène, mais quelques heures après une représentation du 'Malade Imaginaire'.",
    "Voltaire": "Voltaire était un grand amateur de café. On raconte qu'il en buvait entre 40 et 50 tasses par jour !",
    "George Sand": "Aurore Dupin utilisait le pseudo 'George Sand' pour être prise au sérieux et portait des pantalons, ce qui était interdit aux femmes à l'époque."
}

async def moderation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.text:
        text = update.channel_post.text.lower()
        # Supprime si lien externe ou pub
        if "http" in text or "t.me/" in text:
            await update.channel_post.delete()

async def envoyer_histoire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ecrivain = random.choice(list(HISTOIRES_ECRIVAINS.keys()))
    anecdote = HISTOIRES_ECRIVAINS[ecrivain]
    message = f"📚 **Le coin Culture**\n\n**Auteur :** {ecrivain}\n\n{anecdote}"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()
    # Répond à la commande /histoire
    app.add_handler(CommandHandler("histoire", envoyer_histoire))
    # Surveille le canal pour la modération
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, moderation))
    app.run_polling()

if __name__ == "__main__":
    main()
