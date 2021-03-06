Environment configuration
=====

My own environment configuration. Read carefully how to install and configure Tmux.

- Shell: fish
- Custom Tmux
- Custom Vim

Installation
--------

### General

> ~$ cd
> ~$ git clone https://github.com/jask05/MyOS

### Installation - UNDER CONSTRUCTION

I'm developing a script to install and configure everthing. It is not finish yet.

### Fish

> ~$ sudo apt-get install fish
> ~$ chsh -s /usr/bin/fish
> ~$ mkdir -p ~/.config/fish
> ~$ cp -rvfp config.fish ~/.config/fish/
> ~$ cp -rvfp fish_prompt.fish ~/.config/fish/
> ~$ fish_config # Optional

### Vim
> ~$ cp -rvfp vimrc ~/.vimrc

### Tmux
> ~$ sudo apt-get install tmux
> ~$ cd
> ~$ git clone https://github.com/gpakosz/.tmux.git
> ~$ ln -s -f .tmux/.tmux.conf
> ~$ cd
> ~$ cp -rvfp ~/MyOS/Environment/tmux.conf.local ~/.tmux.conf.local


Tmux Bindings (@gpakosz)
--------

tmux may be controlled from an attached client by using a key combination of a
prefix key, followed by a command key. This configuration uses `C-a` as a
secondary prefix while keeping `C-b` as the default prefix. In the following
list of key bindings:
  - `<prefix>` means you have to either hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd>
  - `<prefix> c` means you have to hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd> followed by <kbd>c</kbd>
  - `<prefix> C-c` means you have to hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd> followed by <kbd>Ctrl</kbd> + <kbd>c</kbd>

This configuration uses the following bindings:

 - `<prefix> e` opens `~/.tmux.conf.local` with the editor defined by the
   `$EDITOR` environment variable (defaults to `vim` when empty)
 - `<prefix> r` reloads the configuration
 - `C-l` clears both the screen and the tmux history

 - `<prefix> C-c` creates a new session
 - `<prefix> C-f` lets you switch to another session by name

 - `<prefix> C-h` and `<prefix> C-l` let you navigate windows (default
   `<prefix> n` and `<prefix> p` are unbound)
 - `<prefix> Tab` brings you to the last active window

 - `<prefix> -` splits the current pane vertically
 - `<prefix> _` splits the current pane horizontally
 - `<prefix> h`, `<prefix> j`, `<prefix> k` and `<prefix> l` let you navigate
   panes ala Vim
 - `<prefix> H`, `<prefix> J`, `<prefix> K`, `<prefix> L` let you resize panes
 - `<prefix> <` and `<prefix> >` let you swap panes
 - `<prefix> +` maximizes the current pane to a new window

 - `<prefix> m` toggles mouse mode on or off

 - `<prefix> U` launches Urlview (if available)
 - `<prefix> F` launches Facebook PathPicker (if available)

 - `<prefix> Enter` enters copy-mode
 - `<prefix> b` lists the paste-buffers
 - `<prefix> p` pastes from the top paste-buffer
 - `<prefix> P` lets you choose the paste-buffer to paste from

Additionally, `copy-mode-vi` matches [my own Vim configuration][]

[my own Vim configuration]: https://github.com/gpakosz/.vim.git

Bindings for `copy-mode-vi`:

- `v` begins selection / visual mode
- `C-v` toggles between blockwise visual mode and visual mode
- `H` jumps to the start of line
- `L` jumps to the end of line
- `y` copies the selection to the top paste-buffer
- `Escape` cancels the current operation

Bibliography
------------

- [Tmux configuration](https://github.com/gpakosz/.tmux)
- [Fish documentation](https://fishshell.com/docs/current/index.html)
- [Fish and Vim configuration](https://gist.github.com/killercup/5459372) 
- [More configurations that I did not use](https://pempek.net/articles/2013/04/14/maximizing-tmux-pane-new-window/)
- [Instalar fish interpretrete inteligente](https://miguelmenendez.pro/es/blog/2015/12/instalar-fish-interprete-inteligente-linea-comandos-gnu-linux-hurd-bsd/)


