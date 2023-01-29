import os
from pathlib import Path

class Config:

    API_ID = int(os.environ.get('API_ID', '8564523'))
    API_HASH = os.environ.get('API_HASH', '1a39289e7dc9aa69b32683dc2adfc875')
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5397997424:AAEvZuVX_bR_lEuv-owl20WfNXoO14VqVlA')
    SESSION_NAME = os.environ.get('SESSION_NAME', ':memory:')
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001425688221'))
    DATABASE_URL = os.environ.get('DATABASE_URL', 'mongodb+srv://RF999:RF999@cluster0.uaznbh4.mongodb.net/?retryWrites=true&w=majority')
    AUTH_USERS = [int(i) for i in os.environ.get('AUTH_USERS', '1989750989').split(' ')]
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 2))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 600))
    TRACK_CHANNEL = int(os.environ.get('TRACK_CHANNEL', False))
    SLOW_SPEED_DELAY = int(os.environ.get('SLOW_SPEED_DELAY', 5))
    HOST = os.environ.get('HOST', '')
    TIMEOUT = int(os.environ.get('TIMEOUT', 60 * 30))
    DEBUG = bool(os.environ.get('DEBUG'))
    IAM_HEADER = os.environ.get('IAM_HEADER', '')

    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]
    POSITIONS = ['Top Left', 'Top Center', 'Top Right', 'Center Left' , 'Centered', 'Center Right' , 'Bottom Left', 'Bottom Center', 'Bottom Right']
