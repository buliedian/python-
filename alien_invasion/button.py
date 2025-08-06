import pygame.font#font 字体

class Button:
    def __init__(self,ai_game,msg):
        """初始化按钮的属性"""
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        #设置按钮的尺寸和其他属性
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)#设置字体，默认字体，48号
        #创建rect对象
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #按钮的标签值需创建一次
        self._prep_msg(msg)#将字体渲染为图像


    def _prep_msg(self,msg):
        """将prep渲染成图像，并使其在按钮上居中"""
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)#绘制按钮的矩形
        self.screen.blit(self.msg_image,self.msg_image_rect)
