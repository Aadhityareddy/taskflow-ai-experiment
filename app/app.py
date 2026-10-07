"""TaskFlow application entry point.

Defines the Reflex app object. Routes, theme wiring, and page components are
added with the features in later tasks (see docs/ARCHITECTURE.md).
"""

import reflex as rx

from app import styles


def index() -> rx.Component:
    """Placeholder landing page so the skeleton runs. Replaced in a later task."""
    return rx.center(
        rx.heading(
            "TaskFlow",
            font_size=styles.text_3xl,
            color=styles.color_text,
        ),
    )


app = rx.App()
app.add_page(index)
