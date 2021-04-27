class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1700341854:AAEXIDuCUCtwPd4cUGyqYvMYA2NyleHZ6FM"
    OWNER_ID = "1461968113" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "watts_on_xd"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://stella:stella123@database-1.cuzno6euao1o.us-east-2.rds.amazonaws.com:5431/dbname'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
