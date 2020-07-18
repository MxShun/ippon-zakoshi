import tkinter as tk
import tkinter.font as tkfont
import keyboard
import zakoshi

# faviconの埋め込み
ICON_BASE64 = '''
R0lGODlhIQAgAHAAACH5BAEAAAEALAAAAAAhACAAgQAAAAAAAAAAAAAAAAJDjI+p
y+0Po5y02ouz3rz7/wHAIY5BWVYiuabnKqGy+5rRjCZwvNO1fevtXhacy8czAi/K
EZL3QzxB1Kr1is1qt9xGAQA7
'''

# 全ボタン
ALL_KEYS = '''\
q + w + e + r + t + y + u + i + o + p +\
a + s + d + f + g + h + j + k + l + z +\
x + c + v + b + n + m + esc + shift +\
ctrl + alt + enter\
'''

# ウィンドウ設定
root = tk.Tk()
root.title('IPPON Hollywood Zakoshisyoh')
root.geometry('1280x720')
root.configure(bg = '#ffc700')
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data = ICON_BASE64))

# テキスト表示
body_font = tkfont.Font(family = 'Meiryo UI', size = 90, weight = 'bold')
body = tk.Label(root, text = 'パソコンの全ボタンを\n一斉に押したら\n何が起きますか？', bg = '#ffc700', font = body_font)
body.pack(anchor = 'center', expand = True)
title_font = tkfont.Font(family = 'Meiryo UI', size = 60, weight = 'bold')
title = tk.Label(root, text = 'IPPON GRAND PRIX', fg = '#ffc700', bg = '#000000', font = title_font, width = '50')
title.pack(anchor = 's')

# ホットキー設定
keyboard.add_hotkey(ALL_KEYS, lambda: zakoshi.answer(body))
keyboard.add_hotkey('space', lambda: zakoshi.answer(body)) # シークレットホットキー（テスト用）

root.mainloop()
