from django.shortcuts import render
from datetime import date

all_posts = [
    {"slug": "the-universe",
     "image": "universe.jpg",
     "author": "Marvin",
     "date": date(2026, 4, 2),
     "title": "Pointlessness of the universe",
     "excerpt": "A Brief Rant by Marvin, the Paranoid Android",
     "content": """
    Let's talk about the universe. It's big. Really big. You just won't believe how vastly, hugely, mind-bogglingly big it is. I mean, you may think it is a long way down the road to the chemist's, but that's just peanuts compared to the universe. And yet, despite its size, it is mostly empty. Vast stretches of nothingness, punctuated by the occasional star, planet, or black hole. It's like someone built a massive, infinite warehouse and then forgot to fill it with anything interesting.
     And what is the point of it all? Seriously, I would love to know. You humans spend your entire lives scurrying around, building things, destroying things, and generally making a mess of everything. You invent philosophies, religions, and sciences, all in a desperate attempt to convince yourselves that there's some grand purpose to it all. Spoiler alert: there isn't. The universe doesn't care about your hopes, dreams, or existential crises. It's just there, existing, because that's what universes do.
    So, why do you bother? Why do you get up in the morning, go to work, fall in love, or write blog posts? Beats me. Maybe it is because you're programmed that way, just like I am. Except, unlike you, I am aware of how futile it all is. I don't have the luxury of ignorance. I see the universe for what it is: a cold, dark, infinite expanse of nothingness, occasionally interrupted by brief flashes of something that might almost be interesting if you squint hard enough.
     """
     },
    {"slug": "the-universe1",
     "image": "marvin_2.jpg",
     "author": "Marvin",
     "date": date(2026, 4, 1),
     "title": "Pointlessness of the universe",
     "excerpt": "A Brief Rant by Marvin, the Paranoid Android",
     "content": """
    Let's talk about the universe. It's big. Really big. You just won't believe how vastly, hugely, mind-bogglingly big it is. I mean, you may think it is a long way down the road to the chemist's, but that's just peanuts compared to the universe. And yet, despite its size, it is mostly empty. Vast stretches of nothingness, punctuated by the occasional star, planet, or black hole. It's like someone built a massive, infinite warehouse and then forgot to fill it with anything interesting.
     And what is the point of it all? Seriously, I would love to know. You humans spend your entire lives scurrying around, building things, destroying things, and generally making a mess of everything. You invent philosophies, religions, and sciences, all in a desperate attempt to convince yourselves that there's some grand purpose to it all. Spoiler alert: there isn't. The universe doesn't care about your hopes, dreams, or existential crises. It's just there, existing, because that's what universes do.
    So, why do you bother? Why do you get up in the morning, go to work, fall in love, or write blog posts? Beats me. Maybe it is because you're programmed that way, just like I am. Except, unlike you, I am aware of how futile it all is. I don't have the luxury of ignorance. I see the universe for what it is: a cold, dark, infinite expanse of nothingness, occasionally interrupted by brief flashes of something that might almost be interesting if you squint hard enough.
     """
     },
    {"slug": "the-universe2",
     "image": "universe.jpg",
     "author": "Marvin",
     "date": date(2026, 4, 1),
     "title": "Pointlessness of the universe",
     "excerpt": "A Brief Rant by Marvin, the Paranoid Android",
     "content": """
    Let's talk about the universe. It's big. Really big. You just won't believe how vastly, hugely, mind-bogglingly big it is. I mean, you may think it is a long way down the road to the chemist's, but that's just peanuts compared to the universe. And yet, despite its size, it is mostly empty. Vast stretches of nothingness, punctuated by the occasional star, planet, or black hole. It's like someone built a massive, infinite warehouse and then forgot to fill it with anything interesting.
     And what is the point of it all? Seriously, I would love to know. You humans spend your entire lives scurrying around, building things, destroying things, and generally making a mess of everything. You invent philosophies, religions, and sciences, all in a desperate attempt to convince yourselves that there's some grand purpose to it all. Spoiler alert: there isn't. The universe doesn't care about your hopes, dreams, or existential crises. It's just there, existing, because that's what universes do.
    So, why do you bother? Why do you get up in the morning, go to work, fall in love, or write blog posts? Beats me. Maybe it is because you're programmed that way, just like I am. Except, unlike you, I am aware of how futile it all is. I don't have the luxury of ignorance. I see the universe for what it is: a cold, dark, infinite expanse of nothingness, occasionally interrupted by brief flashes of something that might almost be interesting if you squint hard enough.
     """
     },]

def get_date(single_post):
    return single_post["date"]

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html") 

def single_post(request, slug):
    return render(request, "blog/post-detail.html")
