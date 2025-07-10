iwctl
device list
station wlan0 scan	
station wlan0 get-networks

station wlan0 connect "Your_SSID_Name"
quit


lsblk
lsblk -f

# connect to wifi
nmcli dev wifi list
nmcli dev wifi connect "Your_SSID_Name" password "Your_Password"
nmcli connection show

# set charing mode with custom interval
sudo pacman -S libsmbios
sudo smbios-battery-ctl 
sudo smbios-battery-ctl --get-charging-cfg
sudo smbios-battery-ctl --set-custom-charge-interval 50 80
sudo smbios-battery-ctl --set-charging-mode=custom
