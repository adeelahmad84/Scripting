set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim/
call vundle#begin()

Plugin 'gmarik/Vundle.vim'
Plugin 'mitsuhiko/vim-jinja'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'scrooloose/syntastic'
Plugin 'bling/vim-airline'
Plugin 'chase/vim-ansible-yaml'
Plugin 'jiangmiao/auto-pairs'
Plugin 'godlygeek/tabular'

call vundle#end()
filetype plugin indent on

syntax enable       
colorscheme Monokai

noremap <up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>

set splitbelow
set splitright

set encoding=utf-8
set tabstop=8 expandtab shiftwidth=4 softtabstop=4

set laststatus=2    " Always show status bar
set number          " Turn on line numbers
set cursorline      " Highlight the current line
set showmatch
set incsearch       " Incremental searching (search as you type)
set hlsearch        " Highlight search matches
set noswapfile
set history=100     " Command history"
set ruler           " Always show cursor
set showcmd         " Show incomplete commands
set smartcase       " Ignore case in search
set hidden
set nowrap          " Turn word wrap off
set showmatch       " highlight a matching [{()}] when cursor is placed on start/end character
set wildmenu        " Enhance command-line completion
set binary
set noeol

set list listchars=tab:\ \ ,trail:·             " Highlight tailing whitespace
set timeout timeoutlen=1000 ttimeoutlen=100     " Get rid of the delay when pressing O (for example)

"Syntastic Settings
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let python_highlight_all = 1        "python syntax highlighting    
let g:airline#extensions#tabline#enabled = 1
let g:ansible_options = {'ignore_blank_lines': 0}
let g:AutoPairsFlyMode = 1
let g:netrw_liststyle=3     " Set built-in file system explorer to use layout similar to the NERDTree plugin
