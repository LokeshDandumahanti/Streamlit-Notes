import streamlit as st
import streamlit.components.v1 as components

# Function to create the hamburger menu
def create_hamburger_menu():
    menu_html = """
    <style>
    .sidebar .sidebar-content {
        width: 300px;
        margin-left: -300px;
        transition: margin 0.3s;
    }
    .sidebar-expanded .sidebar-content {
        margin-left: 0;
    }
    </style>
    <div id="hamburger-menu" class="sidebar sidebar-expanded">
        <div class="sidebar-content">
            <h2>Menu</h2>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
    </div>
    <button id="hamburger-btn" onclick="toggleMenu()">☰</button>
    <script>
    function toggleMenu() {
        var sidebar = document.getElementById("hamburger-menu");
        sidebar.classList.toggle("sidebar-expanded");
    }
    </script>
    """
    components.html(menu_html, height=600)

# Function to create the footer
def create_footer():
    footer_html = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <div class="footer">
        <p>My Streamlit Web App</p>
    </div>
    """
    components.html(footer_html)

# Main content of the app
def main():
    create_hamburger_menu()
    st.title("Welcome to my Streamlit Web App!")
    st.write("This is the main content area.")
    create_footer()

if __name__ == "__main__":
    main()
