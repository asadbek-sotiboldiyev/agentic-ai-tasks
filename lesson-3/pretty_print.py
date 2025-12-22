import sys
import time
# ─│┌┐└┘├┤┬┴┼
'''
MODEL: Iker Casillas's first club was **Real Madrid**.

He joined their youth academy (La Fábrica) when he was just nine years old in 1990. He then progressed through their ranks before making his senior team debut in 1999.
USER: first club of iker casillas
'''
# print("┌──────┬" + "─" * (len(text) - 7) + "┐")
# print("│MODEL │" + " " * (len(text) - 7) + "│")
# print("├──────┴" + "─" * (len(text) - 7) + "┤")
# print("│" + text + "│")
# print("└───────" + "─" * (len(text) - 7) + "┘")

def print_model(text):
    print("┌─MODEL─" + "─" * 25)
    print(" " + text)
    print("└──────" + "─" * 25)
def print_model_thinking():
    print("┌─MODEL───────┐")
    print("│ Thinking... │")
    print("└─────────────┘")

def print_user(text):
    print("   ┌─USER─" + "─" * 25)
    print("    " + text)
    print("   └──────" + "─" * 25)
def print_input():
    print("┌─ASK─" + "─" * 25)
    a = input("│ ")
    return a

def print_chats_list(chats: dict):
    for k, v in chats.items():
        print(k, "│", v)


def delete_last_lines(n=1):
    """Deletes the last n lines in the STDOUT."""
    for _ in range(n):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        sys.stdout.flush()
if __name__ == "__main__":
    text = '''Iker Casillas's first club was **Real Madrid**.

He joined their youth academy (La Fábrica) when he was just nine years old in 1990. He then progressed through their ranks before making his senior team debut in 1999.'''
    utext = "first club of iker casillas"
    # print("   ┌─USER─" + "─" * 25)
    # print("    " + text)
    # print("   └──────" + "─" * 25)

    # print("┌─MODEL─" + "─" * 25)
    # print(" " + text)
    # print("└──────" + "─" * 25)

    # print("┌─ASK─" + "─" * 25)
    # a = input("│ ")
    print_user("Nagap")
    print_model("Porohot, o'zingdane?")
    a = print_input()
    delete_last_lines(2)
    print_user(a)
    print_model_thinking()
    time.sleep(2)
    delete_last_lines(3)
    print_model("Yoxshi. Bo'lodi")

