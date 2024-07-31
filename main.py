import pygame
import time
import sqlite3
import random

conn = sqlite3.connect('Brawlers.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Brawlers(id INTEGER PRIMARY KEY, name TEXT, image_name TEXT)")
conn.commit()
conn.close()

pygame.init()

Size = (800, 600)
x = 50
y = 70
Width=300
Height=100
Padding=30
Button1=60
Button2=260
Button3=460
Coins=0
Gems=0
Credits=0
XP=0
Enemyhealth = 5000
FPS = 60
clock = pygame.time.Clock()
list_of_objbox = ["Coins", "Gems", "Brawlers", "Credits", "XP"]

show_message = False
message_time = 0
                                                                          # Aici se fac clasele
class Brawlers(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()
    def Shoot(self):
        Bulet1 = Bulet("bulet.png", self.rect.centerx, self.rect.centery)
        Bulet_group.add(Bulet1)
        all_sprites.add(Bulet1)

    def update(self, position):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.rect.top >=0:
                self.rect.y = self.rect.y - 4
        if keys[pygame.K_DOWN]:
            if self.rect.bottom <=600:
                self.rect.y = self.rect.y + 4
        if keys[pygame.K_LEFT]:
            if self.rect.left >=0:
                self.rect.x = self.rect.x - 4
        if keys[pygame.K_RIGHT]:
            if self.rect.right <=800:
                 self.rect.x = self.rect.x + 4



class Enemies(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()
        self.idk = 0
    def update(self):
        if self.rect.x >= Piper.rect.x:
            self.rect.x -= 5
        if self.rect.x < Piper.rect.x:
            self.rect.x += 5
        if self.rect.y >= Piper.rect.y:
            self.rect.y -= 5
        if self.rect.y < Piper.rect.y:
            self.rect.y += 5
    def Shoot(self):
        Bulet1 = Enemybulet("bulet.png", self.rect.centerx, self.rect.centery)
        Enemybulet_group.add(Bulet1)
        all_sprites.add(Bulet1)
        position = Piper.rect.x, Piper.rect.y
        if Bulet1.rect.x >= Piper.rect.x:
            Bulet1.top = -5
        if Bulet1.rect.x < Piper.rect.x:
            Bulet1.top = 5
        if Bulet1.rect.y >= Piper.rect.y:
            Bulet1.bord = -2
        if Bulet1.rect.y < Piper.rect.y:
            Bulet1.bord = 2


class Boxes(pygame.sprite.Sprite):
    def __init__(self, image, size1, size2):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (size1, size2))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 400

    def update(self):
        pass
class Bulet(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, position):
        if position[0] >=self.rect.x:
           self.rect.x = self.rect.x +5
        if position[1] >=self.rect.y:
            self.rect.y = self.rect.y +5
        if position[0] <self.rect.x:
           self.rect.x = self.rect.x -5
        if position[1] <self.rect.y:
            self.rect.y = self.rect.y -5
        if self.rect.bottom>=600:
            self.kill()
        if self.rect.top<=0:
            self.kill()
        if self.rect.left<=0:
            self.kill()
        if self.rect.right>=800:
            self.kill()

class Health(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

class Enemybulet(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #top = x, bord = y
        self.top = 0
        self.bord = 0
    def update(self, position):
        self.rect.x += self.top
        self.rect.y += self.bord

                                                                         #Aici se fac personajele

screen = pygame.display.set_mode(Size)
pygame.display.set_caption("My game")
White = (255, 240, 245)
Pink = (255, 105, 180)
image = pygame.image.load("piper.jpg")
resized_image = pygame.transform.scale(image, (70, 100))
all_sprites = pygame.sprite.Group()
Piper_group = pygame.sprite.Group()
Brawl_Box = Boxes("brawl box stop.jpg", 140, 140)
Box_group = pygame.sprite.Group()
Box_group.add(Brawl_Box)
Bulet_group = pygame.sprite.Group()
Enemybulet_group = pygame.sprite.Group()


Piper = Brawlers("piper.jpg")
Piper.rect.x = 100
Piper.rect.y = 100
all_sprites.add(Piper)
#all_sprites.add(Mandy)
#all_sprites.add(Emz)
Piper_group.add(Piper)
Kit = Enemies("kit.png")
Kit.rect.x = 600
Kit.rect.y = 100
Enemies_group = pygame.sprite.Group()
Enemies_group.add(Kit)

Imagehealth = pygame.image.load("health.png")
Imagehealth = pygame.transform.scale(Imagehealth, ((130, 100)))
Imagehealth.set_colorkey((255, 255, 255))

Brawlerhealth = pygame.image.load("health.png")
Brawlerhealth = pygame.transform.scale(Brawlerhealth, ((130, 100)))
Brawlerhealth.set_colorkey((255, 255, 255))

a = 0
surprise = 0
Start = 2
Vremea = 0
Imagetime = 0
Imageobjbox = pygame.image.load("coins.jpg")
Imageobjbox = pygame.transform.scale(Imageobjbox, (700, 500))
Nrboxstop = 4
List_of_brawlers = ["piper", "emz", "mandy"]
Imagebrawlers = "emz"
Shopbulet = pygame.image.load("shoot1.png")
Shopbulet.set_colorkey((255, 255, 255))
Shopbulet = pygame.transform.scale(Shopbulet, (150, 120))
Countdown = 3
Shootenemybulet = 1
Timerenemybulet = 1
Ulta = 0
Restore = 0
Brawlerhealthnr = 5000
newenemy = 0
Reloadenemy = False
Respawntimekit = 0
Sectimerespawn = 5000
Canshoot = True


                                                                                            #AICI ESTE JOACA
while True:
    if Start==0:
        conn = sqlite3.connect('Brawlers.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, image_name FROM Brawlers")
        users = cursor.fetchall()

        # Вывод логинов и паролей пользователей в консоль
        for user in users:
            print(f"Логин: {user[0]}, Пароль: {user[1]}")
        conn.commit()
        conn.close()

        Emzstart =pygame.image.load("Emzstart.jpg")
        Emzstart = pygame.transform.scale(Emzstart, (200, 200))
        Emzstartrect = Emzstart.get_rect(center = (250, 250))
        screen.blit(Emzstart, Emzstartrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = event.pos
                if Countdown>0:
                    Countdown -= 1
                    if Countdown == 3:
                        Shopbulet = pygame.image.load("shoot1.png")
                        Shopbulet.set_colorkey((255, 255, 255))
                        Shopbulet = pygame.transform.scale(Shopbulet, (150, 120))
                    if Countdown == 2:
                        Shopbulet = pygame.image.load("shoot2.png")
                        Shopbulet.set_colorkey((255, 255, 255))
                        Shopbulet = pygame.transform.scale(Shopbulet, (150, 120))
                    if Countdown == 1:
                        Shopbulet = pygame.image.load("shoot3.png")
                        Shopbulet.set_colorkey((255, 255, 255))
                        Shopbulet = pygame.transform.scale(Shopbulet, (150, 120))
                    if Countdown == 0:
                        Shopbulet = pygame.image.load("shoot4.png")
                        Shopbulet.set_colorkey((255, 255, 255))
                        Shopbulet = pygame.transform.scale(Shopbulet, (150, 120))
                    Piper.Shoot()


        Showdown = pygame.sprite.spritecollide(Piper, Enemybulet_group, True)
        for i in Showdown:
            Brawlerhealthnr -=1000
            if Brawlerhealthnr == 4000:
                Brawlerhealth = pygame.image.load("health2.png")
                Brawlerhealth = pygame.transform.scale(Brawlerhealth, ((130, 100)))
                Brawlerhealth.set_colorkey((255, 255, 255))
            if Brawlerhealthnr == 3000:
                Brawlerhealth = pygame.image.load("health3.png")
                Brawlerhealth = pygame.transform.scale(Brawlerhealth, ((130, 100)))
                Brawlerhealth.set_colorkey((255, 255, 255))
            if Brawlerhealthnr == 2000:
                Brawlerhealth = pygame.image.load("health4.png")
                Brawlerhealth = pygame.transform.scale(Brawlerhealth, ((130, 100)))
                Brawlerhealth.set_colorkey((255, 255, 255))
            if Brawlerhealthnr == 1000:
                Brawlerhealth = pygame.image.load("health5.png")
                Brawlerhealth = pygame.transform.scale(Brawlerhealth, ((130, 100)))
                Brawlerhealth.set_colorkey((255, 255, 255))
            if Brawlerhealthnr <=0:
                Start = 1




        Showdown = pygame.sprite.spritecollide(Kit, Bulet_group, True)
        for i in Showdown:
            Ulta +=1
            if Ulta <3:
                Enemyhealth -=1000
            if Ulta >=3:
                Enemyhealth -=3580
                Ulta = 0
            if Enemyhealth == 4000:
                Imagehealth = pygame.image.load("health2.png")
                Imagehealth = pygame.transform.scale(Imagehealth, ((130, 100)))
                Imagehealth.set_colorkey((255, 255, 255))
            if Enemyhealth == 3000:
                Imagehealth = pygame.image.load("health3.png")
                Imagehealth = pygame.transform.scale(Imagehealth, ((130, 100)))
                Imagehealth.set_colorkey((255, 255, 255))
            if Enemyhealth == 2000:
                Imagehealth = pygame.image.load("health4.png")
                Imagehealth = pygame.transform.scale(Imagehealth, ((130, 100)))
                Imagehealth.set_colorkey((255, 255, 255))
            if Enemyhealth == 1000:
                Imagehealth = pygame.image.load("health5.png")
                Imagehealth = pygame.transform.scale(Imagehealth, ((130, 100)))
                Imagehealth.set_colorkey((255, 255, 255))
            if Enemyhealth<=0:
                Nrboxstop +=1
                Enemies_group.empty()
                Enemybulet_group.empty()
                Reloadenemy = False

        if Enemyhealth>0:
            font = pygame.font.Font(None, 40)
            text = font.render(f"{Enemyhealth}", True, (0, 0, 0))
            Imagedrawing = Imagehealth.get_rect()
            Imagedrawing.center = (Kit.rect.x, Kit.rect.top)
            screen.blit(Imagehealth, Imagedrawing)
            text_rect = text.get_rect(center=(Kit.rect.x, Kit.rect.y))
            screen.blit(text, text_rect)

        Sometime = pygame.time.get_ticks()
        if not Reloadenemy and Sometime - Respawntimekit >= Sectimerespawn:
            Reloadenemy = True
            Canshoot = True
            Respawntimekit = Sometime
        if Reloadenemy == True:
            Enemies_group.add(Kit)
            Enemyhealth = 5000
            Imagehealth = pygame.image.load("health.png")
            Imagehealth = pygame.transform.scale(Imagehealth, ((130, 100)))
            Imagehealth.set_colorkey((255, 255, 255))
            Reloadenemy = False

        Emzstart = pygame.image.load("Emzstart.jpg")
        Emzstart = pygame.transform.scale(Emzstart, (200, 200))
        Emzstartrect = Emzstart.get_rect(center=(250, 250))
        screen.blit(Emzstart, Emzstartrect)

        Enemies_group.update()
        all_sprites.update(position)
        all_sprites.draw(screen)
        Enemies_group.draw(screen)
        Enemybulet_group.draw(screen)
        piperposition = (Piper.rect.x, Piper.rect.y)
        Enemybulet_group.update(position)

        if Shootenemybulet > 0:
            Shootenemybulet -= 1
            if Canshoot:
                Kit.Shoot()
            Timerenemybulet = 2
        Timerenemybulet -=0.01
        if Timerenemybulet <=0:
            Shootenemybulet = 1


        if Countdown <=0:
            Restore += 0.005
            if Restore >=1:
                Restore = 0
                Countdown = 3
                Shopbulet = pygame.image.load("shoot1.png")
                Shopbulet.set_colorkey((255, 255, 255))
                Shopbulet = pygame.transform.scale(Shopbulet, (150, 120))


        if Imagetime >0:
            Imagetime-=0.009
            Imageobjrect = Imageobjbox.get_rect()
            Imageobjrect.center = ((400,300))
            screen.blit(Imageobjbox, Imageobjrect)



        Piper_group.update(position)
        Piper_group.draw(screen)
        Shopbuletdrawing = Shopbulet.get_rect(center=(Piper.rect.x +17, Piper.rect.y))
        screen.blit(Shopbulet, Shopbuletdrawing)
        Imagebrawler = Brawlerhealth.get_rect(center=(Piper.rect.x +25, Piper.rect.y -19))
        screen.blit(Brawlerhealth, Imagebrawler)
        font = pygame.font.Font(None, 36)
        text = font.render(f"{Brawlerhealthnr}", True, (0, 0, 0))
        text_rect = text.get_rect(center=(Piper.rect.x +21, Piper.rect.y -20))
        screen.blit(text, text_rect)

        clock.tick(FPS)
        pygame.display.update()

    if Start == 2:
        screen.fill((0, 191, 255))
        Profilebutton = pygame.image.load("profilebutton.jpg")
        Profilebutton = pygame.transform.scale(Profilebutton, (80, 60))
        Profilebuttonrect = Profilebutton.get_rect(center=(50, 40))
        screen.blit(Profilebutton, Profilebuttonrect)

        Shopbutton = pygame.image.load("shopbutton.png")
        Shopbutton = pygame.transform.scale(Shopbutton, (80, 60))
        Shopbuttonrect = Shopbutton.get_rect(center=(50, 220))
        screen.blit(Shopbutton, Shopbuttonrect)

        Brawlersbutton = pygame.image.load("brawlersbutton.png")
        Brawlersbutton = pygame.transform.scale(Brawlersbutton, (70, 50))
        Brawlersbuttonrect = Brawlersbutton.get_rect(center=(44, 286))
        screen.blit(Brawlersbutton, Brawlersbuttonrect)

        Playbutton = pygame.image.load("playbutton.png")
        Playbutton = pygame.transform.scale(Playbutton, (250, 100))
        Playbuttonrect = Playbutton.get_rect(center=(670, 540))
        screen.blit(Playbutton, Playbuttonrect)

        Eventbutton = pygame.image.load("eventbutton.png")
        Eventbutton = pygame.transform.scale(Eventbutton, (350, 90))
        Eventbuttonrect = Eventbutton.get_rect(center=(365, 540))
        screen.blit(Eventbutton, Eventbuttonrect)

        Emzbrawler = pygame.image.load("emz.jpg")
        Emzbrawler.set_colorkey((255, 255, 255))
        Emzbrawler = pygame.transform.scale(Emzbrawler, (300, 400))
        Emzbrawlerrect = Emzbrawler.get_rect(center=(400, 270))
        screen.blit(Emzbrawler, Emzbrawlerrect)

        if Nrboxstop <3:
            Box_group.empty()
            Brawl_Box = Boxes("brawl box stop.jpg", 140, 140)
            Box_group.add(Brawl_Box)
        else:
            Box_group.empty()
            Brawl_Box = Boxes("brawl box.jpg", 140, 140)
            Box_group.add(Brawl_Box)
        Box_group.update()
        Box_group.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = event.pos
                if position[0] >= 10 and position[0] <= 90 and position[1] >= 10 and position[1] <= 70:
                    Start = 3
                if position[0] >= 250 and position[0] <= 400 and position[1] >= 500 and position[1] <= 600:
                    Start = 4
                if position[0] >= 10 and position[0] <= 100 and position[1] >= 190 and position[1] <= 240:
                    Start = 5
                if position[0] >= 10 and position[0] <= 100 and position[1] >= 270 and position[1] <= 310:
                    Start = 6
                    print("6")
                if position[0] >= 550 and position[0] <= 800 and position[1] >= 500 and position[1] <= 600:
                    Start = 0

                if position[0] >= 10 and position[0] <= 60 and position[1] >= 10 and position[1] <= 60:
                        # Brawl_Box = Boxes("brawl box.jpg", 600, 600)
                        # Box_group.add(Brawl_Box)
                        show_message = True
                        message_time = time.time()
                        surprise = 1

            if surprise == 1:
                Box_group.update()
                Box_group.draw(screen)
                if show_message and time.time() - message_time < 5:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Loading", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(60, 60))
                    screen.blit(text, text_rect)
                elif show_message and time.time() - message_time >= 5:
                        show_message = False

                        a = "Brawlers"  # random.choice(list_of_objbox)

                        if a == "Coins":
                            Coins += 300
                            Imagetime = 3
                            Imageobjbox = pygame.image.load("coins.jpg")
                        if a == "Gems":
                            Gems += 10
                            Imagetime = 3
                            Imageobjbox = pygame.image.load("gems.png")
                        if a == "Credits":
                            Credits += 500
                            Imagetime = 3
                            Imageobjbox = pygame.image.load("credits.png")
                        if a == "XP":
                            XP += 500
                            Imagetime = 3
                            Imageobjbox = pygame.image.load("XP.png")
                        if a == "Brawlers":
                            a = "emz"  # random.choice(List_of_brawlers)
                            conn = sqlite3.connect('Brawlers.db')
                            cursor = conn.cursor()
                            cursor.execute("INSERT INTO Brawlers (name, image_name) VALUES ('Emz', 'emz.jpg')")
                            print("1")
                            conn.commit()
                            conn.close()
                            Imageobjbox = pygame.image.load(f"{a}cover.jpg")
                            Imageobjbox = pygame.transform.scale(Imageobjbox, ((800, 400)))
                            # Imageobjbox = pygame.image.load(f"{a}.jpg")
                            # Imagebrawlers = a

                            Imagetime = 5
        pygame.display.update()
    if Start == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = event.pos
                if position[0] >= 10 and position[0] <= 150 and position[1] >= 100 and position[1] <= 150:
                    Start = 2

        Profile = pygame.image.load("profile.jpg")
        Profile = pygame.transform.scale(Profile, (800, 400))
        Profilerect = Profile.get_rect(center=(400, 300))
        screen.blit(Profile, Profilerect)
        pygame.display.update()
    if Start == 6:
        screen.fill((65, 105, 225))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        Profile = pygame.image.load("emzbraw.jpg")
        Profile = pygame.transform.scale(Profile, (100, 100))
        Profilerect = Profile.get_rect(center=(80, 110))
        screen.blit(Profile, Profilerect)
        pygame.display.update()