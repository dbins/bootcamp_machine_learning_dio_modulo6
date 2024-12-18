# -*- coding: utf-8 -*-
"""MODULO6_SSD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10ctK8eHjJJ_ScL5KAorD_4N10kvEuTDf
"""

import torch
import matplotlib.pyplot as plt
from torchvision import models, transforms
from PIL import Image, ImageDraw

# Carregar o modelo SSD pré-treinado
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Preparar imagem
img = Image.open("./imagem_teste.jpg")
transform = transforms.Compose([transforms.ToTensor()])
img_tensor = transform(img).unsqueeze(0)

# Realizar a detecção
with torch.no_grad():
    prediction = model(img_tensor)

# Definir um limiar de confiança (threshold) para melhorar as detecções
confidence_threshold = 0.8  # Apenas detectar se a confiança for maior que 80%

# Desenhar as caixas delimitadoras
draw = ImageDraw.Draw(img)
for element, score in zip(prediction[0]['boxes'], prediction[0]['scores']):
    if score > confidence_threshold:  # Verificar a confiança da predição
        x1, y1, x2, y2 = element
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

#Salvar imagem com a marcação dos rostos detectados
img.save("./resultado.jpg")

# Exibir imagem
img.show()

# Exibir a imagem usando matplotlib
plt.imshow(img)
plt.axis('off')  # Para não mostrar os eixos
plt.show()