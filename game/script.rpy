# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Александр:', who_color="#ffffff", who_bold=True)
define e = Character('Этажонок:', who_color="#ffffff", who_bold=True)

# Затемнение неактивного персонажа:

init python:
    def ChangeImage(image):
        if "etajonok" in image:
            renpy.show(image, what = im.MatrixColor(image + ".png", im.matrix.brightness(-0.3)))
        else:
            renpy.show(image, what = im.MatrixColor(image + ".png", im.matrix.brightness(-0.2)))

# Позиционирование персонажей:

transform a_center:
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 500

transform a_left:
    xanchor 0.5
    yanchor 0.5
    xpos 400
    ypos 500

transform e_right:
    xanchor 0.5
    yanchor 0.5
    xpos 1550
    ypos 720

transform show_1_pos:
    xanchor 0.5
    yanchor 0.5
    xpos 656
    ypos 179

transform show_2_pos:
    xanchor 0.5
    yanchor 0.5
    xpos 932
    ypos 472

transform show_3_pos:
    xanchor 0.5
    yanchor 0.5
    xpos 1070
    ypos 277

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg pc_chaos

    show alex neutral at a_center
    a "Вы создали новую игру Ren'Py."

    jump hello_alex

label hello_alex:

    scene bg pc_chaos

    show alex neutral at a_center with dissolve
    a "Ну и беспорядок."

    show alex hair
    a "Кажется, я в полном хаосе… Куча 5 не проработали и двух месяцев. Сделок нет вторую неделю, а ведь я нанимал сильных людей..."

    show alex neutral at a_left with move
    $ ChangeImage("alex neutral")

    show etajonok happy at e_right with moveinright
    e "Здравствуй, Алексей! Похоже, хаос стал частым гостем в вашем отделе."

    show etajonok up
    e "Кажется, я даже знаю почему!"

    $ ChangeImage("etajonok up")

    show alex fold
    a "А ты кто такой?"

    $ ChangeImage("alex fold")

    show etajonok happy
    e "Я Этажонок, прихожу туда, где срочно нужно что-то менять."

    $ ChangeImage("etajonok happy")

    show alex eyebrow
    a "Ну и? Почему же мой отдел в таком хаосе?"

    $ ChangeImage("alex eyebrow")

    show etajonok neutral
    e "Большинство риелторов уходят не потому, что “не получилось”. Они уходят потому, что не поняли, как у них должно получиться."

    $ ChangeImage("etajonok neutral")

    show alex think
    a "Что ты имеешь в виду?"

    $ ChangeImage("alex think")

    show etajonok up
    e "Чтобы сотрудник был успешным и делал много сделок, ему обязательно нужно обучение и развитие!"

    show etajonok neutral
    e "Без обучения риелтор: боится звонков, теряется на показах, не понимает продукт, не видит перспективы. И рано или поздно — уходит."

    $ ChangeImage("etajonok neutral")

    show alex fold
    a "Ну и кто же им мешает обучаться? Пусть берут и смотрят что им нужно!"

    $ ChangeImage("alex fold")

    show etajonok neutral
    e "Потому что есть ещё одна важная вещь. К сожалению, согласно мировой статистике, только 15 процентов сотрудников готовы всегда учиться..."

    show etajonok happy
    e "...70 процентам — обязательно нужен толчок к обучению: задачи от руководителя, много рекламы, отзывы..."
    e "...а оставшиеся 15 процентов вообще не готовы к обучению, и надо это принять."

    show etajonok neutral
    e "Понимаешь? Когда руководитель не контролирует обучение — команда воспринимает его как необязательное."

    show etajonok up
    e "А команды, которые развиваются, показывают лучшую закрепляемость, быстрее выходят на сделки и реже выгорают."

    $ ChangeImage("etajonok neutral")

    show alex think
    a "Звучит это всё конечно красиво, но где мне взять столько времени, чтобы еще и обучение контролировать?"

    $ ChangeImage("alex think")

    show etajonok happy
    e "Именно поэтому у нас в Этажах есть инструмент, который помогает тебе развивать команду системно — Учебный Портал."

    $ ChangeImage("etajonok happy")

    show alex fold
    a "Учебный Портал? А что это вообще такое?"

    $ ChangeImage("alex fold")

    show etajonok up
    e "Это сайт со множеством полезных и качественных электронных курсов, где сотрудники могут учиться легко и с удовольствием."

    show etajonok happy
    e "А ещё там есть вебинары, книги, тесты, учебные программы — в общем всё, что нужно для того, чтобы познавать новое и оставаться в тренде."

    show etajonok neutral
    e "Кстати, сейчас на Портале создаются еще различные тренажеры и игры, через которые тебе легче будет вовлечь команду в обучение."

    show etajonok happy
    e "Я покажу тебе, как это все работает. А дальше — ты сам решишь, как использовать эту силу."

    $ ChangeImage("etajonok happy")

    show alex eyebrow
    a "Учебный Портал? А что это вообще такое?"

    $ ChangeImage("alex eyebrow")

    show etajonok up
    e "Это сайт со множеством полезных и качественных электронных курсов, где сотрудники могут учиться легко и с удовольствием."

    show etajonok happy
    e "А ещё там есть вебинары, книги, тесты, учебные программы — в общем всё, что нужно для того, чтобы познавать новое и оставаться в тренде."

    show etajonok neutral
    e "Кстати, сейчас на Портале создаются еще различные тренажеры и игры, через которые тебе легче будет вовлечь команду в обучение."

    show etajonok happy
    e "Я покажу тебе, как это все работает. А дальше — ты сам решишь, как использовать эту силу."

