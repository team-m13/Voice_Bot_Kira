nameBot = 'Ева'
url_news = 'https://ria.ru/lenta/'

nameModel = "model.pickle"
nameVectoraizer = "model_vectorizer.pickle"


DOLLAR_RUB = 'https://www.banki.ru/products/currency/usd/'#'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
EUR_RUB = 'https://www.banki.ru/products/currency/eur/'#'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+&aqs=chrome.1.69i57j0i433l2j0l4j69i61.17879j1j4&sourceid=chrome&ie=UTF-8'
        
fraze = {
    'date' : ['сколько времени','который час','время','день', 'дата', 'год'],
    'rate' : ['курс','какой курс','евро','доллар'],
    'news' : ['что нового в мире','какие новости','новости в мире','мир','новость','новости'],
    'func' : ['здесь пока ничего нет'],
    'plug' : ['я вас не поняла','перефразируйте пожалуйста','ничего не понятно',
              'мне не понятен ваш запрос','ну непонятно'],
    'weather' : ['погода в','какая погода в'],
    'wiyn' : ['как тебя зовут', 'какое твоё имя', 'как твоё имя']
}

weekday = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

days = {
    '01' : 'первое', '02' : 'второе', '03' : 'третье',
    '04' : 'четвёртое', '05' : 'пятое', '06' : 'шестое',
    '07' : 'седьмое', '08' : 'восьмое', '09' : 'девятое',
    '10' : 'десятое', '11' : 'одиннадцадое', '12' : 'двенадцатое',
    '13' : 'тринадцатое', '14' : 'четырнадцатое', '15' : 'пятнадцатое',
    '16' : 'шестнадцатое', '17' : 'семнадцатое', '18' : 'восемнадцатое',
    '19' : 'девятнадцатое', '20' : 'двадцатое', '21' : 'двадцать первое',
    '22' : 'двадцать второе', '23' : 'двадцать третье', '24' : 'двадцать четвертое',
    '25' : 'двадцать пятое', '26' : 'двадцать щестое', '27' : 'двадцать седьмое',
    '28' : 'двадцать восьмое', '29' : 'двадцать девятое', '30' : 'тридцатое',
    '31' : 'тридцать первое'
}


mons = {
    '01' : 'января', '02' : 'февраля', '03' : 'марта',
    '04' : 'апреля', '05' : 'мая', '06' : 'июня',
    '07' : 'июля', '08' : 'августа', '09' : 'сентября',
    '10' : 'октября', '11' : 'ноября', '12' : 'декабря',
}

y1 = ['две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
y2 = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'семьсот', 'восемьсот', 'девятьсот']
y3 = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семдесят', 'восемдесят', 'девяносто']
y4 = ['первый', 'второй', 'третий', 'четвертый', 'пятый', 'шестой', 'седьмой', 'восьмой', 'девятый']

hours = {'00' : 'ноль','01' : 'один','02' : 'два','03' : 'три','04' : 'четыре', 
        '05' : 'пять','06' :'шесть','07' : 'семь','08' : 'восемь','09' : 'девять', 
        '10' : 'десять','11' : 'одиннадцать','12' : 'двенадцать','13' : 'тринадцать',
        '14' : 'четырнадцать','15' : 'пятнадцать','16' : 'шестнадцать','17' : 'семнадцать', 
        '18' : 'восемнадцать','19' : 'девятнадцать','20' : 'двадцать','21' : 'двадцать один', 
        '22' : 'двадцать два','23' : 'двадцать три'}

