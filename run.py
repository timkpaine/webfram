import os
from webfram import app


if __name__ == "__main__":
    app.run(debug=True, port=str(os.environ.get('PORT', 8080)))
