from datetime import datetime

import pyodbc
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")

try:
    con = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost\\SQLEXPRESS;"
        "Database=aiagentcourse;"
        "Trusted_Connection=yes;"
    )
    cur = con.cursor()

except Exception as e:
    print(f"Error creating connection: {e}")
    now = datetime.now().strftime("%d_%m_%Y_%H_%M_%f")
    with open(now + ".log", "w") as log:
        log.write(str(e) + "\n")
    quit()


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    returns sum of two number
    """
    return a + b


@mcp.tool()
def execute_sql(query: str) -> str:
    """
    Executes given sql query
    """
    try:
        cur.execute(query)
    except Exception as e:
        return "Error during execute query: " + str(e)
    cols = [column[0] for column in cur.description]
    result = "|" + "|".join(cols) + "|\n"
    rows = cur.fetchall()
    for r in rows:
        row = "|"
        for i in r:
            row += str(i) + "|"
        result += row + "\n"
    return result


if __name__ == "__main__":
    mcp.run(transport="stdio")
