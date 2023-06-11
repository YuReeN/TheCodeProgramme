import PySimpleGUI as sg
import time

def timer_gui(n):
    text_list = ['北海道', '青森', '岩手', '宮城', '秋田', '山形', '福島']
    interval = 5

    layout = [
        [sg.Text('')],
        [sg.Text('測定時間:', key='-TIME-', size=(40, 1), justification='center')],
        [sg.Text('')],
        [sg.Text("text1", key="-TEST-")],
        [sg.Text("text2", key="-TEST2-")],
        [sg.Button('スタート', key='-START-', size=(10, 1)), sg.Button('終了', key='-EXIT-', size=(10, 1))]
    ]

    window = sg.Window('タイマー', layout, finalize=True)
    start_time = None

    while True:
        event, values = window.read(timeout=1000)

        if event == sg.WINDOW_CLOSED or event == '-EXIT-':
            break

        if event == '-START-':
            start_time = time.time()
            count = 0

        if start_time is not None:
            elapsed_time = int(time.time() - start_time)
            remaining_time = interval - (elapsed_time % interval)
            
            time_index = elapsed_time // interval
            window["-TEST-"].update(text_list[time_index])
            window["-TEST2-"].update(text_list[time_index + 1])


            if elapsed_time // interval >= n:
                start_time = None
                window['-TIME-'].update('終了')
            else:
                window['-TIME-'].update(f'{remaining_time}秒')



    window.close()


n = 10
timer_gui(10)


# if __name__ == '__main__':
#     n = int(input('繰り返し回数（N）を入力してください: '))
#     timer_gui(n)
