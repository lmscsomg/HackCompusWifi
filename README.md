#HackNUAACompusWifi
This is a small program to brute-force the wifi in campus which is originally for the teachers to use.

##Tools
Wireshark  
Requests library in Python  
Multiprocessing  library in Python

##Environment
OS : OS X Yosemite(version 10.10)  
Browser: Chrome

##Speed
Since I only knew that the password is initially the last six digits in the teacher's ID, I can only brute-force it at the present,so I hardly expect its high speed.

###Improvement
After support multi-threading,the speed improved a lot.  

To the same username:  
Without multi-threading: **259.13s**  
With multi-threading: **43.24s**


##What to do next ?
GUI for the program