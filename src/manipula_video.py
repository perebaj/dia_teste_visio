#!/usr/bin/python3
# -*- coding: utf-8 -
import cv2
from Utils import calcula_tempo_corte, read_jsonfile

class Manipulate():
    """
    Manipula os dados de um video e executa a açao que esta no arquivo Json
    """
    def __init__(self, video, _task):
        """Dados base para manipulação do video

        Args:
            video (String): nome ou caminho para o video
        """
        self.name_video = video
        self.task = _task
        self.cap = cv2.VideoCapture(video)
        self.largura_video = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
        self.altura_video  = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        self.dimensao      = (self.largura_video, self.altura_video)
        self.fourcc        = cv2.VideoWriter_fourcc(*'XVID')
        self.frame_per_sec = self.cap.get(cv2.CAP_PROP_FPS)
        
    def leitura_video(self):
        # frame_count = 0

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            

    def corte_video(self):
        pass

    def time2frames(self, tempo_inicial, tempo_final):
        """calcula o tempo e segundos do corte inicial e final que será feito no video

        Args:
            tempo_inicial ([String]): Tempo incial no qual será feito  o corte
            tempo_final ([String]): Tempo final no qual será feito o corte
        """
        horas, minutos, segundos    = tempo_inicial.split(":")
        horas1, minutos1, segundos1 = tempo_final.split(":")

        tempo_inicial_segundos = int(horas)*3600 + int(minutos) * 60 + int(segundos) 
        tempo_final_segundos   = int(horas1)*3600  + int(minutos1)* 60 + int(segundos1)
        return tempo_final_segundos, tempo_inicial_segundos

    def split_video(self):
        pass
    def slice_video(self):
        nome_sem_extensao = self.name_video.split('.')[0]
        self.name_video = nome_sem_extensao + 'c' + '.mp4'
        out         = cv2.VideoWriter(self.name_video, self.fourcc, self.frame_per_sec, self.dimensao)
        frame_count = 0
        if frame_count >= frame_inicial and frame_count < frame_final:
                out.write(frame)
        elif frame_count == frame_final:
                break
        
        self.cap.release()
        out.release()    
    def append_video(self):
        pass