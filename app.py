import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Git Icon Craetives. - Your Partner in Innovation",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        /* General styles */
        body {
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        .main {
            background-color: #f8f9fa;
            padding: 0;
        }
        .stButton button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }

        /* Hero section */
        .hero {
            background: linear-gradient(135deg, #007bff, #00bfff);
            color: white;
            padding: 6rem 2rem;
            text-align: center;
            border-radius: 0;
            margin-bottom: 2rem;
        }
        .hero h1 {
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .hero p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
        }

        /* Section styles */
        .section {
            margin: 2rem 0;
            padding: 2rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .section h2 {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: #007bff;
        }

        /* Service cards */
        .service-card {
            padding: 1.5rem;
            margin: 1rem 0;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .service-card h3 {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            color: #007bff;
        }
        .service-card p {
            font-size: 1rem;
            color: #666;
        }

        /* Portfolio section */
        .portfolio-card {
            padding: 1rem;
            margin: 1rem 0;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .portfolio-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .portfolio-card img {
            width: 100%;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        .portfolio-card h3 {
            font-size: 1.25rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #007bff;
        }
        .portfolio-card p {
            font-size: 1rem;
            color: #666;
        }
        .portfolio-card a {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }
        .portfolio-card a:hover {
            text-decoration: underline;
        }

        /* Contact form */
        .contact-form {
            padding: 2rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        .contact-form button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .contact-form button:hover {
            background-color: #0056b3;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 4rem;
            padding: 2rem 0;
            background-color: #007bff;
            color: white;
            border-radius: 0;
        }
        .footer p {
            margin: 0;
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <h1>Welcome to Git Icon Creatives.</h1>
        <p>Your Partner in Building Innovative and Scalable Applications</p>
        <a href="#services" class="stButton">Explore Our Services</a>
    </div>
""", unsafe_allow_html=True)

# Services Section
st.markdown("<a id='services'></a>", unsafe_allow_html=True)
st.markdown("## Our Services")
st.markdown("We specialize in delivering cutting-edge solutions tailored to your business needs.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3>Custom App Development</h3>
            <p>We build custom applications that are tailored to your specific business requirements.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3>Web Development</h3>
            <p>From simple websites to complex web applications, we've got you covered.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <h3>Mobile App Development</h3>
            <p>We create mobile apps that provide seamless user experiences across iOS and Android platforms.</p>
        </div>
    """, unsafe_allow_html=True)

# Portfolio Section
st.markdown("## Our Portfolio")
st.markdown("Check out some of the amazing applications we've built for our clients.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="portfolio-card">
            <img src="https://i.ibb.co/NgR35QXL/unnamed-3.jpg" alt="App 1">
            <h3>My Channels TV Uganda App</h3>
            <p>A fully-featured streaming platform with seamless payment integration.</p>
            <a href="http://play.google.com/store/apps/details?id=androi.tadic.oooo" target="_blank">View Project →</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="portfolio-card">
            <img src="https://i.ibb.co/v619btc5/20231231-205008.jpg" alt="App 2">
            <h3>5 Stream Uganda</h3>
            <p>A mobile app with luganda translated series</p>
            <a href="https://play.google.com/store/apps/details?id=androi.fivestream.app" target="_blank">View Project →</a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="portfolio-card">
            <img src="https://i.ibb.co/8ntW1XkG/20240104-132515.jpg" alt="App 3">
            <h3>Project Management Tool</h3>
            <p>A sports application made for those that enjoy sports around the world</p>
            <a href="https://play.google.com/store/apps/details?id=androi.netcobra.bettingtips" target="_blank">View Project →</a>
        </div>
    """, unsafe_allow_html=True)

# About Us Section
st.markdown("## About Us")
st.markdown("""
    <div class="section">
        <p>GIT ICON CREATIVES is a dynamic application development business committed to transforming ideas into powerful digital solutions. With expertise in mobile apps, websites, and software development, we provide innovative and high-quality services tailored to meet the unique needs of our clients.</p>
        <p>Our mission is to empower businesses and individuals with cutting-edge technology that enhances efficiency, growth, and success.</p>
    </div>
""", unsafe_allow_html=True)

# Contact Form Section
st.markdown("## Get in Touch")
st.markdown("""
    <div class="contact-form">
        <p>Have a project in mind? Let's discuss how we can help you achieve your goals.</p>
    </div>
""", unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button("Send Message")

    if submit_button:
        st.success("Thank you for reaching out! We'll get back to you soon.")

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2025 Git Icon Creatives. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)