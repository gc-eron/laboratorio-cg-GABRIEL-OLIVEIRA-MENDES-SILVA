import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")

imagem = np.zeros((8, 8), dtype=np.uint8)
imagem[2, 5] = 255
imagem[4:, :] = 128
st.image(ampliar(imagem))
st.write(imagem)

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)

bandeira[:] = (0, 150, 57)
bandeira[0:5, 0:9] = (255, 255, 255)
bandeira[1:6, 1:10] = (255, 255, 255)
bandeira[2:7, 2:11] = (255, 255, 255)
bandeira[3:8, 3:12] = (255, 255, 255)
bandeira[4:9, 4:13] = (255, 255, 255)
bandeira[5:10, 5:14] = (255, 255, 255)
bandeira[6:11, 6:15] = (255, 255, 255)
bandeira[7:12, 7:16] = (255, 255, 255)
bandeira[8:12, 8:17] = (255, 255, 255)
bandeira[9:12, 17] = (255, 255, 255)
bandeira[5:8, 6:12] = (0, 51, 160)
bandeira[4:9, 7:11] = (0, 51, 160)
st.image(ampliar(bandeira))