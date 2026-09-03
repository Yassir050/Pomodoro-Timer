import time


def countdown(minutes, message):
    seconds = minutes * 60

    while seconds > 0:
        mins, secs = divmod(seconds, 60)

        print(f"\r{message}: {mins:02d}:{secs:02d}", end="")

        time.sleep(1)
        seconds -= 1

    print(f"\n🔔 {message} finished!")


def start_pomodoro(work_minutes=25, break_minutes=5):
    print("🍅 Pomodoro Timer Started!")

    while True:
        countdown(work_minutes, "Work")

        countdown(break_minutes, "Break")

        choice = input("\nStart another Pomodoro? (y/n): ").lower()

        if choice != "y":
            print("👋 Pomodoro Timer stopped.")
            break


if __name__ == "__main__":
    start_pomodoro()
