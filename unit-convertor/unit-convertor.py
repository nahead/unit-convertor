import streamlit as st # type: ignore
from pint import UnitRegistry # type: ignore

# Initialize unit registry
ureg = UnitRegistry()

st.title("Google-Style Unit Converter")

# Unit categories
categories = {
    "Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "cup"]
}

category= st.selectbox("chose category",list(categories.keys()))
from_unit= st.selectbox("from ", categories[category])
to_unit=st.selectbox("to",categories[category])

value=st.number_input(f"enter value" ,min_value=1, format="%.2f")
if st.button("convert"):
    try:
        res=(value*ureg(from_unit)).to(to_unit)
        st.success(f"{from_unit} = {res.magnitude:.4f}  {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")
