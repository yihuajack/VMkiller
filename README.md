# VMkiller
Brief Description: Transmitting Codes from your PC to a VM with Firewall on.
## Background
The institute introduced the usage of Virtual Machine and required all students to code on the VM. The VM is terribly sluggish and coding on it is really a terrible experience. Everyone prefers to code on their own PC. This project gives a potential solution to the problem.
## Identification of the Problem
The professor claims that all internet access to the VM will be blocked, and thus it will be impossible to send codes from PC to VM. The thing is: Codes must be uploaded from the VM to Online Judge in order to get scores.
## Main Idea of the Project
Though all internet connections are blocked, the institute cannot block your access to it: at least the authority to type will be granted. This project reads code from your PC, switch to the interface of the VM automatically, and then output the code letter-by-letter into the VM.
## Users' Guide
- Check your Python Environment whether you have installed "pynput" package. If no, open cmd and run command ```pip3 install pynput```;
- Use your favorite Python IDLE to open VMkiller.py;
- Copy your source code to the same directory of VMkiller.py and change the file name in VMkiller.py to the name of your source file;
- Open your Virtual Machine via Microsoft Desktop, and log in your VM account;
- Open shell in your VM; open an empty txt file (Note: can't be cpp or other kinds of file) with vim. Switch to insert mode by pressing i on the keyboard;
- Minimize your VM Desktop window (IMPORTANT!) and run the Python code (This may fail; retry this step until it works);
- Then your computer automatically shifts to the window of the Virtual Machine and start outputting your source code;
- After the whole process completed, press Esc to switch to the vim normal mode, and input ```:wq``` to save and quit. Done.
