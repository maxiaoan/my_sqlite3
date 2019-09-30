import turtle  # 导入turtle模块
turtle.setup(1200, 800, 0, 0)
turtle.bgcolor("red")      # 背景颜色
turtle.color('yellow')     # 五角星颜色
turtle.speed(5)           # 设置画笔绘制速度
# 绘制最大的主五角星
turtle.begin_fill()        # 填充绘制的五角星
turtle.up()                # 抬笔不绘制
turtle.goto(-520, 240)     # 画笔设置到起始位置
turtle.down()              # 落笔进行绘制
for i in range(5):         # 循环5次
    turtle.forward(240)      # 向前移动150
    turtle.right(144)      # 以角度单位向右转动
turtle.end_fill()          # 结束填充
# 绘制第1颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-230,345)
turtle.setheading(305)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.left(144)
turtle.end_fill()

# 绘制第2颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-150,230)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.right(144)
turtle.end_fill()

# 绘制第3颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-155,130)
turtle.setheading(0)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.right(144)
turtle.end_fill()

# 绘制第4颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-230,68)
turtle.setheading(300)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.left(144)
turtle.end_fill()
turtle.hideturtle()  # 隐藏箭头
turtle.done()        # 开始循环防止窗口自动关闭