import config as cf


class FetchData:

    def __init__(self, bot_id, start_date, end_date):
        self.bot_id = bot_id
        self.start_date = start_date
        self.end_date = end_date

    def main(self):
        cf.curr.execute("""SELECT * FROM file_info 
        WHERE BotId = (%s) AND Date BETWEEN (%s) AND (%s)""",
                        (self.bot_id, self.start_date, self.end_date))
        rows = cf.curr.fetchall()
        return rows
