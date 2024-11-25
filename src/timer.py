import tkinter as tk
import threading
import time
from config import *


class Timer:
    timer_thread = None
    start_time = None
    is_running = False
    time_display = None
    root = None

    @classmethod
    def start(cls, tim_x, tim_y):
        """타이머를 시작하는 메서드."""
        if cls.is_running:
            return  # 이미 실행 중인 경우 무시

        cls.start_time = time.time()
        cls.is_running = True

        # 별도의 스레드에서 tkinter 창 실행
        cls.timer_thread = threading.Thread(
            target=cls._run_timer, args=(tim_x, tim_y),
            daemon=True
        )
        cls.timer_thread.start()

    @classmethod
    def stop(cls):
        """타이머를 종료하는 메서드."""
        cls.is_running = False
        if cls.root:
            cls.root.destroy()
            cls.root = None

    @classmethod
    def _run_timer(cls, tim_x, tim_y):
        """타이머 창과 업데이트 메서드."""
        cls.root = tk.Tk()
        cls.root.title("Timer")
        cls.root.geometry(f"200x100+{tim_x}+{tim_y-30}")

        cls.time_display = tk.Label(cls.root, text="0:00", font=("Helvetica", 18))
        cls.time_display.pack(expand=True)

        cls._update_timer()
        cls.root.mainloop()

    @classmethod
    def _update_timer(cls):
        """타이머 텍스트를 업데이트."""
        if not cls.is_running:
            return

        elapsed_time = int(time.time() - cls.start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        cls.time_display.config(text=f"{minutes}:{seconds:02}")
        cls.root.after(1000, cls._update_timer)
