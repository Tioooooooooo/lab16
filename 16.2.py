import customtkinter as ctk
from datetime import datetime

# общая тема приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class MoodTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # настройка окна
        self.title("Mood Tracker")
        self.geometry("450x550")
        self.resizable(False, False)

        # главный заголовок
        self.title_label = ctk.CTkLabel(
            self,
            text="Как твои дела сегодня?",
            font=ctk.CTkFont(family="Helvetica", size=24, weight="bold")
        )
        self.title_label.pack(pady=(30, 20))

        # контейнер для кнопок настроения
        self.mood_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.mood_frame.pack(pady=10)

        # переменная для хранения выбранного настроения
        self.selected_mood = ctk.StringVar(value="😊 Отлично")

        # Кнопки выбора настроения (Сегментированный контроллер)
        self.mood_segmented = ctk.CTkSegmentedButton(
            self.mood_frame,
            values=["😊 Отлично", "😐 Нормально", "😴 Устал(а)", "😢 Грустно"],
            variable=self.selected_mood,
            font=ctk.CTkFont(size=14)
        )
        self.mood_segmented.pack(ipadx=10, ipady=5)

        # поле для ввода заметки
        self.note_label = ctk.CTkLabel(self, text="Добавь мысль или заметку:", font=ctk.CTkFont(size=14))
        self.note_label.pack(pady=(20, 5), anchor="w", padx=40)

        self.note_entry = ctk.CTkEntry(
            self,
            width=370,
            placeholder_text="Что на тебя повлияло?...",
            font=ctk.CTkFont(size=13)
        )
        self.note_entry.pack(pady=5)

        # кнопка сохранения
        self.save_button = ctk.CTkButton(
            self,
            text="Сохранить момент",
            command=self.save_entry,
            font=ctk.CTkFont(size=14, weight="bold"),
            hover_color="#1a62d6"
        )
        self.save_button.pack(pady=25)

        # область для вывода последней записи
        self.log_card = ctk.CTkFrame(self, width=370, height=120, corner_radius=15)
        self.log_card.pack(pady=10)
        self.log_card.pack_propagate(False) # запрет менять размер под контент

        self.log_title = ctk.CTkLabel(
            self.log_card,
            text="Последняя запись будет здесь...",
            font=ctk.CTkFont(size=13, slant="italic"),
            text_color="gray"
        )
        self.log_title.pack(expand=True)

    def save_entry(self):
        # получаем данные из интерфейса
        current_time = datetime.now().strftime("%H:%M")
        mood = self.selected_mood.get()
        note = self.note_entry.get() if self.note_entry.get() else "Без заметок"

        # очищение от старых записей
        for widget in self.log_card.winfo_children():
            widget.destroy()

        # создание отображения внутри карточки
        time_label = ctk.CTkLabel(self.log_card, text=f"Запись в {current_time}", font=ctk.CTkFont(size=11), text_color="#1f85de")
        time_label.pack(anchor="w", padx=15, pady=(10, 0))

        mood_label = ctk.CTkLabel(self.log_card, text=mood, font=ctk.CTkFont(size=18, weight="bold"))
        mood_label.pack(anchor="w", padx=15, pady=2)

        note_label = ctk.CTkLabel(self.log_card, text=note, font=ctk.CTkFont(size=13), wraplength=340, justify="left")
        note_label.pack(anchor="w", padx=15, pady=(0, 10))

        # очищение поля ввода
        self.note_entry.delete(0, 'end')

if __name__ == "__main__":
    app = MoodTrackerApp()
    app.mainloop()