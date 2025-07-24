import sys
import json
import urllib.request

VALID_CATEGORIES = {"Any", "Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"}
API_URL = "https://v2.jokeapi.dev/joke/{}?format=json"
LOG_FILE = "myJokes.log"

def extract_joke_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        joke_type = data.get("type")
        if joke_type == "single":
            print(f"Joke: {data.get('joke')}")
        elif joke_type == "twopart":
            print(f"Setup: {data.get('setup')}")
            print(f"Punchline: {data.get('delivery')}")
        else:
            print("Error: Unknown joke format.")
    except FileNotFoundError:
        print("Error: No such file!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
    except Exception as e:
        print(f"Error: {e}")

def fetch_joke_from_api(category):
    try:
        with urllib.request.urlopen(API_URL.format(category)) as response:
            print(API_URL.format(category))
            data = json.loads(response.read().decode("utf-8"))
            print('json response ', data)
        if data.get("type") == "single":
            return f"Joke: {data.get('joke')}"
        elif data.get("type") == "twopart":
            return f"Setup: {data.get('setup')}\nPunchline: {data.get('delivery')}"
        else:
            return "Error: Invalid joke type"
    except urllib.error.URLError:
        return "Error: Unable to connect to the Internet."
    except Exception as e:
        return f"Error: {e}"

def conversation_mode():
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as log:
            while True:
                try:
                    user_input = input("What joke category would you like? ")
                    if not user_input.strip():
                        print("Error: You MUST choose a Joke category")
                        continue
                    if user_input not in VALID_CATEGORIES:
                        print(f'Error: Uknown Joke category “{user_input}”')
                        continue
                    joke = fetch_joke_from_api(user_input)
                    print(joke)
                    log.write(joke + "\n\n")
                except EOFError:
                    print("Bye!")
                    break
    except Exception as e:
        print(f"Error: {e}")

def print_usage():
    print("Usage: myJokes --extract <filename> | --bot")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    mode = sys.argv[1]

    if mode == "--extract":
        if len(sys.argv) != 3:
            print_usage()
        else:
            extract_joke_from_file(sys.argv[2])
    elif mode == "--bot":
        conversation_mode()
    else:
        print_usage()

if __name__ == "__main__":
    main()
