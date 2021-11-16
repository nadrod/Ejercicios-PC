#Jairo Santana García, Pablo de Jesus García Medina, Jose Pablo Perez Hernandez.
function New-Directorio{
  param([Parameter(Mandatory)] [string] $archivo,
  [Parameter(Mandatory)] [String] $ruta)
  try{
  Write-Host "Creando el archivo en: $ruta\$archivo"
  New-Item "$ruta\$archivo" -itemType Directory -ErrorAction Stop} catch{
  Write-Host "Ocurrio un error lo sentimos mucho"
  $_.Exception.Message} #Encontramos un error a la hora de crear directorios en carpetas como program files sin permisos de administrador
}

function New-Archivo{ 
  param([Parameter(Mandatory)] [string] $archivo,
  [Parameter(Mandatory)] [String] $ruta,
  [Parameter(Mandatory, HelpMessage="Pon la extension del archivo sin el punto")] [String] $extension)
  try{
  Write-Host "Creando el archivo en: $ruta\$archivo.$extension"
  New-Item "$ruta\$archivo.$extension" -itemType File -ErrorAction Stop} catch{
  Write-Host "Ocurrio un error lo sentimos mucho"
  $_.Exception.Message #Encontramos un error a la hora de crear archivos en carpetas como program files sin permisos de administrador
  }
}

function Remove-Directorio{
  param([Parameter(Mandatory)] [string] $nombre_dir,
  [Parameter(Mandatory)] [String] $ruta)
  try{
  Write-Host "Borrando el Directorio: $ruta\$nombre_dir"
  Remove-Item "$ruta\$nombre_dir" -recurse -ErrorAction Stop} catch {
     Write-Host "Ocurrio un error lo sentimos mucho"
  $_.Exception.Message #Encontramos un error a la hora de eliminar carpetas inexistentes o borrar archivos de administrador sin permisos de admin
  }
}

function Remove-archivo{
  param([Parameter(Mandatory)] [string] $archivo,
  [Parameter(Mandatory)] [String] $ruta,
  [Parameter(Mandatory, HelpMessage="Pon la extension del archivo sin el punto")] [String] $extension)
  try{
  Write-Host "Borrando el archivo: $ruta\$archivo.$extension"
  Remove-Item "$ruta\$archivo.$extension" -ErrorAction Stop} catch{ Write-Host "Ocurrio un error lo sentimos mucho"
  $_.Exception.Message #Encontramos un error a la hora de eliminar archivos inexistentes o borrar archivos de administrador sin permisos de admin
  }
}

function Get-BuscaArchivos{
  param([Parameter(Mandatory)] [string] $extension,
  [Parameter(Mandatory)] [String] $ruta)
  try{
  Write-Host "Buscando archvios en: $ruta con extension .$extension"
  Get-ChildItem "$ruta\" -Filter "*.$extension" -Recurse -ErrorAction Stop} catch{ Write-Host "Ocurrio un error lo sentimos mucho"
  $_.Exception.Message #Encontramos un error al buscar en carpetas que no existen
  }
}