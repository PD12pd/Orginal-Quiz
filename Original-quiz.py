# original funktion diese läuft!


WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["Was ist die Haupstadt von England ...?",
      "London", "Mallorca", "Hello", "Paris", 1]

q2 = ["Welches Land ist in Rom ...?",
      "Korsika", "Vatikanstaat", "Nigeria", "Rom", 2]

q3 = ["Wo steht der schiefe Turm?",
      "Mailand", "Pisa", "Florenz", "Rom", 2]

q4 = ["Wo ist das Morgarten Denkmal?",
      "Oberägeri", "Deutschland", "Tacos", "Links", 1]

q5 = ["Was ist die Hauptstadt von Grichenland?",
      "Oslo", "Athen", "Istambul", "Ankara", 2]


# in question ist die anzahl der zu stellenden fragen, wenn ich die mischen will, 
# muss ich den array questions, zufällig, aus fragen von q1 - q20 ziehe fünf frage zufällig

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0) # hier wird die frage gezogen, und der variablen question zugeordnet, question hat dimension
                            # 6 elementiger zeilenvektor

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("yellow")) # in der schleife werden die antwortboxen belegt, von index 1 - 4
        index = index + 1 # hier wird die index per schleifendurchlauf mit 1 addiert.

# Funktioniert gut

def game_over():
    global question, time_left
    message = "Ende. Du hast %s Fragen richtig" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10

    else:
        print("Das isch ja super gsi!")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Du hast angeklickt:" + str(index))
            if index == question[5]:
                print("Das isch ja MEGA he!")
                correct_answer()
            else:
                game_over()
        index = index + 1

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)
