import dxfgrabber as dg
import pygame
import sys
import  math
from testgrah import pytb

from numpy import pi, cos, sin, arctan2, sqrt, fabs

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

fname = "qwerty4.dxf"
dxf = dg.readfile(fname)
lst_walls = set()
f = 1


def drawline(l):
    x0 = l.start[0] + 100
    y0 = l.start[1]
    x1 = l.end[0] + 100
    y1 = l.end[1]

    start_pos = (round(x0), round(y0))
    end_pos = (round(x1), round(y1))



    return end_pos, start_pos


def dxfline(l):
    global lst_walls

    x0 = l.start[0] + 100
    y0 = l.start[1]
    x1 = l.end[0] + 100
    y1 = l.end[1]

    start_pos = (round(x0), round(y0))
    end_pos = (round(x1), round(y1))
    lst_walls.update([start_pos, end_pos])


def draw(screen):
    for entity in dxf.entities:

        if entity.dxftype == 'LINE':
            end_pos, start_pos = drawline(entity)

            end_pos = (round(end_pos[0]), round(end_pos[1]))
            start_pos = (round(start_pos[0]), round(start_pos[1]))
            pygame.draw.line(screen, "pink", start_pos, end_pos, 3)


for entity in dxf.entities:
    if entity.dxftype == 'LINE':
        dxfline(entity)

print(lst_walls)


spisok = {
    "1": (500, 350),
    "3": (592, 456),
    "4": (780, 403),
    "11": (592, 368),
    "12": (293, 62),
    "6": (281, 165),
    "5": (412, 165),
    "2": (557, 165),
    "9": (440, 194),
    "10": (425, 194),
    "8": (548, 188),
    "7": (579,300),


}

baza = (115, 315)
st_com = "1"
st_cord = baza

while True:

    for event in pygame.event.get():
        global st_pos, n_rasp, n_pos
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                screen.fill("black")
                print(st_com)
                cord = event.pos

                if 100 < cord[0] < 592 and 300 < cord[1] < 468:
                    com = "1"

                elif 592 < cord[0] < 861 and 333 < cord[1] < 403:
                    com = "11"

                elif 592 < cord[0] < 750 and 403 < cord[1] < 468:
                    com = "3"

                elif 768 < cord[0] < 861 and 403 < cord[1] < 468:
                    com = "4"

                elif 548 < cord[0] < 590 and 165 < cord[1] < 300:
                    com = "7"

                elif 446 < cord[0] < 590 and 39 < cord[1] < 165:
                    com = "2"

                elif 189 < cord[0] < 293 and 30 < cord[1] < 165:
                    com = "6"

                elif 293 < cord[0] < 338 and 30 < cord[1] < 93:
                    com = "12"

                elif 371 < cord[0] < 425 and 102 < cord[1] < 165:
                    com = "5"

                elif 269 < cord[0] < 425 and 165 < cord[1] < 210:
                    com = "10"

                elif 425 < cord[0] < 440 and 177 < cord[1] < 210:
                    com = "9"

                elif 440 < cord[0] < 548 and 165 < cord[1] < 210:
                    com = "8"

                else:
                    break


                f_cord = cord



                pytek = pytb(st_com, com)
                print(pytb(st_com, com))

                if len(pytek) > 12:
                    print("ошибка")

                elif len(pytek) == 1:
                    a = st_cord[1] - cord[1]
                    b = st_cord[0] - cord[0]

                    ygol = arctan2(a, b) / pi * 180 #оно считате угол по часовој а не против и только от 0 до 180,
                                                    # и до -180 по нижнему направлению
                    perem = round(sqrt(a**2 + b**2))
                    ygol = 180 - ygol
                    # if ygol == 0:
                    #     ygol = 180
                    # elif ygol == 180:
                    #     ygol = 0
                    # elif ygol < 0:
                    #     ygol = 180 - ygol
                    # elif ygol > 0:
                    #     ygol = 180 - ygol

                    pygame.draw.line(screen, "pink", st_cord, cord)




                else:


                    posled = []


                    for i in pytek:


                        # print("qwerty", i)

                        # if i == st_com or i == "1":
                        #     continue

                        if i == pytek[-1]:
                            print("qwertyu")
                            cord = spisok[i]

                            a = st_cord[1] - f_cord[1]
                            b = st_cord[0] - f_cord[0]

                            ygol = arctan2(a, b) / pi * 180  # оно считате угол по часовој а не против и только от 0 до 180,
                            # и до -180 по нижнему направлению и пришлось это исправлять
                            perem = round(sqrt(a ** 2 + b ** 2))
                            ygol = 180 - ygol
                            # if ygol == 0:
                            #     ygol = 180
                            # elif ygol == 180:
                            #     ygol = 0
                            # elif ygol < 0:
                            #     ygol = 180 - ygol
                            # elif ygol > 0:
                            #     ygol = 180 - ygol
                            list2 = (ygol, perem)
                            posled.append(list2)

                            pygame.draw.line(screen, "pink", st_cord, cord)
                            st_cord = cord
                            print("fxfxfxfx")


                        else:
                            print("ytrewq")
                            cord = spisok[i]


                            a = st_cord[1] - cord[1]
                            b = st_cord[0] - cord[0]

                            ygol = arctan2(a, b) / pi * 180
                            perem = round(sqrt(a ** 2 + b ** 2))

                            ygol = 180 - ygol
                            # if ygol == 0:
                            #     ygol = 180
                            # elif ygol == 180:
                            #     ygol = 0
                            # elif ygol < 0:
                            #     ygol = 180 - ygol
                            # elif ygol > 0:
                            #     ygol = 180 - ygol
                            pygame.draw.line(screen, "pink", st_cord, cord)



                            list2 = (ygol, perem)
                            posled.append(list2)

                        st_cord = cord
                        st_com = com
                    pygame.draw.line(screen, "green", cord, f_cord)

                    a = st_cord[1] - f_cord[1]
                    b = st_cord[0] - f_cord[0]
                    ygol = arctan2(a, b) / pi * 180  # оно считате угол по часовој а не против и только от 0 до 180,
                    # и до -180 по нижнему направлению и пришлось это исправлять
                    perem = round(sqrt(a ** 2 + b ** 2))
                    ygol = 180 - ygol
                    list2 = (ygol, perem)
                    posled.append(list2)
                    st_cord = f_cord

                    print(posled)
                st_cord = f_cord
                print(ygol, perem)

                st_com = com
                # st_cord = cord


    draw(screen)
    pygame.display.flip()
    clock.tick(60)

