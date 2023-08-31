import streamlit as st
from lightgbm import LGBMClassifier
from joblib import load
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import random
from math import *
import time
import base64

base="dark"

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"gif"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('galaxy-knowledge4.gif')



model = load('lgbmnice.pkl')
sc=load('std_scaler.bin')

gas = ['Gas Giant.png', 'Gas Giant2.png']
ice = ['Neptune-like.png', 'Neptune-like2.png']
superEarth = ['Super Earth.png']
terrestrial = ['Terrestrial.png', 'Terrestrial2.png', 'Terrestrial3.png']

st.title("Exoplanet Simulator")
st.subheader("What... is an exoplanet?")
st.write("An exoplanet is basically a planet outside the solar system!")

expa = st.expander("Why should you care?")
with expa:
    st.write("""Exoplanets are very interesting to learn about because: """)
    st.write("1. They teach us more about the past of the universe")
    st.write("2. They may help us discover extra-terrestrial beings (Aliens!) as many are suited to host life.")
    st.write(" ")

st.divider()
if expa:
    st.title("Want to create an Exoplanet with the possibility of life?")
    st.subheader("Know How!")
    st.divider()

    st.subheader("Step 1: Design an Exoplanet")
    st.write("The first thing you need for life to exist is a planet!")
    st.text("Move the sliders around to experiment and see what type of planet is formed.")

    with st.expander("Click on the box to Know More!"):
        with st.chat_message("user"):
            st.info("The Mass of the planet determines how heavy the planet is although it does not determine the type of the planet.")
            st.info("The Radius of the planet determines how massive in terms of length the planet would be. The planet type is mostly determined by the radius because there is not enough solid material in a solar system to form massive terrestrial planets so after a certain limit (around radius twice of earth) the only planets possible are either ice or gas giants.")

    x = st.slider("Planet Mass (w.r.t Earth)",min_value=0.09, max_value=49.9)
    y = st.slider("Planet Radius (w.r.t Earth)",min_value=0.09, max_value=9.9)

    if x > 0.09 and y > 0.09:
        with st.spinner("Your planet is being created..."):
            time.sleep(2)
        
        q = model.predict(sc.transform([[y]]))

        col1, col2 = st.columns([1,3])

        if (q == ['Super Earth']):
            col1.image(superEarth[0])
            col2.markdown("Planet created:")
            col2.header("Super Earth")
            st.info("Super Earths are a class of exoplanets that are larger and more massive than Earth but smaller than gas giants. These rocky worlds, often referred to as super-sized versions of our planet, can vary in size and composition. They have solid surfaces and may possess atmospheres and water in different states.")
        if (q == ['Terrestrial']):
            col1.image(terrestrial[random.randint(0,2)])
            col2.markdown("Planet created:")
            col2.header("Terrestrial Planet")
            st.info("Terrestrial planets, also known as rocky planets, are a class of planets that share similar characteristics to Earth. They are primarily composed of silicate rocks and metals, with a solid surface. Terrestrial planets are relatively smaller in size compared to gas giants and are typically found closer to their host star in planetary systems. They often possess thin atmospheres, if any, and may have features such as mountains, valleys, and even bodies of water. These planets are of particular interest in the search for extraterrestrial life, as they offer the potential for habitability and the presence of complex organic molecules.")
        if (q == ['Neptune-like']):
            col1.image(ice[random.randint(0,1)])
            col2.markdown("Planet created:")
            col2.header("Ice Giant")
            st.info("Ice giants are planets larger than Earth but smaller than gas giants, composed of rock, metal, and a thick layer of icy materials. Their atmospheres contain hydrogen, helium, and ice, giving them a bluish hue. Ice giants, like Uranus and Neptune, display complex weather patterns and have moons with potential geologic activity.")
        if (q == ['Gas Giant']):
            col1.image(gas[random.randint(0,1)])
            col2.markdown("Planet created:")
            col2.header("Gas Giant")
            st.info("Gas giants are enormous planets with extensive atmospheres primarily composed of hydrogen and helium. They lack a solid surface and have massive gravitational pulls. These giant planets exhibit dynamic weather patterns, including powerful storms. Gas giants often have rings and are accompanied by a system of moons.")

        with st.chat_message("assistant"):    
            with st.info(""):
                if (q == ['Super Earth']):
                    succ = st.success("You have created a planet which may potentially be habitable! It has the possibility to possess a stable atmosphere and liquid water on a rocky surface which is required by life!")
                if (q == ['Terrestrial']):
                    succ = st.success("You have created a planet which may potentially be habitable! It has the possibility to possess a stable atmosphere and liquid water on a rocky surface which is required by life!")
                if (q == ['Neptune-like']):
                    warn = st.error("You have created a planet which cannot be habitable! It does not have a proper solid surface required for oceans, the surface is too cold and the planet cannot sustain a stable atmosphere which is required by life! Please create a new planet.")
                if (q == ['Gas Giant']):
                    warn = st.error("You have created a planet which cannot be habitable! There is no solid surface to hold liquid water, The atmosphere is too chaotic and stormy and light (a source of heat) barely makes it past the clouds of the planet! Please create a new planet.")
            st.divider()

        if (q == ['Super Earth']) or (q == ['Terrestrial']):
            st.subheader("Step 2: Design a Star!")
            st.write("The second thing you need for life to exist is a star which will provide the required warmth and heat!")
            st.text("Move the sliders around and experiment with them to create the star for your planet.")
            with st.expander("Click here to receive a Hint!"):
                st.write("Suggested Resource for Better Understanding:")
                st.video("luminosity.mp4")
            temp = st.slider("Surface Temperature of Star (in Kelvins)",min_value=3000, max_value=10000)
            radius = st.slider("Star Radius (w.r.t sun)",min_value=1, max_value=50)
            radius = radius*696340000

            print("hi")


            if temp > 3000 and radius > 1:

                col1,col2 = st.columns([2,5])

                if temp >= 10000 and temp < 30000:
                    col2.markdown("Star Created: ")
                    col2.subheader("B type star")
                    col1.image('b_type.png')
                    st.info("B-type stars are among the hottest and most luminous main-sequence stars. They have surface temperatures ranging from 10,000 to 30,000 Kelvin. These stars appear blue or bluish-white in color and emit a significant amount of ultraviolet radiation. B-type stars have strong absorption lines of neutral helium in their spectra. They are relatively rare compared to other types of stars.")
                elif temp >= 7500 and 10000 < 30000:
                    col2.markdown("Star Created: ")
                    col2.subheader("A type star")
                    col1.image('a_type.png')
                    st.info("A-type stars are also main-sequence stars, but slightly cooler than B-type stars. They have surface temperatures ranging from 7,500 to 10,000 Kelvin. A-type stars appear white or bluish-white in color. They have prominent hydrogen absorption lines in their spectra, as well as ionized metals. A-type stars are generally more common than B-type stars.")
                elif temp >= 6000 and temp < 7500:
                    col2.markdown("Star Created: ")
                    col2.subheader("F type star")
                    col1.image('f_type.png')
                    st.info("F-type stars are intermediate in temperature between A-type and G-type stars. They have surface temperatures ranging from 6,000 to 7,500 Kelvin. F-type stars appear yellowish-white in color and have weaker hydrogen absorption lines compared to A-type stars. They exhibit stronger ionized metal lines, particularly calcium. F-type stars, like our Sun, are common in the galaxy.")
                elif temp >= 5200 and temp < 6000:
                    col2.markdown("Star Created: ")
                    col2.subheader("G type star")
                    col1.image('g_type.png')
                    st.info("G-type stars, also known as yellow dwarfs, are similar to our Sun in terms of temperature and characteristics. They have surface temperatures ranging from 5,000 to 6,000 Kelvin. G-type stars appear yellow in color and have a well-defined spectrum with prominent hydrogen absorption lines. Our Sun is a G-type star, and these stars are considered to be in the middle of the temperature and luminosity range.")
                elif temp >= 3700 and temp < 5200:
                    col2.markdown("Star Created: ")
                    col2.subheader("K type star")
                    col1.image('k_type.png')
                    st.info("K-type stars are cooler than G-type stars and appear orange in color. They have surface temperatures ranging from 3,500 to 5,000 Kelvin. K-type stars have weaker hydrogen absorption lines and prominent lines of ionized metals such as calcium and sodium in their spectra. These stars are relatively common and include many red giants and orange dwarfs.")
                elif temp >= 2400 and temp < 3700:
                    col2.markdown("Star Created: ")
                    col2.subheader("M type star")
                    col1.image('m_type.png')
                    st.info("M-type stars, also known as red dwarfs, are the coolest and most common type of main-sequence stars in the galaxy. They have surface temperatures below 3,500 Kelvin. M-type stars appear red in color and have weak hydrogen absorption lines. Their spectra contain strong molecular absorption bands, particularly of molecules like titanium oxide and water vapor. M-type stars are known for their longevity and can live for tens of billions of years.")

            st.divider()

            if temp > 3000 and radius > 1:

                Luminosity = float(4* pi * (radius**2) * 5.670373 * 10**(-8) * (temp**4))
                Luminosity = round(Luminosity)
                Luminosity106 = "{:,}".format(Luminosity)
                st.metric(label="Luminosity", value=Luminosity106, delta="watts")
                st.warning("The luminosity of a star is the energy emitted over time. It remains constant if the star is stable and doesn't change over distances. The intensity of a star is the luminosity over a specific area. It varies depending on the distance from the star and can increase or decrease based on position, while the luminosity remains unchanged. The star's surface temperature and radius determine its luminosity, which helps identify its type, age, life, and behavior.")
                habitual1 = (142120000000 * sqrt(Luminosity/(3.827 * 10**26)))/(1.496 * 10**11)
                habitual10 = str(habitual1) + ' ' + 'AU'
                habitual2 = 204952000000 * sqrt(Luminosity/(3.827 * 10**26))/(1.496 * 10**11)
                habitual20 = str(habitual2) + ' ' + 'AU'

                st.divider()

                st.subheader("Step 3: Positioning the Planet")
                
                st.info("The Habitual zone is where liquid water can exist, allowing for the potential of organic life. It's an area with optimal conditions, neither too hot nor too cold. In our solar system, it spans from 0.95 AU to 1.37 AU from the sun. The existence of life in a planet depends on whether it falls within this zone, which is determined by the star's luminosity. Planets outside this range would not be suitable for supporting life. In this case the Habitual Zone would be:")
                with st.expander("Click on the box to Know More!"):
                    st.info("Positioning the planet inside the Habitual Zone is important cause it then determines if liquid water can exist on the planet or not. It also tells us whether the planet is receiving apt amount of sunlight or not and whether the heat is perfect for the planet to sustain life without heating it up too much or too little.")
                st.success("Starting Point: -" + ' ' + str(habitual10) + ' ' + 'from the star')
                st.success("Ending Point: -" + ' ' + str(habitual20) + ' ' + 'from the star.')
                
                st.text("Drag the slider and try locating your planet under the habitable zone")
                with st.expander("What is AU?"):
                    st.info("The full form of AU is 'Astronomical Unit' which is the distance between Earth and the Sun. It is generally used to define distances along with light years in the universe. 1 AU is equivalent to 149,600,000 kilometers.")
                distance = st.slider("Distance from the star (in AU)",min_value=0.09, max_value=149.9)
                if distance > 0.9: 
                    if distance > habitual1 and distance < habitual2:
                        st.balloons()
                        st.success("Your planet falls under the habitable zone! It has the potential to support life!")
                    else:
                        st.error("Your planet does not fall under the habitual zone! Please change its distance from the star so that it has the potential to support life!")

