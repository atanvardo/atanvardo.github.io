# Tricks and cheats

This is a list of tricks and cheats that will make your life easier, specially if you use Windows.

## Notepad++

Use a plain text editor for opening and checking your data matrices. Text editing programs (Word, WordPad, etc) can add formatting information to the files, which will cause errors when loading these files in phylogenetic programs.

The Notepad program in Windows is an option, but it is extremly basic, ugly and annoying. Fortunately, there are many alternatives.

My favourite is [Notepad++](https://notepad-plus-plus.org/). It has some good advantages:

- It is quite simple.
- It adds an option to the contextual menu when you right-click a file in Windows, to open directly that file in Notepad++.
- It includes a tool to change the end-of-line (EOL) characters. This is usefull specially if you use Windows, because this system marks the end of each line in text files with *two* special characters: the line feed character (`LF`) and the carriage return (`CR`). In Linux, lines end only with the `LF` character. In some cases, a program may expect to find only the `LF` character, and when it reads the `CR` afterwards it may do strange things. Notepad++ let us use a single click to change all the EOL characters to the Linux version (`Edit` > `EOL conversion` > `Unix (LF)`), which is more universally accepted.
- It can edit several lines at the same time. Pressing the `Alt` key and dragging the mouse cursor, we can select one position in several lines and everything we type or remove will be applied to all of them.

## File extensions

In Windows, each file has a different extension, which tell us which kind of file it is. But, for some reason, Windows decides to hide the extension of file types that are 'known'. In phylogeny, it is always advisable to keep the extensions visible at all times, to avoid confusions about if a file is the matrix in NEXUS format (`.nex`), is the tree obtained in the analysis (`.tre`), or anything else.

In order to active this option, we must open any folder, and then go to the menu and click on `View` > `Options`. In the window that appears, we must go to the `View` tab, and uncheck the box that says `Hide extensions for known file types`.

Just be careful when renaming files, to avoid changing accidentally the extension! (Windows will warn you if this happens).

It's very important, when loading files in any phylogeny program, to correctly write both the name of the file and the extension. For example, if you have a Nexus file named `MyData.nex` and you didn't tell Windows to show the file extensions, it may look as `MyData` in your folder. If you try to open it in MrBayes using the command `execute MyData`, MrBayes will not know which file you are referring to. You have to use the full name: `execute MyData.nex`
