import tkinter as tk
import json
import os

root = tk.Tk()
root.title("MENDABLOX")
root.geometry("340x520")
root.config(bg="#0a0a0a")

fps_on = False
grey_on = False
potato_on = False

# TITOLO
tk.Label(root, text="MENDABLOX", fg="#00ff88", bg="#0a0a0a", font=("Arial", 24, "bold")).pack(pady=15)

def toggle_fps():
    global fps_on
    fps_on = not fps_on
    btn_fps.config(text=f"1000 FPS: {'ON' if fps_on else 'OFF'}")

def toggle_grey():
    global grey_on
    grey_on = not grey_on
    btn_grey.config(text=f"GREY SKY: {'ON' if grey_on else 'OFF'}")

def toggle_potato():
    global potato_on
    potato_on = not potato_on
    btn_potato.config(text=f"POTATO GRAPHICS: {'ON' if potato_on else 'OFF'}")

# STILE BOTTONI
btn_style = {"bg":"#1a1a1a", "fg":"white", "width":26, "font":("Arial", 11)}

btn_fps = tk.Button(root, text="1000 FPS: OFF", command=toggle_fps, **btn_style)
btn_fps.pack(pady=8)

btn_grey = tk.Button(root, text="GREY SKY: OFF", command=toggle_grey, **btn_style)
btn_grey.pack(pady=8)

btn_potato = tk.Button(root, text="POTATO GRAPHICS: OFF", command=toggle_potato, **btn_style)
btn_potato.pack(pady=8)

def save():
    data = {}
    if fps_on: data["FIntTaskSchedulerTargetFps"] = "1000"
    if grey_on: data["DFFlagDisablePostFx"] = "True"
    if potato_on:
        data["FIntRenderShadowIntensity"] = "0"
        data["FFlagHandleAltEnterFullscreenManually"] = "False"
    
    path = "/storage/emulated/0/Download/ClientAppSettings.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    status.config(text="SALVATO IN DOWNLOAD!", fg="#00ff88")

def launch():
    status.config(text="AVVIO ROBLOX...", fg="yellow")
    # Apre Roblox
    os.system("am start -n com.roblox.client/com.roblox.client.AppActivity")

status = tk.Label(root, text="", bg="#0a0a0a", fg="white", font=("Arial", 10))
status.pack(pady=10)

tk.Button(root, text="SAVE", command=save, bg="#00ff88", fg="black", width=18, font=("Arial", 12, "bold")).pack(pady=8)
tk.Button(root, text="LAUNCH ROBLOX", command=launch, bg="#ff0088", fg="white", width=18, font=("Arial", 12, "bold")).pack(pady=8)

root.mainloop()