import telegram
from pytube import YouTube

# تعريف مفاتيح التطبيق والتوكن الخاص بالبوت على تيليجرام
APP_ID = <23526590>
API_HASH = <a5be45f8b50b1e344fc575540beaa432>
BOT_TOKEN = <6278390821:AAEvK8u64g8kADzjpBWRd70r8FD32Lzmmvc>

# تعريف دالة للتحميل من يوتيوب باستخدام pytube
def download_video(video_url, filename):
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(filename=filename)

# تعريف دالة للرد على الرسائل التي تحتوي على روابط الفيديو من يوتيوب
def handle_message(update, context):
    message = update.message.text
    if 'youtube.com/' in message:
        video_url = message.split(' ')[0]
        download_video(video_url, filename='video.mp4')
        context.bot.send_video(chat_id=update.effective_chat.id, video=open('video.mp4', 'rb'))

# تكوين التطبيق وإضافة التعامل مع الرسائل
bot = telegram.Bot(token=BOT_TOKEN)
updater = telegram.ext.Updater(token=BOT_TOKEN, use_context=True)
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# تشغيل البوت
updater.start_polling()