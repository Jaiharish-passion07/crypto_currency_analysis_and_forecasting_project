
# Cryptocurrency Analysis and Forecasting Project

I'm certain that everyone is aware of it. Nevertheless, I'll give a brief introduction to it.
We learn about things like Bitcoin, Ethereum, Dogecoin, Shiba Inu, and 
Solana every day. Cryptocurrency is a brand-new generation of digital money that
offers decentralized finance free from the control of the banking system. It has 
a consensus algorithm and uses blockchain technology as its backing. The market for cryptocurrencies worldwide is $1.07 trillion.


## Goal of the Project

1. Forecasting the bitcoin price in future
2. Why is bitcoin the king of cryptocurrency?
3. Analysis of bear and bull market in each month for every year from 2013 to 2022
4. Which country's market impacts the crypto currency market?

 And still further more analysis will be updated on upcoming days...
## Appendix

This project's study and price prediction mostly focused on the price of bitcoin. Because of its Marketcap, Bitcoin is regarded as the king of the cryptocurrency market.
For additional investigation, we use altcoins such as

- Ethereum
- BNB
- XRP
- Cardano
- Solana


## Architecture Diagram

#### AWS Cloud Architecture Diagram with DataExtract Server and RDS Instance

![Cloud ARchit]()

#### General Architecture Diagram of Model Building and Data Analysis
![data]()

## Roadmap

* [x] Alpha Stage
    * Web Scraping using Selenium
    * Data Extraction and Storing into Database
    * Building and Deploying a Data Extraction Server in AWS Cloud
    * Launch an Bastion Host and RDS DB in AWS Network
    * Launch an AWS Instance Scheduler to Schedule the Instance and RDS for every 24 hours

* [ ] Beta Stage
    * Perform Data Analysis

* [ ] Gamma Stage
    * Building an Forecasting Model




## Tech Skills

**Programming Languages:**

* Python

* SQL

**WebScraping:** 

* Selenium

**AWS Cloud:** 

* Elastic Compute Cloud
* Relational Database Service Instance
* Virtual Private Cloud
* Basic Networking and Security skills

**Other Skills:** 

* Linux Cmds


## Installation

Dependecies Library and other packages required to run this porject 

**Note**:This project is developed in Linux Distros(Ubuntu)

*I hope everyone knows how to launch an EC2 Instance in AWS and having the private key file for your Instance*

### Changing permission of key file into Only readable form

```bash
chmod 400 key_file

ls -l
```
*Output: -r-------- 1 jairam07 jairam07     1674 Aug  3 20:56 demo_key.pem* 

### Connecting to My Server through SSH

```bash
ssh -i key_file ec2_user@public_ip_address
```
*Eg: ssh -i demo_key.pem ubuntu@13.233.xxx.xxx*

### Once connection established Install the necessary packages
```bash
sudo apt update && sudo apt upgrade
```

### Installing google chrome and Webdriver for respective version
```bash
sudo apt install wget

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

ls -l
```
*Output: -rw-rw-r-- 1 ubuntu ubuntu 89563160 Jul 30 12:56 google-chrome-stable_current_amd64.deb*

```bash
google-chrome --version
```
**Tips:** [If you face any error while installing google chrome refer this link here](https://askubuntu.com/questions/220960/cannot-install-google-chrome-how-do-i-fix-it)

### Create one directiory to store webdriver file
```bash
mkdir chrome_driver_selenium
cd chrome_driver_selenium/
```
[**Download Webdriver for Chrome Browser**](https://chromedriver.chromium.org/downloads)


```bash
wget https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip
```
### Unzip that webdriver file
```bash
sudo apt install unzip
unzip chromedriver_linux64.zip
ls -l
```
*Output: -rwxr-xr-x 1 ubuntu ubuntu 13978368 Jul 30 12:47 chromedriver*

### Python Installation and Virtual Environment creation

```bash
sudo apt install -y python3-pip
```
```bash
sudo apt install -y build-essential libssl-dev libpq-dev libffi-dev python3-dev
```
```bash
sudo apt install -y python3-venv
```
**Creating Virtual Environement**
```bash
mkdir environments
```
```bash
cd environments
```
```bash
python3 -m venv my_env
```
```bash
source my_env/bin/activate
```
*Output: (my_env) ubuntu@ip-172-31-32-24:~/environments$*

**Installing packages**
```bash
pip install -r requirements.txt
```


    
## Acknowledgements

 - [Selenium Documentation](https://selenium-python.readthedocs.io/)
 - [Selenium Tutorial Video](https://youtu.be/o3tYiyE_OXE)
 - [Create DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)
 - [AWS Custom VPC Creation Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html#CHAP_Tutorials.WebServerDB.CreateVPC.VPCAndSubnets)

**Will be Update soon with other Necessary Information**