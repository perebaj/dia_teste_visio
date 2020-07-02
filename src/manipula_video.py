#!/usr/bin/python3
# -*- coding: utf-8 -
import cv2
from Utils import calcula_tempo_corte, read_jsonfile

class Manipulate():
    """
    Manipula os dados de um video e executa a açao que esta no arquivo Json
    """
    def __init__(self, video):
        """Dados base para manipulação do video

        Args:
            video (String): nome ou caminho para o video
        """
        cap = cv2.VideoCapture(video)
        largura_video = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
        altura_video  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        dimensao      = (largura_video, altura_video)
        fourcc        = cv2.VideoWriter_fourcc(*'XVID')
        frame_per_sec = cap.get(cv2.CAP_PROP_FPS)
        

    def leitura_video(self):
        pass

    def corte_video(self):
        pass

    def time2frames(self, tempo_inicial, tempo_final):
        pass

    