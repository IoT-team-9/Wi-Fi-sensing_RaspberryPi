# Wi-Fi sensing with Raspberry Pi 4
#### This is a Term project of IoT (Internet of Things)    
# Recognition Human Activities

1. Empty
2. Stand
3. Sit
4. Walk
5. Fall

## Progress setting invironment
### Installing Raspberry pi Image and connecting
### Install Nexmon csi
[Nexmon GitHub Respository](https://github.com/seemoo-lab/nexmon_csi)   
![nexmonInstall](https://github.com/IoT-team-9/Wi-Fi-sensing_RaspberryPi/blob/main/Image/nexmon.png)

## Collect CSI for test first time

#### Environment setting
* Raspberry Pi
* iptiem router 2.4GHx
* laptop   
* Location : Inside a typical home 
* 2 experiments
#### test1
![test1](https://github.com/IoT-team-9/Wi-Fi-sensing_RaspberryPi/blob/main/Image/iot_csi_plot_1.jpg)
#### test2
![test2](https://github.com/IoT-team-9/Wi-Fi-sensing_RaspberryPi/blob/main/Image/iot_csi_plot_2.jpg)

## Collect CSI data in AI Incubator
1. Empty
2. Stand
3. Sit
4. Walk
5. Fall

#### Measured for 5 minutes for each movement
![Walking](https://github.com/IoT-team-9/Wi-Fi-sensing_RaspberryPi/blob/main/Image/walking.gif)

#### Convert to csv file
![CSV](https://github.com/IoT-team-9/Wi-Fi-sensing_RaspberryPi/blob/main/Image/csv%20%EC%B6%94%EC%B6%9C%20%EC%A4%91.jpg)

## Modelling progress
#### git clone
[Wi-Fi sensing GitHub](https://github.com/cheeseBG/wifi-sensing)      
### Supervised learning
<pre>
<code>
python main.py --learning SVL --mode train
python main.py --learning SVl --mode test
</code>
</pre>
![Model test](https://github.com/IoT-team-9/Wi-Fi-sensing_RaspberryPi/blob/main/Image/%EB%AA%A8%EB%8D%B8%EB%A7%81%20%EB%B6%84%EB%A5%98%EA%B2%B0%EA%B3%BC.png)