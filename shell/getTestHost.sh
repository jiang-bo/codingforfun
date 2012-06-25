#!/bin/sh
#获取共用测试环境绑定
#Author:jiangbo
#Date: Mon Jun 25 20:57:48 CST 2012

sudo echo "####mark####" >> /etc/hosts
sudo curl -s http://10.20.141.4/hosts >> /etc/hosts
sudo echo "####end####" >> /etc/hosts
