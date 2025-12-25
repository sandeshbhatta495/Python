class Transaction:
    def __init__(self, transaction_id, account_id, amount, transaction_type, timestamp):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp

    def __repr__(self):
        return f"<Transaction {self.transaction_id}: {self.transaction_type} of Rs {self.amount} on {self.timestamp}>"

    def save(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(
            "INSERT INTO transactions (transaction_id, account_id, amount, transaction_type, timestamp) VALUES (?, ?, ?, ?, ?)",
            (self.transaction_id, self.account_id, self.amount, self.transaction_type, self.timestamp)
        )
        db_connection.commit()

    @staticmethod
    def get_all_transactions(db_connection, account_id):
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM transactions WHERE account_id = ?", (account_id,))
        return cursor.fetchall()