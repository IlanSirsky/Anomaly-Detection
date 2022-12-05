import streamlit as st
import joblib
import numpy as np
import time
from PIL import Image

model = open("./model/finalized_model.pkl", "rb")
anomaly_model = joblib.load(model)


def predict_anomaly(data):
    result = anomaly_model.predict(data)
    return result


def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)


def main():
    """Anomaly Detection App
    With Streamlit

  """

    global prediction
    st.title("Anomaly Classifier")
    html_temp = """
  <div style="background-color:blue;padding:10px">
  <h2 style="color:grey;text-align:center;">Streamlit App </h2>
  </div>

  """
    st.markdown(html_temp, unsafe_allow_html=True)

    dur = st.number_input("Enter connection duration", min_value=0, step=1)
    src = st.number_input("Enter src_byte", min_value=0, step=1)
    dst = st.number_input("Enter dst_byte", min_value=0, step=1)
    if st.button("Predict"):
        result = predict_anomaly([[src]])
        if result[0] == -1:
            prediction = 'Anomaly'
        else:
            prediction = 'Not an anomaly'

        st.success('The connection: was classified as {}'.format(prediction))


if __name__ == '__main__':
    main()
