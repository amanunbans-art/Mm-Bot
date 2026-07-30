from pyrogram import Client, filters

# ===== YOUR CREDENTIALS =====
API_ID = 33753913
API_HASH = "fa159d939cb43fe00935bfaccf623030"
BOT_TOKEN = "8930722456:AAHyhuPwW6pDo7__Fp4Bpn1FNUMTdQdA1Cc"
# ============================

app = Client(
    "MMBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🛡️ Welcome to Official MM Bot!\n\nUse /help to see all commands."
    )

@app.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("""
📋 Available Commands

/qr
/sent
/hold
/release
/refund
/done
/cancel
/rules
/vouch
""")

@app.on_message(filters.command("qr"))
async def qr(client, message):
    await message.reply_text(
        "💳 Please scan the official QR code and send the payment screenshot."
    )

@app.on_message(filters.command("sent"))
async def sent(client, message):
    await message.reply_text(
        "✅ Payment received. Please wait while it is being verified."
    )

@app.on_message(filters.command("hold"))
async def hold(client, message):
    await message.reply_text("🔒 Funds are now on hold with the Middleman.")

@app.on_message(filters.command("release"))
async def release(client, message):
    await message.reply_text("💸 Funds have been released successfully.")

@app.on_message(filters.command("refund"))
async def refund(client, message):
    await message.reply_text("↩️ Refund process has been started.")

@app.on_message(filters.command("done"))
async def done(client, message):
    await message.reply_text("✅ Deal completed successfully.")

@app.on_message(filters.command("cancel"))
async def cancel(client, message):
    await message.reply_text("❌ Deal cancelled.")

@app.on_message(filters.command("rules"))
async def rules(client, message):
    await message.reply_text("""
📜 MM Rules

• I NEVER DM FIRST.
• Verify my username.
• No fake proofs.
• Stay safe.
""")

@app.on_message(filters.command("vouch"))
async def vouch(client, message):
    await message.reply_text("@YourVouchChannel")

print("MM Bot Started...")
app.run()