menu:
    "Вперёд!":
        jump main_main_1

label main_main_1:

    scene main main

    show etajonok up at e_right
    e "Перед тобой — главная страница. Да-да, именно здесь начинается любое обучение."

    show etajonok neutral
    e "Портал работает 24/7, с мобильного или компьютера, но лучше всего дружит с Chrome или Safari — запомни этот лайфхак.»"

    show etajonok happy
    e "Сюда автоматически прилетают курсы по адаптациям, приоритетные курсы, рекомендуемые обучения. Тебе как руководителю важно знать — что здесь видит каждый сотрудник."

    scene main main hover

    show etajonok neutral at e_right
    e "Вот здесь находятся текущие и пройденные курсы. Нажми на них, а я расскажу подробнее..."
    hide etajonok neutral with moveoutright

    $ title = "main_courses"
    $ button = "button_1.png"
    call screen button(title, 932, 825, button)

label main_courses:

    scene main courses

    show etajonok happy at e_right with moveinright
    e "Текущие курсы — это курсы, которые находятся у сотрудников в процессе. Значит, они изучают материал и ещё не завершили тест."

    show etajonok neutral
    e "Теперь давай посмотрим на пройденные курсы."

    hide etajonok neutral with moveoutright

    $ title = "main_passed_courses"
    $ button = "button_2.png"
    call screen button(title, 1175, 407, button)

label main_passed_courses:

    scene main passed courses

    show etajonok up at e_right with moveinright
    e "А вот и они! Тут хранятся курсы, которые сотрудник уже прошёл, а также отображается процент их прохождения."

    show etajonok neutral
    e "Теперь давай спустимся чуть-чуть вниз."

    hide etajonok neutral with moveoutright

    $ title = "main_recs"
    $ button = "button_3_%s.png"
    call screen autobutton(title, 1514, 947, button)

label main_recs:

    scene main recs

    show etajonok up at e_right with moveinright
    e "Здесь находятся крутые курсы, которые рекомендуются всем от Отдела продаж до АУП персонала!"

    show etajonok happy
    e "В основном эти обучения для развития личной эффективности, но также есть курс про Ечат."

    show etajonok neutral
    e "Пора подниматься."

    hide etajonok neutral with moveoutright

    $ title = "main_main_2"
    $ button = "button_4_%s.png"
    call screen autobutton(title, 1514, 947, button)

label main_main_2:

    scene main main

    show etajonok happy at e_right with moveinright
    e "У нас на портале активно развивается геймификация — инструмент для повышения эффективности обучения, основанный на приципах и механиках игры."

    show show_1 at show_1_pos

    show etajonok up
    e "Например, у нас есть своя валюта — эткоины. Их можно зарабатывать проходя курсы или учавствуя в конкурсах в нашем телеграм-канале!"

    show etajonok happy
    e "А куда их тратить я расскажу чуть позже."

    hide show_1

    show etajonok neutral
    e "Также у нас есть достижения, давай перейдём и я расскажу подробнее."

    hide etajonok neutral with moveoutright

    $ title = "main_achievments"
    $ button = "button_5.png"
    call screen button(title, 932, 179, button)

label main_achievments:

    scene main achievments

    show etajonok happy at e_right with moveinright
    e "Достижения можно зарабатывать за прохождение определённых курсов."

    show etajonok neutral
    e "Чтобы узнать какая ачивка к какому курсу относится, просто нажмите на неё."

    show etajonok up
    e "А самое крутое — это то, что некоторые достижения отображаются в Космосе и на сайте Этажи! Такие ачивки выделены красной звёздочкой."

    show etajonok neutral
    e "Давай вернёмся на Главную"

    hide etajonok neutral with moveoutright

    $ title = "main_main_3"
    $ button = "button_6.png"
    call screen button(title, 470, 152, button)

label main_main_3:

    scene main main

    $ title = "main_certs"
    $ button = "button_7.png"
    call screen button(title, 1208, 179, button)

label main_certs:

    scene main certs

    $ title = "main_main_4"
    $ button = "button_6.png"
    call screen button(title, 470, 152, button)

label main_main_4:

    scene main main

    show show_2 at show_2_pos

    show show_3 at show_3_pos

    $ title = "main_news"
    $ button = "button_8.png"
    call screen button(title, 897, 476, button)

label main_news:

    scene main news

    $ title = "main_main_5"
    $ button = "button_9.png"
    call screen button(title, 1299, 207, button)

label main_main_5:

    scene main main

    $ title = "main_priopity"
    $ button = "button_10.png"
    call screen button(title, 157, 662, button)

label main_priopity:

    scene main priority

    e "stop"