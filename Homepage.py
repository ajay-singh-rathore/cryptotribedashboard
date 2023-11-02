import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie


# Set page configuration
st.set_page_config(
    page_title="Crypto Tribe Dashboard",
    page_icon="₿",
    layout="wide"  # You can adjust the layout as needed
)


# Main title and tagline
st.title("Crypto Tribe")
st.subheader("Empowering Your Token Listing Decisions with Data-Driven Insights")

# Sidebar content
st.sidebar.success("Select a page above.")

# Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/f691cb0e-a0f2-415e-bdb7-8a4fd548626b/6ixwDCIuFI.json")

st_lottie(lottie_hello, key="hello")


# Additional homepage content
st.write(
    """
    Welcome to Crypto Tribe, your one-stop solution for making informed decisions about token listings. 
    Explore historical data, compare exchanges, and analyze IEO ROI to ensure your crypto success.
    
    Why Crypto Tribe?
    
    - **Historical Insights:** Dive into comprehensive data on token performance, enabling you to understand past returns and make informed predictions about the future.
    
    - **Exchange Comparison:** Discover the best-suited exchange for your token listing based on factors like trading volume, security features, and community engagement.
    
    - **IEO ROI Analysis:** Uncover the most lucrative IEOs, evaluate their returns, and gain a competitive edge in the crypto market.
    
    - **User-Friendly Interface:** Our intuitive web app is designed to cater to both newcomers and experienced crypto enthusiasts. Navigating through data has never been easier.
    
    - **Data-Driven Decision Making:** Make smart, data-backed choices for your token listing, ensuring that you maximize your potential for success.

    **How It Works:**

    1. **Explore Token Performance:** Input the token you're interested in listing, and gain insights into its historical performance. Analyze its price trends, trading volumes, and more.

    2. **Compare Exchanges:** Evaluate cryptocurrency exchanges based on your specific listing requirements. Discover the pros and cons of each platform.

    3. **IEO ROI Analysis:** Stay ahead of the curve by examining the performance of past Initial Exchange Offerings. Identify IEOs that have delivered exceptional returns.

    4. **Make Informed Decisions:** Armed with our data, you can confidently choose the right exchange for your token listing, increasing your chances of success.

    Crypto Tribe is your all-in-one solution for token listing analysis, tailored to meet your unique needs in the fast-paced world of cryptocurrencies.

    Ready to take control of your token listing journey? Get started with Crypto Tribe today and unlock the power of data-driven decision-making in the crypto universe.
    """
)

import streamlit as st

# Your existing code here...

# Embedding social media icons linked to profiles and adding a button with a hyperlink
st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <a href="https://www.linkedin.com/company/cryptotribe/" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" style="width: 60px; height: 60px; margin: 0 10px;" />
        </a>
        <a href="https://t.me/Mrk0302" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/telegram-app--v2.png" alt="Telegram" style="width: 60px; height: 60px; margin: 0 10px;" />
        </a>
    </div>
    <p><a href="https://t.me/Mrk0302" target="_blank" class="footer-button">Get a Free Consultation</a></p>
    <p>© 2023 CryptoTribe</p>
    """,
    unsafe_allow_html=True
)

# Rest of your code...




