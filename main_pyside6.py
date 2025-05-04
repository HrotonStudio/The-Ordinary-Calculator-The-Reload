from src.lib_usual import *
from src.lib_PySide6_usual import *
from src.base import Base
from src.java_support import *
from src.tips import *
from src.settings import *
from src.background_picture import picture
from src.background_music import *
from ui.py.main_window_ui import Ui_MainWindow
from utils.login import login

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        user_name = login()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        Base.log("I", "主窗口创建", "MyMainWindow.__init__")

        root_dir = os.path.dirname(os.path.abspath(__file__))
        self.setWindowIcon(QIcon(root_dir + "\\icon.jpg"))

        self.main_str = ""

        self.wait_for_operating = []

        self.setWindowTitle("普普通通的计算器：再临")

        self.text_browser_main_displayer = self.ui.TextBrowserMainDisplayer
        self.textBrowserTips = self.ui.textBrowserTips

        self.pushButtonAdd = self.ui.pushButtonAdd
        self.pushButtonSub = self.ui.pushButtonSub
        self.pushButtonMul = self.ui.pushButtonMul
        self.pushButtonTruediv = self.ui.pushButtonTruediv
        self.pushButtonClear = self.ui.pushButtonClear
        self.pushButtonEquals = self.ui.pushButtonEquals
        self.pushButtonNum0 = self.ui.pushButtonNum0
        self.pushButtonNum1 = self.ui.pushButtonNum1
        self.pushButtonNum2 = self.ui.pushButtonNum2
        self.pushButtonNum3 = self.ui.pushButtonNum3
        self.pushButtonNum4 = self.ui.pushButtonNum4
        self.pushButtonNum5 = self.ui.pushButtonNum5
        self.pushButtonNum6 = self.ui.pushButtonNum6
        self.pushButtonNum7 = self.ui.pushButtonNum7
        self.pushButtonNum8 = self.ui.pushButtonNum8
        self.pushButtonNum9 = self.ui.pushButtonNum9
        self.pushButtonPoint = self.ui.pushButtonPoint

        self.pushButtonReloadTips = self.ui.pushButtonReloadTips

        self.button_list = [
            self.pushButtonAdd,
            self.pushButtonSub,
            self.pushButtonMul,
            self.pushButtonTruediv,
            self.pushButtonEquals,
            self.pushButtonClear,

            self.pushButtonNum0,
            self.pushButtonNum1,
            self.pushButtonNum2,
            self.pushButtonNum3,
            self.pushButtonNum4,
            self.pushButtonNum5,
            self.pushButtonNum6,
            self.pushButtonNum7,
            self.pushButtonNum8,
            self.pushButtonNum9,
            self.pushButtonPoint, 
            self.pushButtonReloadTips
        ]

        self.textbrowser_list = [
            self.text_browser_main_displayer,
            self.textBrowserTips
        ]

        self.pushButtonAdd.clicked.connect(self.bt_add_click)
        self.pushButtonSub.clicked.connect(self.bt_sub_click)
        self.pushButtonMul.clicked.connect(self.bt_mul_click)
        self.pushButtonTruediv.clicked.connect(self.bt_truediv_click)
        self.pushButtonClear.clicked.connect(self.bt_clear_click)
        self.pushButtonEquals.clicked.connect(self.bt_equals_click)
        self.pushButtonNum0.clicked.connect(self.bt_0_click)
        self.pushButtonNum1.clicked.connect(self.bt_1_click)
        self.pushButtonNum2.clicked.connect(self.bt_2_click)
        self.pushButtonNum3.clicked.connect(self.bt_3_click)
        self.pushButtonNum4.clicked.connect(self.bt_4_click)
        self.pushButtonNum5.clicked.connect(self.bt_5_click)
        self.pushButtonNum6.clicked.connect(self.bt_6_click)
        self.pushButtonNum7.clicked.connect(self.bt_7_click)
        self.pushButtonNum8.clicked.connect(self.bt_8_click)
        self.pushButtonNum9.clicked.connect(self.bt_9_click)
        self.pushButtonPoint.clicked.connect(self.bt_point_click)

        self.pushButtonReloadTips.clicked.connect(self.reload_tips)

        self.text_browser_main_displayer.setReadOnly(True)

        self.textBrowserTips.setReadOnly(True)
        
        Base.log("I", "初始化完成", "MyMainWindow.__init__")

        self.custom_tips()
        Base.log("I", "提示信息展示", "MyMainWindow.__init__.custom_tips")

        if MusicIsPlaying:
            music_thread = threading.Thread(target=play_music, args=(the_music_list,))
            music_thread.daemon = True
            music_thread.start()
            Base.log("I", "背景音乐播放", "MyMainWindow.play_music")
        else:
            pass

    def paintEvent(self, event:QPaintEvent):

        painter = QPainter(self)

        pixmap = QPixmap(picture)
        painter.drawPixmap(self.rect(), pixmap)
        painter.end()

    @Slot()
    def bt_1_click(self):
        self.main_str+="1"
        Base.log("I", f"字符串添加: '1' ; main_str={self.main_str}", "MainWindow.bt_1_click")
        self.text_browser_main_displayer.insertPlainText("1")

    @Slot()
    def bt_2_click(self):
        self.main_str+="2"
        Base.log("I", f"字符串添加: '2' ; main_str={self.main_str}", "MainWindow.bt_2_click")
        self.text_browser_main_displayer.insertPlainText("2")

    @Slot()
    def bt_3_click(self):
        self.main_str+="3"
        Base.log("I", f"字符串添加: '3' ; main_str={self.main_str}", "MainWindow.bt_3_click")
        self.text_browser_main_displayer.insertPlainText("3")

    @Slot()
    def bt_4_click(self):
        self.main_str+="4"
        Base.log("I", f"字符串添加: '4' ; main_str={self.main_str}", "MainWindow.bt_4_click")
        self.text_browser_main_displayer.insertPlainText("4")

    @Slot()
    def bt_5_click(self):
        self.main_str+="5"
        Base.log("I", f"字符串添加: '5' ; main_str={self.main_str}", "MainWindow.bt_5_click")
        self.text_browser_main_displayer.insertPlainText("5")

    @Slot()
    def bt_6_click(self):
        self.main_str+="6"
        Base.log("I", f"字符串添加: '6' ; main_str={self.main_str}", "MainWindow.bt_6_click")
        self.text_browser_main_displayer.insertPlainText("6")

    @Slot()
    def bt_7_click(self):
        self.main_str+="7"
        Base.log("I", f"字符串添加: '7' ;main_str={self.main_str}", "MainWindow.bt_7_click")
        self.text_browser_main_displayer.insertPlainText("7")

    @Slot()
    def bt_8_click(self):
        self.main_str+="8"
        Base.log("I", f"字符串添加: '8' ;main_str={self.main_str}", "MainWindow.bt_8_click")
        self.text_browser_main_displayer.insertPlainText("8")

    @Slot()
    def bt_9_click(self):
        self.main_str+="9"
        Base.log("I", f"字符串添加: '9' ;main_str={self.main_str}", "MainWindow.bt_9_click")
        self.text_browser_main_displayer.insertPlainText("9")

    @Slot()
    def bt_0_click(self):
        self.main_str+="0"
        Base.log("I", f"字符串添加: '0' ;main_str={self.main_str}", "MainWindow.bt_0_click")
        self.text_browser_main_displayer.insertPlainText("0")

    @Slot()
    def bt_point_click(self):
        self.main_str+="."
        Base.log("I", f"字符串添加: '.' ;main_str={self.main_str}", "MainWindow.bt_point_click")
        self.text_browser_main_displayer.insertPlainText(".")

    @Slot()
    def bt_add_click(self):
        if "." in self.main_str:
            self.wait_for_operating.append(f"HPF({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPF({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_add_click")
        else:
            self.wait_for_operating.append(f"HPI({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPI({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_add_click")
        self.main_str=""
        Base.log("I", f"字符串清空: '' ;main_str={self.main_str}", "MainWindow.bt_add_click")
        self.wait_for_operating.append("+")
        Base.log("I", f"列表元素添加: '+' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_add_click")
        self.text_browser_main_displayer.insertPlainText("+")

    @Slot()
    def bt_sub_click(self):
        if self.main_str == "":
            self.main_str+="-"
            self.text_browser_main_displayer.insertPlainText("-")
        else:
            if "." in self.main_str:
                self.wait_for_operating.append(f"HPF({self.main_str})")
                Base.log("I", f"列表元素添加: 'HPF({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_sub_click")
            else:
                self.wait_for_operating.append(f"HPI({self.main_str})")
                Base.log("I", f"列表元素添加: 'HPI({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_sub_click")
            self.main_str=""
            Base.log("I", f"字符串清空: '' ;main_str={self.main_str}", "MainWindow.bt_sub_click")
            self.wait_for_operating.append("-")
            Base.log("I", f"列表元素添加: '-' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_sub_click")
            self.text_browser_main_displayer.insertPlainText("-")

    @Slot()
    def bt_mul_click(self):
        if "." in self.main_str:
            self.wait_for_operating.append(f"HPF({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPF({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_mul_click")
        else:
            self.wait_for_operating.append(f"HPI({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPI({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_mul_click")
        self.main_str=""
        Base.log("I", f"字符串清空", "MainWindow.bt_mul_click.main_str")
        self.wait_for_operating.append("*")
        Base.log("I", f"列表元素添加: '*' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_mul_click")
        self.text_browser_main_displayer.insertPlainText("x")

    @Slot()
    def bt_truediv_click(self):
        if "." in self.main_str:
            self.wait_for_operating.append(f"HPF({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPF({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_truediv_click")
        else:
            self.wait_for_operating.append(f"HPI({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPI({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_truediv_click")
        self.main_str=""
        Base.log("I", f"字符串清空", "MainWindow.bt_truediv_click.main_str")
        self.wait_for_operating.append("/")
        Base.log("I", f"列表元素添加: '/' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_truediv_click")
        self.text_browser_main_displayer.insertPlainText("÷")

    @Slot()
    def bt_equals_click(self):
        if "." in self.main_str:
            self.wait_for_operating.append(f"HPF({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPF({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_equals_click")
        else:
            self.wait_for_operating.append(f"HPI({self.main_str})")
            Base.log("I", f"列表元素添加: 'HPI({self.main_str})' ; wait_for_operating={self.wait_for_operating}", "MainWindow.bt_equals_click")
        self.main_str=""
        Base.log("I", f"字符串清空", "MainWindow.bt_equals_click.main_str")
        need_operate = ""
        for i in self.wait_for_operating:
            need_operate += i
        self.wait_for_operating = []
        try:
            result = eval(need_operate)
            Base.log("I", f"计算结果获取: {result}", "MainWindow.bt_equals_click")
            self.text_browser_main_displayer.clear()
            Base.log("I", f"文本框清空", "MainWindow.bt_equals_click")
            self.text_browser_main_displayer.insertPlainText(str(result))
            Base.log("I", f"结果展示: {str(result)}", "MainWindow.bt_equals_click.displayer")
            self.main_str = str(result)
            Base.log("I", f"字符串添加: {self.main_str}", "MainWindow.bt_equals_click")
        except Exception as e:
            Base.log("E", f"出现错误: {e}", "MainWindow.bt_equals_click")
            self.text_browser_main_displayer.clear()
            Base.log("I", f"文本框清空", "MainWindow.bt_equals_click")

    @Slot()
    def bt_clear_click(self):
        self.main_str=""
        Base.log("I", f"字符串清空", "MainWindow.bt_clear_click.main_str")
        self.wait_for_operating = []
        Base.log("I", f"列表清空", "MainWindow.bt_clear_click.wait_for_operating")
        self.text_browser_main_displayer.clear()
        Base.log("I", f"文本框清空", "MainWindow.bt_equals_click.displayer")

    @Slot()
    def custom_tips(self):

        self.tips = random.choice(list_tips)

        if self.tips == tips_by_NoneColdWind:
            writer = "NoneColdWind"
        elif self.tips == tips_by_JustNothing:
            writer = "JustNothing"
        elif self.tips == tips_by_NAN:
            writer = "NAN"
        elif self.tips == tips_by_DYD:
            writer = "DYD"
        elif self.tips == tips_by_云沫:
            writer = "云沫"

        text = random.choice(self.tips)

        self.textBrowserTips.setText(f"{text}\n                                                       ————{writer}")

    def reload_tips(self):
        self.tips = random.choice(list_tips)

        if self.tips == tips_by_NoneColdWind:
            writer = "NoneColdWind"
        elif self.tips == tips_by_JustNothing:
            writer = "JustNothing"
        elif self.tips == tips_by_NAN:
            writer = "NAN"
        elif self.tips == tips_by_DYD:
            writer = "DYD"
        elif self.tips == tips_by_云沫:
            writer = "云沫"

        text = random.choice(self.tips)

        self.textBrowserTips.setText(f"{text}\n                                                       ————{writer}")

        Base.log("I", f"提示刷新[文本:{text}, 作者:{writer}]", "MyMainWindow.reload_tips")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())