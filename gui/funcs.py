def hide_widget(event):
    """Remove a Tkinter widget from its master grid without losing its options"""
    if not event.widget.visible:
        return False
    else:
        event.widget.grid_remove()
        event.widget.visible = False
        return True


def show_widget(event):
    """Restore a Tkinter widget to its master grid without losing its options"""
    if event.widget.visible:
        return False
    else:
        event.widget.grid()
        event.widget.visible = True
        return True


def grid_widget(widget, /, **kwargs):
    """Add a child to its parent's grid geometry manager"""
    widget.grid(**kwargs)
    return True
