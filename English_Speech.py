from manim import *

class s(Scene):
	def construct(self):
		#first
		Text11=Text("Hello, everyone!", 
			font="SDK_SC_Web").next_to(Dot([0,0,0]),UP)
		Text12=Text("Teyvat News here.", 
			font="SDK_SC_Web").next_to(Dot([0,0,0]),DOWN)
		self.play(Write(Text11),run_time=1)
		self.play(Write(Text12),run_time=1)
		self.play(FadeOut(Text11),
			FadeOut(Text12),
			run_time=0.5)
		self.wait(0.5)
		#second
		Text21=Text("Recently on May 20th,", 
			font="SDK_SC_Web").move_to(Dot([0,2,0]))
		Text22=Text("miHoYo, what makes Genshin Impact,", 
			font="SDK_SC_Web").move_to(Dot([0,1,0]))
		Text22[0:6].set_color(BLUE)
		Text22[-14:-1].set_color(BLUE)
		Text23=Text("has released their update preview", 
			font="SDK_SC_Web").move_to(Dot([0,0,0]))
		Text232=Text("of version 2.7,", 
			font="SDK_SC_Web").move_to(Dot([0,-1,0]))
		Text24=Text('''
			whose theme is "Hidden Dreams".
			''', 
			font="SDK_SC_Web").move_to(Dot([0,-2,0]))
		Text24[-15:-1].set_color(BLUE)
		self.play(Write(Text21), run_time=2);
		self.wait(0.1)
		self.play(Write(Text22), run_time=3);
		self.wait(0.1)
		self.play(Write(Text23), run_time=4);
		self.play(Write(Text232), run_time=1);
		self.wait(0.1)
		self.play(Write(Text24), run_time=2.5);
		self.wait(0.5)
		#third
		Text31=Text("After delay due to the pandemic,", 
			font="SDK_SC_Web").move_to(Dot([0,1,0]))
		Text32=Text("what does miHoYo", 
			font="SDK_SC_Web").move_to(Dot([0,0,0]))
		Text322=Text("have in store for players?", 
			font="SDK_SC_Web").move_to(Dot([0,-1,0]))
		self.play(ReplacementTransform(VGroup(Text21,Text22),Text31), run_time=1)
		self.wait(1.5)
		self.play(ReplacementTransform(VGroup(Text23,Text24,Text232),VGroup(Text32,Text322)), run_time=1)
		self.wait(2.5)
		self.wait(0.5)
		#fourth
		Text4=Text("Let's watch the promotion video(PV).", 
			font="SDK_SC_Web")
		Text4[-22:-1].set_color(YELLOW)
		self.play(ReplacementTransform(VGroup(Text31,Text32,Text322),Text4))
		self.wait(2)

class e(Scene):
	def construct(self):
		#first
		Text11=Text("So do you have a", 
			font="SDK_SC_Web").next_to(Dot([0,0,0]),UP)
		Text12=Text("general understanding of this update?", 
			font="SDK_SC_Web").next_to(Dot([0,0,0]),DOWN)
		self.play(Write(Text11),run_time=1.2)
		self.play(Write(Text12),run_time=3)
		self.wait(0.5)
		#second
		Text21=Text("If not, don't worry,", 
			font="SDK_SC_Web").move_to(Dot([0,1,0]))
		Text22=Text("you'll find the link to more details", 
			font="SDK_SC_Web").move_to(Dot([0,0,0]))
		Text23=Text("in the text below.", 
			font="SDK_SC_Web").move_to(Dot([0,-1,0]))
		Text23[-10:-6].set_color(RED)
		self.play(ReplacementTransform(VGroup(Text11,Text12),VGroup(Text21,Text22,Text23)))
		self.wait(2)
		URL=Text("https://webstatic.mihoyo.com/ys/event/e20220430-previ-xozn/index.html", 
			font="SDK_SC_Web",font_size=22,color=RED).shift(DOWN*3)
		self.play(Write(URL))
		self.wait(3)
		Text3=Text("That's all, thank you!", 
			font="SDK_SC_Web")
		self.play(ReplacementTransform(VGroup(Text21,Text22,Text23,URL),Text3));
		self.wait(1.5)
		self.play(FadeOut(Text3))
		self.wait()
		GitHub1=Text("GitHub(Source Code and Release):", 
			font="Latin Modren",font_size=30).next_to(Dot([-7,3,0]),RIGHT)
		GitHub2=Text("https://github.com/CaiJi-Feizao/English-Speech-20220523/", 
			font="Latin Modren",font_size=30).next_to(Dot([-7,2,0]),RIGHT)
		Pro=Text("Made with Manim and Premiere", 
			font="Latin Modren",color=BLUE).shift(DOWN*3)
		self.play(Write(GitHub1))
		self.play(Write(GitHub2),run_time=2)
		self.play(Write(Pro))
		self.wait()
		self.play(FadeOut(VGroup(GitHub1,GitHub2,Pro)))