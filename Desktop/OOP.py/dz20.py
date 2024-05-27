import datetime

class Writer:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, text):
        with open(self.file_path, 'a') as file:
            file.write(text + '\n')

class Logger:
    def __init__(self, writer, log_file):
        self.writer = writer
        self.log_file = log_file

    def write(self, exception):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{now} {type(exception).__name__} {str(exception)}"
        self.writer.write(error_message)

def logger(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger_instance = args[0].logger
            logger_instance.write(e)
            raise
    return wrapper

class EmailValidator:
    def __init__(self, logger):
        self.logger = logger

    @logger
    def validate_email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email address")

class CandidateGenerator:
    def __init__(self, logger):
        self.logger = logger

    @logger
    def generate_candidates(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
