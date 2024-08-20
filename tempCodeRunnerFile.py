root.after(10, lambda: root.focus_force())
root.after(10, lambda: root.lift())
root.after(10, lambda: root.attributes('-topmost', True))
root.after(100, lambda: root.attributes('-topmost', False))