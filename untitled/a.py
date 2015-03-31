__author__ = 'TONY'
import _thread
import socket
import json

import requests

from  but import *


class Application():
    server = "irc.oceanirc.net"  # settings
    channel = "#oce@n"
    botnick = "botname"

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defines the socket
    f = ''
    b = ''
    nn=0

    def __init__(self, parent):


        bmp = but(0, parent, 'most popular movies')
        bbd = but(1, parent, 'best dramas this year')
        bpk = but(2, parent, 'popular kids movies')
        btr = but(3, parent, 'top rated movies')
        bnp = but(4, parent, 'now playing movies')

        self.MyButton = Button(parent, text="nnnn")
        self.MyButton['background'] = "#FFFFFF"
        self.MyButton['foreground'] = "red"
        self.MyButton['command'] = self.MyButton_Cl
        self.MyButton.pack({"side": "top", "padx": 10, "pady": 20})

        self.MyBut = Button(parent, text="cpppp")
        self.MyBut['background'] = "#FFFFFF"
        self.MyBut['foreground'] = "red"
        self.MyBut['command'] = self.MyButton_C
        self.MyBut.pack({"side": "top", "padx": 10, "pady": 20})


    def fun(self, a):
        w_now_playingmovies = Toplevel()
        if a == 0:
            w_now_playingmovies.title('most popular movies')
            response = requests.get(
                'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=40e54aabfdbc70f6a680351b0425e65c')
            assert response.status_code == 200
        if a == 1:
            w_now_playingmovies.title('best dramas that were released this year')
            response = requests.get(
                'https://api.themoviedb.org/3/discover/movie?with_genres=18&primary_release_year=2014&api_key=40e54aabfdbc70f6a680351b0425e65c')
            assert response.status_code == 200
        if a == 2:
            w_now_playingmovies.title('the most popular kids movies')
            response = requests.get(
                'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=40e54aabfdbc70f6a680351b0425e65c')
            assert response.status_code == 200
        if a == 3:
            w_now_playingmovies.title('the top rated movies')
            response = requests.get(
                'https://api.themoviedb.org/3/movie/top_rated?api_key=40e54aabfdbc70f6a680351b0425e65c')
            assert response.status_code == 200
        if a == 4:
            w_now_playingmovies.title('the now_playing movies')
            response = requests.get(
                'https://api.themoviedb.org/3/movie/now_playing?api_key=40e54aabfdbc70f6a680351b0425e65c')
            assert response.status_code == 200

        var = StringVar()
        var.set("")
        tb = Text(w_now_playingmovies)
        tb.pack()

        print(response.json())
        b = json.loads(response.text)
        print(b['results'][0]['title'])

        for (i, item) in enumerate(b['results']):
            print(i, item['title'])

            xx = var.get() + '\n'
            xx += str(i) + ' ' + item['title']
            var.set(xx)

        tb.insert(INSERT, xx)


    def MyButton_C(self):
        _thread.start_new_thread(self.loop0, ())


    def MyButton_Cl(self):


        msg6 = str.encode("PRIVMSG XDCC|OceaN|CaRTooN|01 XDCC SEARCH disney\r\n")


        print(msg6)

        self.irc.send(msg6)

        self.f=open ("oppo.avi", "wb")
        self.nn=1


    def loop0(self):

        print('connecting to:' + self.server)
        msg = str.encode("USER " + self.botnick + " " + self.botnick + " " + self.botnick + " :This is a fun bot!\n")
        msg2 = str.encode("NICK " + self.botnick + "\n")
        msg3 = str.encode("PRIVMSG nickserv :iNOOPE\r\n")
        msg4 = str.encode("JOIN " + self.channel + "\n")

        self.irc.connect((self.server, 6667))  # connects to the server
        self.irc.send(msg)  # user authentication
        self.irc.send(msg2)  # sets nick
        self.irc.send(msg3)  # auth
        self.irc.send(msg4)  # join the chan
        self.b=open ("oppo.txt", "wb")

        while 1:  # puts it in a loop
            text = self.irc.recv(2040)  # receive the text
            print(text)  # print text to console
            aa=text.decode("latin-1")

            if aa.find('PING') != -1:
                msgmsg =str.encode('PONG ' + aa.split()[1] + '\r\n')
                self.irc.send(msgmsg)  #returnes 'PONG' back to the server (prevents pinging out!)

            if self.nn==0:


                self.b.write(text)

            if not text: break
            if self.nn==1:

                self.f.write(text)

        # if text.find('PING') != -1:  #check if 'PING' is found
        # irc.send('PONG ' + text.split()[1] + '\r\n')  #returnes 'PONG' back to the server (prevents pinging out!)