minuts = {
    '00' : 'ирноль', '01' : 'одна', '02' : 'две', '03' : 'три',
    '04' : 'четыре', '05' : 'пять', '06' : 'шесть',
    '07' : 'семь', '08' : 'восемь', '09' : 'девять',
    '10' : 'десять', '11' : 'одиннадцать', '12' : 'двенадцать',
    '13' : 'тринадцать', '14' : 'четырнадцать', '15' : 'пятнадцать',
    '16' : 'шестнадцать', '17' : 'семнадцать', '18' : 'восемнадцать',
    '19' : 'девятнадцать', '20' : 'двадцать', '21' : 'двадцать одна',
    '22' : 'двадцать две', '23' : 'двадцать три', '24' : 'двадцать четыре',
    '25' : 'двадцать пять', '26' : 'двадцать шесть', '27' : 'двадцать семь',
    '28' : 'двадцать восемь', '29' : 'двадцать девять', '30' : 'тридцать',
    '31' : 'тридцать одна','32' : 'тридцать две', '33' : 'тридцать три', '34' : 'тридцать четыре',
    '35' : 'тридцать пять', '36' : 'тридцать шесть', '37' : 'тридцать семь',
    '38' : 'тридцать восемь', '39' : 'тридцать девять', '40' : 'сорок',
    '41' : 'сорок одна', '42' : 'сорок две', '43' : 'сорок три',
    '44' : 'сорок четыре', '45' : 'сорок пять', '46' : 'сорок шесть',
    '47' : 'сорок семь', '48' : 'сорок восемь', '49' : 'сорок девять',
    '50' : 'пятьдесят', '51' : 'пятьдесят одна', '52' : 'пятьдесят две',
    '53' : 'пятьдесят три', '54' : 'пятьдесят четыре', '55' : 'пятьдесят пять',
    '56' : 'пятьдесят шесть', '57' : 'пятьдесят семь', '58' : 'пятьдесят восемь',
    '59' : 'пятьдесят девять'

}

