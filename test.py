import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("函数绘图器")
        self.setGeometry(100, 100, 800, 600)

        # 创建中心小部件
        widget = QWidget()
        self.setCentralWidget(widget)

        # 设置垂直布局
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # 添加输入框和按钮
        self.function_input = QLineEdit(self)
        self.function_input.setPlaceholderText("输入函数表达式 (如 x**2)")
        layout.addWidget(self.function_input)

        plot_button = QPushButton("绘制", self)
        plot_button.clicked.connect(self.update_plot)
        layout.addWidget(plot_button)

        # 创建画布用于绘图
        self.canvas = FigureCanvas(Figure())
        layout.addWidget(self.canvas)

        # 初始化图形
        self.ax = self.canvas.figure.subplots()
        self.ax.set_title("函数图像")

    def update_plot(self):
        """更新图像"""
        try:
            # 清除之前的图像
            self.ax.clear()

            # 获取用户输入的函数表达式
            expression = self.function_input.text()
            if not expression:
                return

            # 使用 eval 来计算函数值。注意：在实际应用中直接使用 eval 是不安全的。
            import numpy as np
            x = np.linspace(-10, 10, 400)
            y = eval(expression, {"__builtins__": None}, {'x': x, 'sin': np.sin, 'cos': np.cos, 'exp': np.exp})

            # 绘制新图像
            self.ax.plot(x, y)
            self.ax.set_title(f"y = {expression}")
            self.canvas.draw()
        except Exception as e:
            print(f"错误: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PlotWindow()
    main.show()
    sys.exit(app.exec())