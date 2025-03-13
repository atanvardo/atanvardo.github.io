# Windows Subsystem for Linux (WSL)

*If you have Linux installed in your computer, ignore this section*

The processing of the samples is preferably carried out in a Linux environment. A good solution for Windows users is to use the Windows Subsystem for Linux (WSL), which allows you to install and run a Linux distribution within Windows.

An easy way to get it is to access the Microsoft Store available in all the modern versions of Windows, and install the app Ubuntu, which installs this Linux distribution in your system.

When you load this app, it will start a Linux shell in your Linux home directory. WSL stores the Linux file system in this very hidden folder: `C:\Users\[your_user_name]\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs`

You should automatically have a bookmark to this folder available in the navigation pane of the Windows file explorer.

## Moving files between the WSL and Windows

This is VERY IMPORTANT. If you use Windows to copy a file from your Windows system to a folder in your Linux system, that file won’t have the required permissions to be used in Linux.

To move files from Windows to Linux, use the Linux command line. You copy (command `cp`) the file (to access the Windows file system from Linux, you have to go to the folder `/mnt/c`, which is equivalent to the `C:` drive) to the destination. For example, to copy the file `file.txt` that is in the Desktop of my Windows system to the folder `project` in my Linux home directory, I have to write in the Linux shell:

```
cp /mnt/c/Users/[windows_user_name]/Desktop/file.txt ~/project/
```

To copy from Linux to Windows, do it the opposite way:

```
cp file.txt /mnt/c/Users/[windows_user_name]/Desktop/
```

WARNING: Try to avoid deleting or moving files from the Linux system using the Windows file explorer! The Linux system will still believe that the files are there, and this can cause problems.
