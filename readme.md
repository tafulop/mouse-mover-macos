# MacOS Mouse Mover

## Installation

Install python modules

```bash
pip3 install -r requirements.txt
```

## Usage

To move the cursor to a defined position use the `mouse_mover.py` with arguments.

```bash
python3 mouse_mover.py -x 100 -y 200
```

Configure hotkeys and their reaction by editing the script itself. To add a new combination, add a new dedicated function and register it at the end of the script. The supported key names are listed in the [Pynput documentation](https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key).

```bash
python3 mouse_mover_with_hotkey.py
````

To automatically start the script at login, follow the [macOS User Guide](https://support.apple.com/en-gb/guide/mac-help/mh15189/mac).
