Outfile "HealthTrackerInstaller.exe"
Caption "Fitness Tracker Installer"

InstallDir $PROGRAMFILES\HealthTracker
RequestExecutionLevel admin

!include LogicLib.nsh ; For ${If}, ${EndIf}, etc.

; Define WM_SETTINGCHANGE constant for system notification
!define WM_SETTINGCHANGE 0x001A

!define MUI_PRODUCT "Fitness Tracker Installer"

Name "Fitness Tracker Installer"

Var ADD_PATH
Var CREATE_DESKTOP
Var CREATE_STARTMENU

Page directory
Page custom OptionsPage
Page instfiles
UninstPage uninstConfirm
UninstPage instfiles

Function OptionsPage
    MessageBox MB_YESNO|MB_ICONQUESTION "Add HealthTracker to PATH?" IDYES +2
        StrCpy $ADD_PATH 0
        Goto next1
    StrCpy $ADD_PATH 1
next1:

    MessageBox MB_YESNO|MB_ICONQUESTION "Create Desktop Shortcut?" IDYES +2
        StrCpy $CREATE_DESKTOP 0
        Goto next2
    StrCpy $CREATE_DESKTOP 1
next2:

    MessageBox MB_YESNO|MB_ICONQUESTION "Create Start Menu Shortcut?" IDYES +2
        StrCpy $CREATE_STARTMENU 0
        Goto done
    StrCpy $CREATE_STARTMENU 1
done:
FunctionEnd

Section "Install"

    SetOutPath $INSTDIR

    ; Install your compiled executable
    File "D:\Jhita\Jhita\Documents\Avraj\Health-Tracker\dist\health-tracker.exe"

    ; Register uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\HealthTracker" "DisplayName" "HealthTracker"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\HealthTracker" "UninstallString" "$INSTDIR\uninstall.exe"

    ; Create Desktop Shortcut if selected
    ${If} $CREATE_DESKTOP == 1
        CreateShortCut "$DESKTOP\HealthTracker.lnk" "$INSTDIR\health-tracker.exe"
    ${EndIf}

    ; Create Start Menu Shortcut if selected
    ${If} $CREATE_STARTMENU == 1
        CreateDirectory "$SMPROGRAMS\HealthTracker"
        CreateShortCut "$SMPROGRAMS\HealthTracker\HealthTracker.lnk" "$INSTDIR\health-tracker.exe"
        CreateShortCut "$SMPROGRAMS\HealthTracker\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    ${EndIf}

    ; Add to PATH if selected
    ${If} $ADD_PATH == 1
        ReadRegStr $1 HKCU "Environment" "Path"
        StrCmp $1 "" 0 +3
            StrCpy $1 "$INSTDIR"
            Goto +2
        StrCpy $1 "$1;$INSTDIR"
        WriteRegExpandStr HKCU "Environment" "Path" "$1"
        ; Notify system of PATH update
        System::Call 'kernel32::SendMessageTimeoutA(i 0xffff, i ${WM_SETTINGCHANGE}, i 0, t "Environment", i 0, i 5000, *i .r0)'
    ${EndIf}

SectionEnd

Section "Uninstall"

    Delete "$INSTDIR\health-tracker.exe"
    Delete "$INSTDIR\uninstall.exe"

    Delete "$DESKTOP\HealthTracker.lnk"
    Delete "$SMPROGRAMS\HealthTracker\HealthTracker.lnk"
    Delete "$SMPROGRAMS\HealthTracker\Uninstall.lnk"
    RMDir "$SMPROGRAMS\HealthTracker"

    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\HealthTracker"

    ; Remove PATH entry if exists (Optional)
    ReadRegStr $1 HKCU "Environment" "Path"
    ${If} $1 != ""
        ; Code to remove the path from the environment (if needed)
    ${EndIf}

    RMDir /r "$INSTDIR"

SectionEnd
