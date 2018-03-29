import os
import sys
from webfram import app


if __name__ == "__main__":
    app.run(debug=("debug" in sys.argv), host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
