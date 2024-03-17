import streamlit as st

# Slider heading
st.write("# Slider Example")

# Slider properties
min_value = 0
max_value = 100
default_value = 50
step = 1

# Slider
slider_value = st.slider(
    "Select a value:",
    min_value=min_value,
    max_value=max_value,
    value=default_value,
    step=step
)

# Display current slider value
st.write(f"Selected value: {slider_value}")
