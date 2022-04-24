from base import app
from users import view
from person import view
from rating import view
from game import view


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=13452)
