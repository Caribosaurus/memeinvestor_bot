from models.base import BaseTable


class Investors(BaseTable):
    _primkey = "name"

    def __init__(self, db):
        super().__init__(db)
        self._exec("""
            CREATE TABLE IF NOT EXISTS {table} (
                name VARCHAR(20) PRIMARY KEY,
                balance INTEGER DEFAULT 1000,
                active INTEGER DEFAULT 0,
                completed INTEGER DEFAULT 0,
                broke INTEGER DEFAULT 0
            )
        """)
        self._dbconn.commit()

    def total_coins(self):
        return self._exec("SELECT SUM(balance) FROM {table}").fetchone()[0]
