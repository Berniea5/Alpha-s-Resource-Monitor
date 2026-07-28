import customtkinter
from rich import print
import psutil
import pynvml

#important

update_Rate = 1000 # ms-->second

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

network = psutil.net_io_counters()

disk = psutil.disk_usage('/')

gpu = utilisation.gpu

#defs

def slider(value):
    global update_Rate
    update_Rate = int(value)
    sliderText.configure(text=f"{update_Rate} ms", text_color="#FFFFFF",
    font=customtkinter.CTkFont(family="Comic Sans MS",size=24))
def cpu_usage():
    cputxtLbl.configure(text=f"CPU: {psutil.cpu_percent()}%",font=customtkinter.CTkFont(family="Comic Sans MS", size=28))
    app.after(update_Rate, cpu_usage)
def cpuCoreAmount():
    coreTxtLbl.configure(text=f"Cores: {psutil.cpu_count()}")
    app.after(update_Rate, cpuCoreAmount)
def ram_usageAmount():
    ramTxtLbl.configure(text=f"RAM: {psutil.virtual_memory().percent}%")
    app.after(update_Rate, ram_usageAmount)
def gpu_usage():
    device_handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    utilization = pynvml.nvmlDeviceGetUtilizationRates(device_handle)
    gpuTxtLbl.configure(text=f"GPU: {utilization.gpu}%")
    app.after(update_Rate, gpu_usage)
def vram_total():
    utility = pynvml.nvmlDeviceGetHandleByIndex(0)
    utility = pynvml.nvmlDeviceGetMemoryInfo(utility)
    VramTxtLbl.configure(text=f"VRAM: {utility.total / 1024**3:.2f} GB")
    app.after(update_Rate, vram_total)
def vram_usage():
    utility = pynvml.nvmlDeviceGetHandleByIndex(0)
    utility = pynvml.nvmlDeviceGetMemoryInfo(utility)
    VramUsageTxtLbl.configure(text=f"VRAM Usage: {utility.used / 1024**2:.2f} MB")
    app.after(update_Rate, vram_usage)
def net_usage():
    network = psutil.net_io_counters()
    NetworkUsageTxtLbl.configure(text=f"Net: {network.bytes_sent / 1024**2:.2f} MB")
    print(network)
    app.after(update_Rate, net_usage)
def disk_usage():
    disk = psutil.disk_usage('/')
    DiskUsageTxtLbl.configure(text=f"Disk: {disk.percent}%", text_color="#C07203",
                               font=customtkinter.CTkFont(family="Comic Sans MS", size=24))
    print(disk)
    app.after(update_Rate, disk_usage)

#labels

txtLbl = customtkinter.CTkLabel(
                  app, 
                  text="Alpha's Monitor by Berniea5", text_color="#3E01B8",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=28),
                  justify="center"
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
NetworkUsageTxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"Net: {network.bytes_sent / 1024**2:.2f} MB", text_color="#FFFFFF",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=24),
                  )
DiskUsageTxtLbl = customtkinter.CTkLabel(
                  app, 
                  text=f"Disk: {disk.percent}%", text_color="#0DFF00",
                  font=customtkinter.CTkFont(family="Comic Sans MS",size=24)
                  )
#textbox

TextBoxNotes = customtkinter.CTkTextbox(app,width=600,height=180,font=customtkinter.CTkFont(family="Comic Sans MS",size=18),corner_radius=20)
TextBoxNotes.insert("0.0", "Notes: ",)

#sliders

sliderMain = customtkinter.CTkSlider(app, from_=100, to=2000, command=slider,progress_color="#7A4AD8", button_color="#7A4AD8")
sliderText = customtkinter.CTkLabel(app,text=f"{update_Rate} ms", text_color="#FFFFFF",
                                    font=customtkinter.CTkFont(family="Comic Sans MS",size=24))

#end

app.grid_columnconfigure(1, weight=5)
app.grid_columnconfigure(3, weight=1)
app.grid_rowconfigure(6, weight=2)
txtLbl.grid(row=0, column=0, columnspan=2)
cputxtLbl.grid(row=1, column=0, sticky="w")
coreTxtLbl.grid(row=1, column=1, sticky="w")
ramTxtLbl.grid(row=3, column=0, sticky="w")
gpuTxtLbl.grid(row=2, column=0, sticky="w")
VramTxtLbl.grid(row=2, column=1, sticky="w")
VramUsageTxtLbl.grid(row=3, column=1, sticky="w", columnspan=1)
sliderMain.grid(row=10, column=0, sticky="w", columnspan=1)
sliderText.grid(row=10, column=1, sticky="w", columnspan=1)
NetworkUsageTxtLbl.grid(row=10, column=0, sticky="e", columnspan=2)
DiskUsageTxtLbl.grid(row=5, column=0, sticky="w", columnspan=1)
TextBoxNotes.grid(row=9, column=0, columnspan=2)


cpu_usage()
cpuCoreAmount()
ram_usageAmount()
gpu_usage()
vram_total()
vram_usage()
disk_usage()
net_usage()
app.mainloop()
