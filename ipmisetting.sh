#!/bin/bash 

#IPMI
#cd /mnt/ipmicfg/Smaru/Linux64/
moriacd /mnt/mori/IPMICFG_1.33.1_build.211123/IPMICFG_1.33.1_build.211123/Linux/64bit


#read -p "input IPMI password:"  password
#firefo x -new-instance -private-window $password
./IPMICFG-Linux.x86_64 -m 

#ファクトリーデフォルト

read -p "factory default?(y or n):"  fd
case "$fd" in
  [yY]*) ./IPMICFG-Linux.x86_64 -fd 
echo "wait for IPMI reboot 1min"
sleep 60;;
  *) echo "abort";;
esac





echo "############################"
#echo "#ファンモード#"
echo "############################"
sleep 1

#ファンモードの表示
./IPMICFG-Linux.x86_64 -fan 

#ファンモードを選択し入力
read -p "input fan mode then enter:"  str

#IPMIへ入力したファンモード値の設定
./IPMICFG-Linux.x86_64 -fan $str
sleep 1

#設定後のファンモードの表示
./IPMICFG-Linux.x86_64 -fan |grep -i current
sleep 1

#現在のファン回転数の表示
./IPMICFG-Linux.x86_64 -sdr |grep -i fan 
read -p "check fan rpm then enter:"
sleep 1

echo "############################"
#echo "#画面、センサ、ログ#"
echo "############################"
sleep 1



#現在のセンサー値全て表示
./IPMICFG-Linux.x86_64 -sdr 
read -p "check sensor reading then enter:"

#システムイベントログの表示
./IPMICFG-Linux.x86_64 -sel list
read -p "check System Event Log and CLEAR LOG NOW. OK?:"

#システムイベントログの削除
./IPMICFG-Linux.x86_64 -sel del

sleep 1
echo "############################"
#echo "#UID LED#"
echo "############################"
sleep 1

#UID LED 点灯
./IPMICFG-Linux.x86_64 -raw 0x30 0x0d
read -p "turn ON UID LED.check LED then Enter:"

#UID LED 消灯
./IPMICFG-Linux.x86_64 -raw 0x30 0x0e
echo "turn OFF LED."

sleep 1
echo "############################"
#echo "#swc削除#"
echo "############################"
sleep 1

read -p "IPMIUSER _SWC delete OK?:"
./IPMICFG-Linux.x86_64 -user del 8
echo "swc delete:"

sleep 1
echo "############################"
#echo "#Network Dedicated/Disabled#"
echo "############################"
#https://www.supermicro.com/support/faqs/faq.cfm?faq=21386
sleep 1

#現在のLANモードを取得
let beforeLANmode=$(./IPMICFG-Linux.x86_64 -raw 0x30 0x70 0x0c 0)

#現在のLANモードを表示
case $beforeLANmode in
    0) 
    echo "already LANmode is [00 dedicated] .";;

    1) 
    echo "Interface mode is 01 shared"
    read -p	"change interface mode to [00 DEDICATED]. OK?:";;
    
    2) 
    echo "Interface mode is 02 failover"
    read -p	"change interface mode to [00 DEDICATED]. OK?:";;
    
    *) echo "Please check LAN mode with IPMI web interface. "
    echo $beforeLANmode
esac

#LANモードをDedicated(専用)に変更
./IPMICFG-Linux.x86_64 -raw 0x30 0x70 0x0c 1 0

#変更後のLANモードの値を表示
let afterLANmode=$(./IPMICFG-Linux.x86_64 -raw 0x30 0x70 0x0c 0)

case $afterLANmode in
0) 
echo "Setting Interface mode to [00 dedicated] done.";;
*) 
zenity --question --text="dedicate"
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "!!Please check LAN mode with IPMI web interface. !!" $afterLANmode
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";;
esac

sleep 1
echo "############################"
#echo "#設定終了#"
echo "############################"
sleep 1

##すべての項目を設定したのでWebで確認
echo "Please check IPMI Setting on IPMI WEB Interface."

##HOST INTERFACEをdisableに
#disable設定
./IPMICFG-Linux.x86_64 -raw 30 B5 01 00
#disableになったかステータス確認
echo "00=disble 01=enable"
./IPMICFG-Linux.x86_64 -raw 30 B5 00

#intrusion clear
./IPMICFG-Linux.x86_64 -clrint
