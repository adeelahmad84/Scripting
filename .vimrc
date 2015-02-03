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

set laststatus=2
set number
set showcmd
set cursorline
set showmatch
set incsearch
set hlsearch

"Syntastic Settings
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let python_highlight_all = 1

let g:airline#extensions#tabline#enabled = 1
