"""
现代化灵动岛 - Windows上的动态岛式小部件。
"""
import os
from datetime import datetime
from PySide6.QtCore import (
    QEvent,
    QThread,
    QEasingCurve,
    QPropertyAnimation,
    QPoint,
    QRect,
    Qt,
    QTimer,
    Signal,
)
from PySide6.QtGui import QPixmap, QPainter, QRegion, QPainterPath
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from app.utils import (
    extract_urls,
    get_all_status,
    get_clipboard_text,
    get_system_brightness,
    open_url,
    open_urls,
    set_brightness,
)


class WorkerThread(QThread):
    """后台工作线程，用于执行耗时操作。"""
    finished_signal = Signal(object)
    error_signal = Signal(str)

    def __init__(self, task_func, *args, **kwargs):
        super().__init__()
        self.task_func = task_func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.task_func(*self.args, **self.kwargs)
            self.finished_signal.emit(result)
        except Exception as e:
            self.error_signal.emit(str(e))


class ModernIsland(QWidget):
    """带展开式控制面板的现代化灵动岛小部件。"""
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating, False)

        # 状态与尺寸 - 匹配原始需求
        self.is_expanded = False
        self.screen_w = QApplication.primaryScreen().size().width()
        self.screen_h = QApplication.primaryScreen().size().height()
        self.max_expand_h = self.screen_h // 3
        self.multi_url_btn_top_spacing = 35

        # 核心尺寸：常驻细胶囊 + 展开大胶囊
        self.col_rect = QRect((self.screen_w - 180) // 2, 20, 180, 32)  # 常驻：3cm长×0.8cm高
        self.exp_rect = QRect((self.screen_w - 360) // 2, 20, 360, 160) # 展开：5cm长，适配功能高度
        self.setGeometry(self.col_rect)

        # 拖动相关（已固定，保留代码不启用）
        self.dragging = False
        self.drag_start_pos = None
        self.window_start_pos = None

        # 监听焦点变化
        QApplication.instance().focusChanged.connect(self.on_focus_changed)

        # 主容器 - 胶囊核心
        self.container = QFrame(self)
        self.container.setObjectName("IslandContainer")
        self.container.setFixedSize(180, 32)  # 匹配常驻尺寸
        self.layout = QVBoxLayout(self.container)
        self.layout.setContentsMargins(15, 0, 15, 0)

        # 折叠态时间标签（常驻时透明，仅留黑胶囊）
        self.time_label = QLabel("")
        self.time_label.setObjectName("TimeLabel")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFixedHeight(32)

        # 展开态日期+时间标签
        self.date_label = QLabel("")
        self.date_label.setObjectName("DateLabel")
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFixedHeight(32)
        self.date_label.hide()
        self.date_label.setParent(self.container)

        # 展开态多页面管理
        self.controls = QStackedWidget()
        self.controls.hide()

        # 页面0: 控制面板
        self.ctrl_page = QWidget()
        self.ctrl_layout = QVBoxLayout(self.ctrl_page)
        self.ctrl_layout.setContentsMargins(5, 20, 5, 10)
        self.ctrl_layout.setSpacing(15)

        # 页面1: 单URL提示页面
        self.url_single_page = QWidget()
        self.url_single_layout = QVBoxLayout(self.url_single_page)
        self.url_single_layout.setContentsMargins(10, 15, 10, 15)
        self.url_single_layout.setSpacing(10)

        # 页面2: 多URL提示页面
        self.url_multi_page = QWidget()
        self.url_multi_layout = QVBoxLayout(self.url_multi_page)
        self.url_multi_layout.setContentsMargins(10, 10, 10, 10)
        self.url_multi_layout.setSpacing(8)

        # 页面加入容器
        self.controls.addWidget(self.ctrl_page)
        self.controls.addWidget(self.url_single_page)
        self.controls.addWidget(self.url_multi_page)

        # 图标缓存与亮度控制
        self._icon_cache = {}
        self._preload_icons()
        self.bright_row, self.bright_slider, self.bright_val = \
            self.create_ctrl_row("resources/icons/light.png", "亮度")
        self.bright_slider.valueChanged.connect(
            lambda v: self.update_val(self.bright_val, v, "bright")
        )

        # 状态栏（WiFi/蓝牙/电池）
        self.status_bar = QWidget()
        self.status_layout = QHBoxLayout(self.status_bar)
        self.status_layout.setContentsMargins(10, 5, 10, 5)
        self.status_layout.setSpacing(15)

        # WiFi信息
        self.wifi_icon = QLabel()
        self.wifi_icon.setObjectName("IconLabel")
        if "resources/icons/internet.png" in self._icon_cache:
            self.wifi_icon.setPixmap(self._icon_cache["resources/icons/internet.png"])
        else:
            self.wifi_icon.setText("📶")
        self.wifi_label = QLabel("未连接")
        self.wifi_label.setObjectName("StatusLabel")

        # 蓝牙信息
        self.bluetooth_icon = QLabel()
        self.bluetooth_icon.setObjectName("IconLabel")
        if "resources/icons/bluetooth.png" in self._icon_cache:
            self.bluetooth_icon.setPixmap(self._icon_cache["resources/icons/bluetooth.png"])
        else:
            self.bluetooth_icon.setText("🔵")
        self.bluetooth_label = QLabel("未连接")
        self.bluetooth_label.setObjectName("StatusLabel")

        # 电池信息
        self.battery_icon = QLabel()
        self.battery_icon.setObjectName("IconLabel")
        if "resources/icons/battery.png" in self._icon_cache:
            self.battery_icon.setPixmap(self._icon_cache["resources/icons/battery.png"])
        else:
            self.battery_icon.setText("🔋")
        self.battery_label = QLabel("未知")
        self.battery_label.setObjectName("StatusLabel")

        # 状态栏布局组装
        wifi_layout = QHBoxLayout()
        wifi_layout.setSpacing(5)
        wifi_layout.addWidget(self.wifi_icon)
        wifi_layout.addWidget(self.wifi_label)

        bluetooth_layout = QHBoxLayout()
        bluetooth_layout.setSpacing(5)
        bluetooth_layout.addWidget(self.bluetooth_icon)
        bluetooth_layout.addWidget(self.bluetooth_label)

        battery_layout = QHBoxLayout()
        battery_layout.setSpacing(5)
        battery_layout.addWidget(self.battery_icon)
        battery_layout.addWidget(self.battery_label)

        self.status_layout.addLayout(wifi_layout)
        self.status_layout.addLayout(bluetooth_layout)
        self.status_layout.addLayout(battery_layout)

        self.ctrl_layout.addLayout(self.bright_row)
        self.ctrl_layout.addWidget(self.status_bar)

        self.controls.setFixedHeight(120)
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.controls)

        # 时间更新定时器
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)
        self.update_time()

        # 状态栏更新定时器
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self._start_status_update)
        self.status_timer.start(5000)
        
        self._previous_wifi_status = None
        self._previous_bluetooth_status = None
        self._first_status_check = True
        
        self._start_status_update()

        # 亮度调节防抖
        self.debounce_timer = QTimer(self)
        self.debounce_timer.setSingleShot(True)
        self.debounce_timer.timeout.connect(self._start_brightness_apply)
        self.debounce_timer.setInterval(180)
        self.current_brightness = 50

        # 剪贴板监听
        self._last_clipboard_text = ""
        self._clipboard_first_check = True
        self._clipboard_timer = QTimer(self)
        self._clipboard_timer.timeout.connect(self._check_clipboard)
        self._clipboard_timer.start(1500)

        self._url_dialog = None
        self._url_checkboxes = {}
        self._start_initial_values_load()

        self.current_brightness = 50
        self.load_qss()
        self._update_rounded_mask()

    def _preload_icons(self):
        """预加载图标以提高性能。"""
        icon_files = ["resources/icons/light.png", "resources/icons/volume.png",
                     "resources/icons/internet.png", "resources/icons/bluetooth.png",
                     "resources/icons/battery.png"]
        for path in icon_files:
            if os.path.exists(path):
                pixmap = QPixmap(path)
                self._icon_cache[path] = pixmap.scaled(
                    20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )

    def _start_initial_values_load(self):
        """异步加载初始值。"""
        self._brightness_thread = WorkerThread(get_system_brightness)
        self._brightness_thread.finished_signal.connect(
            self._on_brightness_loaded
        )
        self._brightness_thread.start()

    def _on_brightness_loaded(self, brightness):
        """亮度加载完成回调。"""
        if brightness is not None:
            brightness = max(0, min(100, brightness))
            self.bright_slider.setValue(brightness)
            self.bright_val.setText(f"{brightness}%")
            self.current_brightness = brightness

    def _start_status_update(self):
        """启动异步状态更新。"""
        if hasattr(self, '_status_thread') and self._status_thread.isRunning():
            return
        self._status_thread = WorkerThread(get_all_status)
        self._status_thread.finished_signal.connect(self._on_status_updated)
        self._status_thread.error_signal.connect(self._on_status_error)
        self._status_thread.start()
    
    def _on_status_error(self, error):
        """状态更新错误回调。"""
        print(f"状态更新失败: {error}")

    def _on_status_updated(self, result):
        """状态更新完成回调。"""
        wifi_info, bluetooth_devices, battery_info = result
        ssid, signal, dns_connected = wifi_info

        if ssid and ssid != "未连接":
            self.wifi_label.setText(f"{ssid} ({signal})")
        else:
            self.wifi_label.setText("未连接")

        if bluetooth_devices:
            device_name, status = bluetooth_devices[0]
            self.bluetooth_label.setText(f"{device_name} ({status})")
        else:
            self.bluetooth_label.setText("未连接")

        charge, status = battery_info
        if charge:
            self.battery_label.setText(f"{charge}% ({status})")
        else:
            self.battery_label.setText("未知")

        if self._first_status_check:
            self._previous_wifi_status = (ssid, dns_connected)
            self._previous_bluetooth_status = bluetooth_devices
            self._first_status_check = False
            return

        current_wifi_status = (ssid, dns_connected)
        current_bluetooth_status = bluetooth_devices
        wifi_connected = ssid and ssid != "未连接" and dns_connected
        prev_wifi_connected = self._previous_wifi_status and self._previous_wifi_status[0] and self._previous_wifi_status[0] != "未连接" and self._previous_wifi_status[1]
        bluetooth_connected = bluetooth_devices and bluetooth_devices[0][1] in ["已开启", "Connected", "已连接"]
        prev_bluetooth_connected = self._previous_bluetooth_status and self._previous_bluetooth_status[0][1] in ["已开启", "Connected", "已连接"]

        if wifi_connected != prev_wifi_connected:
            if wifi_connected:
                self._show_connection_animation("WiFi已连接", "📶")
            else:
                self._show_connection_animation("WiFi已断开", "📶")
        elif bluetooth_connected != prev_bluetooth_connected:
            if bluetooth_connected:
                self._show_connection_animation("蓝牙已连接", "🔵")
            else:
                self._show_connection_animation("蓝牙已断开", "🔵")

        self._previous_wifi_status = current_wifi_status
        self._previous_bluetooth_status = current_bluetooth_status

    def create_ctrl_row(self, icon_path, label_text):
        """创建包含图标、标签、滑动条和数值控件的行。"""
        row = QHBoxLayout()
        row.setSpacing(12)

        icon = QLabel()
        icon.setObjectName("IconLabel")
        if icon_path in self._icon_cache:
            icon.setPixmap(self._icon_cache[icon_path])
        elif label_text == "亮度":
            icon.setText("\u0f0a0")
        else:
            icon.setText("\u0f05a")

        label = QLabel(label_text)
        label.setObjectName("ValueLabel")
        label.setFixedWidth(30)

        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setFixedHeight(32)
        slider.setObjectName("CapsuleSlider")
        slider.setFixedWidth(180)

        val_label = QLabel("50%")
        val_label.setFixedWidth(40)
        val_label.setObjectName("ValueLabel")

        row.addWidget(icon)
        row.addWidget(label)
        row.addWidget(slider)
        row.addWidget(val_label)
        return row, slider, val_label

    def update_val(self, label, value, val_type):
        """更新数值标签并触发防抖应用。"""
        label.setText(f"{value}%")
        if val_type == "bright":
            self.current_brightness = value
            self.debounce_timer.stop()
            self.debounce_timer.start(180)

    def _start_brightness_apply(self):
        """异步应用亮度。"""
        if hasattr(self, '_brightness_apply_thread') and \
                self._brightness_apply_thread.isRunning():
            return
        self._brightness_apply_thread = WorkerThread(
            set_brightness, self.current_brightness
        )
        self._brightness_apply_thread.start()

    def mousePressEvent(self, event):
        """处理鼠标按下事件（固定位置，仅响应点击）。"""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_start_pos = event.globalPos()
            self.window_start_pos = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        """处理鼠标移动事件（已禁用拖动，保留代码）。"""
        if self.dragging:
            pass

    def mouseReleaseEvent(self, event):
        """处理鼠标释放事件 - 点击切换展开/折叠。"""
        if event.button() == Qt.LeftButton:
            if self.dragging and \
                    (event.globalPos() - self.drag_start_pos).manhattanLength() < 5:
                self.toggle_island()
            self.dragging = False

    def on_focus_changed(self, old_widget, new_widget):
        """失去焦点时自动收缩。"""
        if self.is_expanded:
            current_widget = new_widget
            while current_widget:
                if current_widget == self:
                    return
                current_widget = current_widget.parent()
            self.toggle_island()

    def toggle_island(self):
        """在展开和折叠状态之间切换 - 平滑渐变动画"""
        if hasattr(self, 'ani') and self.ani:
            self.ani.stop()
            self.ani.deleteLater()

        current_pos = self.pos()
        if not self.is_expanded:
            self.is_expanded = True
            self.time_label.hide()
            self.date_label.hide()

            self.ani = QPropertyAnimation(self, b"geometry")
            self.ani.setDuration(300)  # 平滑充气动画
            self.ani.setEasingCurve(QEasingCurve.InOutCubic)
            start = self.geometry()
            end = QRect(
                current_pos.x() + self.rect().width() / 2 - 180 , current_pos.y(),
                360, 160
            )
            self.ani.setStartValue(start)
            self.ani.setEndValue(end)
            self.ani.valueChanged.connect(self._update_rounded_mask)
            self.ani.finished.connect(lambda: (
                self.date_label.show(),
                self.update_time_display()
            ))
            self.controls.show()
            self.container.setFixedSize(360, 160)
            self.ani.start()
        else:
            self.is_expanded = False
            self.date_label.hide()
            self.time_label.hide()

            self.ani = QPropertyAnimation(self, b"geometry")
            self.ani.setDuration(250)  # 快速缩回动画
            self.ani.setEasingCurve(QEasingCurve.InOutCubic)
            start = self.geometry()
            end = QRect(
                current_pos.x() + self.rect().width() / 2 - 90, current_pos.y(),
                180, 32
            )
            self.ani.setStartValue(start)
            self.ani.setEndValue(end)
            self.ani.valueChanged.connect(self._update_rounded_mask)
            self.controls.setCurrentWidget(self.ctrl_page)
            self.controls.hide()
            self.ani.finished.connect(lambda: (
                self.time_label.show(),
                self.update_time_display(),
                self.container.setFixedSize(180, 32)
            ))
            self.ani.start()

    def update_time(self):
        """更新时间显示。"""
        self.update_time_display()

    def update_time_display(self):
        """根据展开/收起状态更新时间或日期显示。"""
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%m/%d")
        self.time_label.setText(current_time)
        self.date_label.setText(f"{current_date} {current_time}")

        if self.is_expanded:
            temp_label = QLabel(f"{current_date} {current_time}")
            temp_label.setObjectName("DateLabel")
            temp_label.setStyleSheet(self.date_label.styleSheet())
            temp_label.setFont(self.date_label.font())
            temp_label.adjustSize()
            width = temp_label.width()
            x = (360 - width) // 2
            self.date_label.setFixedWidth(width)
            self.date_label.move(x, 0)

    def show_notification_on_time(self, message, icon="📶"):
        """在灵动岛的时间位置显示通知。"""
        if hasattr(self, 'time_label'):
            self._original_time_text = self.time_label.text()
            if hasattr(self, 'time_timer'):
                self.time_timer.stop()
            self.time_label.setText(f"{icon} {message}")
            self._notification_timer = QTimer(self)
            self._notification_timer.setSingleShot(True)
            self._notification_timer.timeout.connect(self._restore_time_display)
            self._notification_timer.start(2000)
    
    def _restore_time_display(self):
        """恢复时间显示。"""
        if hasattr(self, 'time_label') and hasattr(self, '_original_time_text'):
            self.update_time()
            if hasattr(self, 'time_timer'):
                self.time_timer.start(1000)
            if hasattr(self, '_original_time_text'):
                delattr(self, '_original_time_text')
            if hasattr(self, '_notification_timer'):
                delattr(self, '_notification_timer')

    def eventFilter(self, obj, event):
        """事件过滤器，用于处理对话框关闭事件。"""
        if event.type() == QEvent.Close and obj == self._url_dialog:
            self._url_dialog = None
            return True
        return super().eventFilter(obj, event)

    def _check_clipboard(self):
        """检查剪贴板是否有新的 URL。"""
        current_text = get_clipboard_text()
        if not current_text:
            return
        if self._clipboard_first_check:
            self._last_clipboard_text = current_text
            self._clipboard_first_check = False
            return
        urls = extract_urls(current_text)
        if not urls:
            self._last_clipboard_text = current_text
            return
        if current_text == self._last_clipboard_text:
            return
        self._last_clipboard_text = current_text
        self._show_url_notification(urls)

    def _show_url_notification(self, urls: list):
        """显示 URL 通知在灵动岛内部。"""
        if len(urls) == 1:
            self.controls.setCurrentWidget(self.url_single_page)
            self._build_single_url_page(urls[0])
            target_height = 160
        else:
            self.controls.setCurrentWidget(self.url_multi_page)
            target_height = self._build_multi_url_page(urls)
            target_height = min(target_height, self.max_expand_h)

        self._expand_to_url_page(target_height)

        if hasattr(self, '_url_auto_close_timer') and self._url_auto_close_timer.isActive():
            self._url_auto_close_timer.stop()
        self._url_auto_close_timer = QTimer(self)
        self._url_auto_close_timer.setSingleShot(True)
        self._url_auto_close_timer.timeout.connect(self._close_url_page)
        self._url_auto_close_timer.start(5000)  # 5秒自动收缩，匹配原始需求

    def _build_single_url_page(self, url: str):
        """构建单个 URL 的页面。"""
        self._clear_layout(self.url_single_layout)
        title = QLabel("检测到链接")
        title.setObjectName("DialogTitle")
        self.url_single_layout.addWidget(title)

        url_label = QLabel(url[:45] + "..." if len(url) > 45 else url)
        url_label.setObjectName("UrlLabel")
        url_label.setWordWrap(True)
        self.url_single_layout.addWidget(url_label)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        cancel_btn = QPushButton("忽略")
        cancel_btn.setObjectName("DialogButton")
        cancel_btn.clicked.connect(self._close_url_page)
        open_btn = QPushButton("打开链接")
        open_btn.setObjectName("DialogButton")
        open_btn.clicked.connect(lambda: self._open_url_and_close(url))
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(open_btn)
        self.url_single_layout.addLayout(btn_layout)

    def _build_multi_url_page(self, urls: list):
        """构建多个 URL 的选择页面。"""
        self._clear_layout(self.url_multi_layout)
        self._url_checkboxes = {}

        title = QLabel(f"检测到 {len(urls)} 个链接")
        title.setObjectName("DialogTitle")
        self.url_multi_layout.addWidget(title)

        visible_count = min(len(urls), 6)
        item_height = 32
        scroll_height = visible_count * item_height + 10

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded if len(urls) > 6 else Qt.ScrollBarAlwaysOff)
        scroll.setObjectName("UrlScrollArea")
        scroll.setFixedHeight(scroll_height)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(0)

        for i, url in enumerate(urls[:visible_count]):
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(8)
            checkbox = QCheckBox()
            checkbox.setChecked(True)
            checkbox.setFixedWidth(24)
            url_text = url[:35] + "..." if len(url) > 35 else url
            url_label = QLabel(f"{i+1}. {url_text}")
            url_label.setObjectName("UrlLabel")
            url_label.setAlignment(Qt.AlignVCenter)
            row_layout.addWidget(checkbox)
            row_layout.addWidget(url_label)
            scroll_layout.addWidget(row_widget)
            self._url_checkboxes[checkbox] = url

        if len(urls) > visible_count:
            more_label = QLabel(f"...还有 {len(urls) - visible_count} 个")
            more_label.setObjectName("StatusLabel")
            more_label.setMinimumHeight(item_height)
            more_label.setAlignment(Qt.AlignVCenter)
            scroll_layout.addWidget(more_label)

        scroll.setWidget(scroll_content)
        self.url_multi_layout.addWidget(scroll)
        self.url_multi_layout.addSpacing(self.multi_url_btn_top_spacing)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        ignore_btn = QPushButton("忽略")
        ignore_btn.setObjectName("DialogButton")
        ignore_btn.clicked.connect(self._close_url_page)
        open_selected_btn = QPushButton("打开选中")
        open_selected_btn.setObjectName("DialogButton")
        open_selected_btn.clicked.connect(self._open_selected_and_close)
        btn_layout.addWidget(ignore_btn)
        btn_layout.addWidget(open_selected_btn)
        self.url_multi_layout.addLayout(btn_layout)

        target_height = 30 + scroll_height + self.multi_url_btn_top_spacing + 50 + 20
        return target_height

    def _clear_layout(self, layout: QLayout):
        """递归清空 layout。"""
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
                continue
            if item.layout():
                self._clear_layout(item.layout())
                continue

    def _expand_to_url_page(self, target_height: int = 160):
        """展开灵动岛。"""
        if self.is_expanded:
            current_h = self.geometry().height()
            if current_h != target_height:
                self._animate_height_change(current_h, target_height)
            return
        self._do_expand_and_show_url(target_height)

    def _animate_height_change(self, from_h: int, to_h: int):
        """动态调整高度的动画。"""
        current_pos = self.pos()
        current_w = self.geometry().width()
        self.ani = QPropertyAnimation(self, b"geometry")
        self.ani.setDuration(150)
        self.ani.setEasingCurve(QEasingCurve.OutCubic)
        start = QRect(current_pos.x(), current_pos.y(), current_w, from_h)
        end = QRect(current_pos.x(), current_pos.y(), current_w, to_h)
        self.ani.setStartValue(start)
        self.ani.setEndValue(end)
        self.ani.valueChanged.connect(lambda value: (
            self.container.setFixedSize(current_w, value.height()),
            self._set_controls_height(value.height()),
            self._update_rounded_mask()
        ))
        self.ani.finished.connect(lambda: (
            self.container.setFixedSize(current_w, to_h),
            self._set_controls_height(to_h)
        ))
        self.ani.start()

    def _set_controls_height(self, container_h: int):
        """根据容器高度同步设置 controls 高度。"""
        controls_h = max(0, int(container_h) - 32)
        self.controls.setFixedHeight(controls_h)

    def _do_expand_and_show_url(self, target_height: int = 160):
        """执行展开动画并显示链接页面。"""
        current_pos = self.geometry().topLeft()
        current_w = self.rect().width()
        current_h = self.rect().height()
        center_x = current_pos.x() + current_w // 2

        self.time_label.hide()
        self.date_label.show()
        self.update_time_display()

        self.ani = QPropertyAnimation(self, b"geometry")
        self.ani.setDuration(250)
        self.ani.setEasingCurve(QEasingCurve.OutCubic)
        start = QRect(
            center_x, current_pos.y(),
            0, current_h
        )
        end = QRect(
            center_x - 180, current_pos.y(),
            360, target_height
        )
        self.ani.setStartValue(start)
        self.ani.setEndValue(end)
        self.ani.valueChanged.connect(lambda value: (
            self.controls.show() if value.width() > 50 else None,
            self.container.setFixedSize(value.width(), 32 + (target_height - 32) * (value.width() / 360)),
            self._set_controls_height(32 + (target_height - 32) * (value.width() / 360)),
            self._update_rounded_mask()
        ))
        self.ani.finished.connect(lambda: (
            self.controls.show(),
            self.container.setFixedSize(360, target_height),
            self._set_controls_height(target_height)
        ))
        self.ani.start()
        self.is_expanded = True

    def _close_url_page(self):
        """关闭链接页面，收起灵动岛。"""
        self.controls.setCurrentWidget(self.ctrl_page)
        self.controls.setFixedHeight(120)
        if self.is_expanded:
            self.toggle_island()

    def _open_url_and_close(self, url: str):
        """打开 URL 并收起灵动岛。"""
        open_url(url)
        self._close_url_page()

    def _open_selected_and_close(self):
        """打开选中的 URL 并收起灵动岛。"""
        selected_urls = []
        for checkbox, url in self._url_checkboxes.items():
            if checkbox.isChecked():
                selected_urls.append(url)
        if selected_urls:
            open_urls(selected_urls)
        self._close_url_page()

    def _open_all_and_close(self, urls: list):
        """打开所有 URL 并收起灵动岛。"""
        open_urls(urls)
        self._close_url_page()

    def _show_connection_animation(self, message, icon="📶"):
        """显示连接状态变化的动画提示。"""
        self.time_timer.stop()
        
        if not self.is_expanded:
            self._do_expand_and_show_connection(message, icon)
        else:
            self._update_connection_display(message, icon)

        if hasattr(self, '_connection_auto_close_timer') and self._connection_auto_close_timer.isActive():
            self._connection_auto_close_timer.stop()
        self._connection_auto_close_timer = QTimer(self)
        self._connection_auto_close_timer.setSingleShot(True)
        self._connection_auto_close_timer.timeout.connect(self._close_connection_page)
        self._connection_auto_close_timer.start(5000)  # 5秒自动收缩

    def _do_expand_and_show_connection(self, message, icon="📶"):
        """执行展开动画并显示连接状态。"""
        current_pos = self.geometry().topLeft()
        current_w = self.rect().width()
        current_h = self.rect().height()
        center_x = current_pos.x() + current_w // 2

        self.time_label.hide()
        self.date_label.hide()

        self.ani = QPropertyAnimation(self, b"geometry")
        self.ani.setDuration(250)
        self.ani.setEasingCurve(QEasingCurve.OutCubic)
        start = QRect(
            center_x, current_pos.y(),
            0, current_h
        )
        end = QRect(
            center_x - 180, current_pos.y(),
            360, 160
        )
        self.ani.setStartValue(start)
        self.ani.setEndValue(end)
        self.ani.valueChanged.connect(lambda value: (
            self.controls.show() if value.width() > 50 else None,
            self.container.setFixedSize(value.width(), 160),
            self._set_controls_height(160),
            self._update_rounded_mask()
        ))
        self.ani.finished.connect(lambda: (
            self.controls.show(),
            self.container.setFixedSize(360, 160),
            self._set_controls_height(160),
            self._update_connection_display(message, icon)
        ))
        self.ani.start()
        self.is_expanded = True

    def _update_connection_display(self, message, icon="📶"):
        """更新连接状态显示。"""
        self.controls.setCurrentWidget(self.ctrl_page)
        self.time_label.hide()
        self.date_label.setText(f"{icon} {message}")
        self.date_label.show()
        
        temp_label = QLabel(f"{icon} {message}")
        temp_label.setObjectName("DateLabel")
        temp_label.setStyleSheet(self.date_label.styleSheet())
        temp_label.setFont(self.date_label.font())
        temp_label.adjustSize()
        width = temp_label.width()
        x = (360 - width) // 2
        self.date_label.setFixedWidth(width)
        self.date_label.move(x, 0)

    def _close_connection_page(self):
        """关闭连接状态页面，收起灵动岛。"""
        if self.is_expanded:
            self.toggle_island()
        self.time_timer.start(1000)
        self.update_time()

    def load_qss(self):
        """加载QSS样式表。"""
        with open("resources/styles/style.qss", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def _update_rounded_mask(self):
        """动态更新窗口的圆角遮罩，保持完美胶囊形态。"""
        rect = self.rect()
        radius = min(rect.width(), rect.height()) // 2
        path = QPainterPath()
        path.addRoundedRect(rect, radius, radius)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
