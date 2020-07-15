import time

class SessionManager:
    __instance = None

    @staticmethod
    def getInstance():
        if SessionManager.__instance == None:
            SessionManager()
        return SessionManager.__instance

    def __init__(self):
        if SessionManager.__instance != None:
            raise Exception('Classe singleton, utilizar getInstance')
        else:
            SessionManager.__instance = self
            self.sessions = {}

    def updateSession(self, telegram_id, session_id):
        current_timestamp = time.time()
        self.sessions[telegram_id] = (session_id, current_timestamp)


    def checkSession(self, telegram_id):
        current_timestamp = time.time()
        if telegram_id in self.sessions:
            timedelta = current_timestamp - self.sessions[telegram_id][1]
            return timedelta < 300
        else:
            return False

    def getSession(self, telegram_id):
        if self.checkSession(telegram_id):
            return self.sessions[telegram_id][0]
        else:
            return None