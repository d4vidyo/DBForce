import Settings
from GUI import GUI

def main():
    settings = Settings.settings()
    settings.load()

    window = GUI.Window(settings)
    window.run()


if __name__ == "__main__":
    main()
