# importar os pacotes necessários
import cv2
import csv
import os
from imutils import paths

# inicializa a lista de pontos de referência e indicação booleana
# se o corte está sendo executado ou não
refPt = []
cropping = False


def click_and_save(event, x, y, flags, param):

    # referências para as variáveis ​​globais
    global refPt

    # se o botão esquerdo do mouse foi clicado,
    # registre o início(x, y)

    if event == cv2.EVENT_LBUTTONDOWN:
        x != 0
        y != 0
        refPt = [(x, y)]

    # verifique se o botão esquerdo do mouse foi liberado
    elif event == cv2.EVENT_LBUTTONUP:

        # registra as coordenadas finais (x, y)
        # e indica que a operação de corte está terminada
        x != 0
        y != 0
        refPt.append((x, y))

        # desenhe um retângulo ao redor da região de interesse
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


# carrega a imagem, clona-a e configura a função de retorno de chamada do mouse
image = cv2.imread("jurassic_park_kitchen.jpg", 1)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_save)

# manter o loop até que a tecla 'q' seja pressionada
while True:
    # exibir a imagem e esperar por um pressionamento de tecla
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # se a tecla 'r' for pressionada, redefina a região de recorte
    if key == ord("r"):
        image = clone.copy()

    # se a tecla 'c' for pressionada, interrompa o loop
    elif key == ord("c"):
        break


# se houver dois pontos de referência, corte a região de interesse
# da imagem e exiba-a
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.waitKey(0)


# Salvando os dados no arquivo CSV
# inicializando as variáveis do arquivo CSV

for imagePath in paths.list_images("imgs"):
    row_filename = imagePath

# Convertendo as coordenadas em do tipo lista para string
row_coord = str(list(refPt))
row_coord = row_coord.strip("[]")

# Lendo o arquivo CSV
data = csv.reader(open('coordimage.csv', 'r'))


# inserindo dados na planilha CSV
insert = [row_filename, row_coord]
with open(r'coordimage.csv', 'a') as data:
        writer = csv.writer(data)
        writer.writerow(insert)

# Imprimindo as informações na tela para teste
print(row_filename + ', ' + str(row_coord))


# feche todas as janelas abertas
cv2.destroyAllWindows()
