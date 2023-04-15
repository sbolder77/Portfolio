#---------------------------------------------------------------------------------------------------------------------
# Description:
# Thermo Fisher aged file mover script
# v1.0 March 2023
# Author - Simon Bolder
#---------------------------------------------------------------------------------------------------------------------
# This script is used to interrogate a source folder containing many files
# and move the single oldest file to a target folder to be consumed by sweeper agent
# The Script will also check if there is a file in the target folder and wait until it has been consumed
#---------------------------------------------------------------------------------------------------------------------

#region variables and objects
    # Collect the settings froma JSON file
    $sourceDir = (Get-Item $PSScriptRoot).Parent.FullName
    $jsonFile = "Settings.json";
    $jsonsSettings = Get-Content -Path ($sourceDir + '\AppSettings\' + $jsonFile) | ConvertFrom-Json
    Write-Tee "INFO,$(Get-Date -Format "dd/MM/yyyy HH:mm:ss"),Found settings file in - $($sourceDir)\AppSettings\$($jsonFile)"

    # Set file directories
    $logDir = $sourceDir + '\' + $jsonsSettings.Log_Dir.Name
    $fileSource = $sourceDir + '\' + $jsonsSettings.Source_Dir.Name
    $fileTarget = $sourceDir + '\' + $jsonsSettings.Target_Dir.Name

    # Counts of the files in the source and target directories
    $sourceFiles = (get-childitem $FileSource | Measure-Object).Count
    Write-Tee "INFO,$(Get-Date -Format "dd/MM/yyyy HH:mm:ss"),$sourceFiles files in - $($FileSource)"
    $targetFiles = (get-childitem $FileTarget | Measure-Object).Count
    Write-Tee "INFO,$(Get-Date -Format "dd/MM/yyyy HH:mm:ss"),$targetFiles file in - $($FileTarget)"

    # Empty object to hold file names
    $allFileNames = @()

    # Hashtable to hold path and current file count
    $folderCountDictionary = New-Object System.Collections.Generic.SortedDictionary"[String,Int]"

    # List of source files - oldest first
    $oldestSourceFilesFirst = get-childitem $FileSource | sort LastWriteTime

    # List of target files
    $targetFileCount = (get-childitem $FileTarget | Measure-Object).Count
    $targetFile = get-childitem $FileTarget
    #endregion

#region functions
function ProcessFiles {
    #get file count and store filename
    foreach ($item in $FileSource) {
        $fileList = get-childitem $item 
        $fileCount = $($fileList | Measure-Object).Count
        foreach ($existingFile in $fileList) {
            $allFileNames += $existingFile.Name
        }
        # Add path and count to collection
        $folderCountDictionary.add($item , $fileCount)
    }

    if($targetFileCount -eq 0)
    {
        # Moves oldest source file to target folder if target folder empty
        $fileToMove = $oldestSourceFilesFirst[0]
        Write-Tee "INFO,$(Get-Date -Format "dd/MM/yyyy HH:mm:ss"),Moving - $fileToMove from - $($sourceFiles)"
        $destFileName = $fileTarget + "\" + $fileToMove.Name
        Write-Tee "INFO,$(Get-Date -Format "dd/MM/yyyy HH:mm:ss"),Target file path is - $($destFileName)"
        $fileToMove.MoveTo($destFileName)
        Write-Tee "INFO,$(Get-Date -Format "dd/MM/yyyy HH:mm:ss"),$($fileToMove.Name) has been moved to - $($fileTarget)"
    }
    else
    {
        Write-Tee "INFO,$(Get-Date -Format "dd/MM/yyyy HH:mm:ss"), $($fileTarget) directory is not empty"
    }
}

function Write-Tee ( [parameter(Mandatory = $true)]  $message,
    [parameter(Mandatory = $false)] $consoleColor = "white"
) {

    If (!(test-path $logDir)) {
        New-Item -ItemType Directory -Force -Path $logDir | Out-Null
    }

	$logFile = "FileMove_"+"$(Get-Date -Format "MMddyyyy").log"
    $log = Join-Path -Path $logDir -ChildPath $logFile             
    Write-Host $message -ForegroundColor $consoleColor
    if (!($null -eq $log) -and !($log -eq "")) {
        Add-content $log -value $message
    }
}
#endregion

ProcessFiles