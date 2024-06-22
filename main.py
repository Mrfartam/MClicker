from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation
from random import randint
import time


class MyApp(App):
    def __init__(self):
        super().__init__()
        wind = str(Window.size)
        self.wid = int(wind[1:wind.find(',')])
        self.hei = int(wind[wind.find(' ') + 1:-1])
        self.razm = (self.wid / self.hei)
        self.btns = [0]*64
        self.key = 0
        self.count = 10
        self.coord = [randint(0, int(0.8 * self.wid)), randint(0, int(self.hei * (1 - 0.28 * self.razm)))]
        for i in range(64):
            self.btns[i] = Button(text='', size_hint=(0.025, 0.025 * self.razm), background_normal='',
                                  background_down='')
        self.fl = FloatLayout()
        self.btn_start = Button(text='Начать', font_size=30, size_hint=(0.25, 0.1 * self.razm),
                                background_color=[141 / 255, 187 / 255, 37 / 255, 1], background_normal='',
                                background_down='', color=[198 / 255, 3 / 255, 125 / 255, 1],
                                pos=(0.375 * self.wid, 0.5 * self.hei))
        self.btn_record = Button(text='Рекорды', font_size=30, size_hint=(0.25, 0.1 * self.razm),
                                 background_color=[198 / 255, 3 / 255, 125 / 255, 1], background_normal='',
                                 background_down='', color=[141 / 255, 187 / 255, 37 / 255, 1],
                                 pos=(0.375 * self.wid, 0.5 * self.hei - 0.1 * self.wid))
        self.btn_start.bind(on_press=self.start)
        self.btn_record.bind(on_press=self.record)
        self.anch_exit = AnchorLayout(anchor_x='right', anchor_y='top')
        self.anch_count = AnchorLayout(anchor_x='left', anchor_y='top')
        self.fl_lvl = FloatLayout()
        self.btn_exit = Button(text="x", font_size=30, size_hint=(0.07, 0.07*self.razm), background_color=[1, 0, 0, 1],
                               background_normal='', background_down='')
        self.btn_count = Button(font_size=30, size_hint=(0.07, 0.07*self.razm),
                                background_color=[132/255, 132/255, 132/255, 1], background_normal='', background_down='')
        self.btn_lvl = Button(font_size=30, size_hint=(0.25, 0.07*self.razm),
                              pos=(0.375 * self.wid, self.hei * (1 - 0.07 * self.razm)), background_color=[1, 1, 1, 1],
                              background_normal='', background_down='', color=[0, 0, 0, 1])
        self.btn_lvl.bind(on_press=self.recovery)
        self.fl_lvl.add_widget(self.btn_lvl)
        self.btn_exit.bind(on_press=self.exit)
        self.anch_exit.add_widget(self.btn_exit)
        self.anch_count.add_widget(self.btn_count)
        self.time_start = 0
        self.time_end = 0
        self.save_file = open("save.txt", "a+")
        self.cnt = 0
        self.btn_statistic = Button(text='', font_size=30, halign='center', size_hint=(0.25, 0.1 * self.razm),
                                    background_color=[237 / 255, 145 / 255, 33 / 255, 1], background_normal='',
                                    background_down='', color=[49 / 255, 0 / 255, 98 / 255, 1],
                                    pos=(0.375 * self.wid, 0.5 * self.hei))
        self.btn_back = Button(text='Назад', font_size=30, size_hint=(0.25, 0.1 * self.razm),
                               background_color=[141 / 255, 187 / 255, 37 / 255, 1], background_normal='',
                               background_down='', color=[198 / 255, 3 / 255, 125 / 255, 1],
                               pos=(0.375 * self.wid, 0.5 * self.hei - 0.1 * self.wid))
        self.btn_back.bind(on_press=self.back)

    def build(self):
        btns = [0] * 256
        green_1 = randint(0, 31)
        green_2 = randint(0, 31)
        green_3 = randint(1, 31)
        green_4 = randint(1, 31)
        cloud_1 = [randint(128, 255)] * 6
        for j in range(1, 6):
            cloud_1[j] = cloud_1[0] + j
            if j in [4, 5]:
                cloud_1[j] = cloud_1[0] + j + 13
        cloud_2 = [randint(128, 255)] * 6
        for j in range(1, 6):
            cloud_2[j] = cloud_2[0] + j
            if j in [4, 5]:
                cloud_2[j] = cloud_2[0] + j + 13
        cloud_3 = [randint(128, 255)] * 2
        cloud_3[1] = cloud_3[0] + 1
        tree_wood = [40, 56, 72, 73, 88]
        tree_leafs = [86, 87, 89, 90, 102, 103, 104, 105, 106, 119, 120, 121]
        if int(time.strftime('%H', time.localtime(time.time()))) in range(7, 19):
            sun = [238, 237, 222, 221]
            for i in range(256):
                btns[i] = Button(text='', size_hint=(1 / 16, 1 / 16), background_normal='', background_down='',
                                 pos=(self.wid * 1 / 16 * (i % 16), self.hei * 1 / 16 * (i // 16)))
                if i in range(32):
                    btns[i].background_color = [3 / 255, 192 / 255, 60 / 255, 1]
                if i == green_1 or i == green_2:
                    btns[i].background_color = [0 / 255, 168 / 255, 107 / 255, 1]
                if i == green_3 or i == green_4:
                    btns[i - 1].background_color = [0 / 255, 168 / 255, 107 / 255, 1]
                    btns[i].background_color = [0 / 255, 168 / 255, 107 / 255, 1]
                if i in range(32, 256):
                    btns[i].background_color = [0 / 255, 191 / 255, 255 / 255, 1]
                if i in tree_wood:
                    btns[i].background_color = [204 / 255, 119 / 255, 34 / 255, 1]
                if i in tree_leafs:
                    btns[i].background_color = [218 / 255, 112 / 255, 214 / 255, 1]
                if i in sun:
                    btns[i].background_color = [253 / 255, 233 / 255, 16 / 255, 1]
                if i in cloud_1 or i in cloud_2 or i in cloud_3:
                    btns[i].background_color = [255 / 255, 240 / 255, 245 / 255, 1]
                self.fl.add_widget(btns[i])
        else:
            sun = [225, 226, 209, 210]
            for i in range(256):
                btns[i] = Button(text='', size_hint=(1 / 16, 1 / 16), background_normal='', background_down='',
                                 pos=(self.wid * 1 / 16 * (i % 16), self.hei * 1 / 16 * (i // 16)))
                if i in range(32):
                    btns[i].background_color = [17 / 255, 96 / 255, 98 / 255, 1]
                if i == green_1 or i == green_2:
                    btns[i].background_color = [23 / 255, 114 / 255, 69 / 255, 1]
                if i == green_3 or i == green_4:
                    btns[i - 1].background_color = [23 / 255, 114 / 255, 69 / 255, 1]
                    btns[i].background_color = [23 / 255, 114 / 255, 69 / 255, 1]
                if i in range(32, 256):
                    btns[i].background_color = [0 / 255, 20 / 255, 168 / 255, 1]
                if i in tree_wood:
                    btns[i].background_color = [114 / 255, 47 / 255, 55 / 255, 1]
                if i in tree_leafs:
                    btns[i].background_color = [139 / 255, 0 / 255, 255 / 255, 1]
                if i in sun:
                    btns[i].background_color = [146 / 255, 0 / 255, 10 / 255, 1]
                if i in cloud_1 or i in cloud_2 or i in cloud_3:
                    btns[i].background_color = [0 / 255, 49 / 255, 83 / 255, 1]
                self.fl.add_widget(btns[i])
        self.fl.add_widget(self.btn_start)
        self.fl.add_widget(self.anch_exit)
        self.fl.add_widget(self.btn_record)
        return self.fl

    def recovery(self, z):
        if self.key > 10:
            for i in range(64):
                self.fl.remove_widget(self.btns[i])
            self.fl.remove_widget(self.fl_lvl)
            self.fl.remove_widget(self.anch_count)
            self.fl.remove_widget(self.anch_exit)
            self.fl.add_widget(self.btn_start)
            self.fl.add_widget(self.btn_record)
            self.fl.add_widget(self.anch_exit)
            self.key = 0
            return self.fl

    def exit(self, z):
        self.save_file.close()
        Window.close()

    def start(self, z):
        if self.key == 0:
            self.time_start = time.strftime('%H %M %S', time.localtime(time.time()))
            self.cnt = 0
            self.key += 1
        self.fl.remove_widget(self.anch_count)
        self.fl.remove_widget(self.fl_lvl)
        self.fl.remove_widget(self.btn_record)
        self.fl.add_widget(self.anch_count)
        self.fl.add_widget(self.fl_lvl)
        self.btn_count.text = str(self.count)
        if self.key < 11:
            self.btn_lvl.text = "Уровень: " + str(self.key)
            if self.key == 1:
                self.block_1(self.coord)
            elif self.key == 2:
                self.block_2(self.coord)
            elif self.key == 3:
                self.block_3(self.coord)
            elif self.key == 4:
                self.block_4(self.coord)
            elif self.key == 5:
                self.block_5(self.coord)
            elif self.key == 6:
                self.block_6(self.coord)
            elif self.key == 7:
                self.block_7(self.coord)
            elif self.key == 8:
                self.block_8(self.coord)
            elif self.key == 9:
                self.block_9(self.coord)
            elif self.key == 10:
                self.block_10(self.coord)
        else:
            self.win(self.coord)
            self.btn_lvl.text = "Победа!!!"
            self.time_end = time.strftime('%H %M %S', time.localtime(time.time()))
            self.save_file.write(str(self.cnt) + " " + self.time_record(self.time_start, self.time_end)+'\n')

    def record(self, z):
        self.fl.remove_widget(self.btn_record)
        self.fl.remove_widget(self.btn_start)
        self.save_file.close()
        self.save_file = open("save.txt", "r")
        rec = self.save_file.readlines()
        self.save_file.close()
        self.save_file = open("save.txt", "a")
        steps = []
        tm = []
        times = []
        if not rec:
            self.btn_statistic.text = 'Вы ещё ни разу\nне завершили \nигру'
        else:
            for s in rec:
                steps0, tm0 = list(map(str, s.split(' ')))
                times.append(tm0)
                steps.append(int(steps0))
                tm1 = list(map(int, tm0.split(':')))
                tm2 = tm1[0] * 3600 + tm1[1] * 60 + tm1[2]
                tm.append(tm2)
            min_i_tm, min_i_steps = len(tm), len(steps)
            for i in range(len(tm)):
                if tm[i] == min(tm):
                    min_i_tm = i
                    break
            for i in range(len(tm)):
                if steps[i] == min(steps):
                    min_i_steps = i
                    break
            st = str(min(steps)) + ' х. ' + times[min_i_steps]
            tim = str(steps[min_i_tm]) + ' х. ' + times[min_i_tm]
            self.btn_statistic.text = 'Ваши рекорды:\nПо ходам: ' + st + 'По времени: ' + tim
        self.fl.add_widget(self.btn_statistic)
        self.fl.add_widget(self.btn_back)
        return self.fl

    def back(self, z):
        self.fl.remove_widget(self.btn_statistic)
        self.fl.remove_widget(self.btn_back)
        self.fl.add_widget(self.btn_start)
        self.fl.add_widget(self.btn_record)
        return self.fl

    def time_record(self, time_start, time_end):
        hour_start, minute_start, second_start = list(map(int, time_start.split(' ')))
        hour_end, minute_end, second_end = list(map(int, time_end.split(' ')))
        second_different = second_end - second_start
        minute_different = minute_end - minute_start
        hour_different = hour_end - hour_start
        if second_different < 0:
            second_different += 60
            minute_different -= 1
        if minute_different < 0:
            minute_different += 60
            hour_different -= 1
        return str(hour_different) + ':' + str(minute_different) + ':' + str(second_different)

    def lvl_up(self, z):
        self.cnt += 1
        lvl_up = randint(1, 10)
        if lvl_up == 1:
            self.key += 1
            self.count = 10
            self.btn_count.text = str(self.count)
            for i in range(64):
                self.fl.remove_widget(self.btns[i])
            self.start(self.coord)
        else:
            self.anim(1)

    def anim(self, z):
        anim = [0]*64
        self.coord = [randint(0, int(0.8 * self.wid)), randint(0, int(self.hei * (1 - 0.28 * self.razm)))]
        for i in range(64):
            anim[i] = Animation(x=self.coord[0]+self.wid*0.025*(i % 8), y=self.coord[1]+self.wid*0.025*(i//8))
            anim[i].start(self.btns[i])
        self.count -= 1
        self.btn_count.text = str(self.count)
        if self.count == 0:
            self.key = 1
            self.count = 10
            self.btn_count.text = str(self.count)
            self.start(self.coord)

    def block_1(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0]+self.wid*0.025*(i % 8), self.coord[1] + self.wid * 0.025*(i // 8))
            if i in [0, 1, 6, 7, 11, 13, 14, 16, 20, 25, 28, 30, 31, 32, 34, 35, 38, 41]:
                self.btns[i].background_color = [87/255, 62/255, 40/255, 1]
            elif i in [2, 3, 8, 15, 17, 22, 27, 37, 39]:
                self.btns[i].background_color = [133 / 255, 98 / 255, 66 / 255, 1]
            elif i in [4, 5, 9, 18, 19, 21, 24, 26, 29]:
                self.btns[i].background_color = [109 / 255, 79 / 255, 53 / 255, 1]
            elif i in [10, 23, 36, 40, 42, 43, 45, 46, 47, 49, 55]:
                self.btns[i].background_color = [64 / 255, 45 / 255, 29 / 255, 1]
            elif i == 12:
                self.btns[i].background_color = [97 / 255, 99 / 255, 96 / 255, 1]
            elif i == 33:
                self.btns[i].background_color = [78 / 255, 78 / 255, 76 / 255, 1]
            elif i in [44, 48, 53, 54, 56, 60, 62]:
                self.btns[i].background_color = [60 / 255, 95 / 255, 44 / 255, 1]
            elif i in [50, 52]:
                self.btns[i].background_color = [61 / 255, 90 / 255, 44 / 255, 1]
            elif i in [58, 63]:
                self.btns[i].background_color = [54 / 255, 82 / 255, 39 / 255, 1]
            elif i in [51, 57, 59, 61]:
                self.btns[i].background_color = [50 / 255, 78 / 255, 37 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_2(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [0, 1, 6, 7, 39]:
                self.btns[i].background_color = [76 / 255, 59 / 255, 33 / 255, 1]
            elif i in [2, 3, 5]:
                self.btns[i].background_color = [94 / 255, 74 / 255, 41 / 255, 1]
            elif i in [4, 15, 23, 32]:
                self.btns[i].background_color = [111 / 255, 85 / 255, 47 / 255, 1]
            elif i in [8, 16, 26, 31, 40, 47, 57, 59]:
                self.btns[i].background_color = [117 / 255, 98 / 255, 56 / 255, 1]
            elif i in [24, 48, 55, 56, 58]:
                self.btns[i].background_color = [138 / 255, 110 / 255, 71 / 255, 1]
            elif i in [25, 27, 28, 29, 30, 58, 60, 61, 62, 63]:
                self.btns[i].background_color = [144 / 255, 117 / 255, 72 / 255, 1]
            elif i in [9, 13, 20, 41]:
                self.btns[i].background_color = [140 / 255, 16 / 255, 15 / 255, 1]
            elif i in [12, 33]:
                self.btns[i].background_color = [106 / 255, 13 / 255, 12 / 255, 1]
            elif i in [19, 35, 44]:
                self.btns[i].background_color = [86 / 255, 106 / 255, 13 / 255, 1]
            elif i in [11, 36]:
                self.btns[i].background_color = [71 / 255, 85 / 255, 10 / 255, 1]
            elif i in [10, 46]:
                self.btns[i].background_color = [35 / 255, 74 / 255, 120 / 255, 1]
            elif i in [17, 21, 22, 51, 52, 54]:
                self.btns[i].background_color = [32 / 255, 24 / 255, 14 / 255, 1]
            elif i in [18, 43, 49, 50]:
                self.btns[i].background_color = [48 / 255, 37 / 255, 19 / 255, 1]
            elif i == 14:
                self.btns[i].background_color = [12 / 255, 105 / 255, 80 / 255, 1]
            elif i == 34:
                self.btns[i].background_color = [73 / 255, 29 / 255, 5 / 255, 1]
            elif i == 42:
                self.btns[i].background_color = [89 / 255, 36 / 255, 5 / 255, 1]
            elif i == 37:
                self.btns[i].background_color = [101 / 255, 93 / 255, 6 / 255, 1]
            elif i == 45:
                self.btns[i].background_color = [135 / 255, 135 / 255, 135 / 255, 1]
            elif i == 53:
                self.btns[i].background_color = [126 / 255, 115 / 255, 6 / 255, 1]
            elif i == 38:
                self.btns[i].background_color = [32 / 255, 58 / 255, 91 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_3(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [0, 15, 22, 26, 30, 36, 44, 51, 57, 59, 62, 63]:
                self.btns[i].background_color = [119 / 255, 64 / 255, 8 / 255, 1]
            elif i in [1, 3, 6, 7, 20, 28]:
                self.btns[i].background_color = [93 / 255, 45 / 255, 10 / 255, 1]
            elif i in [2, 4, 10, 11, 12, 13, 34, 38, 42, 43, 46]:
                self.btns[i].background_color = [51 / 255, 12 / 255, 0 / 255, 1]
            elif i in [5, 9, 14, 17, 19, 21, 41, 45, 49, 50, 53, 54]:
                self.btns[i].background_color = [34 / 255, 0 / 255, 0 / 255, 1]
            elif i in [8, 18, 55, 61]:
                self.btns[i].background_color = [146 / 255, 83 / 255, 14 / 255, 1]
            elif i in [16, 23, 25, 27, 29, 31, 32, 33, 35, 39, 40, 47, 48, 52, 58, 60]:
                self.btns[i].background_color = [169 / 255, 102 / 255, 21 / 255, 1]
            elif i in [24, 37, 56]:
                self.btns[i].background_color = [169 / 255, 124 / 255, 56 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_4(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [0, 1, 2, 3, 16, 47, 60]:
                self.btns[i].background_color = [44 / 255, 44 / 255, 44 / 255, 1]
            elif i in [4, 5, 6, 7, 8, 15, 23, 24, 31, 32, 39, 40, 48, 55, 56, 57, 58, 59, 61, 62, 63]:
                self.btns[i].background_color = [60 / 255, 58 / 255, 59 / 255, 1]
            elif i in [9, 14, 38, 41, 53]:
                self.btns[i].background_color = [108 / 255, 108 / 255, 108 / 255, 1]
            elif i in [17, 22]:
                self.btns[i].background_color = [131 / 255, 131 / 255, 131 / 255, 1]
            elif i in [21, 33, 42, 46, 50]:
                self.btns[i].background_color = [68 / 255, 68 / 255, 68 / 255, 1]
            elif i in [45, 49, 51, 52, 54]:
                self.btns[i].background_color = [99 / 255, 99 / 255, 99 / 255, 1]
            elif i in [25, 26, 27, 28, 29, 30]:
                self.btns[i].background_color = [147 / 255, 147 / 255, 147 / 255, 1]
            elif i in [10, 13, 19, 20, 34, 37]:
                self.btns[i].background_color = [13 / 255, 13 / 255, 13 / 255, 1]
            elif i in [11, 12, 18, 35, 36, 43, 44]:
                self.btns[i].background_color = [25 / 255, 25 / 255, 25 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_5(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [0, 15, 16, 20, 38, 42, 49, 61]:
                self.btns[i].background_color = [106 / 255, 46 / 255, 47 / 255, 1]
            elif i in [5, 8, 18, 19, 30, 33, 36, 37, 44, 47, 55, 59, 60, 62]:
                self.btns[i].background_color = [94 / 255, 38 / 255, 37 / 255, 1]
            elif i in [2, 4, 13, 29, 32, 41, 48]:
                self.btns[i].background_color = [74 / 255, 25 / 255, 26 / 255, 1]
            elif i in [3, 7, 10, 11, 12, 40, 45]:
                self.btns[i].background_color = [61 / 255, 21 / 255, 21 / 255, 1]
            elif i in [1, 17, 21, 26, 31, 35, 39, 56, 57]:
                self.btns[i].background_color = [215 / 255, 93 / 255, 15 / 255, 1]
            elif i in [6, 9, 25, 27, 34, 46, 52, 54, 63]:
                self.btns[i].background_color = [188 / 255, 73 / 255, 6 / 255, 1]
            elif i in [28, 43, 53, 58]:
                self.btns[i].background_color = [229 / 255, 124 / 255, 32 / 255, 1]
            elif i in [14, 22, 23, 24, 50, 51]:
                self.btns[i].background_color = [233 / 255, 148 / 255, 65 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_6(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [0, 5, 6, 23, 31, 34, 36, 51]:
                self.btns[i].background_color = [120 / 255, 99 / 255, 92 / 255, 1]
            elif i in [7, 15, 35, 43]:
                self.btns[i].background_color = [124 / 255, 110 / 255, 105 / 255, 1]
            elif i in [1, 2, 3, 4, 32, 33, 37, 38, 39, 59]:
                self.btns[i].background_color = [103 / 255, 82 / 255, 77 / 255, 1]
            elif i in [8, 14, 16, 41, 42, 44, 45]:
                self.btns[i].background_color = [91 / 255, 50 / 255, 41 / 255, 1]
            elif i in [11, 12, 13, 22, 40, 52]:
                self.btns[i].background_color = [101 / 255, 51 / 255, 40 / 255, 1]
            elif i in [9, 21, 46, 47, 50, 53]:
                self.btns[i].background_color = [108 / 255, 59 / 255, 47 / 255, 1]
            elif i in [10, 17, 18, 19, 20, 28, 30, 48, 49, 54, 55, 58]:
                self.btns[i].background_color = [116 / 255, 64 / 255, 50 / 255, 1]
            elif i in [26, 27, 29, 56, 57, 63]:
                self.btns[i].background_color = [132 / 255, 72 / 255, 57 / 255, 1]
            elif i in [24, 25, 60, 61, 62]:
                self.btns[i].background_color = [146 / 255, 78 / 255, 60 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_7(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [8, 10, 12, 15, 40]:
                self.btns[i].background_color = [112 / 255, 53 / 255, 32 / 255, 1]
            elif i in [9, 11, 13, 41, 43, 44, 45]:
                self.btns[i].background_color = [111 / 255, 60 / 255, 31 / 255, 1]
            elif i in [14, 42, 46, 47]:
                self.btns[i].background_color = [108 / 255, 48 / 255, 26 / 255, 1]
            elif i in [0, 2, 4, 6, 16, 18, 26, 33, 35, 37, 39, 50, 55]:
                self.btns[i].background_color = [127 / 255, 108 / 255, 27 / 255, 1]
            elif i in [1, 3, 5, 7, 17, 19, 21, 23, 25, 29, 31, 61]:
                self.btns[i].background_color = [150 / 255, 135 / 255, 35 / 255, 1]
            elif i in [20, 22, 24, 28, 32, 34, 38, 49, 54, 56, 58, 60, 62]:
                self.btns[i].background_color = [108 / 255, 94 / 255, 22 / 255, 1]
            elif i in [27, 51, 53, 57, 59, 63]:
                self.btns[i].background_color = [142 / 255, 127 / 255, 36 / 255, 1]
            elif i in [30, 36, 48, 52]:
                self.btns[i].background_color = [103 / 255, 85 / 255, 23 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_8(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [0, 1, 4, 5, 23, 31, 55, 63]:
                self.btns[i].background_color = [157 / 255, 111 / 255, 37 / 255, 1]
            elif i in [2, 3, 6, 7, 15, 39, 47]:
                self.btns[i].background_color = [151 / 255, 106 / 255, 29 / 255, 1]
            elif i in [8, 14, 32, 40, 48, 51, 52, 56, 57, 58, 59, 62]:
                self.btns[i].background_color = [183 / 255, 151 / 255, 28 / 255, 1]
            elif i in [11, 12, 17, 20, 25, 26, 29, 30, 34, 35, 38, 42, 43, 44, 53]:
                self.btns[i].background_color = [191 / 255, 161 / 255, 47 / 255, 1]
            elif i in [13, 18, 19, 22, 27, 28, 33, 36, 37]:
                self.btns[i].background_color = [188 / 255, 167 / 255, 54 / 255, 1]
            elif i in [9, 10, 21, 45, 46, 54]:
                self.btns[i].background_color = [191 / 255, 175 / 255, 58 / 255, 1]
            elif i in [16, 24, 60, 61]:
                self.btns[i].background_color = [186 / 255, 141 / 255, 26 / 255, 1]
            elif i in [41, 50]:
                self.btns[i].background_color = [188 / 255, 189 / 255, 141 / 255, 1]
            elif i == 49:
                self.btns[i].background_color = [189 / 255, 189 / 255, 106 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_9(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [0, 8, 10, 11, 16, 18, 24, 26, 28, 32, 34, 38, 40, 42, 43, 44, 45, 46, 48, 56, 57, 58, 59, 60, 61, 62, 63]:
                self.btns[i].background_color = [17 / 255, 146 / 255, 50 / 255, 1]
            elif i in [1, 2, 3, 4, 5, 6, 15, 23, 31, 39, 47, 55]:
                self.btns[i].background_color = [21 / 255, 112 / 255, 32 / 255, 1]
            elif i in [7, 19, 20, 21, 29, 37]:
                self.btns[i].background_color = [18 / 255, 129 / 255, 38 / 255, 1]
            elif i in [12, 27, 30, 36]:
                self.btns[i].background_color = [15 / 255, 165 / 255, 72 / 255, 1]
            elif i in [9, 13, 22, 33, 36, 54]:
                self.btns[i].background_color = [47 / 255, 197 / 255, 98 / 255, 1]
            elif i in [14, 17, 25, 35, 41, 49, 50, 51, 52, 53]:
                self.btns[i].background_color = [96 / 255, 198 / 255, 130 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def block_10(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        for i in range(64):
            self.btns[i].pos = (self.coord[0] + self.wid * 0.025 * (i % 8), self.coord[1] + self.wid * 0.025 * (i // 8))
            if i in [1, 4, 5, 23, 31, 55]:
                self.btns[i].background_color = [16 / 255, 143 / 255, 146 / 255, 1]
            elif i in [2, 3, 6, 7, 15, 39, 47]:
                self.btns[i].background_color = [9 / 255, 140 / 255, 142 / 255, 1]
            elif i in [0, 8, 32, 40, 48, 52, 56, 57, 58, 59, 62, 63]:
                self.btns[i].background_color = [55 / 255, 192 / 255, 172 / 255, 1]
            elif i in [11, 12, 17, 20, 21, 25, 26, 29, 30, 34, 35, 38, 42, 43, 44, 53]:
                self.btns[i].background_color = [74 / 255, 199 / 255, 167 / 255, 1]
            elif i in [16, 24, 60, 61]:
                self.btns[i].background_color = [45 / 255, 166 / 255, 168 / 255, 1]
            elif i in [13, 18, 19, 22, 27, 28, 36, 37]:
                self.btns[i].background_color = [83 / 255, 202 / 255, 195 / 255, 1]
            elif i in [9, 10, 14, 45, 46, 49, 54]:
                self.btns[i].background_color = [138 / 255, 205 / 255, 191 / 255, 1]
            elif i in [33, 41, 50, 51]:
                self.btns[i].background_color = [206 / 255, 206 / 255, 206 / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl

    def win(self, z):
        self.fl.remove_widget(self.btn_start)
        for i in range(64):
            self.fl.remove_widget(self.btns[i])
        x = self.hei * 0.5
        for i in range(64):
            if i < 5:
                self.btns[i].pos = (self.wid * 0.1925, x + self.wid * 0.025 * (i % 5))
            elif i < 10:
                self.btns[i].pos = (self.wid * 0.2775, x + self.wid * 0.025 * (i % 5))
            elif i < 15:
                self.btns[i].pos = (self.wid * 0.3625, x + self.wid * 0.025 * (i % 5))
            elif i < 20:
                self.btns[i].pos = (self.wid * 0.3975, x + self.wid * 0.025 * (i % 5))
            elif i == 20:
                self.btns[i].pos = (self.wid * 0.5175, x + self.wid * 0.025 * (i % 5))
            elif i < 25:
                self.btns[i].pos = (self.wid * 0.4925, x + self.wid * 0.025 * (i % 5))
            elif i == 25:
                self.btns[i].pos = (self.wid * 0.5675, x + self.wid * 0.025 * (i % 5))
            elif i < 30:
                self.btns[i].pos = (self.wid * 0.5925, x + self.wid * 0.025 * (i % 5))
            elif i < 35:
                self.btns[i].pos = (self.wid * 0.6275, x + self.wid * 0.025 * (i % 5))
            elif i < 40:
                self.btns[i].pos = (self.wid * 0.6625, x + self.wid * 0.025 * (i % 5))
            elif i < 45:
                self.btns[i].pos = (self.wid * 0.7375, x + self.wid * 0.025 * (i % 5))
            elif i == 46:
                self.btns[i].pos = (self.wid * 0.5425, x + self.wid * 0.025 * (i % 5))
            elif i < 50:
                self.btns[i].pos = (self.wid * 0.7825, x + self.wid * 0.025 * (i % 5))
            elif i == 51:
                self.btns[i].pos = (self.wid * 0.2425, x + self.wid * 0.025 * ((i-1) % 5))
            elif i == 53:
                self.btns[i].pos = (self.wid * 0.3275, x + self.wid * 0.025 * (i % 5))
            elif i < 55:
                self.btns[i].pos = (self.wid * 0.2175, x + self.wid * 0.025 * (i % 5))
            elif i == 58:
                self.btns[i].pos = (self.wid * 0.2425, x + self.wid * 0.025 * ((i+1) % 5))
            elif i == 55:
                self.btns[i].pos = (self.wid * 0.4225, x + self.wid * 0.025 * (i % 5))
            elif i == 56:
                self.btns[i].pos = (self.wid * 0.4475, x + self.wid * 0.025 * ((i-1) % 5))
            elif i < 60:
                self.btns[i].pos = (self.wid * 0.3025, x + self.wid * 0.025 * (i % 5))
            elif i == 60:
                self.btns[i].pos = (self.wid * 0.4225, x + self.wid * 0.025 * ((i+4) % 5))
            elif i == 61:
                self.btns[i].pos = (self.wid * 0.4475, x + self.wid * 0.025 * ((i+3) % 5))
            elif i == 62:
                self.btns[i].pos = (self.wid * 0.7125, x + self.wid * 0.025 * (i % 5))
            else:
                self.btns[i].pos = (self.wid * 0.6875, x + self.wid * 0.025 * (i % 5))
            self.btns[i].background_color = [randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1]
            self.btns[i].bind(on_press=self.lvl_up)
            self.fl.add_widget(self.btns[i])
        return self.fl


if __name__ == '__main__':
    MyApp().run()