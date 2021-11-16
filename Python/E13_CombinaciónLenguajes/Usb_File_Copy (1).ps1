
function Get-Usb{
    $drives = [System.IO.DriveInfo]::GetDrives()
    $r = $drives | Where-Object { $_.DriveType -eq 'Removable' -and $_.IsReady }
    if ($r) {
        return @($r)[-1]
    }
    throw "No removable drives found."
}

$usb = Get-Usb
$usb.RootDirectory.Name

New-Item -Path C:\Users\HP\Desktop\Usb_Copy\ -Force 
Copy-Item -Path $usb.RootDirectory.Name -Destination C:\Users\HP\Desktop\Usb_Copy\ -Recurse -Force -Passthru