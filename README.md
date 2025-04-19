---

## 🚀 Features

- ✅ Modern Material Design UI
- ✅ Separate `login.kv` and `sign.kv` interface files
- ✅ Screen transitions (left/right)
- ✅ Toast notifications ready (can be added easily)

---

## 📁 Project Structure

```
├── main.py
├── login.kv
├── sign.kv
└── README.md
```

---

## 🧠 Code Overview

### `main.py`
```python
# Importation des modules
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager

# Set window size (for desktop preview)
Window.size = (398, 804)

# Define main class
class tex(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("sign.kv"))
        return screen_manager

    def back(self):
        screen_manager.transition.direction = "right"
        screen_manager.current = "login_page"

    def sign_in(self):
        screen_manager.transition.direction = "left"
        screen_manager.current = "sign page"

# Run the app
if __name__ == "__main__":
    tex().run()
```

---

## 🛠️ Requirements

- Python 3.x
- Kivy
- KivyMD

Install with:
```bash
pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple
pip install kivymd==1.1.1
```


---

## 📷 Screenshots 
![Cat](https://scontent.flfw5-1.fna.fbcdn.net/v/t39.30808-6/490239142_2114965052344376_6512054200273650440_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=aa7b47&_nc_ohc=2557VNM7MZkQ7kNvwHyLafY&_nc_oc=AdkjI-Rdy5Fb5Dlfdjq8HacJ57kEEmRBd6lABmzHaDXn46xSkCndsw3c_Blwq9T9rro&_nc_zt=23&_nc_ht=scontent.flfw5-1.fna&_nc_gid=T1nkHFEUjzxWyDvXIwhppg&oh=00_AfEx3FpokYbVRj1EUfcyf_oaf6kI7bwuCL40ABF7kULJJA&oe=680050CE)
---

## 📬 Contact

Feel free to reach out if you have questions or want to contribute!
---
[Telegram](https://t.me/Thekingdynamo)
[WhatsApp](https://wa.me/+22897606374)
[Facebook](https://www.facebook.com/alexdynamo.dynamo/)
[Instagram](https://www.instagram.com/thekingdynamo/)
[Beacons](https://beacons.page/thekingdynamo)

---

```
