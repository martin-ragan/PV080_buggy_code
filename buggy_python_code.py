import urllib
import yaml
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    """Index page"""
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person:
    """A person class"""
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    """Print a nametag"""
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    """Fetch a website"""
    if urllib_version is not None:
        exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL

    try:
        http = urllib.PoolManager()
        http.request("GET", url)
    except:
        print("Exception")


def load_yaml(filename):
    """Load a YAML file"""
    with open(filename) as stream:
        deserialized_data = yaml.load(
            stream, Loader=yaml.Loader
        )  # deserializing data
    return deserialized_data


def authenticate(password):
    """Authenticate a user"""
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


if __name__ == "__main__":
    print("Vulnerabilities:")
    print(
        "1. Format string vulnerability: use string={person.__init__.__globals__[CONFIG][API_KEY]}"
    )
    print("2. Code injection vulnerability: use string=;print('Own code executed') #")
    print("3. Yaml deserialization vulnerability: use string=file.yaml")
    print("4. Use of assert statements vulnerability: run program with -O argument")
    choice = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)
