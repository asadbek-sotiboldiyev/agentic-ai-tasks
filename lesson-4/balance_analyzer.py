from typing import Dict, List

import pyodbc
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Balance analyzer")


def db_write_transaction(transaction: Dict):
    """
    Writes a single transaction to the database.
    """
    conn_str = (
        "Driver={SQL Server};"
        "Server=localhost\\SQLEXPRESS;"
        "Database=balance_datas;"
        "Trusted_Connection=yes;"
    )
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO FinanceLog (amount, description, transaction_type, date) VALUES (?, ?, ?, ?)",
            transaction["amount"],
            transaction["description"],
            transaction["transaction_type"],
            transaction["date"],
        )
        conn.commit()


@mcp.tool()
def balance_writer(transactions: List[Dict]):
    """
    Writes the transaction list to database:
    transactions: [{"amount": ..., "description": ..., "transaction_type": "in|out",  "date": "DD-MM-YYYY"}]
    """
    for transaction in transactions:
        db_write_transaction(transaction)
    return f"{len(transactions)} Transactions written successfully"


if __name__ == "__main__":
    mcp.run(transport="stdio")
