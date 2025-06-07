if status is-interactive
    # Commands to run in interactive sessions can go here
end

## ailac22-mine

#https://fishshell.com/docs/current/cmds/fish_greeting.html#example
set -U fish_greeting


set -gx TERM alacritty
set -gx EDITOR nvim
set -gx VISUAL nvim
set -gx PAGER bat
set -gx OPENER xdg-open
set -gx BROWSER firefox
set -gx PATH $PATH /home/ailac22/.local/bin $HOME/.local/bin /home/ailac22/go/bin

# Aliases
alias cpth copypath
alias scs 'systemctl suspend'
alias sdn 'shutdown now'
alias lg lazygit
alias ldo lazydocker
alias isxwayland xlsclients
alias b buku
alias cat bat
alias li 'eza --icons -a --group-directories-first'
alias ls eza
alias hx helix
alias nv nvim

# Proton VPN
alias pvpnup 'sudo wg-quick up proton-free'
alias pvpndown 'sudo wg-quick down proton-free'
alias pvpncheck 'sudo wg'

# Chezmoi aliases
alias chez chezmoi
alias cheza 'chezmoi add'
alias cheze 'chezmoi edit'
alias chezs 'chezmoi status'
alias chezapp 'chezmoi apply'

set -gx DISABLE_AUTO_TITLE true

# Source fzf for Fish (adjust path if needed)
alias zj zellij
alias update 'paru -Syu --noconfirm'

# Aliases
alias mount_seg_dades 'udisksctl unlock -b /dev/sda1'
alias desactivar_suspension 'pkill -STOP swayidle'
alias reanudar_suspension 'pkill -CONT swayidle'
alias hacer_backup '/run/media/ailac22/dades/setup_files/install_and_backup/backup/backup.sh'

# Yazi function
# https://yazi-rs.github.io/docs/quick-start#shell-wrapper
function y
    set tmp (mktemp -t "yazi-cwd.XXXXXX")
    yazi $argv --cwd-file="$tmp"
    if read -z cwd <"$tmp"; and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
        builtin cd -- "$cwd"
    end
    rm -f -- "$tmp"
end

# For hacking
# Save attacked IPAttack function
# TODO: Hacer en fish
# function attack
#     echo "set -gx TGT $argv[1]" > ~/.ataca_tanaka
#     exec fish
# end
#
# # Source ataca_tanaka if it exists
# if test -f ~/.ataca_tanaka
#     source ~/.ataca_tanaka
# end



# Source broot launcher
#if tEst -f /home/ailac22/.config/broot/launcher/bash/br
#source /home/ailac22/.config/broot/launcher/bash/br
#end

# nvm (commented out as in original, for review)
# if test -f /usr/share/nvm/init-nvm.sh
#     source /usr/share/nvm/init-nvm.sh
# end

# ??
# pnpm
set -gx PNPM_HOME /home/ailac22/.local/share/pnpm
if not string match -q "*$PNPM_HOME*" $PATH
    set -gx PATH $PNPM_HOME $PATH
end

# zoxide initialization
# https://github.com/ajeetdsouza/zoxide?tab=readme-ov-file#installation
zoxide init fish | source

# Starfish initialization
# https://github.com/starship/starship?tab=readme-ov-file#-installation
starship init fish | source

## end-mine
