Param(
  [string[]]$Slides = @(1,3,6)
)
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path))
$pptPath = Join-Path $repo 'Azure and ML in Oil and Gas Industry.pptx'
$outDir  = Join-Path $repo 'Module 1\data\exported_slides'
if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }
$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = $false
$pres = $pp.Presentations.Open($pptPath, $true, $false, $false)
foreach ($i in $Slides) {
  $out = Join-Path $outDir ("slide_{0}.png" -f $i)
  $pres.Slides.Item([int]$i).Export($out, 'PNG', 1600, 900)
}
$pres.Close()
$pp.Quit()
Write-Output ("Exported slides: {0} -> {1}" -f ($Slides -join ', '), $outDir)
