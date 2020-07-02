#!/usr/bin/python3
# -*- coding: utf-8 -
import cv2

class Manipulate():
    """
    Manipula os dados de um video e executa a açao que esta no arquivo Json
    """
    def __init__(self, video, _task, _timestamps):
        """Dados base para manipulação do video

        Args:
            video (String): nome ou caminho para o video
        """
        self.nome_video = video
        self.task = _task
        self.timestamps = _timestamps
        self.cap = cv2.VideoCapture(video)
        self.largura_video = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
        self.altura_video  = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        self.dimensao      = (self.largura_video, self.altura_video)
        self.fourcc        = cv2.VideoWriter_fourcc(*"mp4v")
        # self.fourcc = int(self.cap.get(cv2.CAP_PROP_FOURCC))
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

        tempo_inicial_segundos = int(horas) *3600  + int(minutos) * 60 + int(segundos) 
        tempo_final_segundos   = int(horas1)*3600  + int(minutos1)* 60 + int(segundos1)

        frame_inicial  =  self.frame_per_sec * tempo_inicial_segundos
        frame_final    =  self.frame_per_sec * tempo_final_segundos
        return frame_inicial, frame_final

    def split_video(self, frame_split):
        """Cortar video de acordo com o parâmetro de corte {frame_split} gerando dois videos 

        Args:
            frame_split (Int): frame que sera cortado
        """
        nome_sem_extensao = self.nome_video.split('.')[0]
        nome_video_saida1 = nome_sem_extensao + 'a' + '.mp4'
        nome_video_saida2 = nome_sem_extensao + 'b' + '.mp4'
        out1              = cv2.VideoWriter(nome_video_saida1, self.fourcc, self.frame_per_sec, self.dimensao)
        out2              = cv2.VideoWriter(nome_video_saida2, self.fourcc, self.frame_per_sec, self.dimensao)
        frame_count        = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret == True:
                if frame_count < frame_split:
                    out1.write(frame)
                elif frame_count >= frame_split:
                    out2.write(frame)
            else:
                break
            frame_count += 1
            # print(frame_count)
        self.cap.release()
        out1.release()
        out2.release()   
        cv2.destroyAllWindows()

    def slice_video(self):
        nome_sem_extensao = self.nome_video.split('.')[0]
        nome_video_saida  = nome_sem_extensao + 'c' + '.mp4'
        out               = cv2.VideoWriter(nome_video_saida, self.fourcc, self.frame_per_sec, self.dimensao)
        frame_inicial, frame_final = self.time2frames(self.timestamps[0], self.timestamps[1])
        frame_count       = 0 
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if frame_count >= frame_inicial and frame_count < frame_final:
                out.write(frame)
            elif frame_count == frame_final:
                break
            frame_count += 1

        self.cap.release()
        out.release()    
        cv2.destroyAllWindows()

    def append_video(self, to_append):
        video2_append     = cv2.VideoCapture(to_append)
        nome_sem_extensao = self.nome_video.split('.')[0]
        nome_video_saida  = nome_sem_extensao + 'd' + '.mp4'
        out               = cv2.VideoWriter(nome_video_saida, self.fourcc, self.frame_per_sec, self.dimensao)
        frame_count        = 0 
        while self.cap.isOpened():
            # print(self.cap.isOpened())
            ret, frame = self.cap.read()
            if ret == True:
                out.write(frame)
            else:
                ret2, frame2 = video2_append.read()
                if ret2 == True:
                    out.write(frame2)
                else: break


        self.cap.release()
        out.release()
        # video2_append.release()
        cv2.destroyAllWindows()

teste = Manipulate('1591803600_033a.mp4', 'slice', ['00:01:30', '00:01:50'])
# teste.split_video(1000)
teste.append_video('1591803600_033b.mp4')