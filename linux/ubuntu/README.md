#Automate software installations on Ubuntu/Mint with remote bash script 

Method 1: Installing "install-softwares" as system command

Step 1 : Download install-softwares

Step 2 : Change file permission to executable and make it a command

      $chmod +x install-softwares && sudo cp install-softwares /usr/bin
Step 3 : Run command with "yes" pipe

      $ yes | install-softwares
      
Method 2: Run bash file from repository

      $ yes | https://raw.githubusercontent.com/sushilshinde/config/master/linux/ubuntu/install-softwares  | sudo -E bash - 
