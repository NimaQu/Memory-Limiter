import psutil
import time

limit = 500  # MB
proc_name = "OP.GG.exe"


def find_procs_by_name(name):
    # "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls


def main():
    print("Monitoring...")

    while True:
        try:
            for proc in find_procs_by_name(proc_name):
                usage = int(proc.memory_info().rss / 1024 / 1024)
                if usage > limit:
                    proc.kill()
                    print("Killed process: " + proc.name() + " Memory usage: " + str(usage) + "MB")
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
