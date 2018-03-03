"Execute the script
inoremap <M-F5> <esc>:! python C:\_util\auto_cmake\auto_cmake.py %<RETURN><RETURN>
map <M-F5> <esc>:! python C:\_util\auto_cmake\auto_cmake.py %<RETURN><RETURN>

"Run the compiled executable
inoremap <F5> <esc>:! %:p:h:t.exe<RETURN><RETURN>
map <F5> <esc>:! %:p:h:t.exe<RETURN><RETURN>
