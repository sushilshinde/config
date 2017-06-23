#General Desktop Configuration Documentation 


#Using updateme bash script for Ubuntu/Mint updates

Method 1: Installing updateme as system command

Step 1 :  Download updateme

Step 2 :  Change file permission to executable and make it a command
          
          $chmod +x updateme && sudo cp updateme /usr/bin

Step 3 :  Run command with "yes" pipe 
          
          $ yes | updateme


Method 2: Run bash file from repository 

          $ yes | sudo curl -sL https://raw.githubusercontent.com/sushilshinde/config/master/updateme | sudo -E bash -
