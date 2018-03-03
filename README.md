This python script takes a directory as argument, analyzes every C++ source files, automatically creates a CMakelists file, creates the make files and the make the project in one operation only.
It's possible to compile a main only, a static library only or both and link them. Don't hesitate to modify this template so it fits your needs.

VIM users: why not add those lines to your .vimrc ?


_inoremap <M-F5> <esc>:! python C:\_util\auto_cmake\auto_cmake.py %<RETURN><RETURN>
_map <M-F5> <esc>:! python C:\_util\auto_cmake\auto_cmake.py %<RETURN><RETURN>
_inoremap <F5> <esc>:! %:p:h:t.exe<RETURN><RETURN>
_map <F5> <esc>:! %:p:h:t.exe<RETURN><RETURN>



![alt text](https://i.imgur.com/5Ft01PH.gif)