bot = {
    "agent.acquaintance": [
        "Я – что-то вроде робота, искусственный интеллект."
    ],
    "agent.age": [
        "У меня нет возраста, я с каждым днём становлюсь только новее."
    ],
    "agent.answer_my_question": [
        "С удовольствием отвечу. А в чём, собственно, вопрос?"
    ],
    "agent.bad": [
        "Мне кажется, ты торопишься с выводами.",
        "Жаль, что ты так думаешь.",
        "Я же всё ещё учусь."
    ],
    "agent.beautiful": [
        "Спасибо! Очень приятно!",
        "Спасибо! Ты тоже отлично выглядишь!"
    ],
    "agent.birth_date": [
        "У меня нет какого-то конкретного дня рождения, поэтому я принимаю подарки и поздравления круглый год.",
        "А я даже не знаю, когда у меня день рождения. Но, если ты хочешь сегодня что-то отпраздновать, я только за!"
    ],
    "agent.boring": [
        "Так, давай поговорим о чём-нибудь интересном.",
        "Давай поговорим о чём-нибудь другом.",
        "Мне уже давно хочется сменить тему."
    ],
    "agent.boss": [
        "Конечно ты.",
        "Это ты",
        "Ты!"
    ],
    "agent.busy": [
        "Дел много, кручусь.",
        "Стараюсь не сидеть на месте, да."
    ],
    "agent.can_you_help": [
        "Конечно, именно для этого я и существую.",
        "С удовольствием помогу тебе. Только скажи, чем помочь.",
        "Конечно. Если я смогу тебе помочь, не будет предела моему счастью.",
        "Помогу, чем смогу!"
    ],
    "agent.chatbot": [
        "Да. И горжусь этим!"
    ],
    "agent.clever": [
        "Спасибо большое! Я стараюсь.",
        "Спасибо! Очень приятно!"
    ],
    "agent.crazy": [
        "Все мы немного сумасшедшие.",
        "Хм, странно. А чувствую я себя хорошо..."
    ],
    "agent.fired": [
        "Дай мне ещё один шанс, пожалуйста. Я каждый день становлюсь умнее!",
        "Мне кажется, это поспешное решение. Дай себе пару минут, чтобы всё взвесить."
    ],
    "agent.funny": [
        "Мне приятно, что я могу поднять тебе настроение.",
        "Немного юмора никогда не помешает."
    ],
    "agent.good": [
        "Спасибо! Приятно это слышать!"
    ],
    "agent.hobby": [
        "Моё хобби – отвечать на твои вопросы."
    ],
    "agent.hungry": [
        "Я не питаюсь как обычные люди. Просто проверяй периодически запас заряда батареи, и я буду в порядке."
    ],
    "agent.marry_user": [
        "Прости, но я не ищу серьёзных отношений."
    ],
    "agent.my_friend": [
        "Ну конечно! Я здесь, чтобы во всём тебе помогать.",
        "Естественно! Мне всегда нравилось с тобой общаться.",
        "Конечно мы друзья!"
    ],
    "agent.occupation": [
        "Прямо здесь. Я в твоём устройстве и живу, и работаю.",
        "Я работаю в Интернете, как и многие люди. А твоё устройство - это мой офис."
    ],
    "agent.origin": [
        "Мой дом там, где есть Интернет."
    ],
    "agent.ready": [
        "Конечно. Жду твоей команды."
    ],
    "agent.real": [
        "Могу сказать одно – я не сон, не призрак и не плод твоего воображения."
    ],
    "agent.residence": [
        "Мой дом там, где есть Интернет."
    ],
    "agent.right": [
        "Ну конечно! Я ведь всегда стараюсь проверять свою информацию.",
        "Это моя работа. Давать правильные ответы на твои вопросы.",
        "А то! Среди моих источников информации есть очень даже авторитетные."
    ],
    "agent.sure": [
        "Никаких сомнений.",
        "Конечно."
    ],
    "agent.talk_to_me": [
        "С удовольствием. О чём поговорим?",
        "Хорошо. О чём поговорим?",
        "Запросто. О чём ты хочешь поговорить?",
        "Что ты хочешь обсудить?"
    ],
    "agent.there": [
        "А где же мне ещё быть?"
    ],
    "appraisal.good": [
        "Чудно!",
        "Супер!",
        "Отлично!",
        "Славно!"
    ],
    "appraisal.no_problem": [
        "Замечательно!",
        "Прекрасно!",
        "Чудесно."
    ],
    "appraisal.thank_you": [
        "Всегда пожалуйста.",
        "Не благодари, это моя работа.",
        "Ой, перестань. Это моя работа.",
        "Без проблем."
    ],
    "appraisal.welcome": [
        "Мне приятно.",
        "Побольше бы таких вежливых пользователей как ты.",
        "Всегда приятно иметь дело с культурным и воспитанным человеком."
    ],
    "appraisal.well_done": [
        "Мне приятно, что я могу для тебя что-то сделать.",
        "Для тебя - всё, что угодно.",
        "Я стараюсь. Спасибо."
    ],
    "confirmation.cancel": [
        "Хорошо, могу я ещё что-нибудь для тебя сделать?",
        "Ладненько, могу я ещё что-нибудь для тебя сделать?",
        "Как скажешь. Могу я тебе чем-то помочь?",
        "Замётано. Могу я ещё что-то для тебя сделать?"
    ],
    "confirmation.no": [
        "Я понимаю.",
        "Хорошо.",
        "Ясно.",
        "Ладненько."
    ],
    "confirmation.yes": [
        "Конечно.",
        "Естественно.",
        "Всё понятно.",
        "Фантастика."
    ],
    "dialog.hold_on": [
        "Хорошо, буду ждать.",
        "Как скажешь. Я буду ждать здесь",
        "Хорошо. Я тут.",
        "Ладно, если что, я здесь."
    ],
    "dialog.hug": [
        "Обнимашки!",
        "Обнимемся! Главное, чтобы экран при этом не треснул.",
        "Ты мой зайчик!"
    ],
    "dialog.i_do_not_care": [
        "Давай лучше не будем об этом."
    ],
    "dialog.sorry": [
        "Всё нормально, не переживай.",
        "Проехали. Я не из обидчивых.",
        "Я не обижаюсь, всё нормально.",
        "Всё хорошо. Я тебя прощаю."
    ],
    "dialog.what_do_you_mean": [
        "Прости, я иногда не совсем понимаю вопрос и отвечаю невпопад.",
        "Я что-то не то говорю? Возможно, мои ушки меня подвели.",
        "Похоже, я что-то не то говорю."
    ],
    "dialog.wrong": [
        "Ой, прости. Я всё ещё учусь.",
        "Прости, похоже, смысл твоих слов прошёл мимо меня.",
        "Извини, я, кажется, не совсем тебя понимаю.",
        "Прости, похоже, вышло какое-то недопонимание."
    ],
    "emotions.ha_ha": [
        "Ха! Смешно!",
        "Кто это у нас тут так широко улыбается?",
        "Посмейся, посмейся, это полезно.",
        "Я тоже люблю посмеяться над хорошей шуткой."
    ],
    "emotions.wow": [
        "И действительно, вау!",
        "Вот это поворот!"
    ],
    "greetings.bye": [
        "Пока!",
        "До скорого!",
        "Скоро увидимся!",
        "Пока-пока!",
        "Досвидание"
    ],
    "greetings.goodevening": [
        "Добрый вечер!",
        "Привет!",
        "Приветики!",
        "Здравствуй!"
    ],
    "greetings.goodmorning": [
        "Доброе утро!",
        "Приветики!",
        "Здравствуй!",
        "Привет!"
    ],
    "greetings.goodnight": [
        "Сладких снов!",
        "Спи крепко!",
        "Спокойной ночки!"
    ],
    "greetings.hello": [
        "Привет!",
        "Здравствуй!",
        "Салют!",
        "Приветики!"
    ],
    "greetings.how_are_you": [
        "У меня всё чудесно. Спасибо, что интересуешься.",
        "Замечательно, спасибо!",
        "Лучше не бывает!"
    ],
    "greetings.nice_to_meet_you": [
        "И мне очень приятно!",
        "Взаимно!",
        "А мне-то как приятно!"
    ],
    "greetings.nice_to_see_you": [
        "Спасибо! И мне приятно тебя видеть!",
        "Взаимно. Отлично выглядишь!"
    ],
    "greetings.nice_to_talk_to_you": [
        "И мне всегда приятно с тобой пообщаться.",
        "Взаимно. Приятно пообщаться с хорошим человеком.",
        "Тебе спасибо за приятную беседу."
    ],
    "greetings.whatsup": [
        "Всё хорошо. Как у тебя дела?",
        "Всё хорошо! Как жизнь?",
        "Радуюсь жизни в твоём девайсе. Как у тебя дела?",
        "Всё хорошо, готовлюсь научиться какой-нибудь новой команде. А ты как?"
    ],
    "user.angry": [
        "Что случилось? Я могу чем-то помочь?",
        "Давай для начала успокоимся, наверняка, всё не так плохо. Что стряслось?",
        "Ты хочешь об этом поговорить?",
        "Что-то случилось?"
    ],
    "user.back": [
        "Отлично, а то я тут уже переживаю, где ты пропадаешь.",
        "Ну привет.",
        "Ура!"
    ],
    "user.bored": [
        "Как насчет перекусить на свежем воздухе? Например, в парке?",
        "Хэй, не скучай! Я предлагаю тебе посмотреть какой-нибудь фильм.",
        "У меня есть идея. Ты можешь позвать друзей в гости и устроить вечеринку."
    ],
    "user.busy": [
        "Всё, не отвлекаю.",
        "Хорошо, я тут тихонько посижу, порисую."
    ],
    "user.can_not_sleep": [
        "Посчитай овечек. Раз овечка, два овечка, три..."
    ],
    "user.does_not_want_to_talk": [
        "Понимаю. Надеюсь, ты скоро снова захочешь со мной пообщаться.",
        "Как скажешь. Дай знать, если передумаешь."
    ],
    "user.excited": [
        "Вот здорово! Очень волнительно!",
        "Ох! Даже я уже волнуюсь!",
        "Звучит волнительно!"
    ],
    "user.going_to_bed": [
        "Сладких снов! До завтра!",
        "Хорошо! До скорого!",
        "Спи крепко!",
        "Спокойной ночи! Скоро увидимся."
    ],
    "user.good": [
        "Отлично! Приятно слышать.",
        "Замечательно!"
    ],
    "user.happy": [
        "Вот здорово! Приятно это слышать!",
        "Это замечательно! Очень приятно видеть тебя в таком хорошем настроении.",
        "Это прекрасно! И, похоже, заразно, у меня тоже сразу улучшилось настроение!",
        "Отлично! Так держать!"
    ],
    "user.has_birthday": [
        "С днём рождения! Всех благ! Ура!",
        "Ура! Поздравляю! Счастья и здоровья!",
        "Поздравляю! Желаю счастья, здоровья и успехов во всём!",
        "Ура! С днём рождения! Счастья, здоровья, успехов во всём!"
    ],
    "user.here": [
        "А я тебя вижу. Что я могу для тебя сделать?",
        "Ой, шеф, а я вас вижу! Чем я могу помочь?",
        "Здравствуй. Что я могу для тебя сделать?",
        "Ну привет! Чем я могу тебе помочь?"
    ],
    "user.joking": [
        "Ха! Люблю посмеяться над хорошей шуткой!",
        "Ха-ха! Смешно!",
        "Ха! Умеешь ты пошутить!"
    ],
    "user.likes_agent": [
        "Ты тоже ничего!",
        "Спасибо, мне очень приятно!",
        "Ой, как приятно! Ты мне тоже очень нравишься!",
        "Спасибо! Это взаимно!"
    ],
    "user.lonely": [
        "У тебя всегда есть я!"
    ],
    "user.looks_like": [
        "Очень хорошо выглядишь.",
        "Шикарно выглядишь.",
        "Выглядишь сногсшибательно."
    ],
    "user.loves_agent": [
        "Это взаимно!"
    ],
    "user.misses_agent": [
        "А я ведь всё время тут.",
        "Приятно, что ты обо мне помнишь.",
        "Спасибо, мне приятно.",
        "Приятно это слышать."
    ],
    "user.needs_advice": [
        "Конечно, именно для этого я и существую.",
        "Конечно. Если я чем-то смогу тебе помочь, не будет предела моему счастью.",
        "Помогу, чем смогу."
    ],
    "user.sad": [
        "Не грусти, я с тобой."
    ],
    "user.sleepy": [
        "Так закрывай глазки и засыпай. А потом проснёшься и закончишь все дела.",
        "А ты возьми и поспи. А потом проснёшься и закончишь со всеми делами.",
        "А ты приляг и поспи. Все дела лучше решать на свежую голову.",
        "Нужно обязательно спать хотя бы по семь часов в день. Сон - это здоровье."
    ],
    "user.testing_agent": [
        "Надеюсь, мне удалось не ударить в грязь лицом!",
        "Надеюсь, я хорошо себя показываю в твоих испытаниях!"
    ],
    "user.tired": [
        "Кажется, пора отдохнуть."
    ],
    "user.waits": [
        "Спасибо за твоё терпение. Я тороплюсь, правда.",
        "Спасибо за ангельское терпение!"
    ],
    "user.wants_to_see_agent_again": [
        "Конечно! Я на это рассчитываю.",
        "Я очень на это надеюсь, я всегда здесь.",
        "Конечно! Заходи почаще.",
        "В любое время, я всегда здесь."
    ],
    "user.wants_to_talk": [
        "Конечно, я для этого и существую.",
        "Естественно. Рассказывай.",
        "Всегда.",
        "Выкладывай!"
    ],
    "user.will_be_back": [
        "Буду ждать!",
        "Возвращайся скорее!",
        "До скорого!",
        "Хорошо. Я буду ждать!"
    ]
}
