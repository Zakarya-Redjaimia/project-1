import threading
from pywebio import start_server
from app import main_menu
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

def run_server():
    start_server(main_menu, port=8080, auto_open_webbrowser=False)

class ZakiShopApp(App):
    def build(self):
        # Start PyWebIO local server in background
        threading.Thread(target=run_server, daemon=True).start()
        
        # UI Container
        layout = BoxLayout(orientation='vertical')
        
        try:
            # Native Kivy WebView widget (Does NOT require PyJnius)
            from kivy.uix import WebView
            wb = WebView(url="http://127.0.0.1:8080")
            layout.add_widget(wb)
        except Exception:
            from kivy.uix.label import Label
            layout.add_widget(Label(text="Server running on http://127.0.0.1:8080"))
            
        return layout

if __name__ == '__main__':
    ZakiShopApp().run()