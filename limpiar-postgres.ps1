#Requires -RunAsAdministrator

$ErrorActionPreference = "Continue"

Write-Host "ADVERTENCIA: se eliminaran PostgreSQL y todas sus bases locales." -ForegroundColor Red
$confirmacion = Read-Host 'Escribe BORRAR POSTGRES para continuar'

if ($confirmacion -cne "BORRAR POSTGRES") {
    Write-Host "Operacion cancelada."
    exit
}

$servicios = Get-CimInstance Win32_Service |
    Where-Object {
        $_.Name -match "(?i)postgres" -or
        $_.DisplayName -match "(?i)postgres"
    }

$rutasDatos = foreach ($servicio in $servicios) {
    if ($servicio.PathName -match '(?i)-D\s+"([^"]+)"') {
        $matches[1]
    }
}

Write-Host "Deteniendo procesos PostgreSQL..."
Get-Process |
    Where-Object { $_.ProcessName -match "(?i)^(postgres|pg_ctl|psql)$" } |
    Stop-Process -Force -ErrorAction SilentlyContinue

foreach ($servicio in $servicios) {
    Write-Host "Eliminando servicio: $($servicio.Name)"
    Stop-Service -Name $servicio.Name -Force -ErrorAction SilentlyContinue
    & sc.exe delete $servicio.Name
}

$rutas = @(
    "$env:ProgramFiles\PostgreSQL",
    "${env:ProgramFiles(x86)}\PostgreSQL",
    "$env:ProgramData\PostgreSQL",
    "$env:APPDATA\postgresql",
    "$env:LOCALAPPDATA\PostgreSQL"
)

$rutas += $rutasDatos
$rutas = $rutas | Where-Object { $_ } | Sort-Object -Unique

Write-Host "`nSe eliminaran estas carpetas:" -ForegroundColor Yellow
$rutas | ForEach-Object { Write-Host "  $_" }

$segundaConfirmacion = Read-Host 'Escribe ELIMINAR DATOS para confirmar'

if ($segundaConfirmacion -cne "ELIMINAR DATOS") {
    Write-Host "No se eliminaron las carpetas."
    exit
}

foreach ($ruta in $rutas) {
    if (Test-Path -LiteralPath $ruta) {
        Write-Host "Eliminando: $ruta"
        Remove-Item -LiteralPath $ruta -Recurse -Force -ErrorAction Continue
    }
}

Write-Host "`nLimpieza terminada. Reinicia Windows." -ForegroundColor Green
