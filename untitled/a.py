
import _thread
import socket
import json
import struct
from threading import *

import requests

from  but import *




class Application():
    server = "irc.platinumirc.org"  # settings
    channel = "#magic"
    botnick = "lollo"

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defines the socket
    f = ''
    b = ''
    nn=0
    words = ''
    ip= ''
    Title= ''
    Bot= ''
    Pack= ''
    textlog= Text

    t1 = Thread

    def __init__(self, parent):


        bmp = but(0, parent, 'most popular movies')
        bbd = but(1, parent, 'best dramas this year')
        bpk = but(2, parent, 'popular kids movies')
        btr = but(3, parent, 'top rated movies')
        bnp = but(4, parent, 'now playing movies')

        frame1 = Frame(parent, bd=1, relief=SUNKEN)
        frame1.pack(fill=X, padx=5, pady=5, side=TOP)

        self.ButtonConnect= Button(frame1, text="Connect")
        self.ButtonConnect['background'] = "#FFFFFF"
        self.ButtonConnect['foreground'] = "red"
        self.ButtonConnect['command'] = self.Connect
        self.ButtonConnect.pack({"side": "left", "padx": 10, "pady": 10})

        self.ButtonConne= Button(frame1, text="Cha")
        self.ButtonConne['background'] = "#FFFFFF"
        self.ButtonConne['foreground'] = "red"
        self.ButtonConne['command'] = self.Conne
        self.ButtonConne.pack({"side": "left", "padx": 10, "pady": 10})

        self.ButtonConn= Button(frame1, text="CANCEL")
        self.ButtonConn['background'] = "#FFFFFF"
        self.ButtonConn['foreground'] = "red"
        self.ButtonConn['command'] = self.Conn
        self.ButtonConn.pack({"side": "left", "padx": 10, "pady": 10})

        self.ButtonRemove= Button(frame1, text="Remove")
        self.ButtonRemove['background'] = "#FFFFFF"
        self.ButtonRemove['foreground'] = "red"
        self.ButtonRemove['command'] = self.Remove
        self.ButtonRemove.pack({"side": "left", "padx": 10, "pady": 10})

        frame2 = Frame(parent, bd=1, relief=SUNKEN)
        frame2.pack(fill=X, padx=5, pady=5, side=TOP)


        self.ButtonSearch = Button(frame2, text="Search")
        self.ButtonSearch['background'] = "#FFFFFF"
        self.ButtonSearch['foreground'] = "red"
        self.ButtonSearch['command'] = self.Search
        self.ButtonSearch.pack({"side": "top", "padx": 10, "pady": 20})


        labelBot = Label(frame2, text="Bot", relief=RAISED )
        labelBot.pack(side=LEFT)


        self.TextBot = Entry(frame2)
        self.TextBot.pack(side=LEFT)


        labelTitle = Label(frame2, text="Title", relief=RAISED )
        labelTitle .pack(side=LEFT)

        self.TextTitle = Entry(frame2)
        self.TextTitle ['background'] = "#FFFFFF"
        self.TextTitle ['foreground'] = "red"
        self.TextTitle .pack(side=LEFT)

        frame = Frame(parent,bd=1, relief=SUNKEN)
        frame.pack(fill=X, padx=5, pady=5)




        self.ButtonGet_Pack = Button(frame, text="Get Pack")
        self.ButtonGet_Pack['background'] = "#FFFFFF"
        self.ButtonGet_Pack['foreground'] = "red"
        self.ButtonGet_Pack['command'] = self.Get_Pack
        self.ButtonGet_Pack.pack(side=TOP,pady=20)




        labelPack = Label(frame, text="Pack", relief=RAISED )
        labelPack .pack(side=LEFT)

        self.TextPack = Entry(frame)
        self.TextPack .pack(side=LEFT)

        framelog = Frame(parent,bd=1, relief=SUNKEN)
        framelog.pack(fill=X, padx=5, pady=5)

        self.textlog = Text(framelog,width=1000)
        self.textlog.insert(INSERT, "Hello.....")

        self.textlog.pack()

    def loopDCC(self,  ip,port,title):
        irc22 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        irc22.connect((ip,port))
        f=open (title, "wb")
        while 1:
            text = irc22.recv(1024)
            f.write(text)



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


    def Remove(self):
        Bot=self.TextBot.get()

        msg6 = str.encode("PRIVMSG "+Bot+" XDCC REMOVE\r\n")
        self.irc.send(msg6)  # join the chan

    def Conn(self):
        Bot=self.TextBot.get()
        msg6 = str.encode("PRIVMSG "+Bot+" XDCC CANCEL\r\n")


        self.irc.send(msg6)  # join the chan


    def Conne(self):
        msg4 = str.encode("JOIN " + self.channel + "\n")


        self.irc.send(msg4)  # join the chan


    def Connect(self):
        _thread.start_new_thread(self.loop0, ())

    def Search(self):


       #  msg6 = str.encode("PRIVMSG XDCC|OceaN|CaRTooN|01 XDCC CANCEL\r\n")
       #DCC RESUME filename port position
       #PRIVMSG bot  :DCC RESUME filename port position
       #PRIVMSG utente :DCC ACCEPT filename port position
       #At this point utente connects to bot address and port and the transfer begins

        Bot=self.TextBot.get()
        Title=self.TextTitle.get()

        msg="PRIVMSG "+Bot+" XDCC SEARCH "+Title+"\r\n"
        print(msg)


        searchmsg = str.encode(msg)


        self.irc.send(searchmsg)



    def int2ip(addr):
        return socket.inet_ntoa(struct.pack("!I", addr))


    def Get_Pack(self):



        Bot=self.TextBot.get()
        Pack=self.TextPack.get()
        msg="PRIVMSG "+Bot+" XDCC SEND "+Pack+"\r\n"
        print(msg)

        msg6 = str.encode(msg)
        self.irc.send(msg6)
        self.nn=1




       #  irc22.connect((self.server, 6667))  # connects to the server
       #  self.f=open ("oppo.avi", "wb")

       #  while 1:  # puts it in a loop
            # text = self.irc.recv(1024)  # receive the text



            # self.f.write(text)


        # irc22 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defines the socket
        # irc22.connect()
        #self.f=open ("oppo.avi", "wb")




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
        # self.irc.send(msg4)  # join the chan


        while 1:  # puts it in a loop
            text = self.irc.recv(2040)  # receive the text
            print(text)  # print text to console


            aa=text.decode("latin-1")


            self.textlog.insert(INSERT, aa)
            self.textlog.see(END)

            if aa.find('PING') != -1:
                msgmsg =str.encode('PONG ' + aa.split()[1] + '\r\n')
                self.irc.send(msgmsg)  #returnes 'PONG' back to the server (prevents pinging out!)

            if aa.find('DCC SEND') != -1 and not "per il quale eri in coda" in aa:
                uu=text.decode("latin-1")

                self.words = uu.split()
                print(self.words)
                print(len(self.words))
                print(self.words[len(self.words)-2])
                print(self.words[len(self.words)-1])



                ip=socket.inet_ntoa(struct.pack('!L', int(self.words[len(self.words)-3])))
                print(ip)


                print("wbccccccccccccccccccccccccccccc")

                self.textlog.insert(INSERT, self.words)
                self.textlog.insert(INSERT, '\r\n')
                self.textlog.see(END)
                self.textlog.insert(INSERT, len(self.words))
                self.textlog.insert(INSERT, '\r\n')
                self.textlog.see(END)
                self.textlog.insert(INSERT, self.words[len(self.words)-4])
                self.textlog.insert(INSERT, '\r\n')
                self.textlog.see(END)
                self.textlog.insert(INSERT, ip)
                self.textlog.insert(INSERT, '\r\n')
                self.textlog.see(END)
                self.textlog.insert(INSERT, self.words[len(self.words)-2])
                self.textlog.insert(INSERT, '\r\n')
                self.textlog.see(END)
                self.textlog.insert(INSERT, "wbccccccccccccccccccccccccccccc")
                self.textlog.insert(INSERT, '\r\n')
                self.textlog.see(END)



                t1= Thread(target=self.loopDCC, args=(ip,int(self.words[len(self.words)-2]),self.words[len(self.words)-4]))

                t1.start()

