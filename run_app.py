#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.app_web import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)