from sniff.sniff_manager import Sniff_Manager


def main():
    manager = Sniff_Manager(10,"wlp3s0")
    manager.start()


if __name__ == "__main__":
    main()
