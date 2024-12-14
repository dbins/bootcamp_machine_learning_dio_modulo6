# -*- coding: utf-8 -*-
"""MODULO6_Yolo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1puiTsFiO5qHLDWR15E8o84NIr8kz4LKU
"""

# Commented out IPython magic to ensure Python compatibility.
import torch
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

# Carregar o modelo YOLOv5 pré-treinado (você pode usar o modelo 'yolov5s', que é mais leve e rápido)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' é uma versão mais leve e rápida

# Carregar a imagem de entrada
image_path = './imagem_teste.jpg'  # Substitua pelo caminho da sua imagem
img = cv2.imread(image_path)

# Realizar a detecção
results = model(img)

# Exibir o resultado na tela
results.show()  # Exibe a imagem com as caixas delimitadoras

# Salvar a imagem com o resultado
results.save()  # Salva a imagem na pasta 'runs/detect/exp'

# Exibir a imagem com o matplotlib para visualizar no Colab
# 'results.render()' retorna uma lista de imagens, então pegamos a primeira imagem da lista
rendered_img = results.render()[0]

# Converter de BGR para RGB para exibição no matplotlib
rendered_img_rgb = cv2.cvtColor(rendered_img, cv2.COLOR_BGR2RGB)

# Exibir a imagem com o matplotlib para visualizar no Colab
plt.imshow(rendered_img_rgb)  # Renderiza a imagem com a caixa delimitadora
plt.axis('off')
plt.show()