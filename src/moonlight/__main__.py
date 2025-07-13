"""
Main entry point for the Wage Monitor application.
This script initializes the command-line interface (CLI) for the application.
"""

import sys
import os
import pathlib
from streamlit.web import cli as stcli


def main() -> None:
    os.chdir(pathlib.Path(__file__).parent)
    cwd = os.getcwd()
    sys.path.append(cwd)
    st_init_file = os.path.join("app.py")

    sys.argv = ["streamlit", "run", st_init_file]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
