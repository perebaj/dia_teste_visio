#!/usr/bin/python3
# -*- coding: utf-8 -
import cv2

class Manipulate():
    """
    Manipula os dados de um video e executa a açao que esta no arquivo Json
    """
    def __init__(self, video, _task, _params):
        """Dados base para manipulação do video

        Args:
            video (String): nome ou caminho para o video
        """
        self.params        = _params
        self.nome_video    = video
        # print(self.nome_video)
        self.task          = _task
        self.cap           = cv2.VideoCapture(self.nome_video, cv2.CAP_FFMPEG)
        self.largura_video = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
        self.altura_video  = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        self.dimensao      = (self.largura_video, self.altura_video)
        self.fourcc        = cv2.VideoWriter_fourcc(*"mp4v")
        self.frame_per_sec = self.cap.get(cv2.CAP_PROP_FPS)
        # self.fourcc        = int(self.cap.get(cv2.CAP_PROP_FOURCC))

        # self.fourcc        = cv2.VideoWriter_fourcc(cap_fourcc)
    
            
    def execute_tasks(self):
        if self.task == 'split':
            timestamp = self.params['timestamp']
            frame = self.time2frames(timestamp)
            self.split_video(frame)
        if self.task == 'slice':
            timestamp = self.params['timestamps']
            frames = []
            for times in timestamp: frames.append(self.time2frames(times))
            self.slice_video(frames[0], frames[1])
        if self.task == 'append':
            self.append_video(self.params['to_append'])


    def time2frames(self, time):
        """calcula o tempo e segundos do corte inicial e final que será feito no video

        Args:
            tempo_inicial ([String]): Tempo incial no qual será feito  o corte
            tempo_final ([String]): Tempo final no qual será feito o corte
        """
        horas, minutos, segundos    = time.split(":")
        tempo_segundos = int(horas) *3600  + int(minutos) * 60 + int(segundos) 
    

        frame  =  self.frame_per_sec * tempo_segundos
        return frame
    def split_video(self, frame_split):
        """Cortar video de acordo com o parâmetro de corte {frame_split} gerando dois videos 

        Args:
            frame_split (Int): frame que sera cortado
        """
        nome_sem_extensao = self.nome_video.split('.')[0]
        nome_video_saida1 = nome_sem_extensao + 'a' + '.mp4'
        nome_video_saida2 = nome_sem_extensao + 'b' + '.mp4'
        out1              = cv2.VideoWriter(nome_video_saida1, cv2.CAP_FFMPEG, self.fourcc, self.frame_per_sec, self.dimensao)
        out2              = cv2.VideoWriter(nome_video_saida2, cv2.CAP_FFMPEG,self.fourcc, self.frame_per_sec, self.dimensao)
        print('teste')
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

    def slice_video(self, frame_inicial, frame_final):
        nome_sem_extensao = self.nome_video.split('.')[0]
        nome_video_saida  = nome_sem_extensao + 'c' + '.mp4'
        out               = cv2.VideoWriter(nome_video_saida, cv2.CAP_FFMPEG, self.fourcc, self.frame_per_sec, self.dimensao)
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
        video2_append     = cv2.VideoCapture(to_append, cv2.CAP_FFMPEG)
        nome_sem_extensao = self.nome_video.split('.')[0]
        nome_video_saida  = nome_sem_extensao + 'd' + '.mp4'
        out               = cv2.VideoWriter(nome_video_saida, cv2.CAP_FFMPEG, self.fourcc, self.frame_per_sec, self.dimensao)
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
        video2_append.release()
        cv2.destroyAllWindows()


mensagem_teste_append = {
        "video": "1591821600_015.mp4",
        "task": "append",
        "params": {
            "to_append": "1591822800_002.mp4"
        }
    }

mensagem_teste_slice = {
        "video": "1591821600_015.mp4",
        "task": "slice",
        "params": {
            "timestamps": [
                "00:00:20",
                "00:00:50"
            ]
        }
    }
mensagem_teste_split ={
        "video": "1591821600_015.mp4",
        "task": "split",
        "params": {
            "timestamp": "00:0:20"
        }
    }

teste = Manipulate(mensagem_teste_split['video'], mensagem_teste_split['task'], mensagem_teste_split['params'])
# teste.append_video('1591803600_033a.mp4')
teste.execute_tasks()
