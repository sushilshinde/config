## Automate software installations and updatation using bash script

**Method 1: Run bash file from repository**

First time installations 

`
$ yes | curl -sL https://raw.githubusercontent.com/sushilshinde/config/master/linux/ubuntu/install-packages  | sudo -E bash - 
`

Update packages

`
$ yes | curl -sL https://raw.githubusercontent.com/sushilshinde/config/master/linux/ubuntu/update-packages  | sudo -E bash -
`


**Method 2: Installing "update-packages" as system command**

Step 1 : Download update-packages

Step 2 : Change file permission to executable and make it a command

`
$chmod +x update-packages && sudo cp update-packages /usr/bin
`

Step 3 : Run command with "yes" pipe

`
$ yes | update-packages
`

