```
Exception: WebBrowserInterop.x86.dll not found
```

```
pyinstaller --clean pywebview.py --hidden-import "clr" --add-data "/c/Users/justin/dev/desktop-demos/venv/Lib/site-packages/webview/lib/WebBrowserInterop.x86.dll;./" --onefile --noconsole
```

## Freezing on Windows

This worked 

```
pyinstaller --clean pywebview.py --hidden-import "clr"  --noconsole
```

after making [this change](https://github.com/r0x0r/pywebview/issues/346#issuecomment-513567220) (was finicky, had to open the file in vscode from command prompt. editing in vscode bash wasn't having any effect...). Also 