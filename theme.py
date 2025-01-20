import streamlit as st

# Initialize themes in session state
def init_themes():
    ms = st.session_state
    if "themes" not in ms:
        ms.themes = {
            "current_theme": "light",  # Default theme
            "refreshed": False,
            "light": {
                "theme.base": "light",
                "theme.backgroundColor": "black",
                "theme.primaryColor": "#c98bdb",
                "theme.secondaryBackgroundColor": "#5591f5",
                "theme.textColor": "white",
                "button_face": "🌜",
            },
            "dark": {
                "theme.base": "dark",
                "theme.backgroundColor": "white",
                "theme.primaryColor": "#5591f5",
                "theme.secondaryBackgroundColor": "#82E1D7",
                "theme.textColor": "#0a1464",
                "button_face": "🌞",
            },
        }

# Apply selected theme
def apply_theme(theme):
    theme_dict = st.session_state.themes[theme]
    for key, value in theme_dict.items():
        if key.startswith("theme"):
            st._config.set_option(key, value)

# Toggle theme
def change_theme():
    ms = st.session_state
    previous_theme = ms.themes["current_theme"]
    new_theme = "dark" if previous_theme == "light" else "light"
    ms.themes["current_theme"] = new_theme
    apply_theme(new_theme)

# Initialize themes on script load
init_themes()

# Apply the current theme
change_theme()

# Display the current theme
st.write(f"Current theme: {st.session_state.themes['current_theme']}")
