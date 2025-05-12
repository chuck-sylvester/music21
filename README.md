# music21
Learning and creating music using the Python library, music21

## Getting Started
For local development, follow the guidelines below.

### Python
For Macbook users, macOS comes with a system version of Python pre-installed, but it is often outdated and not recommended for development. For my 2025 MacBook Air running macOS 15.4.1, the built-in Python version is 3.9.6.  The music21 v9 toolkit is compatible with Python v3.10 and higher, so you will need to ensure that this version is available.

You can check the version:
```bash
python3 --version
```

If it's an older version, consider a new installation via Homebrew.

Install Homebrew (if not already installed):  
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Python:  
```bash
brew install python
```

Note: After installing via homebrew, the new version may not be recognized. If this is the case, refresh (or close/restart) your terminal session.

Verify Installation:  
```bash
python3 --version
pip3 --version
```

This will show the latest Python3 and PIP3 versions, e.g., 3.13.3.

#### Python Virtual Environment
It is recommended that you set up a Python virtual environment. This provides a self-contained directory with a Python interpreter and a set of installed packages, which isolates the dependencies required for this project.

For my local setup for this learning project, I selected the root folder as the location for the virtual environment.

Create a virtual environment:   
```txt
cd ~/swdev/cps/music21
python3 -m venv myenv
```

Replace "cmyenv" with your preferred name for the environment folder that's created. For simplicity and standardization, I typically go with "venv".

Once created, you must activate the virtual environment for it to be in effect. Do this everytime you start a new coding and terminal session.  

Below are the Linux/macOS and Windows commands, respectively, to activate a Python virtual environment.

```txt
source venv/bin/activate

venv\Scripts\activate
```

For Git Bash, use a slightly different command:
```text
source venv\Scripts\Activate
```

After activation, you’ll notice the environment name `(venv)` appears in your terminal prompt. You can invoke Python with the command, `python` (as opposed to `python3`).

You can then install packages as normal using `pip` or install all packages from `requirements.txt`.

To activate an environment and install from a `requirements.txt` file:
```txt
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Python dontenv Module
The middleware component uses the Python `dotenv` module, provided by the `python-dotenv` package. Use of this module requires a `.env` file to be placed in the root middleware folder. This file is not under source control, so you will need to ask a peer developer for information on file contents, or to get a copy for your local development environment.

### music21
Music21 is a Python-based toolkit for computer-aided musicology.  

Project website: [https://www.music21.org/music21docs/](https://www.music21.org/music21docs/)  
Official GitHub repository: [https://github.com/cuthbertLab/music21/releases/tag/v9.1.0](https://github.com/cuthbertLab/music21/releases/tag/v9.1.0)  

#### Installation
Use `pip` to install the music21 library into your Python project virtual environment:

```text
cd ~/swdev/cps/music21
pip install music21
```

Note that the music21 installation guide recommends that you also run their custom configuration script. This sets a few default values, including the musicxml app that you will use for visualizing music scores. Run the following (outside of your venv environment) to start the configuration module:

```text
python3 -m music21.configure
```
