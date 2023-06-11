import PySimpleGUI as sg
import time
import winsound
import threading

interval = 1
text_list = ["首を左右、前後、ゆっくり回す",
             "胸を張って肩を耳に当てる",
             "肩を大きく回す",
             "上から肩甲骨を寄せる",
             "大きく腕を挙げる",
             "体側を伸ばす",
             "肘を伸ばして腕を後ろに回す",
             "力こぶを収縮",
             "二の腕を収縮",
             "腕を横で大きく回す",
             "腹筋を意識して足を引き上げる",
             "お尻を突き出して軽く屈伸",
             "つま先をタッチ",
             "屈伸、膝回し",
             "足首を掴んでスクワット",
             "膝に手をついて肩を入れる",
             "股関節開きながらスクワット",
             "股関節の前を伸ばす、左",
             "股関節の前を伸ばす、右",
             "足を左右に開いてつま先タッチ",
             "腓腹筋伸ばし、左",
             "腓腹筋伸ばし、右",
             ""
             ]


def play_beep_small():
    winsound.Beep(400, 500)

def play_beep_big():
    winsound.Beep(600, 1000)
    

def timer_gui(n):

    
    sg.theme("DarkAmber")
    size1 = (10, 1)
    
    text1_layout = [
        [sg.Text('', font=60, ), sg.Text("", key="-TEST-", font = 60)]
    ]
    
    text2_layout = [
        [sg.Text('', font = 60), sg.Text("", key="-TEST2-")]
    ]
    
    button_layout = [
        [sg.Button('スタート' , key='-START-', font = 10), sg.Button('終了', key='-EXIT-', font = 10)]
    ]

    
    layout = [
        [sg.Text('')],
        [sg.Text('開始', key='-TIME-', justification='center', font=5000, size=(200,2))],
        [sg.Text('')],
        [sg.Column(text1_layout, justification="center")],
        [sg.Text('')],
        [sg.Column(text2_layout,justification="center")],
        [sg.Text('')],
        [sg.Column(button_layout, justification="center")],
    ]

    window = sg.Window('動的ストレッチ', layout, finalize=True, size=(800, 500))
    start_time = None

    while True:
        event, values = window.read(timeout=1000)

        if event == sg.WINDOW_CLOSED or event == '-EXIT-':
            break

        if event == '-START-':
            
            for i in range(3, 0, -1):
                window['-TIME-'].update(f"{i}秒")
                window.refresh()
                if 2 <= i <= 3:
                    winsound.Beep(400, 500)
                    time.sleep(0.5)
                elif i == 1:
                    winsound.Beep(600, 1000)
                    time.sleep(0)

            start_time = time.time()

        if start_time is not None:
            elapsed_time = int(time.time() - start_time)
            remaining_time = interval - (elapsed_time % interval)
            if 2 <= remaining_time <= 3:
                threading.Thread(target=play_beep_small).start()
            elif remaining_time == 1:
                threading.Thread(target=play_beep_big).start()
            
            time_index = elapsed_time // interval
            window["-TEST-"].update(text_list[time_index])
            window["-TEST2-"].update(text_list[time_index + 1])


            if elapsed_time // interval >= n:
                start_time = None
                window['-TIME-'].update('終了')
            else:
                window['-TIME-'].update(f'{remaining_time}秒')



    window.close()


times = len(text_list)
timer_gui(times)


# if __name__ == '__main__':
#     n = int(input('繰り返し回数（N）を入力してください: '))
#     timer_gui(n)
