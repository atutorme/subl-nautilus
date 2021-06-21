# subl-nautilus
Open with SublimeText from Ubuntu GNOME context menu (nautilus).

This script is inspired by [code-nautilus](https://github.com/harry-cpp/code-nautilus) which creates a context menu entry for GNOME/nautilus based environments for opening files with VsCode.

`subl-nautilus` is a clone of `code-nautils` for opening files with SublimeText.

## Instructions for Ubuntu 21.04 and similar systems
1. `sudo apt install python3-nautilus`
2. `mkdir -p ~/.local/share/nautilus-python/extensions`
3. copy the `subl-nautilus.py` file to `~/.local/share/nautilus-python/extensions/subl-nautilus.py`
4. `nautilus -q && nautilus &`
