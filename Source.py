import customtkinter
from rich import print
import psutil
import pynvml
#important

print("[bold red]App Launched![/bold red]")
app = customtkinter.CTk()
app.title("Alpha's Resource Monitor")
app.geometry("600x400")
app.resizable(False,False)
customtkinter.set_appearance_mode("system")

#gpu stuff

pynvml.nvmlInit()
device_handle = pynvml.nvmlDeviceGetHandleByIndex(0)
memory = pynvml.nvmlDeviceGetMemoryInfo(device_handle)
utilisation = pynvml.nvmlDeviceGetUtilizationRates(device_handle)
gpu = utilisation.gpu

#defs

def cpu_usage():
    cputxtLbl.configure(text=f"CPU: {psutil.cpu_percent()}%",font=customtkinter.CTkFont(family="Comic Sans MS", size=28))
    app.after(1000, cpu_usage)
def cpuCoreAmount():
    coreTxtLbl.configure(text=f"Cores: {psutil.cpu_count()}")
    app.after(1000, cpuCoreAmount)
def ram_usageAmount():
    ramTxtLbl.configure(text=f"RAM: {psutil.virtual_memory().percent}%")
    app.after(1000, ram_usageAmount)
def gpu_usage():
    device_handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    utilization = pynvml.nvmlDeviceGetUtilizationRates(device_handle)
    gpuTxtLbl.configure(text=f"GPU: {utilization.gpu}%")
    app.after(1000, gpu_usage)
def vram_total():
    utility = pynvml.nvmlDeviceGetHandleByIndex(0)
    utility = pynvml.nvmlDeviceGetMemoryInfo(utility)
    VramTxtLbl.configure(text=f"VRAM: {utility.total / 1024**3:.2f} GB")
    app.after(1000, vram_total)
def vram_usage():
    utility = pynvml.nvmlDeviceGetHandleByIndex(0)
    utility = pynvml.nvmlDeviceGetMemoryInfo(utility)
    VramUsageTxtLbl.configure(text=f"VRAM Usage: {utility.used / 1024**2:.2f} MB")
    app.after(1000, vram_usage)
#label

txtLbl = customtkinter.CTkLabel(
                  app, 
                  text="Alpha's Monitor by Berniea5", text_color="#7A4AD8",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=28),
                  )
cputxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"CPU: {psutil.cpu_percent()}%", text_color="#4393EF",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=28)
                  )
coreTxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"Cores: {psutil.cpu_count()}", text_color="#4393EF",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=28)
                  )
ramTxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"RAM USAGE: {psutil.virtual_memory().percent}%", text_color="#018C4B",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=28)
                  )
gpuTxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"GPU: {gpu}%", text_color="#07F43E",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=28)
                  )
VramTxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"VRAM: {memory.total / 1024**3:.2f} GB", text_color="#07F43E",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=24)
                  )
VramUsageTxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"VRAM: {memory.used / 1024**3:.2f} GB", text_color="#07F43E",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=24)
                  )
#end

app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(3, weight=1)
txtLbl.grid(row=0, column=0, columnspan=2)
cputxtLbl.grid(row=1, column=0, sticky="w")
coreTxtLbl.grid(row=1, column=1, sticky="w")
ramTxtLbl.grid(row=2, column=0, sticky="w")
gpuTxtLbl.grid(row=3, column=0, sticky="w")
VramTxtLbl.grid(row=3, column=1, sticky="w")
VramUsageTxtLbl.grid(row=4, column=1, sticky="w", columnspan=1)
cpu_usage()
cpuCoreAmount()
ram_usageAmount()
gpu_usage()
vram_total()
vram_usage()
app.mainloop()

'''
jul 26 
GPU SHOWING IN % | CORE AMOUNTS | RAM USAGE
'''
