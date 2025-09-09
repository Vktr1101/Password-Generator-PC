[Setup]

AppName=Password Generator
AppVersion=1.0
AppPublisher=Victor
AppPublisherURL=https://example.com
DefaultDirName={commonpf}\Password Generator
DefaultGroupName=Password Generator
UninstallDisplayIcon={app}\PasswordGenerator.exe
OutputBaseFilename=PasswordGeneratorSetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

; Dacă vrei ca installer-ul să fie doar pentru userul curent (fără admin):
; PrivilegesRequired=lowest

[Files]
; Copiază executabilul și icon-ul în folderul de instalare
Source: "C:\Projects\PasswordGenerator\dist\PasswordGenerator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Projects\PasswordGenerator\psswd_icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Creează shortcut în Start Menu
Name: "{group}\Password Generator"; Filename: "{app}\PasswordGenerator.exe"; IconFilename: "{app}\psswd_icon.ico"
; Creează shortcut pe Desktop
Name: "{commondesktop}\Password Generator"; Filename: "{app}\PasswordGenerator.exe"; IconFilename: "{app}\psswd_icon.ico"

[Run]
; Rulează aplicația după instalare (opțional)
Filename: "{app}\PasswordGenerator.exe"; Description: "Lansează Password Generator"; Flags: nowait postinstall skipifsilent
