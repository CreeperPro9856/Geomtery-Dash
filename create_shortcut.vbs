' VBScript to create a shortcut on the Desktop
Set objShell = CreateObject("WScript.Shell")
strDesktop = objShell.SpecialFolders("Desktop")

' Get the directory where this script is located
objFSO = CreateObject("Scripting.FileSystemObject")
strScriptDir = objFSO.GetParentFolderName(WScript.ScriptFullName)
strGamePath = strScriptDir & "\Geometry_Dash"
strPythonPath = "python"

' Create the shortcut
Set objLink = objShell.CreateShortCut(strDesktop & "\Geometry Dash PRO.lnk")
objLink.TargetPath = strPythonPath
objLink.Arguments = Chr(34) & strGamePath & Chr(34)
objLink.WorkingDirectory = strScriptDir
objLink.Description = "Geometry Dash PRO"
objLink.IconLocation = strGamePath & ",0"
objLink.Save

' Show confirmation message
MsgBox "Parancsikon sikeresen létrehozva az asztalon!", vbInformation, "Geometry Dash PRO"
